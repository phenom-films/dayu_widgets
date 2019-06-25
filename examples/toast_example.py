#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.toast import MToast
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import QWidget, QHBoxLayout, QVBoxLayout


class ToastExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ToastExample, self).__init__(parent)
        self.setWindowTitle('Examples for MToast')
        self._init_ui()

    def _init_ui(self):
        button3 = MPushButton(text='Normal Message').primary()
        button4 = MPushButton(text='Success Message').success()
        button5 = MPushButton(text='Warning Message').warning()
        button6 = MPushButton(text='Error Message').danger()
        button3.clicked.connect(
            functools.partial(self.slot_show_message, MToast.info, {'text': u'好像没啥用'}))
        button4.clicked.connect(
            functools.partial(self.slot_show_message, MToast.success, {'text': u'领取成功'}))
        button5.clicked.connect(
            functools.partial(self.slot_show_message, MToast.warning, {'text': u'暂不支持'}))
        button6.clicked.connect(
            functools.partial(self.slot_show_message, MToast.error, {'text': u'支付失败，请重试'}))

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(button3)
        sub_lay1.addWidget(button4)
        sub_lay1.addWidget(button5)
        sub_lay1.addWidget(button6)

        loading_button = MPushButton('Loading Toast').primary()
        loading_button.clicked.connect(self.slot_show_loading)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(MLabel(u'不同的提示状态：成功、失败、加载中。默认2秒后消失'))
        main_lay.addWidget(loading_button)

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(parent=self, **config)

    def slot_set_config(self, func, config):
        func(**config)

    def slot_show_loading(self):
        msg = MToast.loading(u'正在加载中', parent=self)
        msg.sig_closed.connect(functools.partial(MToast.success, u'加载成功', self))


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    app = QApplication(sys.argv)
    test = ToastExample()
    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
