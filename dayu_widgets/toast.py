#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
MToast
"""
from dayu_widgets import dayu_theme
from dayu_widgets.avatar import MAvatar
from dayu_widgets.label import MLabel
from dayu_widgets.loading import MLoading
from dayu_widgets.qt import QWidget, Signal, Qt, QSize, MPixmap, QHBoxLayout, QVBoxLayout, \
    QTimer, QPropertyAnimation, QEasingCurve, QAbstractAnimation, QPoint


class MToast(QWidget):
    """
    MToast
    A Phone style message.
    """
    InfoType = 'info'
    SuccessType = 'success'
    WarningType = 'warning'
    ErrorType = 'error'
    LoadingType = 'loading'

    default_config = {
        'duration': 2,
    }

    sig_closed = Signal()

    def __init__(self, text, duration=None, dayu_type=None, parent=None):
        super(MToast, self).__init__(parent)
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.Dialog | Qt.WA_TranslucentBackground | Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_StyledBackground)

        _icon_lay = QHBoxLayout()
        _icon_lay.addStretch()

        if dayu_type == MToast.LoadingType:
            _icon_lay.addWidget(MLoading(size=dayu_theme.huge, color=dayu_theme.text_color_inverse))
        else:
            _icon_label = MAvatar()
            _icon_label.set_dayu_size(60)
            _icon_label.set_dayu_image(MPixmap('{}_line.svg'.format(dayu_type or MToast.InfoType),
                                               dayu_theme.text_color_inverse))
            _icon_lay.addWidget(_icon_label)
        _icon_lay.addStretch()

        _content_label = MLabel()
        _content_label.setText(text)
        _content_label.setAlignment(Qt.AlignCenter)

        _main_lay = QVBoxLayout()
        _main_lay.setContentsMargins(0, 0, 0, 0)
        _main_lay.addStretch()
        _main_lay.addLayout(_icon_lay)
        _main_lay.addSpacing(10)
        _main_lay.addWidget(_content_label)
        _main_lay.addStretch()
        self.setLayout(_main_lay)
        self.setFixedSize(QSize(120, 120))

        _close_timer = QTimer(self)
        _close_timer.setSingleShot(True)
        _close_timer.timeout.connect(self.close)
        _close_timer.timeout.connect(self.sig_closed)
        _close_timer.setInterval((duration or self.default_config.get('duration')) * 1000)

        _ani_timer = QTimer(self)
        _ani_timer.timeout.connect(self._fade_out)
        _ani_timer.setInterval((duration or self.default_config.get('duration')) * 1000 - 300)

        _close_timer.start()
        _ani_timer.start()

        self._opacity_ani = QPropertyAnimation()
        self._opacity_ani.setTargetObject(self)
        self._opacity_ani.setDuration(300)
        self._opacity_ani.setEasingCurve(QEasingCurve.OutCubic)
        self._opacity_ani.setPropertyName(b'windowOpacity')
        self._opacity_ani.setStartValue(0.0)
        self._opacity_ani.setEndValue(0.9)

        self._get_center_position(parent)
        self._fade_int()

    def _fade_out(self):
        self._opacity_ani.setDirection(QAbstractAnimation.Backward)
        self._opacity_ani.start()

    def _fade_int(self):
        self._opacity_ani.start()

    def _get_center_position(self, parent):
        parent_geo = parent.geometry()
        pos = parent_geo.topLeft() \
            if parent.parent() is None else parent.mapToGlobal(parent_geo.topLeft())
        offset = 0
        for child in parent.children():
            if isinstance(child, MToast) and child.isVisible():
                offset = max(offset, child.y())
        target_x = pos.x() + parent_geo.width() / 2 - self.width() / 2
        target_y = pos.y() + parent_geo.height() / 2 - self.height() / 2
        self.setProperty('pos', QPoint(target_x, target_y))

    @classmethod
    def info(cls, text, parent, duration=None):
        """Show a normal toast message"""
        inst = cls(text, duration=duration, dayu_type=MToast.InfoType, parent=parent)
        inst.show()
        return inst

    @classmethod
    def success(cls, text, parent, duration=None):
        """Show a success toast message"""
        inst = cls(text, duration=duration, dayu_type=MToast.SuccessType, parent=parent)
        inst.show()
        return inst

    @classmethod
    def warning(cls, text, parent, duration=None):
        """Show a warning toast message"""
        inst = cls(text, duration=duration, dayu_type=MToast.WarningType, parent=parent)
        inst.show()
        return inst

    @classmethod
    def error(cls, text, parent, duration=None):
        """Show an error toast message"""
        inst = cls(text, duration=duration, dayu_type=MToast.ErrorType, parent=parent)
        inst.show()
        return inst

    @classmethod
    def loading(cls, text, parent):
        """Show a toast message with loading animation"""
        inst = cls(text, dayu_type=MToast.LoadingType, parent=parent)
        inst.show()
        return inst

    @classmethod
    def config(cls, duration):
        """
        Config the global MToast duration setting.
        :param duration: int (unit is second)
        :return: None
        """
        if duration is not None:
            cls.default_config['duration'] = duration
