# Import built-in modules
import sys
import os

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application


def main():
    """
    Main entry point for the dayu_widgets demo application.
    This function is called when running the package as a module:
    `python -m dayu_widgets` or `uvx --python 3.10 --with pyside2 dayu_widgets`
    """
    # Add the examples directory to the Python path
    examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'examples')
    sys.path.insert(0, os.path.dirname(examples_dir))
    
    # Import the demo module
    from examples.demo import MDemo
    
    # Start the application
    with application() as app:
        test = MDemo()
        dayu_theme.apply(test)
        test.show()


if __name__ == "__main__":
    main()
