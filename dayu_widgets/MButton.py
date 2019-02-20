#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from qt import *
from static import request_file

qss = '''
QPushButton {
    color: white;
    border-radius: 4px;
    font-size: 12px;
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}


QPushButton[button_size=large]{
    font-size:14px;
    padding: 1px 10px;
    height: 36px;
}
QPushButton[button_size=default]{
    padding: 0 12px;
    height: 32px;
}
QPushButton[button_size=small]{
    height: 24px;
}


QPushButton[type=default]{
    color: grey;
    background-color: #f8f8f9;
    border: 1px solid #dcdee2;
}
QPushButton[type=default]:hover{
    color: #2d8cf0;
    border-color: #5cadff;
}
QPushButton[type=default]:pressed{
    color: #2b85e4;
    border-color: #2b85e4;
}


QPushButton[type=primary]{
    background-color: #2d8cf0;

}
QPushButton[type=primary]:hover{
    background-color: #5cadff;

}
QPushButton[type=primary]:pressed{
    background-color: #2b85e4;
}


QPushButton[type=info]{
    background-color: #2db7f5;
}
QPushButton[type=info]:hover{
    background-color: #57c5f7;
}
QPushButton[type=info]:pressed{
    background-color: #2baee9;
}


QPushButton[type=success]{
    background-color: #19be6b;
}
QPushButton[type=success]:hover{
    background-color: #47cb89;
}
QPushButton[type=success]:pressed{
    background-color: #18b566;
}


QPushButton[type=warning]{
    background-color: #ff9900;
}
QPushButton[type=warning]:hover{
    background-color: #ffad33;
}
QPushButton[type=warning]:pressed{
    background-color: #f29100;
}


QPushButton[type=error]{
    background-color: #ed4014;
}
QPushButton[type=error]:hover{
    background-color: #f16643;
}
QPushButton[type=error]:pressed{
    background-color: #e13d13;
}



QPushButton:disabled{
    color: grey;
    border: 2px dashed #dcdee2;
    background-color: #f7f7f7;
}
'''


class MButton(QPushButton):
    def __init__(self, text='', type='default', button_size='default', button_icon=None, parent=None):
        super(MButton, self).__init__(parent=parent)
        if button_icon:
            self.setProperty('icon', MIcon(request_file(button_icon or '' + '.png')))

        self.setProperty('text', text)
        self.setProperty('type', type)
        self.setProperty('button_size', button_size)
        self.setStyleSheet(qss)
