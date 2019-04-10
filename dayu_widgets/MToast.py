#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MAvatar import MAvatar
from dayu_widgets.MLoading import MLoading
from dayu_widgets.MLabel import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


@property_mixin
class MToast(QWidget):
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
    }

    sig_closed = Signal()

    def __init__(self, text, duration=None, type=None, parent=None):
        super(MToast, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog | Qt.WA_TranslucentBackground | Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_StyledBackground)

        if type == MToast.LoadingType:
            self._icon_label = MLoading(size=dayu_theme.huge, color=dayu_theme.text_color_inverse)
        else:
            self._icon_label = QLabel()
            fixed_height = 60
            self.setFixedSize(QSize(fixed_height, fixed_height))
            pix = MPixmap('{}_line.svg'.format(type or MToast.InfoType), dayu_theme.text_color_inverse)
            self._icon_label.setPixmap(pix.scaledToWidth(fixed_height, Qt.SmoothTransformation))

        icon_lay = QHBoxLayout()
        icon_lay.addStretch()
        icon_lay.addWidget(self._icon_label)
        icon_lay.addStretch()

        self._content_label = QLabel(parent=self)
        self._content_label.setText(text)
        self._content_label.setAlignment(Qt.AlignCenter)

        main_lay = QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.addStretch()
        main_lay.addLayout(icon_lay)
        main_lay.addSpacing(10)
        main_lay.addWidget(self._content_label)
        main_lay.addStretch()
        self.setLayout(main_lay)
        self.setFixedSize(QSize(120, 120))

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

        self.opacity_ani = QPropertyAnimation()
        self.opacity_ani.setTargetObject(self)
        self.opacity_ani.setDuration(300)
        self.opacity_ani.setEasingCurve(QEasingCurve.OutCubic)
        self.opacity_ani.setPropertyName('windowOpacity')
        self.opacity_ani.setStartValue(0.0)
        self.opacity_ani.setEndValue(0.9)

    def _fade_out(self):
        self.opacity_ani.setDirection(QAbstractAnimation.Backward)
        self.opacity_ani.start()

    def _fade_int(self):
        self.opacity_ani.start()

    @classmethod
    def _show(cls, text, duration=2, type=None, parent=None):
        msg = MToast(text=text, duration=duration, type=type, parent=parent)
        parent_geo = parent.geometry()
        pos = parent_geo.topLeft() if parent.parent() is None else parent.mapToGlobal(parent_geo.topLeft())
        offset = 0
        for child in parent.children():
            if isinstance(child, MToast) and child.isVisible():
                offset = max(offset, child.y())
        target_x = pos.x() + parent_geo.width() / 2 - msg.width() / 2
        target_y = pos.y() + parent_geo.height() / 2 - msg.height() / 2
        msg.setProperty('pos', QPoint(target_x, target_y))
        msg.show()
        msg._fade_int()
        return msg

    @classmethod
    def info(cls, text, parent, duration=None):
        return cls._show(text, type=MToast.InfoType, duration=duration, parent=parent)

    @classmethod
    def success(cls, text, parent, duration=None):
        return cls._show(text, type=MToast.SuccessType, duration=duration, parent=parent)

    @classmethod
    def warning(cls, text, parent, duration=None):
        return cls._show(text, type=MToast.WarningType, duration=duration, parent=parent)

    @classmethod
    def error(cls, text, parent, duration=None):
        return cls._show(text, type=MToast.ErrorType, duration=duration, parent=parent)

    @classmethod
    def loading(cls, text, parent, duration=None):
        # TODO: 一般是不需要设置 duration 的,需要等待线程完成信号再关闭
        return cls._show(text, type=MToast.LoadingType, duration=duration, parent=parent)

    @classmethod
    def config(cls, duration):
        if duration is not None:
            cls.default_config['duration'] = duration
