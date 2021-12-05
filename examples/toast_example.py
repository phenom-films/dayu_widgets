#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import functools

# Import third-party modules
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import QHBoxLayout
from dayu_widgets.qt import QThread
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.toast import MToast


class MWorkThread(QThread):
    def __init__(self, parent=None):
        super(MWorkThread, self).__init__(parent)

    def run(self):
        # Import built-in modules
        import time

        time.sleep(3)


class ToastExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ToastExample, self).__init__(parent)
        self.setWindowTitle("Examples for MToast")
        self._init_ui()

    def _init_ui(self):
        button3 = MPushButton(text="Normal Message").primary()
        button4 = MPushButton(text="Success Message").success()
        button5 = MPushButton(text="Warning Message").warning()
        button6 = MPushButton(text="Error Message").danger()
        button3.clicked.connect(
            functools.partial(self.slot_show_message, MToast.info, {"text": "好像没啥用"})
        )
        button4.clicked.connect(
            functools.partial(self.slot_show_message, MToast.success, {"text": "领取成功"})
        )
        button5.clicked.connect(
            functools.partial(self.slot_show_message, MToast.warning, {"text": "暂不支持"})
        )
        button6.clicked.connect(
            functools.partial(
                self.slot_show_message, MToast.error, {"text": "支付失败，请重试"}
            )
        )

        sub_lay1 = QHBoxLayout()
        sub_lay1.addWidget(button3)
        sub_lay1.addWidget(button4)
        sub_lay1.addWidget(button5)
        sub_lay1.addWidget(button6)

        loading_button = MPushButton("Loading Toast").primary()
        loading_button.clicked.connect(self.slot_show_loading)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(MLabel("不同的提示状态：成功、失败、加载中。默认2秒后消失"))
        main_lay.addWidget(loading_button)

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(parent=self, **config)

    def slot_set_config(self, func, config):
        func(**config)

    def slot_show_loading(self):
        my_thread = MWorkThread(parent=self)
        my_thread.finished.connect(self.slot_finished)
        my_thread.start()
        self.msg = MToast.loading("正在加载中", parent=self)

    def slot_finished(self):
        self.msg.close()
        MToast.success("加载成功", self)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import third-party modules
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = ToastExample()
    # Import third-party modules
    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
