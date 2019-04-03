#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MMessage import MMessage
from dayu_widgets.MLineTabWidget import MLineTabWidget
from dayu_widgets.qt import *


class MLineTabWidgetTest(QWidget):
    def __init__(self, parent=None):
        super(MLineTabWidgetTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QVBoxLayout()

        tab_center = MLineTabWidget()
        tab_center.add_tab(MLabel('test 1'), u'Current Element')
        tab_center.add_tab(MLabel('test 2'), u'Linked Assets')
        tab_center.add_tab(MLabel('test 3'), u'Hero Shots')
        tab_center.add_tab(MLabel('test 4'), u'Linked Metadata')
        tab_center.tool_button_group.set_checked(0)

        tab_left = MLineTabWidget(alignment=Qt.AlignLeft)
        tab_left.add_tab(MLabel('test 1'), u'标签一')
        tab_left.add_tab(MLabel('test 2'), u'标签二')
        tab_left.add_tab(MLabel('test 3'), u'标签三')
        tab_left.tool_button_group.set_checked(0)

        tab_right = MLineTabWidget(alignment=Qt.AlignRight)
        tab_right.add_tab(MLabel('test 1'), u'标签一')
        tab_right.add_tab(MLabel('test 2'), u'标签二')
        tab_right.add_tab(MLabel('test 3'), u'标签三')
        tab_right.tool_button_group.set_checked(0)

        main_lay.addWidget(MDivider('Center'))
        main_lay.addWidget(tab_center)
        main_lay.addWidget(MDivider('Left'))
        main_lay.addWidget(tab_left)
        main_lay.addWidget(MDivider('Right'))
        main_lay.addWidget(tab_right)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_close_tab(self, index):
        if index > 0:
            text = self.tab_left.tabText(index)
            self.tab_left.removeTab(index)
            MMessage.info(u'成功关闭一个标签: {}'.format(text), closable=True, parent=self)
        else:
            MMessage.warning(u'请不要关闭第一个标签', closable=True, parent=self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MLineTabWidgetTest()

    from dayu_widgets import dayu_theme

    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
