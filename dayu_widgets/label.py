#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import QLabel, QSizePolicy, Qt, QSize, QPainter, QPoint, Property


class MLabel(QLabel):
    """
    Display title in different level.
    Property:
        dayu_level: integer
        dayu_type: str
    """
    SecondaryType = 'secondary'
    WarningType = 'warning'
    DangerType = 'danger'
    H1Level = 1
    H2Level = 2
    H3Level = 3
    H4Level = 4

    def __init__(self, text='', parent=None, flags=0):
        super(MLabel, self).__init__(text, parent, flags)
        self.setTextInteractionFlags(Qt.TextBrowserInteraction | Qt.LinksAccessibleByMouse)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        self._actual_text = text
        self._dayu_type = ''
        self._dayu_underline = False
        self._dayu_mark = False
        self._dayu_delete = False
        self._dayu_strong = False
        self._dayu_code = False
        self._dayu_level = 0
        self._elide_mode = Qt.ElideRight
        self.setText(text)

    def get_dayu_level(self):
        """Get MTitle level."""
        return self._dayu_level

    def set_dayu_level(self, value):
        """Set MTitle level"""
        self._dayu_level = value
        self.style().polish(self)

    def set_dayu_underline(self, value):
        self._dayu_underline = value
        self.style().polish(self)

    def get_dayu_underline(self):
        return self._dayu_underline

    def set_dayu_delete(self, value):
        self._dayu_delete = value
        self.style().polish(self)

    def get_dayu_delete(self):
        return self._dayu_delete

    def set_dayu_strong(self, value):
        self._dayu_strong = value
        self.style().polish(self)

    def get_dayu_strong(self):
        return self._dayu_strong

    def set_dayu_mark(self, value):
        self._dayu_mark = value
        self.style().polish(self)

    def get_dayu_mark(self):
        return self._dayu_mark

    def set_dayu_code(self, value):
        self._dayu_code = value
        self.style().polish(self)

    def get_dayu_code(self):
        return self._dayu_code

    def get_elide_mode(self):
        return self._elide_mode

    def set_elide_mode(self, value):
        self._elide_mode = value
        self._update_elided_text()

    def get_dayu_type(self):
        return self._dayu_type

    def set_dayu_type(self, value):
        self._dayu_type = value
        self.style().polish(self)

    dayu_level = Property(int, get_dayu_level, set_dayu_level)
    dayu_type = Property(str, get_dayu_type, set_dayu_type)
    dayu_underline = Property(bool, get_dayu_underline, set_dayu_underline)
    dayu_delete = Property(bool, get_dayu_delete, set_dayu_delete)
    dayu_strong = Property(bool, get_dayu_strong, set_dayu_strong)
    dayu_mark = Property(bool, get_dayu_mark, set_dayu_mark)
    dayu_code = Property(bool, get_dayu_code, set_dayu_code)
    dayu_elide_mod = Property(Qt.TextElideMode, get_dayu_code, set_dayu_code)

    def minimumSizeHint(self):
        return QSize(1, self.fontMetrics().height())

    def text(self):
        """
        Overridden base method to return the original unmodified text

        :returns:   The original unmodified text
        """
        return self._actual_text

    def setText(self, text):
        """
        Overridden base method to set the text on the label

        :param text:    The text to set on the label
        """
        self._actual_text = text
        self._update_elided_text()

    def _update_elided_text(self):
        """
        Update the elided text on the label
        """
        font_metrics = self.fontMetrics()
        elided_text = font_metrics.elidedText(self._actual_text, self._elide_mode,
                                              self.width() - 2 * 2)
        super(MLabel, self).setText(elided_text)

    def resizeEvent(self, event):
        """
        Overridden base method called when the widget is resized.

        :param event:    The resize event
        """
        self._update_elided_text()

    @classmethod
    def h1(cls, text=''):
        """Create a QLabel with h1 type."""
        ins = cls(text=text)
        ins.set_dayu_level(MLabel.H1Level)
        return ins

    @classmethod
    def h2(cls, text=''):
        """Create a QLabel with h2 type."""
        ins = cls(text=text)
        ins.set_dayu_level(MLabel.H2Level)
        return ins

    @classmethod
    def h3(cls, text=''):
        """Create a QLabel with h3 type."""
        ins = cls(text=text)
        ins.set_dayu_level(MLabel.H3Level)
        return ins

    @classmethod
    def h4(cls, text=''):
        """Create a QLabel with h4 type."""
        ins = cls(text=text)
        ins.set_dayu_level(MLabel.H4Level)
        return ins

    @classmethod
    def secondary(cls, text=''):
        """Create a QLabel with secondary type."""
        ins = cls(text=text)
        ins.set_dayu_type(MLabel.SecondaryType)
        return ins

    @classmethod
    def warning(cls, text=''):
        """Create a QLabel with warning type."""
        ins = cls(text=text)
        ins.set_dayu_type(MLabel.WarningType)
        return ins

    @classmethod
    def danger(cls, text=''):
        """Create a QLabel with danger type."""
        ins = cls(text=text)
        ins.set_dayu_type(MLabel.DangerType)
        return ins

    @classmethod
    def strong(cls, text=''):
        """Create a QLabel with strong style."""
        ins = cls(text=text)
        ins.set_dayu_strong(True)
        return ins

    @classmethod
    def mark(cls, text=''):
        """Create a QLabel with mark style."""
        ins = cls(text=text)
        ins.set_dayu_mark(True)
        return ins

    @classmethod
    def code(cls, text=''):
        """Create a QLabel with code style."""
        ins = cls(text=text)
        ins.set_dayu_code(True)
        return ins

    @classmethod
    def delete(cls, text=''):
        """Create a QLabel with delete style."""
        ins = cls(text=text)
        ins.set_dayu_delete(True)
        return ins

    @classmethod
    def underline(cls, text=''):
        """Create a QLabel with underline style."""
        ins = cls(text=text)
        ins.set_dayu_underline(True)
        return ins
