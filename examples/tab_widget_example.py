#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.divider import MDivider
from dayu_widgets3.label import MLabel
from dayu_widgets3.message import MMessage
from dayu_widgets3.tab_widget import MTabWidget


class TabWidgetExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TabWidgetExample, self).__init__(parent)
        self._init_ui()
        self.resize(500, 500)

    def _init_ui(self):
        main_lay = QtWidgets.QVBoxLayout()

        tab_card = MTabWidget()
        tab_card.addTab(MLabel("test 1"), "Current Element")
        tab_card.addTab(MLabel("test 2"), "Linked Assets")
        tab_card.addTab(MLabel("test 2"), "Hero Shots")
        tab_card.addTab(MLabel("test 3"), "Linked Metadata")

        self.tab_closable = MTabWidget()
        self.tab_closable.setTabsClosable(True)
        self.tab_closable.addTab(MLabel("test 1"), "标签一")
        self.tab_closable.addTab(MLabel("test 2"), "标签二")
        self.tab_closable.addTab(MLabel("test 3"), "标签三")
        self.tab_closable.tabCloseRequested.connect(self.slot_close_tab)
        main_lay.addWidget(MDivider("Normal"))
        main_lay.addWidget(tab_card)
        main_lay.addWidget(MDivider("Closable"))
        main_lay.addWidget(self.tab_closable)
        self.setLayout(main_lay)

    @QtCore.Slot(int)
    def slot_close_tab(self, index):
        if index > 0:
            text = self.tab_closable.tabText(index)
            self.tab_closable.removeTab(index)
            MMessage.info("成功关闭一个标签: {}".format(text), closable=True, parent=self)
        else:
            MMessage.warning("请不要关闭第一个标签", closable=True, parent=self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = TabWidgetExample()
        dayu_theme.apply(test)
        test.show()
