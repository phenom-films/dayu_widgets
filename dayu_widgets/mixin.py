#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
import functools


def property_mixin(cls):
    def event(self, event):
        if event.type() == QEvent.DynamicPropertyChange:
            p = event.propertyName()
            if hasattr(self, '_set_{}'.format(p)):
                callback = getattr(self, '_set_{}'.format(p))
                callback(self.property(str(p)))
        return super(cls, self).event(event)

    setattr(cls, 'event', event)
    return cls


def cursor_mixin(cls):
    old_enter_event = cls.enterEvent
    old_leave_event = cls.leaveEvent

    def enterEvent(self, *args, **kwargs):
        old_enter_event(self, *args, **kwargs)
        QApplication.setOverrideCursor(Qt.PointingHandCursor if self.isEnabled() else Qt.ForbiddenCursor)
        return super(cls, self).enterEvent(*args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        old_leave_event(self, *args, **kwargs)
        QApplication.restoreOverrideCursor()
        return super(cls, self).leaveEvent(*args, **kwargs)

    setattr(cls, 'enterEvent', enterEvent)
    setattr(cls, 'leaveEvent', leaveEvent)
    return cls


def focus_shadow_mixin(cls):
    old_focus_in_event = cls.focusInEvent
    old_focus_out_event = cls.focusOutEvent

    def focusInEvent(self, *args, **kwargs):
        old_focus_in_event(self, *args, **kwargs)
        if not self.graphicsEffect():
            from dayu_widgets import dayu_theme
            shadow_effect = QGraphicsDropShadowEffect(self)
            dayu_type = self.property('type')
            color = vars(dayu_theme).get('{}_color'.format(dayu_type or 'primary'))
            shadow_effect.setColor(color)
            shadow_effect.setOffset(0, 0)
            shadow_effect.setBlurRadius(5)
            shadow_effect.setEnabled(False)
            self.setGraphicsEffect(shadow_effect)
        if self.isEnabled():
            self.graphicsEffect().setEnabled(True)

    def focusOutEvent(self, *args, **kwargs):
        old_focus_out_event(self, *args, **kwargs)
        if self.graphicsEffect():
            self.graphicsEffect().setEnabled(False)

    setattr(cls, 'focusInEvent', focusInEvent)
    setattr(cls, 'focusOutEvent', focusOutEvent)
    return cls


def hover_shadow_mixin(cls):
    old_enter_event = cls.enterEvent
    old_leave_event = cls.leaveEvent

    def enterEvent(self, *args, **kwargs):
        old_enter_event(self, *args, **kwargs)
        if not self.graphicsEffect():
            from dayu_widgets import dayu_theme
            shadow_effect = QGraphicsDropShadowEffect(self)
            dayu_type = self.property('type')
            color = vars(dayu_theme).get('{}_color'.format(dayu_type or 'primary'))
            shadow_effect.setColor(color)
            shadow_effect.setOffset(0, 0)
            shadow_effect.setBlurRadius(5)
            shadow_effect.setEnabled(False)
            self.setGraphicsEffect(shadow_effect)
        if self.isEnabled():
            self.graphicsEffect().setEnabled(True)

    def leaveEvent(self, *args, **kwargs):
        old_leave_event(self, *args, **kwargs)
        if self.graphicsEffect():
            self.graphicsEffect().setEnabled(False)

    setattr(cls, 'enterEvent', enterEvent)
    setattr(cls, 'leaveEvent', leaveEvent)
    return cls


def stacked_animation_mixin(cls):
    old_init = cls.__init__

    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        self._previous_index = 0
        self._to_show_pos_ani = QPropertyAnimation()
        self._to_show_pos_ani.setDuration(400)
        self._to_show_pos_ani.setPropertyName('pos')
        self._to_show_pos_ani.setEndValue(QPoint(0, 0))
        self._to_show_pos_ani.setEasingCurve(QEasingCurve.OutCubic)

        self._to_hide_pos_ani = QPropertyAnimation()
        self._to_hide_pos_ani.setDuration(400)
        self._to_hide_pos_ani.setPropertyName('pos')
        self._to_hide_pos_ani.setEndValue(QPoint(0, 0))
        self._to_hide_pos_ani.setEasingCurve(QEasingCurve.OutCubic)

        self._opacity_eff = QGraphicsOpacityEffect()
        self._opacity_ani = QPropertyAnimation()
        self._opacity_ani.setDuration(400)
        self._opacity_ani.setEasingCurve(QEasingCurve.InCubic)
        self._opacity_ani.setPropertyName('opacity')
        self._opacity_ani.setStartValue(0.0)
        self._opacity_ani.setEndValue(1.0)
        self._opacity_ani.setTargetObject(self._opacity_eff)
        self._opacity_ani.finished.connect(self._disable_opacity)
        self.currentChanged.connect(self._play_anim)

    def _play_anim(self, index):
        current_widget = self.widget(index)
        if self._previous_index < index:
            self._to_show_pos_ani.setStartValue(QPoint(self.width(), 0))
            self._to_show_pos_ani.setTargetObject(current_widget)
            self._to_show_pos_ani.start()
        else:
            self._to_hide_pos_ani.setStartValue(QPoint(-self.width(), 0))
            self._to_hide_pos_ani.setTargetObject(current_widget)
            self._to_hide_pos_ani.start()
        current_widget.setGraphicsEffect(self._opacity_eff)
        current_widget.graphicsEffect().setEnabled(True)
        self._opacity_ani.start()
        self._previous_index = index

    def _disable_opacity(self):
        # 如果不关掉effect，会跟子控件的 effect 或 paintEvent 冲突引起 crash
        # QPainter::begin: A paint device can only be painted by one painter at a time.
        self.currentWidget().graphicsEffect().setEnabled(False)

    setattr(cls, '__init__', new_init)
    setattr(cls, '_play_anim', _play_anim)
    setattr(cls, '_disable_opacity', _disable_opacity)
    return cls
