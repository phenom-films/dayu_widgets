# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3 import dayu_theme
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.push_button import MPushButton
from dayu_widgets3.qt import MIcon


class PushButtonExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(PushButtonExample, self).__init__(parent)
        self.setWindowTitle("Example for MPushButton")

        sub_lay1 = QtWidgets.QHBoxLayout()
        sub_lay1.addWidget(MPushButton("Default"))
        sub_lay1.addWidget(MPushButton("Primary").primary())
        sub_lay1.addWidget(MPushButton("Success").success())
        sub_lay1.addWidget(MPushButton("Warning").warning())
        sub_lay1.addWidget(MPushButton("Danger").danger())

        sub_lay2 = QtWidgets.QHBoxLayout()
        sub_lay2.addWidget(MPushButton("Upload", MIcon("cloud_line.svg")))
        sub_lay2.addWidget(
            MPushButton("Submit", MIcon("folder_line.svg", "#ddd")).primary()
        )
        sub_lay2.addWidget(
            MPushButton("Submit", MIcon("success_line.svg", "#ddd")).success()
        )
        sub_lay2.addWidget(
            MPushButton("Edit", MIcon("edit_line.svg", "#ddd")).warning()
        )
        sub_lay2.addWidget(
            MPushButton("Delete", MIcon("trash_line.svg", "#ddd")).danger()
        )

        sub_lay3 = QtWidgets.QHBoxLayout()
        sub_lay3.addWidget(MPushButton("Large").large().primary())
        sub_lay3.addWidget(MPushButton("Medium").medium().primary())
        sub_lay3.addWidget(MPushButton("Small").small().primary())

        disabled_button_1 = MPushButton("Disabled").huge()
        disabled_button_1.setEnabled(False)
        disabled_button_2 = MPushButton("Disabled").large()
        disabled_button_2.setEnabled(False)
        disabled_button_3 = MPushButton("Disabled")
        disabled_button_3.setEnabled(False)
        disabled_button_4 = MPushButton("Disabled").small()
        disabled_button_4.setEnabled(False)
        disable_lay = QtWidgets.QHBoxLayout()
        disable_lay.addWidget(disabled_button_1)
        disable_lay.addWidget(disabled_button_2)
        disable_lay.addWidget(disabled_button_3)
        disable_lay.addWidget(disabled_button_4)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addWidget(MDivider("different size"))
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider("disabled"))
        main_lay.addLayout(disable_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = PushButtonExample()
        dayu_theme.apply(test)
        test.show()
