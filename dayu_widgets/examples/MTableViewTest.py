#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
import functools

import dayu_widgets.examples._mock_data as mock
from dayu_widgets import dayu_theme
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MItemModel import MTableModel, MSortFilterModel
from dayu_widgets.MItemView import MTableView
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MLoading import MLoadingWrapper
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.qt import *


def h(*args):
    cls = args[0]
    widget = cls()
    for i in args:
        if isinstance(i, dict):
            for attr, value in i.get('props', {}).items():
                widget.setProperty(attr, value)
            for signal, slot in i.get('on', {}).items():
                widget.connect(widget, SIGNAL(signal), slot)
        elif isinstance(i, list):
            lay = QHBoxLayout()
            for j in i:
                lay.addWidget(j)
            widget.setLayout(lay)
    return widget


class MFetchDataThread(QThread):
    def __init__(self, parent=None):
        super(MFetchDataThread, self).__init__(parent)

    def run(self, *args, **kwargs):
        import time
        time.sleep(4)


class MTableViewTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MTableViewTest, self).__init__(parent)
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
        thread.started.connect(functools.partial(self.loading_wrapper.set_loading, True))
        thread.finished.connect(functools.partial(self.loading_wrapper.set_loading, False))
        thread.finished.connect(functools.partial(table_default.setModel, model_sort))
        button = MPushButton(text='Get Data: 4s')
        button.clicked.connect(thread.start)
        switch_lay = QHBoxLayout()
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

        line_edit = MLineEdit.search(size=dayu_theme.small)
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        main_lay = QVBoxLayout()
        main_lay.addWidget(line_edit)
        main_lay.addWidget(MDivider('Small Size'))
        main_lay.addWidget(table_small)
        main_lay.addWidget(MDivider('Default Size'))
        main_lay.addLayout(switch_lay)
        main_lay.addWidget(self.loading_wrapper)
        main_lay.addWidget(MDivider('Large Size (Hide Row Count)'))
        main_lay.addWidget(table_large)
        main_lay.addWidget(MDivider('With Grid'))
        main_lay.addWidget(table_grid)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MTableViewTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
