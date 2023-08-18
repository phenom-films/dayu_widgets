"""
MCheckBox
"""

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.mixin import cursor_mixin


@cursor_mixin
class MCheckBox(QtWidgets.QCheckBox):
    """
    MCheckBox just use stylesheet and set cursor shape when hover. No more extend.
    """

    def __init__(self, text="", parent=None):
        super(MCheckBox, self).__init__(text=text, parent=parent)
