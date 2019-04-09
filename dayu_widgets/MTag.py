#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets import dayu_theme
from dayu_widgets import utils
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MTheme import QssTemplate
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin, cursor_mixin
from dayu_widgets.qt import *


@property_mixin
@cursor_mixin
class MTag(QLabel):
    sig_closed = Signal()
    sig_clicked = Signal()

    def __init__(self, text='', color=None, border=True, closable=False, parent=None):
        super(MTag, self).__init__(parent)
        self._is_pressed = False
        self._close_button = MToolButton(type=MToolButton.IconOnlyType,
                                         size=dayu_theme.tiny, icon=MIcon('close_line.svg'))
        self._close_button.clicked.connect(self.sig_closed)
        self._close_button.clicked.connect(self.close)

        self._main_lay = QHBoxLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)

        self.setLayout(self._main_lay)

        self._close_button.setVisible(closable)
        self._border = border
        self._closable = closable
        if border:
            self._style = QssTemplate('''
                MTag{
                    font-size: 12px;
                    padding: 3px;
                    color: @text_color;
                    border-radius: @border_radius;
                    border: 1px solid @border_color;
                    background-color: @background_color;
                }
                MTag:hover{
                    color: @hover_color;
                }
            ''')
        else:
            self._style = QssTemplate('''
                MTag{
                    font-size: 12px;
                    padding: 4px;
                    border-radius: @border_radius;
                    color: @text_color;
                    border: 0 solid @border_color;
                    background-color: @background_color;
                }
                MTag:hover{
                    background-color:@hover_color;
                }
            ''')
        self.setText(text)
        self.set_color(color or dayu_theme.secondary_text_color)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

    def minimumSizeHint(self, *args, **kwargs):
        orig = super(MTag, self).minimumSizeHint(*args, **kwargs)
        orig.setWidth(orig.width() + (dayu_theme.tiny if self._closable else 0))
        return orig

    def set_color(self, value):
        self.setProperty('color', value)

    def _set_color(self, value):
        if self._border:
            self.setStyleSheet(self._style.substitute(background_color=utils.fade_color(value, '15%'),
                                                      border_radius=dayu_theme.border_radius_base,
                                                      border_color=utils.fade_color(value, '35%'),
                                                      hover_color=utils.generate_color(value, 5),
                                                      text_color=value))
        else:
            self.setStyleSheet(self._style.substitute(background_color=utils.generate_color(value, 6),
                                                      border_radius=dayu_theme.border_radius_base,
                                                      border_color=utils.generate_color(value, 6),
                                                      hover_color=utils.generate_color(value, 5),
                                                      text_color=dayu_theme.text_color_inverse))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_pressed = True
        return super(MTag, self).mousePressEvent(event)

    def leaveEvent(self, event):
        self._is_pressed = False
        return super(MTag, self).leaveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self._is_pressed:
            self.sig_clicked.emit()
        self._is_pressed = False
        return super(MTag, self).mouseReleaseEvent(event)


@cursor_mixin
class MCheckableTag(QCheckBox):
    def __init__(self, text, parent=None):
        super(MCheckableTag, self).__init__(text, parent)
        self.setCheckable(True)


@cursor_mixin
class MNewTag(QWidget):
    sig_add_tag = Signal(str)

    def __init__(self, text='New Tag', parent=None):
        super(MNewTag, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        self._add_button = MToolButton(size=dayu_theme.tiny, icon=MIcon('add_line.svg'), text=text)
        self._add_button.clicked.connect(self._slot_show_edit)
        self._line_edit = MLineEdit(size=dayu_theme.tiny)
        self._line_edit.returnPressed.connect(self._slot_return_pressed)
        self._line_edit.setVisible(False)

        self._main_lay = QGridLayout()
        self._main_lay.setContentsMargins(3, 3, 3, 3)
        self._main_lay.addWidget(self._add_button, 0, 0)
        self._main_lay.addWidget(self._line_edit, 0, 0)
        self.setLayout(self._main_lay)

    def set_completer(self, completer):
        self._line_edit.setCompleter(completer)

    def _slot_show_edit(self):
        self._line_edit.setVisible(True)
        self._add_button.setVisible(False)
        self._line_edit.setFocus(Qt.MouseFocusReason)

    def _slot_return_pressed(self):
        self._line_edit.setVisible(False)
        self._add_button.setVisible(True)
        if self._line_edit.text():
            self.sig_add_tag.emit(self._line_edit.text())
        self._line_edit.clear()

    def focusOutEvent(self, *args, **kwargs):
        self._line_edit.setVisible(False)
        self._add_button.setVisible(True)
