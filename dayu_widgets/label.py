#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import QLabel, QSizePolicy, Qt, QSize, Property, QEvent


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
        self._elide_mode = Qt.ElideNone
        self.setProperty('dayu_text', text)

    def get_dayu_level(self):
        """Get MLabel level."""
        return self._dayu_level

    def set_dayu_level(self, value):
        """Set MLabel level"""
        self._dayu_level = value
        self.style().polish(self)

    def set_dayu_underline(self, value):
        """Set MLabel underline style."""
        self._dayu_underline = value
        self.style().polish(self)

    def get_dayu_underline(self):
        return self._dayu_underline

    def set_dayu_delete(self, value):
        """Set MLabel a delete line style."""
        self._dayu_delete = value
        self.style().polish(self)

    def get_dayu_delete(self):
        return self._dayu_delete

    def set_dayu_strong(self, value):
        """Set MLabel bold style."""
        self._dayu_strong = value
        self.style().polish(self)

    def get_dayu_strong(self):
        return self._dayu_strong

    def set_dayu_mark(self, value):
        """Set MLabel mark style."""
        self._dayu_mark = value
        self.style().polish(self)

    def get_dayu_mark(self):
        return self._dayu_mark

    def set_dayu_code(self, value):
        """Set MLabel code style."""
        self._dayu_code = value
        self.style().polish(self)

    def get_dayu_code(self):
        return self._dayu_code

    def get_elide_mode(self):
        return self._elide_mode

    def set_elide_mode(self, value):
        """Set MLabel elide mode.
        Only accepted Qt.ElideLeft/Qt.ElideMiddle/Qt.ElideRight/Qt.ElideNone"""
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
        self.setToolTip(text)

    def _update_elided_text(self):
        """
        Update the elided text on the label
        """
        _font_metrics = self.fontMetrics()
        _elided_text = _font_metrics.elidedText(self._actual_text, self._elide_mode,
                                                self.width() - 2 * 2)
        super(MLabel, self).setText(_elided_text)

    def resizeEvent(self, event):
        """
        Overridden base method called when the widget is resized.

        :param event:    The resize event
        """
        self._update_elided_text()

    def h1(self):
        """Set QLabel with h1 type."""
        self.set_dayu_level(MLabel.H1Level)
        return self

    def h2(self):
        """Set QLabel with h2 type."""
        self.set_dayu_level(MLabel.H2Level)
        return self

    def h3(self):
        """Set QLabel with h3 type."""
        self.set_dayu_level(MLabel.H3Level)
        return self

    def h4(self):
        """Set QLabel with h4 type."""
        self.set_dayu_level(MLabel.H4Level)
        return self

    def secondary(self):
        """Set QLabel with secondary type."""
        self.set_dayu_type(MLabel.SecondaryType)
        return self

    def warning(self):
        """Set QLabel with warning type."""
        self.set_dayu_type(MLabel.WarningType)
        return self

    def danger(self):
        """Set QLabel with danger type."""
        self.set_dayu_type(MLabel.DangerType)
        return self

    def strong(self):
        """Set QLabel with strong style."""
        self.set_dayu_strong(True)
        return self

    def mark(self):
        """Set QLabel with mark style."""
        self.set_dayu_mark(True)
        return self

    def code(self):
        """Set QLabel with code style."""
        self.set_dayu_code(True)
        return self

    def delete(self):
        """Set QLabel with delete style."""
        self.set_dayu_delete(True)
        return self

    def underline(self):
        """Set QLabel with underline style."""
        self.set_dayu_underline(True)
        return self

    def event(self, event):
        if event.type() == QEvent.DynamicPropertyChange and event.propertyName() == 'dayu_text':
            self.setText(self.property('dayu_text'))
        return super(MLabel, self).event(event)
