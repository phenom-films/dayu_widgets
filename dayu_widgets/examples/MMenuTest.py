#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MMenu import MMenu
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.qt import *


class MMenuTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MMenuTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        self.register_field('button1_selected', u'北京')
        self.register_field('button1_selected_text', lambda: self.field('button1_selected'))
        button1 = MPushButton(text='Normal Menu')
        menu1 = MMenu(parent=self)
        menu1.set_data([u'北京', u'上海', u'广州', u'深圳'])
        button1.setMenu(menu1)
        button1.clicked.connect(button1.showMenu)
        label1 = MLabel()

        self.bind('button1_selected', menu1, 'value', signal='sig_value_changed')
        self.bind('button1_selected_text', label1, 'text')

        self.register_field('button2_selected', [u'北京'])
        self.register_field('button2_selected_text', lambda: ', '.join(self.field('button2_selected')))
        button2 = MPushButton(text='Multi Select Menu')
        menu2 = MMenu(exclusive=False, parent=self)
        menu2.set_data([u'北京', u'上海', u'广州', u'深圳'])
        button2.setMenu(menu2)
        button2.clicked.connect(button2.showMenu)
        label2 = MLabel()
        self.bind('button2_selected', menu2, 'value', signal='sig_value_changed')
        self.bind('button2_selected_text', label2, 'text')

        self.register_field('button3_selected', '')
        self.register_field('button3_selected_text', lambda: self.field('button3_selected'))
        button3 = MPushButton(text=u'回调函数获取选项')
        menu3 = MMenu(parent=self)
        menu3.set_load_callback(lambda: [u'北京', u'上海', u'广州', u'深圳'])
        button3.setMenu(menu3)
        button3.clicked.connect(button2.showMenu)
        label3 = MLabel()
        self.bind('button3_selected', menu3, 'value', signal='sig_value_changed')
        self.bind('button3_selected_text', label3, 'text')

        self.register_field('button4_selected', '')
        self.register_field('button4_selected_text', lambda: ' / '.join(self.field('button4_selected')))
        button4 = MPushButton(text=u'级联选择')
        menu4 = MMenu(cascader=True, parent=self)
        menu4.set_data([u'北京/故宫', u'北京/天坛', u'北京/王府井', u'江苏/南京/夫子庙', u'江苏/苏州/拙政园', u'江苏/苏州/狮子林'])
        button4.setMenu(menu4)
        button4.clicked.connect(button4.showMenu)
        label4 = MLabel()
        self.bind('button4_selected', menu4, 'value', signal='sig_value_changed')
        self.bind('button4_selected_text', label4, 'text')

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

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(button1)
        sub_lay1.addWidget(label1)
        sub_lay2 = QHBoxLayout()
        sub_lay2.addWidget(button2)
        sub_lay2.addWidget(label2)
        sub_lay3 = QHBoxLayout()
        sub_lay3.addWidget(button3)
        sub_lay3.addWidget(label3)
        sub_lay4 = QHBoxLayout()
        sub_lay4.addWidget(button4)
        sub_lay4.addWidget(label4)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider(u'Select'))
        main_lay.addLayout(sub_lay1)
        main_lay.addLayout(sub_lay2)
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider(u'级联选择'))
        main_lay.addLayout(sub_lay4)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MMenuTest()
    from dayu_widgets.MTheme import apply_theme
    apply_theme(test)
    test.show()
    sys.exit(app.exec_())
