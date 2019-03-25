#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MItemModel import MTableModel, MSortFilterModel
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MItemView import MTableView
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets import dayu_theme
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

class MTableViewTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MTableViewTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        data_list = [
            {
                'name': 'John Brown',
                'sex': 'Male',
                'sex_list': ['Male', 'Female'],
                'age': 18,
                'score': 89,
                'city': 'New York',
                'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
                'date': '2016-10-03',
            }, {
                'name': 'Jim Green',
                'sex': 'Male',
                'sex_list': ['Male', 'Female'],
                'age': 24,
                'score': 55,
                'city': 'London',
                'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
                'date': '2016-10-01',
            }, {
                'name': 'Zhang Xiaoming',
                'sex': 'Male',
                'sex_list': ['Male', 'Female'],
                'age': 30,
                'score': 70,
                'city': '',
                'city_list': ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou'],
                'date': '2016-10-02',
            }, {
                'name': 'Jon Snow',
                'sex': 'Female',
                'sex_list': ['Male', 'Female'],
                'age': 26,
                'score': 60,
                'city': 'Ottawa',
                'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
                'date': '2016-10-04',
            }, {
                'name': 'Li Xiaohua',
                'sex': 'Female',
                'sex_list': ['Male', 'Female'],
                'age': 18,
                'score': 97,
                'city': 'Ottawa',
                'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
                'date': '2016-10-04',
            }
        ]

        def score_color(score, y):
            if score < 60:
                return dayu_theme.color.get('error')
            elif score < 80:
                return dayu_theme.color.get('warning')
            elif score >= 90:
                return dayu_theme.color.get('success')
            return dayu_theme.color.get('info')

        header_list = [
            {
                'label': 'Name',
                'key': 'name',
                'checkable': True,
                'searchable': True,
                'icon': 'user_fill.svg'
            }, {
                'label': 'Sex',
                'key': 'sex',
                'searchable': True,
                'selectable': True,
                'icon': lambda x, y: ('{}.svg'.format(x.lower()), dayu_theme.color.get(x.lower()))
            }, {
                'label': 'Age',
                'key': 'age',
                'searchable': True,
                'editable': True,
                'display': lambda x, y: u'{} 岁'.format(x),
            }, {
                'label': 'Address',
                'key': 'city',
                'selectable': True,
                'searchable': True,
                'exclusive': False,
                'width': 140,
                'display': lambda x, y: ' & '.join(x) if isinstance(x, list) else x,
                'bg_color': lambda x, y: 'transparent' if x else dayu_theme.color.get('error')
            }, {
                'label': 'Score',
                'key': 'score',
                'searchable': True,
                'editable': True,
                'bg_color': score_color,
                'color': '#fff'
            },
            {
                'label': 'Score Copy',
                'key': 'score',
                'searchable': True,
                'color': score_color,
                'order': Qt.DescendingOrder
            },
        ]
        table_1 = MTableView(size=dayu_theme.size.small, show_row_count=True)
        self.table_2 = MTableView(size=dayu_theme.size.small, show_row_count=True)
        self.table_2.setShowGrid(True)
        table_default = MTableView(size=dayu_theme.size.medium, show_row_count=True)
        table_large = MTableView(size=dayu_theme.size.large, show_row_count=False)

        model_1 = MTableModel()
        model_1.set_header_list(header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)
        table_1.setModel(model_sort)
        table_1.load_state('table_test_1')
        self.table_2.setModel(model_sort)
        self.table_2.load_state('table_test_1')
        table_default.setModel(model_sort)
        table_default.load_state('table_test_default')
        table_large.setModel(model_sort)
        table_large.load_state('table_test_large')
        model_sort.set_header_list(header_list)
        table_1.set_header_list(header_list)
        self.table_2.set_header_list(header_list)
        table_default.set_header_list(header_list)
        table_large.set_header_list(header_list)
        model_1.set_data_list(data_list)

        line_edit = MLineEdit.search(size=dayu_theme.size.small)
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        button = MPushButton(text='show loading')
        button.clicked.connect(self.slot_show_loading)
        main_lay = QVBoxLayout()
        main_lay.addWidget(line_edit)
        main_lay.addWidget(MDivider('Small Size'))
        main_lay.addWidget(table_1)
        main_lay.addWidget(MDivider('Default Size'))
        main_lay.addWidget(table_default)
        main_lay.addWidget(MDivider('Large Size (Hide Row Count)'))
        main_lay.addWidget(table_large)
        main_lay.addWidget(MDivider('With Grid'))
        main_lay.addWidget(self.table_2)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_loading(self):
        self.table_2.show_loading()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MTableViewTest()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
