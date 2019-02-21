#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MButton import MButton
from MTheme import global_theme
from qt import *

qss = '''
QLineEdit{{
    {text_font}
    border: 1px solid {border};
    border-radius: 3px;
}}

QLineEdit:focus{{
    border: 1px solid {primary};
}}


QLineEdit[type=error]{{
    color: {error};
}}
QLineEdit[type=error]:focus{{
    border: 1px solid {error};
}}

QLineEdit[line_size=default]{{
    
}}
QLineEdit[line_size=large]{{
    font-size: 16px;
    border-radius: 4px;
}}
QLineEdit[line_size=small]{{
    border-radius: 2px;
}}


'''.format(**global_theme)


# @property_mixin
class MLineEdit(QLineEdit):
    sig_prefix_button_clicked = Signal()
    sig_suffix_button_clicked = Signal()

    SearchType = 'search'
    ErrorType = 'error'
    SearchEngineType = 'search_engine'

    LargeSize = 'large'
    DefaultSize = 'default'
    SmallSize = 'small'
    _alignment_map = {
        Qt.AlignCenter: 50,
        Qt.AlignLeft: 20,
        Qt.AlignRight: 80,
    }

    def __init__(self, text='', type=None, prefix_icon=None, prefix_text=None, suffix_icon=None, suffix_text=None,
                 size=None, parent=None):
        super(MLineEdit, self).__init__(text, parent)
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        margin = QMargins(4, 2, 4, 2)
        fixed_height = global_theme.get((size or MLineEdit.DefaultSize) + '_size') + 1
        self.setFixedHeight(fixed_height)
        self.setProperty('line_size', size or MLineEdit.DefaultSize)
        if prefix_icon or prefix_text:
            prefix_button = MButton(text=prefix_text, icon=prefix_icon, size=size, type=MButton.PrimaryType)
            prefix_button.setProperty('combine', 'horizontal')
            prefix_button.setFixedWidth(fixed_height)
            prefix_button.clicked.connect(self.sig_prefix_button_clicked)
            button_layout.addWidget(prefix_button)
            margin.setLeft(prefix_button.width() + 4)
        button_layout.addStretch()
        if type or suffix_icon or suffix_text:
            self.setProperty('type', type)
            if type == MLineEdit.ErrorType:
                self.setReadOnly(True)
                suffix_button = MButton(icon=MIcon('icon-detail.png'), size=size, type=MButton.ErrorType)
                suffix_button.clicked.connect(self.slot_show_detail)
                suffix_button.setFixedWidth(fixed_height)
                self.setPlaceholderText('Error information will be here...')
            elif type == MLineEdit.SearchType:
                suffix_button = MButton(icon=MIcon('icon-search.png'), size=size, type=MButton.PrimaryType)
                suffix_button.clicked.connect(self.returnPressed)
                suffix_button.setFixedWidth(fixed_height)
                self.setPlaceholderText('Enter key word to search...')
            elif type == MLineEdit.SearchEngineType:
                suffix_button = MButton(text='Search', size=size, type=MButton.PrimaryType)
                suffix_button.clicked.connect(self.returnPressed)
                suffix_button.setFixedWidth(100)
                self.setPlaceholderText('Enter key word to search...')
            else:
                suffix_button = MButton(text=suffix_text, icon=suffix_icon, size=size, type=MButton.PrimaryType)
                if not suffix_text:
                    suffix_button.setFixedWidth(fixed_height)
            suffix_button.clicked.connect(self.sig_suffix_button_clicked)
            suffix_button.setProperty('combine', 'horizontal')
            button_layout.addWidget(suffix_button)
            margin.setRight(suffix_button.width() + 4)

        self.setTextMargins(margin)
        self.setLayout(button_layout)
        self.setStyleSheet(qss)
        self.setProperty('content', self.property('text'))

    def append(self, text):
        self.setProperty('text', text)
        self.setProperty('content', u'{}\n{}'.format(self.property('content'), text))

    def setText(self, text):
        self.setProperty('content', text)
        return super(MLineEdit, self).setText(text)

    def clear(self):
        self.setProperty('content', '')
        return super(MLineEdit, self).clear()

    @Slot()
    def slot_show_detail(self):
        dialog = QTextEdit(self)
        dialog.setReadOnly(True)
        geo = QApplication.desktop().screenGeometry()
        dialog.setGeometry(geo.width() / 2, geo.height() / 2, geo.width() / 4, geo.height() / 4)
        dialog.setWindowTitle(self.tr('Error Detail Information'))
        dialog.setText(self.property('content'))
        dialog.setWindowFlags(Qt.Dialog)
        dialog.show()
