#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from MBrowser import MClickBrowserFileButton, MClickBrowserFolderButton
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
    min-height: {default_size}px;
    max-height: {default_size}px;
}}
QLineEdit[line_size=large]{{
    font-size: 16px;
    border-radius: 4px;
    min-height: {large_size}px;
    max-height: {large_size}px;
}}
QLineEdit[line_size=small]{{
    border-radius: 2px;
    min-height: {small_size}px;
    max-height: {small_size}px;
}}


'''.format(**global_theme)


@property_mixin
class MLineEdit(QLineEdit):

    def __init__(self, text='', size=None, parent=None):
        super(MLineEdit, self).__init__(text, parent)
        self._main_layout = QHBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.addStretch()
        self.setProperty('line_size', size or MView.DefaultSize)
        self.setLayout(self._main_layout)
        self.setStyleSheet(qss)
        self.setProperty('history', self.property('text'))
        self.setTextMargins(2, 0, 2, 0)

    def add_prefix_widget(self, widget):
        margin = self.textMargins()
        margin.setLeft(margin.left() + widget.width())
        self.setTextMargins(margin)
        self._main_layout.insertWidget(0, widget)

    def add_suffix_widget(self, widget):
        margin = self.textMargins()
        margin.setRight(margin.right() + widget.width())
        self.setTextMargins(margin)
        self._main_layout.addWidget(widget)

    def setText(self, text):
        self.setProperty('history', u'{}\n{}'.format(self.property('history'), text))
        return super(MLineEdit, self).setText(text)

    def clear(self):
        self.setProperty('history', '')
        return super(MLineEdit, self).clear()

    @classmethod
    def search(cls, size=None, parent=None):
        size = size or MView.DefaultSize
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MButton(icon=MIcon('search_line.svg', '#fff'), size=size, type=MButton.PrimaryType, parent=parent)
        suffix_button.setProperty('combine', 'horizontal')
        suffix_button.clicked.connect(line_edit.returnPressed)
        suffix_button.setFixedWidth(global_theme.get(size + '_size') + 1)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText('Enter key word to search...')
        return line_edit

    @classmethod
    def error(cls, size=None, parent=None):
        @Slot()
        def slot_show_detail(self):
            dialog = QTextEdit(self)
            dialog.setReadOnly(True)
            geo = QApplication.desktop().screenGeometry()
            dialog.setGeometry(geo.width() / 2, geo.height() / 2, geo.width() / 4, geo.height() / 4)
            dialog.setWindowTitle(self.tr('Error Detail Information'))
            dialog.setText(self.property('history'))
            dialog.setWindowFlags(Qt.Dialog)
            dialog.show()

        size = size or MView.DefaultSize
        line_edit = MLineEdit(size=size, parent=parent)
        line_edit.setProperty('type', 'error')
        line_edit.setReadOnly(True)
        suffix_button = MButton(icon=MIcon('detail_line.svg', '#fff'), size=size, type=MButton.ErrorType)
        suffix_button.setProperty('combine', 'horizontal')
        suffix_button.clicked.connect(functools.partial(slot_show_detail, line_edit))
        suffix_button.setFixedWidth(global_theme.get(size + '_size') + 1)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText('Error information will be here...')
        return line_edit

    @classmethod
    def search_engine(cls, size=None, parent=None):
        size = size or MView.LargeSize
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MButton(text='Search', size=size, type=MButton.PrimaryType)
        suffix_button.setProperty('combine', 'horizontal')
        suffix_button.clicked.connect(line_edit.returnPressed)
        suffix_button.setFixedWidth(100)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText('Enter key word to search...')
        return line_edit

    @classmethod
    def file(cls, size=None, format=None, parent=None):
        size = size or MView.DefaultSize
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MClickBrowserFileButton(size=size)
        suffix_button.sig_file_changed.connect(line_edit.setText)
        suffix_button.setFixedWidth(global_theme.get(size + '_size') + 1)
        suffix_button.setProperty('combine', 'horizontal')
        suffix_button.set_format(format or [])
        line_edit.textChanged.connect(suffix_button.set_path)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText('Click button to browser files')
        return line_edit

    @classmethod
    def folder(cls, size=None, parent=None):
        size = size or MView.DefaultSize
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MClickBrowserFolderButton(size=size)
        suffix_button.sig_folder_changed.connect(line_edit.setText)
        line_edit.textChanged.connect(suffix_button.set_path)
        suffix_button.setFixedWidth(global_theme.get(size + '_size') + 1)
        suffix_button.setProperty('combine', 'horizontal')
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText('Click button to browser folder')
        return line_edit
