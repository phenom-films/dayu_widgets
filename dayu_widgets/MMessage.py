#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from MTheme import global_theme
from MButton import MButton
from MLabel import MLabel
from MAvatar import MAvatar
from qt import *

qss = '''
QWidget#message{{
    padding: 2px;
    border: 1px solid {border};
    border-radius: 2px;
    background-color: {background};
}}

'''.format(**global_theme)


@property_mixin
class MMessage(QWidget):
    '''
    自定义 props:
        config
    '''
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'
    LoadingType = 'loading'

    default_config = {
        'duration': 2,
        'top': 24
    }

    def __init__(self, config, type=None, parent=None):
        super(MMessage, self).__init__(parent)
        self.setObjectName('message')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WA_TranslucentBackground)
        self.setProperty('type', type or MMessage.InfoType)

        if isinstance(config, basestring):
            config = {'content': config}

        self._icon_label = MAvatar(size=MAvatar.SmallSize, image='icon-{}.png'.format(self.property('type')))

        self._content_label = MLabel(parent=self)
        self._content_label.setText(config.get('content'))

        self._close_button = MButton(size=MButton.SmallSize, icon=MIcon('icon-clear.png'), type=MButton.IconType,
                                     parent=self)
        self._close_button.clicked.connect(self.close)
        self._close_button.setVisible(config.get('closable', False))

        self._main_lay = QHBoxLayout()
        self._main_lay.addWidget(self._icon_label)
        self._main_lay.addWidget(self._content_label)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)
        self.setLayout(self._main_lay)
        self.setStyleSheet(qss)
        timer = QTimer(self)
        timer.timeout.connect(self.close)
        timer.setInterval(config.get('duration', self.default_config.get('duration')) * 1000)
        timer.start()

    @classmethod
    def _show(cls, config, type, parent):
        msg = MMessage(config=config, type=type, parent=parent)
        geo = QApplication.topLevelWidgets()[0].geometry()
        msg.move(geo.x() + geo.width() / 2 - 100, geo.y() + cls.default_config.get('top'))
        msg.show()

    @classmethod
    def info(cls, config, parent):
        cls._show(config, type=MMessage.InfoType, parent=parent)

    @classmethod
    def success(cls, config, parent):
        cls._show(config, type=MMessage.SuccessType, parent=parent)

    @classmethod
    def warning(cls, config, parent):
        cls._show(config, type=MMessage.WarningType, parent=parent)

    @classmethod
    def error(cls, config, parent):
        cls._show(config, type=MMessage.ErrorType, parent=parent)

    @classmethod
    def config(cls, duration=None, top=None):
        if duration is not None:
            cls.default_config['duration'] = duration
        if top is not None:
            cls.default_config['top'] = top
