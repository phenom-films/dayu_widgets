# Import built-in modules
import os
import sys
from pathlib import Path

# Import third-party modules
import nox


@nox.session
def maya_test(session: nox.Session) -> None:
    """Run tests in Maya environment."""
    # Get the project root directory
    root_dir = Path(__file__).parent.parent.absolute()
    print(f"Project root directory: {root_dir}")

    # Check if we're running in CI
    in_ci = os.environ.get("CI") is not None
    print(f"Running in CI: {in_ci}")

    # Get Maya version from environment variable or default to 2022
    maya_version = os.environ.get("MAYA_VERSION", "2022")
    print(f"Using Maya version: {maya_version}")

    # Check if Docker is available
    try:
        session.run("docker", "--version", external=True)
        docker_available = True
        print("Docker is available")
    except Exception as e:
        docker_available = False
        print(f"Docker is not available: {e}")

    if in_ci and not docker_available:
        # In CI without Docker, just print a message
        print("Maya compatibility test skipped in CI without Docker")
        print("For local testing, use Docker:")
        print("docker pull mottosso/maya:2022")
        print("nox -s maya-test")
        return

    # Install dependencies
    print("Installing dependencies...")
    session.install("pytest>=7.0.0", "pytest-cov>=4.1.0", "qtpy>=2.3.1")

    # Install the package with PySide2 (Maya uses PySide2)
    print("Installing the package...")
    try:
        session.install("PySide2>=5.15.2.1")
        session.install("-e", ".")
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        print("Continuing with minimal installation...")
        session.install("-e", ".", "--no-deps")

    # Set environment variables
    env = {
        "QT_API": "pyside2",
        "PYTHONPATH": str(root_dir),
        "CI": "1",
        "QT_QPA_PLATFORM": "offscreen"
    }

    if docker_available:
        # Run the Maya tests using Docker with better error handling
        print("Running Maya tests with Docker...")

        # Pull the Docker image with timeout and retry
        print(f"Pulling Docker image mottosso/maya:{maya_version}...")
        try:
            session.run(
                "docker", "pull", f"mottosso/maya:{maya_version}",
                external=True
            )
            print(f"Successfully pulled mottosso/maya:{maya_version} image")
        except Exception as e:
            print(f"Failed to pull Docker image: {e}")
            print("Attempting to use existing image if available...")
            # Check if image exists locally
            try:
                session.run(
                    "docker", "images", f"mottosso/maya:{maya_version}",
                    external=True
                )
                print(f"Found existing mottosso/maya:{maya_version} image")
            except Exception as e2:
                print(f"No existing image found: {e2}")
                raise Exception(f"Cannot proceed without Maya {maya_version} Docker image")

        # Convert Windows path to Docker-compatible path if needed
        docker_path = str(root_dir).replace('\\', '/')
        if os.name == 'nt' and ':' in docker_path:  # Windows path with drive letter
            drive, path = docker_path.split(':', 1)
            docker_path = f"//{drive.lower()}{path}"
            print(f"Converted Windows path to Docker path: {docker_path}")

        # Create a simplified test script focused on the core issue
        test_script = f"""import sys
import os

print("=== Maya {maya_version} Environment Info ===")
print(f"Python version: {{sys.version}}")
print(f"Python executable: {{sys.executable}}")
print(f"QT_API environment: {{os.environ.get('QT_API', 'not set')}}")

print("\\n=== Testing qtpy import ===")
try:
    import qtpy
    print(f"✓ qtpy imported: {{qtpy.__version__ if hasattr(qtpy, '__version__') else 'version unknown'}}")

    # Test qtpy.API import (expected to fail in older versions)
    try:
        from qtpy import API
        print(f"✓ qtpy.API: {{API}}")
    except ImportError:
        print("✗ qtpy.API not available (using fallback)")

except ImportError as e:
    print(f"✗ qtpy import failed: {{e}}")
    sys.exit(1)

print("\\n=== Testing dayu_widgets import ===")
try:
    import dayu_widgets
    print(f"✓ dayu_widgets imported from: {{dayu_widgets.__file__}}")

    # Test the specific module that had issues
    from dayu_widgets import menu
    print("✓ dayu_widgets.menu imported successfully")

    print("\\n🎉 Maya Docker test PASSED!")

except Exception as e:
    print(f"\\n❌ dayu_widgets import failed: {{e}}")
    import traceback
    print("\\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)
"""
        test_script_path = os.path.join(root_dir, "maya_test_script.py")
        with open(test_script_path, "w") as f:
            f.write(test_script)
        print(f"Created detailed test script at {test_script_path}")

        # Run the Docker container with better error handling
        print("Running Docker container...")
        print(f"Docker command: docker run --rm -v {docker_path}:/dayu_widgets -w /dayu_widgets mottosso/maya:{maya_version} mayapy maya_test_script.py")

        try:
            session.run(
                "docker", "run", "--rm",
                "-v", f"{docker_path}:/dayu_widgets",
                "-w", "/dayu_widgets",
                "--user", "root",  # Run as root to avoid permission issues
                f"mottosso/maya:{maya_version}",
                "mayapy", "maya_test_script.py",
                external=True
            )
            print("✅ Maya Docker test completed successfully!")
        except Exception as e:
            print(f"❌ Docker container failed: {e}")
            print("Attempting to get more information...")

            # Try to run a simple test to see if the container works at all
            try:
                print("Testing basic container functionality...")
                session.run(
                    "docker", "run", "--rm",
                    f"mottosso/maya:{maya_version}",
                    "mayapy", "-c", "print('Maya container is working')",
                    external=True
                )
                print("Basic container test passed - issue is with our script")
            except Exception as e2:
                print(f"Basic container test also failed: {e2}")

            raise e
    else:
        # Without Docker, run a detailed test - NO EXCEPTION HANDLING
        print("Running detailed Maya compatibility test without Docker...")
        session.run(
            "python", "-c",
            """import sys;
import os;
print(f'Python version: {sys.version}');
print(f'Environment QT_API: {os.environ.get("QT_API", "not set")}');

try:
    from qtpy import API;
    print(f'qtpy.API: {API}');
except ImportError as e:
    print(f'qtpy.API import failed: {e}');
    api_from_env = os.environ.get('QT_API', 'unknown');
    print(f'Using QT_API from environment: {api_from_env}');

import dayu_widgets;
from dayu_widgets import menu;
print('Maya compatibility test passed!');
""",
            env=env
        )
