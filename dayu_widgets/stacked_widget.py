"""MStackedWidget"""

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.mixin import stacked_animation_mixin


@stacked_animation_mixin
class MStackedWidget(QtWidgets.QStackedWidget):
    """Just active animation when current index changed."""

    def __init__(self, parent=None):
        super(MStackedWidget, self).__init__(parent)

    def disable_animation(self):
        self.currentChanged.disconnect(self._play_anim)
