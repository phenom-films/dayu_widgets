"""MSlider"""

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets


class MSlider(QtWidgets.QSlider):
    """
    A Slider component for displaying current value and intervals in range.

    MSlider just apply qss for QSlider.
    """

    def __init__(self, orientation=QtCore.Qt.Horizontal, parent=None):
        super(MSlider, self).__init__(orientation, parent=parent)
        self._show_text_when_move = True

    def disable_show_text(self):
        self._show_text_when_move = False

    def mouseMoveEvent(self, event):
        """Override the mouseMoveEvent to show current value as a tooltip."""
        if self._show_text_when_move:
            QtWidgets.QToolTip.showText(event.globalPos(), str(self.value()), self)
        return super(MSlider, self).mouseMoveEvent(event)
