#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *


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
