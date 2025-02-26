# Import built-in modules
import os

# Import local modules
from dayu_widgets import DEFAULT_STATIC_FOLDER


def request_file(file_name):
    """
    Get the absolute path of a static file.
    
    Args:
        file_name (str): Name of the file to find in static folder
        
    Returns:
        str: Absolute path to the file
    """
    static_file = os.path.join(DEFAULT_STATIC_FOLDER, file_name)
    if os.path.exists(static_file):
        return static_file
    return ""

