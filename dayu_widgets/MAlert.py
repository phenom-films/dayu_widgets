#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from MAvatar import MAvatar
from MButton import MButton
from MLabel import MLabel
from MTheme import global_theme
from qt import *

qss = '''
QFrame#alert{{
    border: 1px solid {border};
    border-radius: 4px;
}}
QFrame#alert[type=info]{{
    border-color: {primary_light};
    background-color: {primary_opacity};
}}
QFrame#alert[type=success]{{
    border-color: {success_light};
    background-color: {success_opacity};
}}
QFrame#alert[type=warning]{{
    border-color: {warning_light};
    background-color: {warning_opacity};
}}
QFrame#alert[type=error]{{
    border-color: {error_light};
    background-color: {error_opacity};
}}
'''.format(**global_theme)


@property_mixin
class MAlert(QFrame):
    '''
    自定义 props:
        text:
        type:
    '''
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'

    def __init__(self, text='', type=None, closable=False, show_icon=True, parent=None, flags=0):
        super(MAlert, self).__init__(parent, flags)
        self.setObjectName('alert')
        self._icon_label = MAvatar(size=MView.TinySize)
        self._content_label = MLabel()
        self._close_button = MButton(size=MView.TinySize, icon=MIcon('close_line.svg'), type=MButton.IconType)
        self._close_button.clicked.connect(functools.partial(self.setVisible, False))

        self._main_lay = QHBoxLayout()
        self._main_lay.setContentsMargins(8, 8, 8, 8)
        self._main_lay.addWidget(self._icon_label)
        self._main_lay.addWidget(self._content_label)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)

        self.setLayout(self._main_lay)

        self._icon_label.setVisible(show_icon)
        self._close_button.setVisible(closable)
        self.set_type(type or MAlert.InfoType)
        self.set_text(text)

        self.setStyleSheet(qss)

    def _set_text(self, value):
        self._content_label.setProperty('text', value)
        self.setVisible(bool(value))

    def set_text(self, value):
        self.setProperty('text', value)

    def _set_type(self, value):
        self._icon_label.set_image(MPixmap('{}_fill.svg'.format(self.property('type')), global_theme.get(self.property('type'))))
        self.style().polish(self)

    def set_type(self, value):
        self.setProperty('type', value or MAlert.InfoType)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MAlert(text='hahahha')
    test.show()
    sys.exit(app.exec_())
