#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *


class MDivider(MWidget):
    _property_map = None
    _orientation_map = {
        Qt.AlignCenter: 50,
        Qt.AlignLeft: 20,
        Qt.AlignRight: 80,
    }

    def __init__(self, text='', orientation=Qt.Horizontal, alignment=Qt.AlignCenter, parent=None):
        super(MDivider, self).__init__(parent)
        self._text_label = QLabel()
        self._text_label.setStyleSheet('padding:4px')
        self._left_frame = QFrame()
        self._right_frame = QFrame()
        self.main_lay = QHBoxLayout()
        self.main_lay.setContentsMargins(0, 0, 0, 0)
        self.main_lay.setSpacing(0)
        self.main_lay.addWidget(self._left_frame)
        self.main_lay.addWidget(self._text_label)
        self.main_lay.addWidget(self._right_frame)
        self.setLayout(self.main_lay)

        self.addProperty('text', text)
        self.addProperty('orientation', orientation)
        self.addProperty('alignment', alignment)

    def set_text(self, value):
        self._text_label.setProperty('text', value)
        with_text = bool(value)
        if not with_text:
            font = self.font()
            font.setPointSize(1)
            self._text_label.setFont(font)
            self._text_label.setStyleSheet('padding:0')

    def set_orientation(self, value):
        if value == Qt.Horizontal:
            self._left_frame.setVisible(True)
            self._text_label.setVisible(True)
            self._right_frame.setVisible(True)
            self._left_frame.setFrameShape(QFrame.HLine)
            self._left_frame.setFrameShadow(QFrame.Sunken)
            self._right_frame.setFrameShape(QFrame.HLine)
            self._right_frame.setFrameShadow(QFrame.Sunken)
        else:
            self._left_frame.setVisible(True)
            self._text_label.setVisible(False)
            self._right_frame.setVisible(False)
            self._left_frame.setFrameShape(QFrame.VLine)
            self._left_frame.setFrameShadow(QFrame.Plain)
            self.setFixedWidth(2)

    def set_alignment(self, value):
        self.main_lay.setStretchFactor(self._left_frame, self._orientation_map.get(value, 50))
        self.main_lay.setStretchFactor(self._right_frame, 100 - self._orientation_map.get(value, 50))

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MDivider(text='hahaha')
    test.show()
    sys.exit(app.exec_())
