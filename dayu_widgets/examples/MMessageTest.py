#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.MButton import MButton
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MMessage import MMessage
from dayu_widgets.MButtonGroup import MButtonGroup
from dayu_widgets.MLabel import MLabel
import functools


class MMessageTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MMessageTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        button3 = MButton(text='Normal Message', type=MButton.PrimaryType)
        button4 = MButton(text='Success Message', type=MButton.SuccessType)
        button5 = MButton(text='Warning Message', type=MButton.WarningType)
        button6 = MButton(text='Error Message', type=MButton.ErrorType)
        button3.clicked.connect(functools.partial(self.slot_show_message, MMessage.info, {'content': u'这是一条普通提示'}))
        button4.clicked.connect(functools.partial(self.slot_show_message, MMessage.success, {'content': u'恭喜你，成功啦！'}))
        button5.clicked.connect(functools.partial(self.slot_show_message, MMessage.warning, {'content': u'我警告你哦！'}))
        button6.clicked.connect(functools.partial(self.slot_show_message, MMessage.error, {'content': u'失败了！'}))

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(button3)
        sub_lay1.addWidget(button4)
        sub_lay1.addWidget(button5)
        sub_lay1.addWidget(button6)

        button_duration = MButton(text='show 5s Message')
        button_duration.clicked.connect(functools.partial(self.slot_show_message, MMessage.info,
                                                          {'content': u'该条消息将显示10秒后关闭',
                                                           'duration': 5
                                                           }))
        button_closable = MButton(text='closable Message')
        button_closable.clicked.connect(functools.partial(self.slot_show_message, MMessage.info,
                                                          {'content': u'可手动关闭提示',
                                                           'closable': True
                                                           }))
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(MLabel(u'不同的提示状态：普通、成功、警告、错误。默认2秒后消失'))
        main_lay.addWidget(MDivider('set duration'))
        main_lay.addWidget(button_duration)
        main_lay.addWidget(MLabel(u'自定义时长，config中设置duration值，单位为秒'))

        main_lay.addWidget(MDivider('set closable'))
        main_lay.addWidget(button_closable)
        main_lay.addWidget(MLabel(u'设置是否可关闭，config中设置closable 为 True'))

        button_grp = MButtonGroup()
        for text, func, arg in [
            ('set duration to 1s', MMessage.config, {'duration': 1}),
            ('set duration to 10s', MMessage.config, {'duration': 10}),
            ('set top to 5', MMessage.config, {'top': 5}),
            ('set top to 50', MMessage.config, {'top': 50}),
        ]:
            button = MButton(text=text)
            button.clicked.connect(functools.partial(self.slot_set_config, func, arg))
            button_grp.add_button(button)

        main_lay.addWidget(MDivider('set global setting'))
        main_lay.addWidget(button_grp)
        main_lay.addWidget(MLabel(u'全局设置默认duration（默认2秒）；top（离parent顶端的距离，默认24px）'))

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(config, parent=self)

    def slot_set_config(self, func, config):
        func(**config)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MMessageTest()
    test.show()
    sys.exit(app.exec_())
