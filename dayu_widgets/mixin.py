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
    def enterEvent(self, *args, **kwargs):
        QApplication.setOverrideCursor(Qt.PointingHandCursor if self.isEnabled() else Qt.ForbiddenCursor)
        return super(cls, self).enterEvent(*args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        QApplication.restoreOverrideCursor()
        return super(cls, self).leaveEvent(*args, **kwargs)

    setattr(cls, 'enterEvent', enterEvent)
    setattr(cls, 'leaveEvent', leaveEvent)
    return cls
