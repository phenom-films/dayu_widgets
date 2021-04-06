#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: TimmyLiang
# Date  : 2021-4-6
# Email : 820472580@qq.com
###################################################################
"""MOverlay"""

from functools import partial
from collections import namedtuple

from Qt import QtCore, QtWidgets, QtGui

class MOverlay(QtWidgets.QWidget):
    
    resized = QtCore.Signal(QtCore.QEvent)
    painted = QtCore.Signal(QtCore.QEvent)

    DIRECTION = namedtuple("Direction", "E S W N")(0, 1, 2, 3)
    STRETCH = namedtuple("Stretch", "NoStretch Vertical Horizontal Center Auto")(
        0, 1, 2, 3, 4
    )

    def __init__(self, parent=None):
        super(MOverlay, self).__init__(parent=parent)
        QtCore.QTimer.singleShot(0, self._initialize)
        self.stretch = self.STRETCH.Auto
        self.direction = self.DIRECTION.E

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.Resize:
            self.resized.emit(event)
        if event.type() == QtCore.QEvent.Paint:
            self.painted.emit(event)
        return super(MOverlay, self).eventFilter(obj, event)

    def _traverse_layout(self, layout):

        target = None
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if isinstance(item, QtWidgets.QLayout):
                target = self._traverse_layout(item)
                if target:
                    break
            elif isinstance(item, QtWidgets.QWidgetItem) and item.widget() is self:
                target = (layout, i)
                break

        return target

    def _initialize(self):
        # NOTE 将组件放到最上面 https://stackoverflow.com/a/31197643
        self.raise_()

        stretch = self.property("stretch")
        stretch = self.STRETCH._asdict().get(stretch)
        if not stretch is None and self.stretch == self.STRETCH.Auto:
            self.set_stretch(stretch)

        # NOTE 根据方向获取依附组件
        direction = self.property("direction")
        direction = direction.upper() if isinstance(direction, str) else ""
        direction = self.DIRECTION._asdict().get(direction)
        if not direction is None and self.direction == self.DIRECTION.E:
            self.set_direction(direction)

        layout = self.parentWidget().layout()
        info = self._traverse_layout(layout)
        assert info, "%s cannot find layout" % (self)

        parent_layout, index = info
        value = 1 if self.direction <= 1 else -1
        item = parent_layout.itemAt(index - value)
        assert item, "%s wrong overlay direction" % (self)

        parent_widget = parent_layout.parentWidget()
        parent_widget.installEventFilter(self)
        data = {
            "index": index,
            "item": item,
            "layout": parent_layout,
        }

        # NOTE 在 Tab 组件下 确保显示状态才去 生成 Overlay
        self.painted.connect(partial(self._init_resize, data))

    def _init_resize(self, data, event):
        # NOTE 注销 init_resize
        self.painted.disconnect()
        self.painted.connect(self._update_mask)

        layout = data.get("layout")
        index = data.get("index")
        item = data.get("item")

        layout.takeAt(index)

        data["geometry"] = item.geometry()
        data["original_pos"] = self.pos()

        self.resized.connect(partial(self._resize_overlay, data))
        # NOTE 更新界面
        QtCore.QTimer.singleShot(0, lambda: self._resize_overlay(data, None))

    def _resize_overlay(self, data, event):
        item = data.get("item")
        geometry = data.get("geometry")
        layout = data.get("layout")
        original_pos = data.get("original_pos")

        width = self.geometry().width()
        height = self.geometry().height()
        spacing = layout.spacing()

        new_geometry = item.geometry()
        delta_x = new_geometry.x() - geometry.x()
        delta_y = new_geometry.y() - geometry.y()
        delta_width = new_geometry.width() - geometry.width()
        delta_height = new_geometry.height() - geometry.height()

        x = 0
        y = 0
        if self.direction == self.DIRECTION.W:
            x = delta_x + width + spacing
            y = delta_y
        elif self.direction == self.DIRECTION.E:
            x = delta_width + delta_x - width - spacing
            y = delta_y
        elif self.direction == self.DIRECTION.N:
            x = delta_x
            y = delta_y + height + spacing
        elif self.direction == self.DIRECTION.S:
            x = delta_x
            y = delta_height + delta_y - height - spacing

        self.move(original_pos + QtCore.QPoint(x, y))

        if self.stretch == self.STRETCH.Auto:
            if self.direction in [1, 3]:
                self.setFixedWidth(new_geometry.width())
            else:
                self.setFixedHeight(new_geometry.height())
        elif self.stretch == self.STRETCH.Horizontal:
            self.setFixedWidth(new_geometry.width())
        elif self.stretch == self.STRETCH.Vertical:
            self.setFixedHeight(new_geometry.height())
        elif self.stretch == self.STRETCH.Center:
            self.move(original_pos)
            self.setFixedWidth(new_geometry.width())
            self.setFixedHeight(new_geometry.height())

    def _update_mask(self):
        # NOTE https://stackoverflow.com/q/27855137
        reg = QtGui.QRegion(self.frameGeometry())
        reg -= QtGui.QRegion(self.geometry())
        reg += self.childrenRegion()
        self.setMask(reg)

    def set_stretch(self, stretch):
        self.stretch = stretch

    def set_direction(self, direction):
        self.direction = direction
        
        
        