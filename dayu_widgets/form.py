#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import QWidget, QHBoxLayout, QVBoxLayout, QFormLayout


class MForm(QWidget):
    Horizontal = 'horizontal'
    Vertical = 'vertical'
    Inline = 'inline'

    def __init__(self, layout=None, parent=None):
        super(MForm, self).__init__(parent)
        layout = layout or MForm.Horizontal
        if layout == MForm.Inline:
            self._main_layout = QHBoxLayout()
        elif layout == MForm.Vertical:
            self._main_layout = QVBoxLayout()
        else:
            self._main_layout = QFormLayout()
        self._model = None
        self._label_list = []

    def set_model(self, m):
        self._model = m

    def set_label_align(self, align):
        for label in self._label_list:
            label.setAlignment(align)
        self._main_layout.setLabelAlignment(align)

    @classmethod
    def horizontal(cls):
        return cls(layout=cls.Horizontal)

    @classmethod
    def vertical(cls):
        return cls(layout=cls.Vertical)

    @classmethod
    def inline(cls):
        return cls(layout=cls.Inline)
