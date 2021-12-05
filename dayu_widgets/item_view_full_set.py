#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets.button_group import MToolButtonGroup
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_view import MBigView
from dayu_widgets.item_view import MTableView
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.page import MPage
from dayu_widgets.qt import MIcon
from dayu_widgets.qt import QApplication
from dayu_widgets.qt import QHBoxLayout
from dayu_widgets.qt import QItemSelection
from dayu_widgets.qt import QModelIndex
from dayu_widgets.qt import QStackedWidget
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.qt import Qt
from dayu_widgets.qt import Signal
from dayu_widgets.qt import Slot
from dayu_widgets.tool_button import MToolButton


class MItemViewFullSet(QWidget):
    sig_double_clicked = Signal(QModelIndex)
    sig_left_clicked = Signal(QModelIndex)
    sig_current_changed = Signal(QModelIndex, QModelIndex)
    sig_current_row_changed = Signal(QModelIndex, QModelIndex)
    sig_current_column_changed = Signal(QModelIndex, QModelIndex)
    sig_selection_changed = Signal(QItemSelection, QItemSelection)
    sig_context_menu = Signal(object)

    def __init__(self, table_view=True, big_view=False, parent=None):
        super(MItemViewFullSet, self).__init__(parent)
        self.sort_filter_model = MSortFilterModel()
        self.source_model = MTableModel()
        self.sort_filter_model.setSourceModel(self.source_model)

        self.stack_widget = QStackedWidget()

        self.view_button_grp = MToolButtonGroup(exclusive=True)
        data_group = []
        if table_view:
            self.table_view = MTableView(show_row_count=True)
            self.table_view.doubleClicked.connect(self.sig_double_clicked)
            self.table_view.pressed.connect(self.slot_left_clicked)
            self.table_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.table_view)
            data_group.append(
                {"svg": "table_view.svg", "checkable": True, "tooltip": "Table View"}
            )
        if big_view:
            self.big_view = MBigView()
            self.big_view.doubleClicked.connect(self.sig_double_clicked)
            self.big_view.pressed.connect(self.slot_left_clicked)
            self.big_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.big_view)
            data_group.append(
                {"svg": "big_view.svg", "checkable": True, "tooltip": "Big View"}
            )

        # 设置多个view 共享 MItemSelectionModel
        leader_view = self.stack_widget.widget(0)
        self.selection_model = leader_view.selectionModel()
        for index in range(self.stack_widget.count()):
            if index == 0:
                continue
            other_view = self.stack_widget.widget(index)
            other_view.setSelectionModel(self.selection_model)

        self.selection_model.currentChanged.connect(self.sig_current_changed)
        self.selection_model.currentRowChanged.connect(self.sig_current_row_changed)
        self.selection_model.currentColumnChanged.connect(
            self.sig_current_column_changed
        )
        self.selection_model.selectionChanged.connect(self.sig_selection_changed)

        self.tool_bar = QWidget()
        self.top_lay = QHBoxLayout()
        self.top_lay.setContentsMargins(0, 0, 0, 0)
        if data_group and len(data_group) > 1:
            self.view_button_grp.sig_checked_changed.connect(
                self.stack_widget.setCurrentIndex
            )
            self.view_button_grp.set_button_list(data_group)
            self.view_button_grp.set_dayu_checked(0)
            self.top_lay.addWidget(self.view_button_grp)
        self.search_line_edit = MLineEdit().search().small()
        self.search_attr_button = MToolButton().icon_only().svg("down_fill.svg").small()
        self.search_line_edit.set_prefix_widget(self.search_attr_button)
        self.search_line_edit.textChanged.connect(
            self.sort_filter_model.set_search_pattern
        )
        self.search_line_edit.setVisible(False)

        self.top_lay.addStretch()
        self.top_lay.addWidget(self.search_line_edit)
        self.tool_bar.setLayout(self.top_lay)

        self.page_set = MPage()
        self.main_lay = QVBoxLayout()
        self.main_lay.setSpacing(5)
        self.main_lay.setContentsMargins(0, 0, 0, 0)
        self.main_lay.addWidget(self.tool_bar)
        self.main_lay.addWidget(self.stack_widget)
        self.main_lay.addWidget(self.page_set)
        self.setLayout(self.main_lay)

    def enable_context_menu(self):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.enable_context_menu(True)
            view.sig_context_menu.connect(self.sig_context_menu)

    def set_no_data_text(self, text):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.set_no_data_text(text)

    def set_selection_mode(self, mode):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.setSelectionMode(mode)

    def tool_bar_visible(self, flag):
        self.tool_bar.setVisible(flag)

    @Slot(QModelIndex)
    def slot_left_clicked(self, start_index):
        button = QApplication.mouseButtons()
        if button == Qt.LeftButton:
            real_index = self.sort_filter_model.mapToSource(start_index)
            self.sig_left_clicked.emit(real_index)

    def set_header_list(self, header_list):
        self.source_model.set_header_list(header_list)
        self.sort_filter_model.set_header_list(header_list)
        self.sort_filter_model.setSourceModel(self.source_model)
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.set_header_list(header_list)

    def tool_bar_append_widget(self, widget):
        self.top_lay.addWidget(widget)

    def tool_bar_insert_widget(self, widget):
        self.top_lay.insertWidget(0, widget)

    @Slot()
    def setup_data(self, data_list):
        self.source_model.clear()
        if data_list:
            self.source_model.set_data_list(data_list)
        self.set_record_count(len(data_list))
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.set_header_list(self.source_model.header_list)

    @Slot(int)
    def set_record_count(self, total):
        self.page_set.set_total(total)

    def get_data(self):
        return self.source_model.get_data_list()

    def searchable(self):
        """Enable search line edit visible."""
        self.search_line_edit.setVisible(True)
        return self
