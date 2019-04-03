#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import *


class MLoading(QWidget):
    def __init__(self, size=None, color=None, parent=None):
        super(MLoading, self).__init__(parent)
        size = size or dayu_theme.default_size
        self.setFixedSize(QSize(size, size))
        self.pix = MPixmap('loading.svg', color or dayu_theme.primary_color).scaledToWidth(size,
                                                                                           Qt.SmoothTransformation)
        self.rotation = 0
        self.loading_ani = QPropertyAnimation()
        self.loading_ani.setTargetObject(self)
        # self.loading_ani.setEasingCurve(QEasingCurve.InOutQuad)
        self.loading_ani.setDuration(1000)
        self.loading_ani.setPropertyName('rotation')
        self.loading_ani.setStartValue(0)
        self.loading_ani.setEndValue(360)
        self.loading_ani.setLoopCount(-1)
        self.loading_ani.start()

    def _set_rotation(self, value):
        self._value = value
        self.update()

    def _get_rotation(self):
        return self._value

    rotation = Property(int, _get_rotation, _set_rotation)

    def paintEvent(self, *args, **kwargs):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.translate(self.pix.width() / 2, self.pix.height() / 2)
        painter.rotate(self.rotation)
        painter.drawPixmap(-self.pix.width() / 2, -self.pix.height() / 2, self.pix.width(), self.pix.height(), self.pix)
        painter.end()


@property_mixin
class MLoadingWrapper(QWidget):
    def __init__(self, widget, loading=True, parent=None):
        super(MLoadingWrapper, self).__init__(parent)
        self._widget = widget
        self._mask_widget = QFrame()
        self._mask_widget.setObjectName('mask')
        self._mask_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._loading_widget = MLoading()
        self._loading_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self._main_lay = QGridLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self._main_lay.addWidget(widget, 0, 0)
        self._main_lay.addWidget(self._mask_widget, 0, 0)
        self._main_lay.addWidget(self._loading_widget, 0, 0, Qt.AlignCenter)
        self.setLayout(self._main_lay)
        self.set_loading(loading)

    def _set_loading(self, value):
        self._loading_widget.setVisible(value)
        self._mask_widget.setVisible(value)

    def set_loading(self, value):
        self.setProperty('loading', value)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    test = MLoading(size=dayu_theme.tiny)
    test.show()
    sys.exit(app.exec_())
