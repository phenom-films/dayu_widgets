#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

import dayu_widgets.utils as utils
from dayu_widgets.MButtonGroup import MToolButtonGroup
from dayu_widgets.MItemModel import MSortFilterModel, MTableModel
from dayu_widgets.MItemView import MTableView, MTreeView, MListView, MBigView
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.MSwitch import MSwitch
from dayu_widgets.MLabel import MLabel
from dayu_widgets.MTheme import global_theme
from dayu_widgets.filter_tool_box import MFilterToolBox
from dayu_widgets.qt import *


class MItemViewSet(QWidget):
    sig_double_clicked = Signal(QModelIndex)
    sig_left_clicked = Signal(QModelIndex)
    sig_current_changed = Signal(QModelIndex, QModelIndex)
    sig_current_row_changed = Signal(QModelIndex, QModelIndex)
    sig_current_column_changed = Signal(QModelIndex, QModelIndex)
    sig_selection_changed = Signal(QItemSelection, QItemSelection)
    sig_context_menu = Signal(object)

    def __init__(self, table_view=True, list_view=False, big_view=False, tree_view=False, parent=None):
        super(MItemViewSet, self).__init__(parent)
        self.has_filter = False
        self.has_search = True
        self.sort_filter_model = MSortFilterModel()
        self.source_model = MTableModel()
        self.sort_filter_model.setSourceModel(self.source_model)

        self.stack_widget = QStackedWidget()

        self.view_button_grp = MToolButtonGroup(checkable=True)
        data_group = []
        if table_view:
            self.table_view = MTableView(show_row_count=True)
            self.table_view.doubleClicked.connect(self.sig_double_clicked)
            self.table_view.pressed.connect(self.slot_left_clicked)
            self.table_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.table_view)
            data_group.append({'icon': MIcon('table_view.svg'),
                               'icon_checked': MIcon('table_view.svg', global_theme.get('primary')),
                               'tooltip': u'Table View'})
        if list_view:
            self.list_view = MListView()
            self.list_view.doubleClicked.connect(self.sig_double_clicked)
            self.list_view.pressed.connect(self.slot_left_clicked)
            self.list_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.list_view)
            data_group.append({'icon': MIcon('list_view.svg'),
                               'icon_checked': MIcon('list_view.svg', global_theme.get('primary')),
                               'tooltip': u'List View'})
        if big_view:
            self.big_view = MBigView()
            self.big_view.doubleClicked.connect(self.sig_double_clicked)
            self.big_view.pressed.connect(self.slot_left_clicked)
            self.big_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.big_view)
            data_group.append({'icon': MIcon('big_view.svg'),
                               'icon_checked': MIcon('big_view.svg', global_theme.get('primary')),
                               'tooltip': u'Big View'})
        if tree_view:
            self.tree_view = MTreeView()
            self.tree_view.doubleClicked.connect(self.sig_double_clicked)
            self.tree_view.pressed.connect(self.slot_left_clicked)
            self.tree_view.setModel(self.sort_filter_model)
            self.stack_widget.addWidget(self.tree_view)
            data_group.append({'icon': MIcon('tree_view.svg'),
                               'icon_checked': MIcon('tree_view.svg', global_theme.get('primary')),
                               'tooltip': u'Tree View'})

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
        self.selection_model.currentColumnChanged.connect(self.sig_current_column_changed)
        self.selection_model.selectionChanged.connect(self.sig_selection_changed)

        self.status_bar = MLabel()
        self.status_bar.setVisible(False)

        self.row_count_bar = MLabel()
        self.row_count_bar.setVisible(False)

        self.tool_bar = QWidget()
        self.top_lay = QHBoxLayout()
        self.top_lay.setContentsMargins(0, 0, 0, 0)
        self.top_lay.addStretch()
        self.top_lay.addWidget(self.status_bar)
        self.top_lay.addStretch()
        self.top_lay.addWidget(self.row_count_bar)
        self.tool_bar.setLayout(self.top_lay)

        if len(data_group) > 1:
            self.view_button_grp.sig_checked_changed.connect(self.stack_widget.setCurrentIndex)
            self.view_button_grp.set_button_list(data_group)
            self.view_button_grp.set_checked(0)
            self.top_lay.addWidget(self.view_button_grp)

        self.main_lay = QVBoxLayout()
        self.main_lay.setSpacing(5)
        self.main_lay.setContentsMargins(0, 0, 0, 0)
        self.main_lay.addWidget(self.tool_bar)
        self.main_lay.addWidget(self.stack_widget)
        self.setLayout(self.main_lay)

    def show_row_count(self, flag):
        self.row_count_bar.setVisible(flag)

    def enable_context_menu(self):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.enable_context_menu(True)
            view.sig_context_menu.connect(self.sig_context_menu)

    def set_selection_mode(self, mode):
        for index in range(self.stack_widget.count()):
            view = self.stack_widget.widget(index)
            view.setSelectionMode(mode)

    def enable_search(self):
        search_line_edit = MLineEdit.search(size=MView.SmallSize)
        search_line_edit.textChanged.connect(self.sort_filter_model.set_search_pattern)
        self.tool_bar_insert_widget(search_line_edit)

    def enable_status_bar(self):
        self.status_bar.setVisible(True)

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

    def current_view(self):
        return self.stack_widget.currentWidget()

    @Slot()
    def setup_data(self, data_list):
        self.source_model.clear()
        if data_list:
            self.source_model.set_data_list(data_list)
        self.row_count_bar.setText(self.tr('Total: ') + str(self.source_model.rowCount()))
        # self.status_bar.setText(self.tr('Total: ') + str(self.source_model.root_item.child_count()))

    def get_data(self):
        return self.source_model.get_data_list()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MItemViewSet(list_view=True)
    test.set_header_list(
        [{'label': 'Name', 'key': 'name', 'editable': True, 'selectable': True, 'exclusive': False, 'width': 200,
          }])
    # only_work_check_box = QCheckBox('Show Special Tasks')
    # only_work_check_box.setChecked(False)
    # only_work_check_box.stateChanged.connect(test.slot_update)
    # test.add_button(only_work_check_box)
    test.setup_data([{'name': ['xiaoming'], 'name_list': ['li', 'haha', 'xiaoming']}])
    test.enable_search()
    # test.enable_filter()
    test.show_row_count(True)
    test.show()
    sys.exit(app.exec_())
