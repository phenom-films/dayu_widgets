#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MLabel import MLabel
from MLineEdit import MLineEdit
from MFieldMixin import MFieldMixin
from qt import *
import functools
from dayu_path import DayuPath


@property_mixin
class MSequenceFile(QWidget, MFieldMixin):
    '''
    这个类必须依赖 DayuPath
    props:
        text: basestring
    '''
    sig_is_sequence_changed = Signal(bool)

    def __init__(self, size=None, parent=None):
        super(MSequenceFile, self).__init__(parent)
        self.sequence_obj = None
        size = size or MView.SmallSize
        self._file_label = MLineEdit(size=size)
        self._file_label.setReadOnly(True)
        self._is_sequence_check_box = QCheckBox('Sequence')
        self._is_sequence_check_box.toggled.connect(functools.partial(self.setProperty, 'sequence'))
        self._is_sequence_check_box.toggled.connect(self.sig_is_sequence_changed)

        self._info_label = MLabel(type=MLabel.HelpType)
        self._error_label = MLabel(type=MLabel.HelpType)
        self._error_label.setProperty('error', True)

        seq_lay = QHBoxLayout()
        seq_lay.addWidget(self._is_sequence_check_box)
        seq_lay.addWidget(self._info_label)
        seq_lay.addWidget(self._error_label)
        seq_lay.setStretchFactor(self._is_sequence_check_box, 0)
        seq_lay.setStretchFactor(self._info_label, 0)

        self._main_lay = QVBoxLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self._main_lay.addWidget(self._file_label)
        self._main_lay.addLayout(seq_lay)
        self.setLayout(self._main_lay)
        self.set_sequence(True)

    def _set_path(self, value):
        path = DayuPath(value)
        for seq_obj in path.scan():
            self.sequence_obj = seq_obj
        self._update_info()

    def set_path(self, value):
        self.setProperty('path', value)

    def set_sequence(self, value):
        self.setProperty('sequence', value)

    def _set_sequence(self, value):
        assert isinstance(value, bool)
        if value != self._is_sequence_check_box.isChecked():
            # 更新来自代码
            self._is_sequence_check_box.setChecked(value)
            self.sig_is_sequence_changed.emit(value)
        self._update_info()

    def _update_info(self):
        self._file_label.setProperty('text', self.sequence_obj if self.property('sequence') else self.property('path'))
        if self.sequence_obj:
            self._info_label.setText(u'Format: {ext}  '
                                     u'Total: {count}  '
                                     u'Range: {start}-{end}'.format(ext=self.sequence_obj.ext,
                                                                    count=len(self.sequence_obj.frames),
                                                                    start=self.sequence_obj.frames[
                                                                        0] if self.sequence_obj.frames else '/',
                                                                    end=self.sequence_obj.frames[
                                                                        -1] if self.sequence_obj.frames else '/'))
            self._error_label.setText(
                u'Missing: {}'.format(self.sequence_obj.missing) if self.sequence_obj.missing else '')
        self._info_label.setVisible(self.property('sequence'))
        self._error_label.setVisible(self.property('sequence'))
