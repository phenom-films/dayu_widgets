# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3 import dayu_theme
from dayu_widgets3.button_group import MPushButtonGroup
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.label import MLabel
from dayu_widgets3.push_button import MPushButton
from dayu_widgets3.qt import MIcon


class PushButtonGroupExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(PushButtonGroupExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button_config_list = [
            {
                "text": "Add",
                "icon": MIcon("add_line.svg", "#fff"),
                "type": MPushButton.PrimaryType,
            },
            {
                "text": "Edit",
                "icon": MIcon("edit_fill.svg", "#fff"),
                "type": MPushButton.WarningType,
            },
            {
                "text": "Delete",
                "icon": MIcon("trash_line.svg", "#fff"),
                "type": MPushButton.DangerType,
            },
        ]
        button_group_h = MPushButtonGroup()
        button_group_h.set_dayu_size(dayu_theme.large)
        button_group_h.set_button_list(button_config_list)
        h_lay = QtWidgets.QHBoxLayout()
        h_lay.addWidget(button_group_h)
        h_lay.addStretch()

        button_group_v = MPushButtonGroup(orientation=QtCore.Qt.Vertical)
        button_group_v.set_button_list(button_config_list)
        h_lay_2 = QtWidgets.QHBoxLayout()
        h_lay_2.addWidget(button_group_v)
        h_lay_2.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MLabel("MPushButtonGroup is MPushButton collection. they are not exclusive."))
        main_lay.addWidget(MDivider("MPushButton group: Horizontal & Small Size"))
        main_lay.addLayout(h_lay)
        main_lay.addWidget(MDivider("MPushButton group: Vertical & Default Size"))
        main_lay.addLayout(h_lay_2)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = PushButtonGroupExample()
        dayu_theme.apply(test)
        test.show()
