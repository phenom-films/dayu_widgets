# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.button_group import MPushButtonGroup
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.slider import MSlider
from dayu_widgets3.spin_box import MSpinBox


class SliderExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(SliderExample, self).__init__(parent)
        self.setWindowTitle("Examples for MSlider")
        self._init_ui()

    def _init_ui(self):
        self.register_field("percent", 20)
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different orientation"))
        for orn in [QtCore.Qt.Horizontal, QtCore.Qt.Vertical]:
            line_edit_hor = MSlider(orn)
            line_edit_hor.setRange(1, 100)
            self.bind("percent", line_edit_hor, "value")
            lay = QtWidgets.QVBoxLayout()
            lay.addWidget(line_edit_hor)
            main_lay.addLayout(lay)
        spin_box = MSpinBox()
        spin_box.setRange(1, 100)
        self.bind("percent", spin_box, "value", signal="valueChanged")

        lay3 = QtWidgets.QHBoxLayout()
        button_grp = MPushButtonGroup()
        button_grp.set_button_list(
            [
                {"text": "+", "clicked": functools.partial(self.slot_change_value, 10)},
                {
                    "text": "-",
                    "clicked": functools.partial(self.slot_change_value, -10),
                },
            ]
        )
        lay3.addWidget(spin_box)
        lay3.addWidget(button_grp)
        lay3.addStretch()
        main_lay.addWidget(MDivider("data bind"))
        main_lay.addLayout(lay3)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_value(self, value):
        self.set_field("percent", max(0, min(self.field("percent") + value, 100)))


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = SliderExample()
        dayu_theme.apply(test)
        test.show()
