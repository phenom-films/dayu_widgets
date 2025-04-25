# -*- coding: utf-8 -*-
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import os
import sys
import importlib
import signal

# Import third-party modules
from Qt import QtWidgets


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
    
    # Import the demo module
    try:
        from examples.demo import MDemo
    except ImportError:
        print("Error: Could not import the demo module. Make sure the examples directory is available.")
        sys.exit(1)
    
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application
    
    with application() as app:
        test = MDemo()
        dayu_theme.apply(test)
        test.show()


if __name__ == "__main__":
    main()
