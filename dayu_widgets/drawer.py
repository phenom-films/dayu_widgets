#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.6
# Email : muyanru345@163.com
###################################################################
"""MDrawer"""
# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.qt import Property
from dayu_widgets.qt import QAbstractAnimation
from dayu_widgets.qt import QEasingCurve
from dayu_widgets.qt import QHBoxLayout
from dayu_widgets.qt import QPoint
from dayu_widgets.qt import QPropertyAnimation
from dayu_widgets.qt import QScrollArea
from dayu_widgets.qt import QTimer
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.qt import Qt
from dayu_widgets.qt import Signal
from dayu_widgets.qt import get_scale_factor
from dayu_widgets.tool_button import MToolButton


class MDrawer(QWidget):
    """
    A panel which slides in from the edge of the screen.
    """

    LeftPos = "left"
    RightPos = "right"
    TopPos = "top"
    BottomPos = "bottom"

    sig_closed = Signal()

    def __init__(self, title, position="right", closable=True, parent=None):
        super(MDrawer, self).__init__(parent)
        self.setObjectName("message")
        self.setWindowFlags(Qt.Popup)
        # self.setWindowFlags(
        #     Qt.FramelessWindowHint | Qt.Popup | Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_StyledBackground)

        self._title_label = MLabel(parent=self).h4()
        # self._title_label.set_elide_mode(Qt.ElideRight)
        self._title_label.setText(title)

        self._close_button = (
            MToolButton(parent=self).icon_only().svg("close_line.svg").small()
        )
        self._close_button.clicked.connect(self.close)
        self._close_button.setVisible(closable or False)

        self._title_extra_lay = QHBoxLayout()
        _title_lay = QHBoxLayout()
        _title_lay.addWidget(self._title_label)
        _title_lay.addStretch()
        _title_lay.addLayout(self._title_extra_lay)
        _title_lay.addWidget(self._close_button)
        self._bottom_lay = QHBoxLayout()
        self._bottom_lay.addStretch()

        self._scroll_area = QScrollArea()
        self._scroll_area.setWidgetResizable(True)
        self._main_lay = QVBoxLayout()
        self._main_lay.addLayout(_title_lay)
        self._main_lay.addWidget(MDivider())
        self._main_lay.addWidget(self._scroll_area)
        self._main_lay.addWidget(MDivider())
        self._main_lay.addLayout(self._bottom_lay)
        self.setLayout(self._main_lay)

        self._position = position

        self._close_timer = QTimer(self)
        self._close_timer.setSingleShot(True)
        self._close_timer.timeout.connect(self.close)
        self._close_timer.timeout.connect(self.sig_closed)
        self._close_timer.setInterval(300)
        self._is_first_close = True

        self._pos_ani = QPropertyAnimation(self)
        self._pos_ani.setTargetObject(self)
        self._pos_ani.setEasingCurve(QEasingCurve.OutCubic)
        self._pos_ani.setDuration(300)
        self._pos_ani.setPropertyName(b"pos")

        self._opacity_ani = QPropertyAnimation()
        self._opacity_ani.setTargetObject(self)
        self._opacity_ani.setDuration(300)
        self._opacity_ani.setEasingCurve(QEasingCurve.OutCubic)
        self._opacity_ani.setPropertyName(b"windowOpacity")
        self._opacity_ani.setStartValue(0.0)
        self._opacity_ani.setEndValue(1.0)

    def set_widget(self, widget):
        self._scroll_area.setWidget(widget)

    def add_widget_to_bottom(self, button):
        self._bottom_lay.addWidget(button)

    def add_widget_to_top(self, button):
        self._title_extra_lay.addWidget(button)

    def _fade_out(self):
        self._pos_ani.setDirection(QAbstractAnimation.Backward)
        self._pos_ani.start()
        self._opacity_ani.setDirection(QAbstractAnimation.Backward)
        self._opacity_ani.start()

    def _fade_int(self):
        self._pos_ani.start()
        self._opacity_ani.start()

    def _set_proper_position(self):
        parent = self.parent()
        parent_geo = parent.geometry()
        if self._position == MDrawer.LeftPos:
            pos = (
                parent_geo.topLeft()
                if parent.parent() is None
                else parent.mapToGlobal(parent_geo.topLeft())
            )
            target_x = pos.x()
            target_y = pos.y()
            self.setFixedHeight(parent_geo.height())
            self._pos_ani.setStartValue(QPoint(target_x - self.width(), target_y))
            self._pos_ani.setEndValue(QPoint(target_x, target_y))
        if self._position == MDrawer.RightPos:
            pos = (
                parent_geo.topRight()
                if parent.parent() is None
                else parent.mapToGlobal(parent_geo.topRight())
            )
            self.setFixedHeight(parent_geo.height())
            target_x = pos.x() - self.width()
            target_y = pos.y()
            self._pos_ani.setStartValue(QPoint(target_x + self.width(), target_y))
            self._pos_ani.setEndValue(QPoint(target_x, target_y))
        if self._position == MDrawer.TopPos:
            pos = (
                parent_geo.topLeft()
                if parent.parent() is None
                else parent.mapToGlobal(parent_geo.topLeft())
            )
            self.setFixedWidth(parent_geo.width())
            target_x = pos.x()
            target_y = pos.y()
            self._pos_ani.setStartValue(QPoint(target_x, target_y - self.height()))
            self._pos_ani.setEndValue(QPoint(target_x, target_y))
        if self._position == MDrawer.BottomPos:
            pos = (
                parent_geo.bottomLeft()
                if parent.parent() is None
                else parent.mapToGlobal(parent_geo.bottomLeft())
            )
            self.setFixedWidth(parent_geo.width())
            target_x = pos.x()
            target_y = pos.y() - self.height()
            self._pos_ani.setStartValue(QPoint(target_x, target_y + self.height()))
            self._pos_ani.setEndValue(QPoint(target_x, target_y))

    def set_dayu_position(self, value):
        """
        Set the placement of the MDrawer.
        top/right/bottom/left, default is right
        :param value: str
        :return: None
        """
        self._position = value
        scale_x, _ = get_scale_factor()
        if value in [MDrawer.BottomPos, MDrawer.TopPos]:
            self.setFixedHeight(200 * scale_x)
        else:
            self.setFixedWidth(200 * scale_x)

    def get_dayu_position(self):
        """
        Get the placement of the MDrawer
        :return: str
        """
        return self._position

    dayu_position = Property(str, get_dayu_position, set_dayu_position)

    def left(self):
        """Set drawer's placement to left"""
        self.set_dayu_position(MDrawer.LeftPos)
        return self

    def right(self):
        """Set drawer's placement to right"""
        self.set_dayu_position(MDrawer.RightPos)
        return self

    def top(self):
        """Set drawer's placement to top"""
        self.set_dayu_position(MDrawer.TopPos)
        return self

    def bottom(self):
        """Set drawer's placement to bottom"""
        self.set_dayu_position(MDrawer.BottomPos)
        return self

    def show(self):
        self._set_proper_position()
        self._fade_int()
        return super(MDrawer, self).show()

    def closeEvent(self, event):
        if self._is_first_close:
            self._is_first_close = False
            self._close_timer.start()
            self._fade_out()
            event.ignore()
        else:
            event.accept()
