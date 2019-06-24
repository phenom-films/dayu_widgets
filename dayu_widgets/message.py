#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.avatar import MAvatar
from dayu_widgets.loading import MLoading
from dayu_widgets.label import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.tool_button import MToolButton
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

    sig_closed = Signal()

    def __init__(self, text, duration=None, type=None, closable=False, parent=None):
        super(MMessage, self).__init__(parent)
        self.setObjectName('message')
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WA_TranslucentBackground | Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_StyledBackground)

        if type == MMessage.LoadingType:
            self._icon_label = MLoading.tiny()
        else:
            self._icon_label = MAvatar.tiny()

        self._content_label = MLabel(parent=self)
        self._content_label.set_elide_mode(Qt.ElideMiddle)
        self._content_label.setText(text)

        self._close_button = MToolButton(type=MToolButton.IconOnlyType,
                                         size=dayu_theme.tiny,
                                         icon=MIcon('close_line.svg'),
                                         parent=self)
        self._close_button.clicked.connect(self.close)
        self._close_button.setVisible(closable or False)

        self._main_lay = QHBoxLayout()
        self._main_lay.addWidget(self._icon_label)
        self._main_lay.addWidget(self._content_label)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)
        self.setLayout(self._main_lay)

        self.set_type(type or MMessage.InfoType)
        close_timer = QTimer(self)
        close_timer.setSingleShot(True)
        close_timer.timeout.connect(self.close)
        close_timer.timeout.connect(self.sig_closed)
        close_timer.setInterval((duration or self.default_config.get('duration')) * 1000)

        ani_timer = QTimer(self)
        ani_timer.timeout.connect(self._fade_out)
        ani_timer.setInterval((duration or self.default_config.get('duration')) * 1000 - 300)

        close_timer.start()
        ani_timer.start()

        self.pos_ani = QPropertyAnimation(self)
        self.pos_ani.setTargetObject(self)
        self.pos_ani.setEasingCurve(QEasingCurve.OutCubic)
        self.pos_ani.setDuration(300)
        self.pos_ani.setPropertyName('pos')

        self.opacity_ani = QPropertyAnimation()
        self.opacity_ani.setTargetObject(self)
        self.opacity_ani.setDuration(300)
        self.opacity_ani.setEasingCurve(QEasingCurve.OutCubic)
        self.opacity_ani.setPropertyName('windowOpacity')
        self.opacity_ani.setStartValue(0.0)
        self.opacity_ani.setEndValue(1.0)

    def _fade_out(self):
        self.pos_ani.setDirection(QAbstractAnimation.Backward)
        self.pos_ani.start()
        self.opacity_ani.setDirection(QAbstractAnimation.Backward)
        self.opacity_ani.start()

    def _fade_int(self):
        self.pos_ani.start()
        self.opacity_ani.start()

    def set_type(self, value):
        self.setProperty('type', value)

    def _set_type(self, value):
        if isinstance(self._icon_label, MAvatar):
            self._icon_label.set_dayu_image(MPixmap('{}_fill.svg'.format(value), vars(dayu_theme).get(value + '_color')))

    @classmethod
    def _show(cls, text, duration=None, type=None, closable=False, parent=None):
        msg = MMessage(text=text, duration=duration, type=type, closable=closable, parent=parent)
        parent_geo = parent.geometry()
        pos = parent_geo.topLeft() if parent.parent() is None else parent.mapToGlobal(parent_geo.topLeft())
        offset = 0
        for child in parent.children():
            if isinstance(child, MMessage) and child.isVisible():
                offset = max(offset, child.y())
        base = pos.y() + cls.default_config.get('top')
        target_x = pos.x() + parent_geo.width() / 2 - 100
        target_y = (offset + 50) if offset else base
        msg.show()
        msg.pos_ani.setStartValue(QPoint(target_x, target_y - 40))
        msg.pos_ani.setEndValue(QPoint(target_x, target_y))
        msg._fade_int()
        return msg

    @classmethod
    def info(cls, text, parent, duration=None, closable=None):
        return cls._show(text, type=MMessage.InfoType, duration=duration, closable=closable, parent=parent)

    @classmethod
    def success(cls, text, parent, duration=None, closable=None):
        return cls._show(text, type=MMessage.SuccessType, duration=duration, closable=closable, parent=parent)

    @classmethod
    def warning(cls, text, parent, duration=None, closable=None):
        return cls._show(text, type=MMessage.WarningType, duration=duration, closable=closable, parent=parent)

    @classmethod
    def error(cls, text, parent, duration=None, closable=None):
        return cls._show(text, type=MMessage.ErrorType, duration=duration, closable=closable, parent=parent)

    @classmethod
    def loading(cls, text, parent, duration=None, closable=None):
        # TODO: 一般是不需要设置 duration 的,需要等待线程完成信号再关闭
        return cls._show(text, type=MMessage.LoadingType, duration=duration, closable=closable, parent=parent)

    @classmethod
    def config(cls, duration=None, top=None):
        if duration is not None:
            cls.default_config['duration'] = duration
        if top is not None:
            cls.default_config['top'] = top
