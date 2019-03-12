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
from dayu_widgets.MTableView import MTableView
from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *


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
                return global_theme.get('error')
            elif score < 80:
                return global_theme.get('warning')
            elif score >= 90:
                return global_theme.get('success')
            return global_theme.get('info')

        header_list = [
            {
                'title': 'Name',
                'key': 'name',
                'checkable': True,
                'searchable': True,
                'icon': 'user_fill.svg'
            }, {
                'title': 'Sex',
                'key': 'sex',
                'searchable': True,
                'selectable': True,
                'icon': lambda x, y: ('{}.svg'.format(x.lower()), global_theme.get(x.lower()))
            }, {
                'title': 'Age',
                'key': 'age',
                'searchable': True,
                'editable': True,
                'display': lambda x, y: u'{} 岁'.format(x),
            }, {
                'title': 'Address',
                'key': 'city',
                'selectable': True,
                'searchable': True,
                'exclusive': False,
                'width': 140,
                'display': lambda x, y: ' & '.join(x) if isinstance(x, list) else x,
                'bg_color': lambda x, y: 'transparent' if x else global_theme.get('error')
            }, {
                'title': 'Score',
                'key': 'score',
                'searchable': True,
                'editable': True,
                'bg_color': score_color,
                'color': '#fff'
            },
            {
                'title': 'Score Copy',
                'key': 'score',
                'searchable': True,
                'color': score_color,
                'order': Qt.DescendingOrder
            },
        ]
        table_1 = MTableView(size=MView.SmallSize, show_row_count=True)
        table_2 = MTableView(size=MView.SmallSize, show_row_count=True)
        table_2.setShowGrid(True)
        table_default = MTableView(size=MView.DefaultSize, show_row_count=True)
        table_large = MTableView(size=MView.LargeSize, show_row_count=False)

        model_1 = MTableModel()
        model_1.set_header_list(header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)
        table_1.setModel(model_sort)
        table_1.load_state('table_test_1')
        table_2.setModel(model_sort)
        table_2.load_state('table_test_1')
        table_default.setModel(model_sort)
        table_default.load_state('table_test_default')
        table_large.setModel(model_sort)
        table_large.load_state('table_test_large')
        model_sort.set_header_list(header_list)
        table_1.set_header_list(header_list)
        table_2.set_header_list(header_list)
        table_default.set_header_list(header_list)
        table_large.set_header_list(header_list)
        model_1.set_data_list(data_list)

        line_edit = MLineEdit.search(size=MView.SmallSize)
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        main_lay = QVBoxLayout()
        main_lay.addWidget(line_edit)
        main_lay.addWidget(MDivider('Small Size'))
        main_lay.addWidget(table_1)
        main_lay.addWidget(MDivider('Default Size'))
        main_lay.addWidget(table_default)
        main_lay.addWidget(MDivider('Large Size (Hide Row Count)'))
        main_lay.addWidget(table_large)
        main_lay.addWidget(MDivider('With Grid'))
        main_lay.addWidget(table_2)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MTableViewTest()
    test.show()
    sys.exit(app.exec_())
