#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
import functools

import examples._mock_data as mock
from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_model import MTableModel, MSortFilterModel
from dayu_widgets.item_view import MTreeView
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton
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


class TreeViewExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(TreeViewExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        model_1 = MTableModel()
        model_1.set_header_list(mock.header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)

        tree_view = MTreeView()
        tree_view.setModel(model_sort)

        model_sort.set_header_list(mock.header_list)
        tree_view.set_header_list(mock.header_list)
        model_1.set_data_list(mock.tree_data_list)

        line_edit = MLineEdit().search().small()
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        expand_all_button = MPushButton('Expand All').small()
        expand_all_button.clicked.connect(tree_view.expandAll)
        collapse_all_button = MPushButton('Collapse All').small()
        collapse_all_button.clicked.connect(tree_view.collapseAll)
        button_lay = QHBoxLayout()
        button_lay.addWidget(expand_all_button)
        button_lay.addWidget(collapse_all_button)
        button_lay.addWidget(line_edit)
        button_lay.addStretch()

        main_lay = QVBoxLayout()
        main_lay.addLayout(button_lay)
        main_lay.addWidget(tree_view)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = TreeViewExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
