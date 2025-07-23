# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.alert import MAlert
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_view import MTableView
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton
import examples._mock_data as mock


def h(*args):
    cls = args[0]
    widget = cls()
    for i in args:
        if isinstance(i, dict):
            for attr, value in i.get("props", {}).items():
                widget.setProperty(attr, value)
            for signal, slot in i.get("on", {}).items():
                getattr(widget, signal).connect(slot)
        elif isinstance(i, list):
            lay = QtWidgets.QHBoxLayout()
            for j in i:
                lay.addWidget(j)
            widget.setLayout(lay)
    return widget


class MFetchDataThread(QtCore.QThread):
    def __init__(self, parent=None):
        super(MFetchDataThread, self).__init__(parent)

    def run(self, *args, **kwargs):
        # Import built-in modules
        import time

        time.sleep(4)


class TableViewExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(TableViewExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        model_1 = MTableModel()
        model_1.set_header_list(mock.header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)

        table_small = MTableView(size=dayu_theme.small, show_row_count=True)
        table_grid = MTableView(size=dayu_theme.small, show_row_count=True)
        table_grid.setShowGrid(True)
        table_default = MTableView(size=dayu_theme.medium, show_row_count=True)
        thread = MFetchDataThread(self)

        self.loading_wrapper = MLoadingWrapper(widget=table_default, loading=False)
        thread.started.connect(functools.partial(self.loading_wrapper.set_dayu_loading, True))
        thread.finished.connect(functools.partial(self.loading_wrapper.set_dayu_loading, False))
        thread.finished.connect(functools.partial(table_default.setModel, model_sort))
        button = MPushButton(text="Get Data: 4s")
        button.clicked.connect(thread.start)
        switch_lay = QtWidgets.QHBoxLayout()
        switch_lay.addWidget(button)
        switch_lay.addStretch()
        table_large = MTableView(size=dayu_theme.large, show_row_count=False)

        table_small.setModel(model_sort)
        table_grid.setModel(model_sort)
        table_large.setModel(model_sort)
        model_sort.set_header_list(mock.header_list)
        table_small.set_header_list(mock.header_list)
        table_grid.set_header_list(mock.header_list)
        table_default.set_header_list(mock.header_list)
        table_large.set_header_list(mock.header_list)
        model_1.set_data_list(mock.data_list)

        line_edit = MLineEdit().search().small()
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(line_edit)
        main_lay.addWidget(MDivider("Small Size"))
        main_lay.addWidget(table_small)
        main_lay.addWidget(MDivider("Default Size"))
        main_lay.addLayout(switch_lay)
        main_lay.addWidget(self.loading_wrapper)
        main_lay.addWidget(MDivider("Large Size (Hide Row Count)"))
        main_lay.addWidget(table_large)
        main_lay.addWidget(MDivider("With Grid"))
        main_lay.addWidget(table_grid)
        main_lay.addStretch()
        main_lay.addWidget(MDivider('Simply use "MItemViewSet" or "MItemViewFullSet"'))
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = TableViewExample()
        dayu_theme.apply(test)
        test.show()
