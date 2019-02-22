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
class MCircle(QWidget):
    '''
    自定义 props:
        text:
        type:
    '''
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'

    def __init__(self, radius=120, color=None, percent=25, parent=None, flags=0):
        super(MCircle, self).__init__(parent, flags)
        self._main_lay = QHBoxLayout()
        self._default_label = QLabel()
        self._default_label.setStyleSheet('color:{}'.format(global_theme.get('content')))
        self._default_label.setAlignment(Qt.AlignCenter)
        self._main_lay.addWidget(self._default_label)
        self.setLayout(self._main_lay)
        self.set_radius(radius)
        self.set_percent(percent)
        self.set_color(color or global_theme.get('primary'))

    def set_widget(self, widget):
        self._default_label.setVisible(False)
        self._main_lay.addWidget(widget)

    def _set_radius(self, value):
        border = 3 * value / 50.0 + 1
        self.setFixedSize(QSize(value + border, value + border))
        font = self._default_label.font()
        font.setPixelSize(12 + int(value / 10))
        self._default_label.setFont(font)

    def set_radius(self, value):
        self.setProperty('radius', value)

    def _set_color(self, value):
        self.update()

    def set_color(self, value):
        self.setProperty('color', value)

    def _set_percent(self, value):
        self._default_label.setText('{}%'.format(value))
        self.update()

    def set_percent(self, value):
        self.setProperty('percent', int(value))

    def paintEvent(self, event):
        radius = self.property('radius')
        pen_width = 3 * radius / 50.0
        rect_background = QRectF()
        rect_background.setSize(QSize(radius - pen_width, radius - pen_width))
        rect_background.setTopLeft(QPoint(pen_width, pen_width))
        pen_background = QPen()
        pen_background.setWidth(pen_width)
        pen_background.setColor(global_theme.get('background_dark'))
        pen_foreground = QPen()
        pen_foreground.setWidth(pen_width)
        pen_foreground.setColor(self.property('color'))
        pen_foreground.setCapStyle(Qt.RoundCap)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)
        painter.setPen(pen_background)
        painter.drawEllipse(QPoint(self.width() / 2, self.width() / 2), radius / 2.0, radius / 2.0)
        painter.setPen(pen_foreground)
        painter.drawArc(pen_width / 2.0, pen_width / 2.0, radius, radius, 90 * 16, -self.property('percent') * 3.6 * 16)
        return super(MCircle, self).paintEvent(event)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MCircle(radius=200)
    test.show()
    sys.exit(app.exec_())
