#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MMessage import MMessage
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MMenuTabWidget import MMenuTabWidget
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *
import functools


class MMenuTabWidgetTest(QWidget):
    def __init__(self, parent=None):
        super(MMenuTabWidgetTest, self).__init__(parent)
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
        tool_bar = MMenuTabWidget()
        tool_bar_small = MMenuTabWidget(size=dayu_theme.small)
        tool_bar_large = MMenuTabWidget(size=dayu_theme.large)
        tool_bar_large.tool_bar_insert_widget(MLabel.h3('DEMO'))
        stack_lay = QStackedLayout()
        for data_dict in item_list:
            tool_bar.add_menu(data_dict)
            tool_bar_small.add_menu(data_dict)
            stack_lay.addWidget(MLabel(data_dict.get('text')))
            tool_bar_large.add_menu(data_dict, stack_lay.count() - 1)
        tool_bar_large.tool_button_group.sig_checked_changed.connect(stack_lay.setCurrentIndex)

        tool_bar.tool_button_group.set_checked(0)
        tool_bar_small.tool_button_group.set_checked(0)
        tool_bar_large.tool_button_group.set_checked(0)
        lay = QVBoxLayout()
        lay.addWidget(MDivider('size small'))
        lay.addWidget(tool_bar_small)
        lay.addWidget(MDivider('size medium'))
        lay.addWidget(tool_bar)
        lay.addWidget(MDivider('size large'))
        lay.addWidget(tool_bar_large)
        lay.addLayout(stack_lay)
        main_lay.addLayout(lay)

        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MMenuTabWidgetTest()
    dayu_theme.apply(test)

    test.show()
    sys.exit(app.exec_())
