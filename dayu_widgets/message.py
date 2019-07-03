#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""MMessage"""
from dayu_widgets.avatar import MAvatar
from dayu_widgets.loading import MLoading
from dayu_widgets.label import MLabel
from dayu_widgets import dayu_theme
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.qt import QWidget, Qt, Signal, QHBoxLayout, QTimer, QPropertyAnimation, \
    QEasingCurve, QAbstractAnimation, MPixmap, QPoint, QGraphicsDropShadowEffect, QPainterPath, QRegion, QRectF


class MMessage(QWidget):
    """
    Display global messages as feedback in response to user operations.
    """
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

    def __init__(self, text, duration=None, dayu_type=None, closable=False, parent=None):
        super(MMessage, self).__init__(parent)
        self.setObjectName('message')
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.Dialog | Qt.WA_TranslucentBackground | Qt.WA_DeleteOnClose)
        self.setAttribute(Qt.WA_StyledBackground)

        if dayu_type == MMessage.LoadingType:
            _icon_label = MLoading.tiny()
        else:
            _icon_label = MAvatar.tiny()
            current_type = dayu_type or MMessage.InfoType
            _icon_label.set_dayu_image(MPixmap('{}_fill.svg'.format(current_type),
                                               vars(dayu_theme).get(current_type + '_color')))

        self._content_label = MLabel(parent=self)
        # self._content_label.set_elide_mode(Qt.ElideMiddle)
        self._content_label.setText(text)

        self._close_button = MToolButton(parent=self).icon_only().svg('close_line.svg').tiny()
        self._close_button.clicked.connect(self.close)
        self._close_button.setVisible(closable or False)

        self._main_lay = QHBoxLayout()
        self._main_lay.addWidget(_icon_label)
        self._main_lay.addWidget(self._content_label)
        self._main_lay.addStretch()
        self._main_lay.addWidget(self._close_button)
        self.setLayout(self._main_lay)

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

        self._pos_ani = QPropertyAnimation(self)
        self._pos_ani.setTargetObject(self)
        self._pos_ani.setEasingCurve(QEasingCurve.OutCubic)
        self._pos_ani.setDuration(300)
        self._pos_ani.setPropertyName('pos')

        self._opacity_ani = QPropertyAnimation()
        self._opacity_ani.setTargetObject(self)
        self._opacity_ani.setDuration(300)
        self._opacity_ani.setEasingCurve(QEasingCurve.OutCubic)
        self._opacity_ani.setPropertyName('windowOpacity')
        self._opacity_ani.setStartValue(0.0)
        self._opacity_ani.setEndValue(1.0)

        self._set_proper_position(parent)
        self._fade_int()

    def _fade_out(self):
        self._pos_ani.setDirection(QAbstractAnimation.Backward)
        self._pos_ani.start()
        self._opacity_ani.setDirection(QAbstractAnimation.Backward)
        self._opacity_ani.start()

    def _fade_int(self):
        self._pos_ani.start()
        self._opacity_ani.start()

    def _set_proper_position(self, parent):
        parent_geo = parent.geometry()
        pos = parent_geo.topLeft() if parent.parent() is None else parent.mapToGlobal(
            parent_geo.topLeft())
        offset = 0
        for child in parent.children():
            if isinstance(child, MMessage) and child.isVisible():
                offset = max(offset, child.y())
        base = pos.y() + MMessage.default_config.get('top')
        target_x = pos.x() + parent_geo.width() / 2 - 100
        target_y = (offset + 50) if offset else base
        self._pos_ani.setStartValue(QPoint(target_x, target_y - 40))
        self._pos_ani.setEndValue(QPoint(target_x, target_y))

    @classmethod
    def info(cls, text, parent, duration=None, closable=None):
        """Show a normal message"""
        inst = cls(text, dayu_type=MMessage.InfoType, duration=duration, closable=closable,
                   parent=parent)
        inst.show()
        return inst

    @classmethod
    def success(cls, text, parent, duration=None, closable=None):
        """Show a success message"""
        inst = cls(text, dayu_type=MMessage.SuccessType, duration=duration, closable=closable,
                   parent=parent)

        inst.show()
        return inst

    @classmethod
    def warning(cls, text, parent, duration=None, closable=None):
        """Show a warning message"""
        inst = cls(text, dayu_type=MMessage.WarningType, duration=duration, closable=closable,
                   parent=parent)
        inst.show()
        return inst

    @classmethod
    def error(cls, text, parent, duration=None, closable=None):
        """Show an error message"""
        inst = cls(text, dayu_type=MMessage.ErrorType, duration=duration, closable=closable,
                   parent=parent)
        inst.show()
        return inst

    @classmethod
    def loading(cls, text, parent):
        """Show a message with loading animation"""
        inst = cls(text, dayu_type=MMessage.LoadingType, parent=parent)
        inst.show()
        return inst

    @classmethod
    def config(cls, duration=None, top=None):
        """
        Config the global MMessage duration and top setting.
        :param duration: int (unit is second)
        :param top: int (unit is px)
        :return: None
        """
        if duration is not None:
            cls.default_config['duration'] = duration
        if top is not None:
            cls.default_config['top'] = top
