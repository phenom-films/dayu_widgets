#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MFieldMixin import MFieldMixin
from MTheme import global_theme
from qt import *

qss = '''
QProgressBar {{
    {text_font}
    {font_family}
    color: #555;
    border: 0 solid {border};
    background-color: {border};
    min-height: 12px;
    max-height: 12px;
    border-radius: 6px;
}}

QProgressBar::chunk {{
    min-height: 12px;
    max-height: 12px;
    border-radius: 5px;
}}
QProgressBar[status=error]::chunk {{
    background-color: {error};
}}
QProgressBar[status=success]::chunk {{
    background-color: {success};
}}
QProgressBar[status=primary]::chunk {{
    background-color: {primary};
}}
'''.format(**global_theme)


@property_mixin
class MProgress(QProgressBar, MFieldMixin):
    '''
    props:
        status: int
            signal: sig_checked_changed

    '''
    ErrorStatus = 'error'
    NormalStatus = 'primary'
    SuccessStatus = 'success'

    def __init__(self, status=None, parent=None):
        super(MProgress, self).__init__(parent=parent)
        self.setAlignment(Qt.AlignCenter)
        self.set_status(status or MProgress.NormalStatus)
        self.setStyleSheet(qss)

    def set_status(self, value):
        self.setProperty('status', value)

    def _set_status(self, value):
        self.style().polish(self)
