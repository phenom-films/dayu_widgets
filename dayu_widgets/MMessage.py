#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MAvatar import MAvatar
from dayu_widgets.MLabel import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


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
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WA_TranslucentBackground | Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_StyledBackground)

        if isinstance(config, basestring):
            config = {'content': config}

        self._icon_label = MAvatar(size=dayu_theme.size.tiny)

        self._content_label = MLabel(parent=self)
        self._content_label.set_elide_mode(Qt.ElideMiddle)
        self._content_label.setText(config.get('content'))

        self._close_button = MToolButton(type=MToolButton.IconOnlyType,
                                         size=dayu_theme.size.tiny,
                                         icon=MIcon('close_line.svg'),
                                         parent=self)
        self._close_button.clicked.connect(self.close)
        self._close_button.setVisible(config.get('closable', False))

        self._main_lay = QHBoxLayout()
        self._main_lay.addWidget(self._icon_label)
        self._main_lay.addWidget(self._content_label)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)
        self.setLayout(self._main_lay)

        type = type or MMessage.InfoType
        self._icon_label.set_image(MPixmap('{}_fill.svg'.format(type), dayu_theme.color.get(type)))
        timer = QTimer(self)
        timer.timeout.connect(self.close)
        timer.setInterval(config.get('duration', self.default_config.get('duration')) * 1000)
        timer.start()

    @classmethod
    def _show(cls, config, type, parent):
        msg = MMessage(config=config, type=type, parent=parent)
        parent_geo = parent.geometry()
        pos = parent_geo.topLeft() if parent.parent() is None else parent.mapToGlobal(parent_geo.topLeft())
        offset = 0
        for child in parent.children():
            if isinstance(child, MMessage) and child.isVisible():
                offset = max(offset, child.y())
        base = pos.y() + cls.default_config.get('top')
        msg.move(pos.x() + parent_geo.width() / 2 - 100, (offset + 50) if offset else base)
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
