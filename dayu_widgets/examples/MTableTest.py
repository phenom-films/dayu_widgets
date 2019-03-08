#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
from PySide.QtSvg import *
from dayu_widgets.qt import *
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MTable import MTable
from dayu_widgets.MItemModel import MTableModel, MSortFilterModel


class MTableTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MTableTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        data_list = [
            {
                'name': 'John Brown',
                'sex': 'Male',
                'sex_list': ['Male', 'Female'],
                'age': 18,
                'city': 'New York',
                'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
                'date': '2016-10-03',
            }, {
                'name': 'Jim Green',
                'sex': 'Male',
                'sex_list': ['Male', 'Female'],
                'age': 24,
                'city': 'London',
                'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
                'date': '2016-10-01',
            }, {
                'name': 'Zhang Xiaoming',
                'sex': 'Male',
                'sex_list': ['Male', 'Female'],
                'age': 30,
                'city': '',
                'city_list': ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou'],
                'date': '2016-10-02',
            }, {
                'name': 'Jon Snow',
                'sex': 'Female',
                'sex_list': ['Male', 'Female'],
                'age': 26,
                'city': 'Ottawa',
                'city_list': ['New York', 'Ottawa', 'London', 'Sydney'],
                'date': '2016-10-04',
            }
        ]
        header_list = [
            {'title': 'Name', 'key': 'name', 'checkable': True},
            {'title': 'Sex', 'key': 'sex', 'selectable': True},
            {'title': 'Age', 'key': 'age', 'editable': True},
            {'title': 'Address', 'key': 'city',
             'selectable': True, 'exclusive': False, 'width': 200,
             'display': lambda x, y: ' & '.join(x) if isinstance(x, list) else x},
        ]
        table_1 = MTable(size=MView.SmallSize, show_row_count=True)
        # table_1.setShowGrid(True)
        model_1 = MTableModel()
        model_1.set_header_list(header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)
        table_1.setModel(model_sort)
        table_1.set_header_list(header_list)
        table_1.load_state('table_test_1')
        model_1.set_data_list(data_list)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('normal'))
        main_lay.addWidget(table_1)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def computed_text(self):
        return 'Clicked: ' + str(self.field('count'))

    def slot_change_divider_text(self):
        self.set_field('count', self.field('count') + 1)

    def closeEvent(self, *args, **kwargs):
        return super(MTableTest, self).closeEvent(*args, **kwargs)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MTableTest()
    test.show()
    sys.exit(app.exec_())
