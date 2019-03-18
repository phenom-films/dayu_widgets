#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MTheme import global_theme
from dayu_widgets.qt import *

qss = '''
QLabel{{
    padding: 2px;
}}
QLabel[type=main_head]{{
    {main_head_font}
    {font_family}
}}
QLabel[type=sub_head]{{
    {sub_head_font}
    {font_family}
}}
QLabel[type=small_head]{{
    {small_head_font}
    {font_family}
}}
QLabel[type=text]{{
    {text_font}
    {font_family}
}}
QLabel[type=help]{{
    {help_font}
    {font_family}
}}

QLabel[link=true]{{
    color: {primary};
}}
QLabel[link=true]:hover{{
    color: {primary_light};
}}
QLabel[link=true]:pressed{{
    color: {primary_dark};
}}

QLabel[error=true]{{
    color: {error_light};
}}

QLabel:disabled{{
    {disabled_font}
    {font_family}
}}
'''.format(**global_theme)


@property_mixin
class MLabel(QLabel):
    '''
    自定义 props:
        type: enum
        link: bool
    '''
    MainHeadType = 'main_head'
    SubHeadType = 'sub_head'
    SmallHeadType = 'small_head'
    TextType = 'text'
    HelpType = 'help'

    def __init__(self, text='', type=None, link=False, parent=None, flags=0):
        super(MLabel, self).__init__(text, parent, flags)
        self.setProperty('type', type or MLabel.TextType)
        self.setTextInteractionFlags(Qt.TextBrowserInteraction | Qt.LinksAccessibleByMouse)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setStyleSheet(qss)
        self.set_link(link)
        self.elide_mode = None

    def _set_link(self, value):
        self.setCursor(Qt.PointingHandCursor if value else Qt.ArrowCursor)
        self.style().polish(self)

    def set_link(self, value):
        self.setProperty('link', value)

    def set_elide_mode(self, value):
        self.elide_mode = value
        self.update()

    def minimumSizeHint(self):
        return QSize(1, self.fontMetrics().height())

    def paintEvent(self, event):
        if self.elide_mode is None:
            return QLabel.paintEvent(self, event)
        else:
            # TODO: no interaction( can't select text)
            _text = self.text()
            if not _text:
                return
            painter = QPainter(self)
            font_metrics = painter.fontMetrics()
            elided_text = font_metrics.elidedText(_text, self.elide_mode, self.width() - 2 * 2)
            painter.drawText(QPoint(2, font_metrics.ascent() + 3), elided_text)
            painter.end()

    @classmethod
    def h1(cls, text=''):
        return cls(text=text, type=MLabel.MainHeadType)

    @classmethod
    def h2(cls, text=''):
        return cls(text=text, type=MLabel.SubHeadType)

    @classmethod
    def h3(cls, text=''):
        return cls(text=text, type=MLabel.SmallHeadType)

    @classmethod
    def help(cls, text=''):
        return cls(text=text, type=MLabel.HelpType)
