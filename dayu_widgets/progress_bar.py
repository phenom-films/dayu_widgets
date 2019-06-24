#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import QProgressBar, Qt


class MProgressBar(QProgressBar):
    '''
    props:
        status: str

    '''
    ErrorStatus = 'error'
    NormalStatus = 'primary'
    SuccessStatus = 'success'

    def __init__(self, status=None, parent=None):
        super(MProgressBar, self).__init__(parent=parent)
        self.setAlignment(Qt.AlignCenter)
        self.set_status(status or MProgressBar.NormalStatus)

    def set_status(self, value):
        self.setProperty('status', value)

    def _set_status(self, value):
        self.style().polish(self)

    # def paintEvent(self, event):
    #     pass
"""
MProgressBar {
    font-size: @font_size_small;
    color: @primary_text_color;
    border: 0 solid @border_color;
    background-color: @border_color;
    min-height: 12px;
    max-height: 12px;
    border-radius: 6px;
}

MProgressBar::chunk {
    min-height: 12px;
    max-height: 12px;
    border-radius: 5px;
}
MProgressBar[status=error]::chunk {
    background-color: @error_6;
}
MProgressBar[status=success]::chunk {
    background-color: @success_6;
}
MProgressBar[status=primary]::chunk {
    background-color: @primary_color;
}"""
