#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.divider import MDivider
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.push_button import MPushButton
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.message import MMessage
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu
from dayu_widgets.label import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *


class LineEditExample(QWidget):
    def __init__(self, parent=None):
        super(LineEditExample, self).__init__(parent)
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
        push_button = MPushButton.primary(text='Go')
        push_button.set_dayu_size(dayu_theme.small)
        push_button.setFixedWidth(40)
        line_edit_button.add_suffix_widget(push_button)

        line_edit_error = MLineEdit.error(size=dayu_theme.small)
        line_edit_error.setText('waring: file d:/ddd/ccc.jpg not exists.')

        line_edit_search = MLineEdit.search(size=dayu_theme.small)
        line_edit_search_engine = MLineEdit.search_engine(size=dayu_theme.large)
        line_edit_search_engine.add_prefix_widget(MToolButton(type=MToolButton.IconOnlyType,
                                                              icon=MIcon('filter_line.svg', '#cccccc'),
                                                              size=dayu_theme.large))
        line_edit_search_engine.returnPressed.connect(self.slot_search)
        # line_edit_search_engine.sig_delay_text_changed.connect(self.slot_search)

        line_edit_file = MLineEdit.file()
        line_edit_folder = MLineEdit.folder()

        line_edit_options = MLineEdit()
        combobox = MComboBox()
        option_menu = MMenu()
        option_menu.set_separator('|')
        option_menu.set_data([r'http://', r'https://'])
        combobox.set_menu(option_menu)
        combobox.set_value('http://')
        combobox.setFixedWidth(90)
        line_edit_options.add_prefix_widget(combobox)

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
        main_lay.addWidget(MLabel('MLineEdit.options()'))
        main_lay.addWidget(line_edit_options)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @Slot()
    def slot_search(self):
        MMessage.info(u'查无此人', parent=self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = LineEditExample()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
