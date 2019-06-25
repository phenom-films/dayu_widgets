#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
MDivider
"""
from dayu_widgets.label import MLabel
from dayu_widgets.qt import QWidget, Qt, QFrame, QHBoxLayout, Property


class MDivider(QWidget):
    '''
    A divider line separates different content.

    Property:
        dayu_text: basestring
    '''
    _alignment_map = {
        Qt.AlignCenter: 50,
        Qt.AlignLeft: 20,
        Qt.AlignRight: 80,
    }

    def __init__(self, text='', orientation=Qt.Horizontal, alignment=Qt.AlignCenter, parent=None):
        super(MDivider, self).__init__(parent)
        self._orient = orientation
        self._text_label = MLabel().secondary()
        self._left_frame = QFrame()
        self._right_frame = QFrame()
        self._main_lay = QHBoxLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self._main_lay.setSpacing(0)
        self._main_lay.addWidget(self._left_frame)
        self._main_lay.addWidget(self._text_label)
        self._main_lay.addWidget(self._right_frame)
        self.setLayout(self._main_lay)

        if orientation == Qt.Horizontal:
            self._left_frame.setFrameShape(QFrame.HLine)
            self._left_frame.setFrameShadow(QFrame.Sunken)
            self._right_frame.setFrameShape(QFrame.HLine)
            self._right_frame.setFrameShadow(QFrame.Sunken)
        else:
            self._text_label.setVisible(False)
            self._right_frame.setVisible(False)
            self._left_frame.setFrameShape(QFrame.VLine)
            self._left_frame.setFrameShadow(QFrame.Plain)
            self.setFixedWidth(2)
        self._main_lay.setStretchFactor(self._left_frame,
                                        self._alignment_map.get(alignment, 50))
        self._main_lay.setStretchFactor(self._right_frame,
                                        100 - self._alignment_map.get(alignment, 50))
        self._text = None
        self.set_dayu_text(text)

    def set_dayu_text(self, value):
        """
        Set the divider's text.
        When text is empty, hide the text_label and right_frame to ensure the divider not has a gap.

        :param value: basestring
        :return: None
        """
        self._text = value
        self._text_label.setText(value)
        if self._orient == Qt.Horizontal:
            self._text_label.setVisible(bool(value))
            self._right_frame.setVisible(bool(value))

    def get_dayu_text(self):
        """
        Get current text
        :return: basestring
        """
        return self._text

    dayu_text = Property(basestring, get_dayu_text, set_dayu_text)

    @classmethod
    def left(cls, text=''):
        """Create a horizontal divider with text at left."""
        return cls(text, alignment=Qt.AlignLeft)

    @classmethod
    def right(cls, text=''):
        """Create a horizontal divider with text at right."""
        return cls(text, alignment=Qt.AlignRight)

    @classmethod
    def center(cls, text=''):
        """Create a horizontal divider with text at center."""
        return cls(text, alignment=Qt.AlignCenter)

    @classmethod
    def vertical(cls):
        """Create a vertical divider"""
        return cls(orientation=Qt.Vertical)
