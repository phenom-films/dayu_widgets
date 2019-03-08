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
from dayu_widgets.MButton import MButton
from dayu_widgets.MBrowser import MClickBrowserFileButton, MClickBrowserFolderButton, MDragFileButton, \
    MDragFolderButton
from dayu_widgets.qt import *


class MBrowserTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MBrowserTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        browser_1 = MClickBrowserFileButton(size=MView.SmallSize, text='Browser File (Small)')
        browser_2 = MClickBrowserFileButton(size=MView.DefaultSize, text='Browser File (Default)')
        browser_3 = MClickBrowserFileButton(size=MView.LargeSize, type=MButton.PrimaryType, text='Browser File (Large)')
        lay_1 = QHBoxLayout()
        lay_1.addWidget(browser_1)
        lay_1.addWidget(browser_2)
        lay_1.addWidget(browser_3)

        browser_4 = MClickBrowserFileButton()
        label_4 = MLabel()
        browser_4.sig_file_changed.connect(label_4.setText)
        browser_5 = MClickBrowserFolderButton(text='Browser Folder')
        label_5 = MLabel()
        browser_5.sig_folder_changed.connect(label_5.setText)
        browser_6 = MDragFileButton(text='Click or drag file here')
        browser_7 = MDragFolderButton(text='Click or drag folder here')
        label_6 = MLabel()
        browser_6.sig_file_changed.connect(label_6.setText)
        label_7 = MLabel()
        browser_7.sig_folder_changed.connect(label_7.setText)

        lay_2 = QGridLayout()
        lay_2.addWidget(browser_4, 0, 0)
        lay_2.addWidget(browser_5, 0, 1)
        lay_2.addWidget(label_4, 1, 0)
        lay_2.addWidget(label_5, 1, 1)
        lay_2.addWidget(browser_6, 2, 0)
        lay_2.addWidget(browser_7, 2, 1)
        lay_2.addWidget(label_6, 3, 0)
        lay_2.addWidget(label_7, 3, 1)

        browser_8 = MDragFileButton(text='Click or drag media file here', icon=MIcon('media_fill.svg', '#cccccc'), multiple=False)
        browser_8.set_format(['.mov', '.mp4'])
        browser_8_label = MLabel()
        self.register_field('current_file', '')
        self.bind('current_file', browser_8, 'path', signal='sig_file_changed')
        self.bind('current_file', browser_8_label, 'text')

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        main_lay.addLayout(lay_1)
        main_lay.addWidget(MDivider('different Type'))
        main_lay.addLayout(lay_2)
        main_lay.addWidget(MDivider('data bind'))
        main_lay.addWidget(browser_8)
        main_lay.addWidget(browser_8_label)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_prefix_button_clicked(self):
        print 'prefix button clicked'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MBrowserTest()
    test.show()
    sys.exit(app.exec_())
