#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.message import MMessage
from dayu_widgets.qt import *
from dayu_widgets.tab_widget import MTabWidget


class MTabWidgetTest(QWidget):
    def __init__(self, parent=None):
        super(MTabWidgetTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()

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
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot(int)
    def slot_close_tab(self, index):
        if index > 0:
            text = self.tab_closable.tabText(index)
            self.tab_closable.removeTab(index)
            MMessage.info("成功关闭一个标签: {}".format(text), closable=True, parent=self)
        else:
            MMessage.warning("请不要关闭第一个标签", closable=True, parent=self)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QApplication(sys.argv)
    test = MTabWidgetTest()

    # Import local modules
    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
