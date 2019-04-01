#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.MMessage import MMessage
from dayu_widgets.MLabel import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *


class MLineEditTest(QWidget):
    def __init__(self, parent=None):
        super(MLineEditTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        size_list = [('Large', dayu_theme.large),
                     ('Medium', dayu_theme.medium),
                     ('Small', dayu_theme.small)]
        size_lay = QVBoxLayout()
        for label, size in size_list:
            line_edit_size = MLineEdit(size=size)
            line_edit_size.setPlaceholderText(label)
            size_lay.addWidget(line_edit_size)

        line_edit_icon = MLineEdit(text='Xiao Hua', size=dayu_theme.small)
        tool_button = MToolButton(type=MToolButton.IconOnlyType, icon=MIcon('female.svg'), size=dayu_theme.small)
        line_edit_icon.add_suffix_widget(tool_button)

        line_edit_button = MLineEdit(text='Beijing', size=dayu_theme.small)
        push_button = MPushButton(text='Go', size=dayu_theme.small, type='primary')
        line_edit_button.add_suffix_widget(push_button)

        line_edit_error = MLineEdit.error(size=dayu_theme.small)
        line_edit_error.setText('waring: file d:/ddd/ccc.jpg not exists.')

        line_edit_search = MLineEdit.search(size=dayu_theme.small)
        line_edit_search_engine = MLineEdit.search_engine(size=dayu_theme.large)
        line_edit_search_engine.add_prefix_widget(MToolButton(type=MToolButton.IconOnlyType,
                                                              icon=MIcon('filter_line.svg', '#cccccc'),
                                                              size=dayu_theme.large))
        line_edit_search_engine.returnPressed.connect(self.slot_search)

        line_edit_file = MLineEdit.file()
        line_edit_folder = MLineEdit.folder()

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different size'))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider('icon/button'))
        main_lay.addWidget(line_edit_icon)
        main_lay.addWidget(line_edit_button)
        main_lay.addWidget(MDivider('preset'))

        main_lay.addWidget(MLabel('MLineEdit.error()'))
        main_lay.addWidget(line_edit_error)
        main_lay.addWidget(MLabel('MLineEdit.search()'))
        main_lay.addWidget(line_edit_search)
        main_lay.addWidget(MLabel('MLineEdit.search_engine()'))
        main_lay.addWidget(line_edit_search_engine)
        main_lay.addWidget(MLabel('MLineEdit.file()'))
        main_lay.addWidget(line_edit_file)
        main_lay.addWidget(MLabel('MLineEdit.folder()'))
        main_lay.addWidget(line_edit_folder)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_search(self):
        MMessage.info(u'查无此人', parent=self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MLineEditTest()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
