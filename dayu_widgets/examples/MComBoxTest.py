#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MComboBox import MComboBox
from dayu_widgets.MMenu import MMenu
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin

import random


class MComBoxTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MComBoxTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.register_field('button1_selected', u'北京')
        menu1 = MMenu()
        menu1.set_data([u'北京', u'上海', u'广州', u'深圳'])
        select1 = MComboBox()
        select1.set_menu(menu1)
        select1_small = MComboBox(size=MView.SmallSize)
        select1_small.set_menu(menu1)
        select1_large = MComboBox(size=MView.LargeSize)
        select1_large.set_menu(menu1)
        self.bind('button1_selected', select1, 'value', signal='sig_value_changed')
        self.bind('button1_selected', select1_small, 'value', signal='sig_value_changed')
        self.bind('button1_selected', select1_large, 'value', signal='sig_value_changed')

        self.register_field('button2_selected', [u'北京'])
        menu2 = MMenu(exclusive=False)
        menu2.set_data([u'北京', u'上海', u'广州', u'深圳'])
        select2 = MComboBox()
        select2.set_menu(menu2)
        self.bind('button2_selected', select2, 'value', signal='sig_value_changed')

        def dynamic_get_city():
            data = [u'北京', u'上海', u'广州', u'深圳', u'郑州', u'石家庄']
            start = random.randint(0, len(data))
            end = random.randint(start, len(data))
            return data[start:end]

        self.register_field('button3_selected', '')
        menu3 = MMenu()
        menu3.set_load_callback(dynamic_get_city)
        select3 = MComboBox()
        select3.set_menu(menu3)
        self.bind('button3_selected', select3, 'value', signal='sig_value_changed')

        a = [{'children': [{'value': u'\u6545\u5bab', 'label': u'\u6545\u5bab'},
                           {'value': u'\u5929\u575b', 'label': u'\u5929\u575b'},
                           {'value': u'\u738b\u5e9c\u4e95', 'label': u'\u738b\u5e9c\u4e95'}],
              'value': u'\u5317\u4eac',
              'label': u'\u5317\u4eac'},
             {'children': [{'children': [{'value': u'\u592b\u5b50\u5e99', 'label': u'\u592b\u5b50\u5e99'}],
                            'value': u'\u5357\u4eac',
                            'label': u'\u5357\u4eac'},
                           {'children': [{'value': u'\u62d9\u653f\u56ed', 'label': u'\u62d9\u653f\u56ed'},
                                         {'value': u'\u72ee\u5b50\u6797', 'label': u'\u72ee\u5b50\u6797'}],
                            'value': u'\u82cf\u5dde',
                            'label': u'\u82cf\u5dde'}],
              'value': u'\u6c5f\u82cf',
              'label': u'\u6c5f\u82cf'}]

        self.register_field('button4_selected', '')
        menu4 = MMenu(cascader=True)
        menu4.set_data(a)
        select4 = MComboBox()
        select4.set_menu(menu4)
        select4.set_formatter(lambda x: ' / '.join(x))
        self.bind('button4_selected', select4, 'value', signal='sig_value_changed')

        self.register_field('button5_selected', '')
        menu5 = MMenu(exclusive=False)
        menu5.set_data([u'北京', u'上海', u'广州', u'深圳'])
        select5 = MComboBox()
        select5.set_menu(menu5)
        select5.set_formatter(lambda x: ' & '.join(x))
        self.bind('button5_selected', select5, 'value', signal='sig_value_changed')

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(MLabel(u'普通单选'))
        sub_lay1.addWidget(select1_large)
        sub_lay1.addWidget(select1)
        sub_lay1.addWidget(select1_small)
        sub_lay1.addStretch()
        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(MLabel(u'多选'))
        sub_lay2.addWidget(select2)
        sub_lay2.addStretch()
        sub_lay3 = QHBoxLayout()
        sub_lay3.addWidget(MLabel(u'动态生成选项'))
        sub_lay3.addWidget(select3)
        sub_lay3.addStretch()
        sub_lay4 = QHBoxLayout()
        sub_lay4.addWidget(MLabel(u'级联选择'))
        sub_lay4.addWidget(select4)
        sub_lay4.addStretch()
        sub_lay5 = QHBoxLayout()
        sub_lay5.addWidget(MLabel(u'自定义显示'))
        sub_lay5.addWidget(select5)
        sub_lay5.addStretch()

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider(u'Select'))
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider(u'自定义格式'))
        main_lay.addLayout(sub_lay4)
        main_lay.addLayout(sub_lay5)
        main_lay.addStretch()

        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MComBoxTest()
    test.show()
    sys.exit(app.exec_())
