#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.6
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import QSizeGrip, QTextEdit, QGridLayout, Qt


class MSizeGrip(QSizeGrip):
    def __init__(self, parent=None):
        super(MSizeGrip, self).__init__(parent)


class MTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(MTextEdit, self).__init__(parent)
        self.setWindowFlags(Qt.SubWindow)
        self._size_grip = MSizeGrip(self)
        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._size_grip, 0, 0, Qt.AlignBottom | Qt.AlignRight)
        self.setLayout(layout)
        self._size_grip.setVisible(False)

    def autosize(self):
        self.textChanged.connect(self._autosize_text_edit)
        return self

    def _autosize_text_edit(self):
        # w = self.width()
        doc = self.document()
        print (self.width(), doc.lineCount(), doc.idealWidth())

    def resizeable(self):
        """Show the size grip on bottom right. User can use it to resize MTextEdit"""
        self._size_grip.setVisible(True)
        return self
