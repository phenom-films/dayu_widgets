"""
MRadioButton
"""

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.mixin import cursor_mixin


@cursor_mixin
class MRadioButton(QtWidgets.QRadioButton):
    """
    MRadioButton just use stylesheet and set cursor shape when hover. No more extend.
    """

    def __init__(self, text="", parent=None):
        super(MRadioButton, self).__init__(text=text, parent=parent)
