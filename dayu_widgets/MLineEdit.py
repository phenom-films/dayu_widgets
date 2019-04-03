#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets import dayu_theme
from dayu_widgets.MBrowser import MClickBrowserFileToolButton, MClickBrowserFolderToolButton
from dayu_widgets.MPushButton import MPushButton
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin, focus_shadow_mixin
from dayu_widgets.qt import *


@property_mixin
@focus_shadow_mixin
class MLineEdit(QLineEdit):

    def __init__(self, text='', size=None, parent=None):
        super(MLineEdit, self).__init__(text, parent)
        self._main_layout = QHBoxLayout()
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self._main_layout.addStretch()
        self.setProperty('dayu_size', size or dayu_theme.default_size)
        self.setLayout(self._main_layout)
        self.setProperty('history', self.property('text'))
        self.setTextMargins(2, 0, 2, 0)

    def add_prefix_widget(self, widget):
        if isinstance(widget, MPushButton):
            widget.setProperty('combine', 'horizontal')
        margin = self.textMargins()
        margin.setLeft(margin.left() + widget.width())
        self.setTextMargins(margin)
        self._main_layout.insertWidget(0, widget)
        return widget

    def add_suffix_widget(self, widget):
        if isinstance(widget, MPushButton):
            widget.setProperty('combine', 'horizontal')
        margin = self.textMargins()
        margin.setRight(margin.right() + widget.width())
        self.setTextMargins(margin)
        self._main_layout.addWidget(widget)
        return widget

    def setText(self, text):
        self.setProperty('history', u'{}\n{}'.format(self.property('history'), text))
        return super(MLineEdit, self).setText(text)

    def clear(self):
        self.setProperty('history', '')
        return super(MLineEdit, self).clear()

    @classmethod
    def search(cls, size=None, parent=None):
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MToolButton(type=MToolButton.IconOnlyType,
                                    icon=MIcon('close_line.svg'), size=size, parent=parent)
        suffix_button.clicked.connect(line_edit.clear)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText(line_edit.tr('Enter key word to search...'))
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

        line_edit = MLineEdit(size=size, parent=parent)
        line_edit.setProperty('type', 'error')
        line_edit.setReadOnly(True)
        suffix_button = MToolButton(type=MToolButton.IconOnlyType,
                                    icon=MIcon('detail_line.svg', dayu_theme.error_color),
                                    size=size)
        suffix_button.clicked.connect(functools.partial(slot_show_detail, line_edit))
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText(line_edit.tr('Error information will be here...'))
        return line_edit

    @classmethod
    def search_engine(cls, size=None, parent=None):
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MPushButton(text='Search', size=size, type=MPushButton.PrimaryType)
        suffix_button.clicked.connect(line_edit.returnPressed)
        suffix_button.setFixedWidth(100)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText(line_edit.tr('Enter key word to search...'))
        return line_edit

    @classmethod
    def file(cls, size=None, format=None, parent=None):
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MClickBrowserFileToolButton(size=size)
        suffix_button.sig_file_changed.connect(line_edit.setText)
        suffix_button.set_format(format or [])
        line_edit.textChanged.connect(suffix_button.set_path)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText(line_edit.tr('Click button to browser files'))
        return line_edit

    @classmethod
    def folder(cls, size=None, parent=None):
        line_edit = MLineEdit(size=size, parent=parent)
        suffix_button = MClickBrowserFolderToolButton(size=size)
        suffix_button.sig_folder_changed.connect(line_edit.setText)
        line_edit.textChanged.connect(suffix_button.set_path)
        line_edit.add_suffix_widget(suffix_button)
        line_edit.setPlaceholderText(line_edit.tr('Click button to browser folder'))
        return line_edit
