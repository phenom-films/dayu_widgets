#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MMessage import MMessage
from dayu_widgets.MToolBar import MToolBar
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *
import functools


class MToolBarTest(QWidget):
    def __init__(self, parent=None):
        super(MToolBarTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()
        item_list = [
            {'text': 'Overview', 'icon': MIcon('home_line.svg'),
             'clicked': functools.partial(MMessage.info, u'首页', parent=self)},
            {'text': u'我的', 'icon': MIcon('user_line.svg'),
             'clicked': functools.partial(MMessage.info, u'编辑账户', parent=self)},
            {'text': u'Notice', 'icon': MIcon('alert_line.svg'),
             'clicked': functools.partial(MMessage.info, u'查看通知', parent=self)},
        ]
        tool_bar = MToolBar()
        tool_bar_small = MToolBar(size=dayu_theme.size.small)
        tool_bar_large = MToolBar(size=dayu_theme.size.large)
        tool_bar.set_item_list(item_list)
        tool_bar_small.set_item_list(item_list)
        tool_bar_large.set_item_list(item_list)

        lay = QVBoxLayout()
        lay.addWidget(tool_bar)
        lay.addWidget(tool_bar_small)
        lay.addWidget(tool_bar_large)
        main_lay.addLayout(lay)

        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MToolBarTest()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
