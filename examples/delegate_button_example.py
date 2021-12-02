# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets import dayu_theme
from dayu_widgets import utils
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_view import MTableView
from dayu_widgets.qt import *


class MPushButtonDelegate(QStyledItemDelegate):
    sig_clicked = Signal(object)

    def __init__(self, parent=None):
        super(MPushButtonDelegate, self).__init__(parent)
        self.editor = None
        self.showed = False
        self.exclusive = True
        self.parent_widget = None

    def editorEvent(self, pEvent, model, option, index):
        if pEvent.type() == QEvent.MouseButtonRelease:
            index = utils.real_index(index)
            self.sig_clicked.emit(index.internalPointer())
            return True
        return False

    def paint(self, painter, option, index):
        button = QStyleOptionButton()
        button.rect = option.rect
        button.text = "Click Me (" + str(index.data(Qt.DisplayRole)) + ")"
        button.state = QStyle.State_Enabled

        QApplication.style().drawControl(QStyle.CE_PushButton, button, painter)


header_list = [
    {
        "label": "Name",
        "key": "name",
        "checkable": True,
        "searchable": True,
        "width": 200,
        "font": lambda x, y: {"underline": True},
        "icon": "user_fill.svg",
    },
    {
        "label": "Sex",
        "key": "sex",
        "searchable": True,
        "selectable": True,
        "icon": lambda x, y: (
            "{}.svg".format(x.lower()),
            getattr(dayu_theme, x.lower() + "_color"),
        ),
    },
    {
        "label": "Age",
        "key": "age",
        "width": 90,
        "searchable": True,
        "editable": True,
        "display": lambda x, y: "{} 岁".format(x),
        "font": lambda x, y: {"bold": True},
    },
    {
        "label": "Address",
        "key": "city",
        "selectable": True,
        "searchable": True,
        "exclusive": False,
        "width": 120,
        "display": lambda x, y: " & ".join(x) if isinstance(x, list) else x,
        "bg_color": lambda x, y: "transparent" if x else dayu_theme.error_color,
    },
    {
        "label": "Score",
        "key": "score",
    },
]


class TableViewExample(QWidget):
    def __init__(self, parent=None):
        super(TableViewExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        model_1 = MTableModel()
        model_1.set_header_list(header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)

        table_grid = MTableView(size=dayu_theme.small, show_row_count=True)
        table_grid.setShowGrid(True)
        table_grid.setModel(model_sort)
        model_sort.set_header_list(header_list)
        table_grid.set_header_list(header_list)
        button_delegate = MPushButtonDelegate(parent=self)
        table_grid.setItemDelegateForColumn(4, button_delegate)
        button_delegate.sig_clicked.connect(self.slot_cell_clicked)
        model_1.set_data_list(
            [
                {
                    "name": "John Brown",
                    "sex": "Male",
                    "sex_list": ["Male", "Female"],
                    "age": 18,
                    "score": 89,
                    "city": "New York",
                    "city_list": ["New York", "Ottawa", "London", "Sydney"],
                    "date": "2016-10-03",
                },
                {
                    "name": "Jim Green",
                    "sex": "Male",
                    "sex_list": ["Male", "Female"],
                    "age": 24,
                    "score": 55,
                    "city": "London",
                    "city_list": ["New York", "Ottawa", "London", "Sydney"],
                    "date": "2016-10-01",
                },
            ]
        )

        main_lay = QVBoxLayout()
        main_lay.addWidget(table_grid)
        self.setLayout(main_lay)

    def slot_cell_clicked(self, data_dict):
        print(data_dict)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QApplication(sys.argv)
    test = TableViewExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
