# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.breadcrumb import MBreadcrumb
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.message import MMessage


class BreadcrumbExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(BreadcrumbExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBreadcrumb")
        self._init_ui()

    def _init_ui(self):
        MMessage.config(duration=1)
        entity_list = [
            {
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Home Page"'),
                "svg": "home_line.svg",
            },
            {
                "text": "pl",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "pl"'),
                "svg": "user_line.svg",
            },
            {
                "text": "pl_0010",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "pl_0010"'),
            },
        ]
        no_icon_eg = MBreadcrumb()
        no_icon_eg.set_item_list(entity_list)

        separator_eg = MBreadcrumb(separator="=>")
        separator_eg.set_item_list(entity_list)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("normal"))
        main_lay.addWidget(no_icon_eg)
        main_lay.addWidget(MDivider("separator: =>"))
        main_lay.addWidget(separator_eg)

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(config, parent=self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = BreadcrumbExample()
        dayu_theme.apply(test)
        test.show()
