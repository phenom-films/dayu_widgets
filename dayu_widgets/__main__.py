# -*- coding: utf-8 -*-
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import os
import sys
import signal


def main():
    """
    Main entry point for the dayu_widgets package when run as a module.
    This function runs the demo application.
    """
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Add the parent directory to sys.path to ensure examples can be imported
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    # Try different import strategies to find the demo module
    try:
        # First try: direct import (when installed as a package with examples included)
        from examples.demo import MDemo
    except ImportError:
        try:
            # Second try: import from package (when examples is inside the package)
            from dayu_widgets.examples.demo import MDemo
        except ImportError:
            # Third try: look for examples in common locations
            examples_paths = [
                # Current directory
                os.path.join(os.getcwd(), 'examples'),
                # Parent directory of the package
                os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'examples'),
                # Inside the package
                os.path.join(os.path.dirname(os.path.abspath(__file__)), 'examples'),
            ]

            found = False
            for path in examples_paths:
                if os.path.exists(os.path.join(path, 'demo.py')):
                    if path not in sys.path:
                        sys.path.insert(0, os.path.dirname(path))
                    try:
                        from examples.demo import MDemo
                        found = True
                        break
                    except ImportError:
                        continue

            if not found:
                print("Error: Could not import the demo module. Make sure the examples directory is available.")
                print("Searched in the following locations:")
                for path in examples_paths:
                    print(f"  - {path}")
                sys.exit(1)

    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    # Create application and run the demo
    with application() as app:
        test = MDemo()
        dayu_theme.apply(test)
        test.show()
        # Return the app's exit code (this will implicitly use the app variable)
        return app.exec_()


if __name__ == "__main__":
    main()
