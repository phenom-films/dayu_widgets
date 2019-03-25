#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MLabel(QLabel):
    '''
    自定义 props:
        link: bool
    '''
    H1Type = 'h1'
    H2Type = 'h2'
    H3Type = 'h3'
    TextType = 'text'
    HelpType = 'help'

    def __init__(self, text='', type=None, link=False, parent=None, flags=0):
        super(MLabel, self).__init__(text, parent, flags)
        self.setProperty('type', type or MLabel.TextType)
        self.setTextInteractionFlags(Qt.TextBrowserInteraction | Qt.LinksAccessibleByMouse)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
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
            # TODO: can not interaction( can't select text)
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
        return cls(text=text, type=MLabel.H1Type)

    @classmethod
    def h2(cls, text=''):
        return cls(text=text, type=MLabel.H2Type)

    @classmethod
    def h3(cls, text=''):
        return cls(text=text, type=MLabel.H3Type)

    @classmethod
    def help(cls, text=''):
        return cls(text=text, type=MLabel.HelpType)
