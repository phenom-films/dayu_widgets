# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.push_button import MPushButton
from dayu_widgets.text_edit import MTextEdit


class TextEditExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TextEditExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QtWidgets.QVBoxLayout()

        main_lay.addWidget(MDivider("no size grip"))
        main_lay.addWidget(MTextEdit(self))
        main_lay.addWidget(MDivider("size grip"))
        main_lay.addWidget(MTextEdit(self).resizeable())
        main_lay.addWidget(MPushButton("text").primary())

        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = TextEditExample()
        dayu_theme.apply(test)
        test.show()
