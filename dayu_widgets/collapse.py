#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import functools

# Import third-party modules
from Qt import QtCore
from Qt import QtWidgets

# Import local modules
from dayu_widgets.label import MLabel
from dayu_widgets.mixin import property_mixin
from dayu_widgets.qt import MPixmap
from dayu_widgets.tool_button import MToolButton


@property_mixin
class MSectionItem(QtWidgets.QWidget):
    sig_context_menu = QtCore.Signal(object)

    def __init__(self, title="", expand=False, widget=None, closable=False, parent=None):
        super(MSectionItem, self).__init__(parent)
        self._central_widget = None
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.title_label = MLabel(parent=self)
        self.expand_icon = MLabel(parent=self)
        self.expand_icon.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self._close_button = MToolButton().icon_only().tiny().svg("close_line.svg")
        self._close_button.clicked.connect(self.close)

        header_lay = QtWidgets.QHBoxLayout()
        header_lay.addWidget(self.expand_icon)
        header_lay.addWidget(self.title_label)
        header_lay.addStretch()
        header_lay.addWidget(self._close_button)
        self.header_widget = QtWidgets.QWidget(parent=self)
        self.header_widget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.header_widget.setObjectName("title")
        self.header_widget.setLayout(header_lay)
        self.header_widget.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.header_widget.setCursor(QtCore.Qt.PointingHandCursor)
        self.title_label.setCursor(QtCore.Qt.PointingHandCursor)
        self.header_widget.installEventFilter(self)
        self.title_label.installEventFilter(self)

        self.content_widget = QtWidgets.QWidget(parent=self)
        self.content_layout = QtWidgets.QHBoxLayout()
        self.content_widget.setLayout(self.content_layout)

        self.main_lay = QtWidgets.QVBoxLayout()
        self.main_lay.setContentsMargins(0, 0, 0, 0)
        self.main_lay.setSpacing(0)
        self.main_lay.addWidget(self.header_widget)
        self.main_lay.addWidget(self.content_widget)
        self.setLayout(self.main_lay)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.setMouseTracking(True)
        self.set_title(title)
        self.set_closable(closable)
        if widget:
            self.set_content(widget)
        self.set_expand(expand)

    def set_content(self, widget):
        if self._central_widget:
            self.content_layout.removeWidget(self._central_widget)
            self._central_widget.close()
        self.content_layout.addWidget(widget)
        self._central_widget = widget

    def get_content(self):
        return self._central_widget

    def set_closable(self, value):
        self.setProperty("closable", value)

    def _set_closable(self, value):
        self.content_widget.setVisible(value)
        self._close_button.setVisible(value)

    def set_expand(self, value):
        self.setProperty("expand", value)

    def _set_expand(self, value):
        self.content_widget.setVisible(value)
        self.expand_icon.setPixmap(MPixmap("down_line.svg" if value else "right_line.svg").scaledToHeight(12))

    def set_title(self, value):
        self.setProperty("title", value)

    def _set_title(self, value):
        self.title_label.setText(value)

    def eventFilter(self, widget, event):
        if widget in [self.header_widget, self.title_label]:
            if event.type() == QtCore.QEvent.MouseButtonRelease:
                self.set_expand(not self.property("expand"))
        return super(QtWidgets.QWidget, self).eventFilter(widget, event)


class MCollapse(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MCollapse, self).__init__(parent)
        self._section_list = []
        self._main_layout = QtWidgets.QVBoxLayout()
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self._main_layout.setSpacing(1)
        self._main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_layout)

    def add_section(self, section_data):
        section_widget = MSectionItem(
            title=section_data.get("title"),
            expand=section_data.get("expand", False),
            widget=section_data.get("widget"),
            closable=section_data.get("closable", False),
        )
        self._main_layout.insertWidget(self._main_layout.count(), section_widget)
        return section_widget

    def add_section_list(self, section_list):
        for section_data in section_list:
            section_widget = self.add_section(section_data)
            section_widget._close_button.clicked.connect(functools.partial(self.remove_section, section_widget))
            self._section_list.append(section_widget)

    def remove_section(self, widget):
        self._section_list.remove(widget)

    def sections(self):
        return self._section_list

    def clear(self):
        for widget in self._section_list:
            self._main_layout.removeWidget(widget)
            del widget
