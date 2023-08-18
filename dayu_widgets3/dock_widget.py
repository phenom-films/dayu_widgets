"""MDockWidget"""

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets


class MDockWidget(QtWidgets.QDockWidget):
    """
    Just apply the qss. No more extend.
    """

    def __init__(self, title="", parent=None, flags=QtCore.Qt.Widget):
        super(MDockWidget, self).__init__(title, parent=parent, flags=flags)
