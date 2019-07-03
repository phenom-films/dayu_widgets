#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.item_model import MSortFilterModel, MTableModel
from dayu_widgets.item_view import MTableView, MTreeView, MBigView, MListView
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.qt import QWidget, QModelIndex, Signal, QVBoxLayout, QApplication, Qt, Slot, QHBoxLayout


class MItemViewSet(QWidget):
    sig_double_clicked = Signal(QModelIndex)
    sig_left_clicked = Signal(QModelIndex)
    TableViewType = MTableView
    BigViewType = MBigView
    TreeViewType = MTreeView
    ListViewType = MListView

    def __init__(self, view_type=None, parent=None):
        super(MItemViewSet, self).__init__(parent)
        self._main_lay = QVBoxLayout()
        self._main_lay.setSpacing(5)
        self._main_lay.setContentsMargins(0, 0, 0, 0)

        self.sort_filter_model = MSortFilterModel()
        self.source_model = MTableModel()
        self.sort_filter_model.setSourceModel(self.source_model)
        view_class = view_type or MItemViewSet.TableViewType
        self.item_view = view_class()
        self.item_view.doubleClicked.connect(self.sig_double_clicked)
        self.item_view.pressed.connect(self.slot_left_clicked)
        self.item_view.setModel(self.sort_filter_model)

        self._search_line_edit = MLineEdit().search().small()
        self._search_attr_button = MToolButton().icon_only().svg('down_fill.svg').small()
        self._search_line_edit.set_prefix_widget(self._search_attr_button)
        self._search_line_edit.textChanged.connect(self.sort_filter_model.set_search_pattern)
        self._search_line_edit.setVisible(False)
        _search_lay = QHBoxLayout()
        _search_lay.setContentsMargins(0, 0, 0, 0)
        _search_lay.addStretch()
        _search_lay.addWidget(self._search_line_edit)

        self._main_lay.addLayout(_search_lay)
        self._main_lay.addWidget(self.item_view)
        self.setLayout(self._main_lay)

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
        self.item_view.set_header_list(header_list)

    @Slot()
    def setup_data(self, data_list):
        self.source_model.clear()
        if data_list:
            self.source_model.set_data_list(data_list)

    def get_data(self):
        return self.source_model.get_data_list()

    def searchable(self):
        """Enable search line edit visible."""
        self._search_line_edit.setVisible(True)
        return self
