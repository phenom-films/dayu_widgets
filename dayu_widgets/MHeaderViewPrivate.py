#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

import functools

import utils
from qt import *
from MMenu import MMenu
from MTheme import global_theme
from . import STATIC_FOLDERS

qss = '''
QHeaderView {{
    background-color: {background_selected};
    {small_head_font}
}}
QHeaderView::section, QTableCornerButton::section{{
    background-color: {background_selected};
    border: 0 solid {border};
    padding: 1px 6px;
}}
QHeaderView[line_size=large]::section{{
    min-height: {large_size}px;
    max-height: {large_size}px;
}}
QHeaderView[line_size=default]::section{{
    min-height: {default_size}px;
    max-height: {default_size}px;
}}
QHeaderView[line_size=small]::section{{
    min-height: {small_size}px;
    max-height: {small_size}px;
}}

QHeaderView[grid=true][orientation=horizontal]::section{{
    border-right: 1px solid {border};
    border-left: none;
    border-top: none;
    border-bottom: none;
}}


QHeaderView[grid=true][orientation=vertical]::section{{
    border-bottom: 1px solid {border};
    border-right: none;
    border-left: none;
    border-top: none;
}}

QHeaderView::section:hover {{
    color: {primary};
}}
QHeaderView::focus{{
    background-color: red;
    border: 0 solid {border};
}}
QHeaderView::up-arrow {{
    width: 12px;
    height: 12px;
    position: relative;
    bottom: 8;
    right: 50%;
    color: red;
    image: url(icon-up-arrow.png);
}}

QHeaderView::down-arrow {{
    width: 12px;
    height: 12px;
    position: relative;
    bottom: 2px;
    right: 10px;
    image: url(icon-down-arrow.png);
}}
'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


class MHeaderViewPrivate(QHeaderView):
    def __init__(self, orientation, parent=None):
        super(MHeaderViewPrivate, self).__init__(orientation, parent)
        self.setObjectName('test')

        self.setMovable(True)
        self.setClickable(True)
        self.setSortIndicatorShown(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._slot_context_menu)
        self.setDefaultAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setProperty('orientation', 'horizontal' if orientation == Qt.Horizontal else 'vertical')
        self.setStyleSheet(qss)

    # def enterEvent(self, *args, **kwargs):
    #     # 调整表头宽度的 cursor 就被覆盖了
    #     QApplication.setOverrideCursor(Qt.PointingHandCursor)
    #     return super(MHeaderViewPrivate, self).enterEvent(*args, **kwargs)
    #
    # def leaveEvent(self, *args, **kwargs):
    #     QApplication.restoreOverrideCursor()
    #     return super(MHeaderViewPrivate, self).leaveEvent(*args, **kwargs)

    @Slot(QPoint)
    def _slot_context_menu(self, point):
        context_menu = MMenu(parent=self)
        logical_column = self.logicalIndexAt(point)
        model = utils.real_model(self.model())
        if logical_column >= 0 and model.header_list[logical_column].get('checkable', False):
            action_select_all = context_menu.addAction(self.tr('Select All'))
            action_select_none = context_menu.addAction(self.tr('Select None'))
            action_select_invert = context_menu.addAction(self.tr('Select Invert'))
            self.connect(action_select_all, SIGNAL('triggered()'),
                         functools.partial(self._slot_set_select, logical_column, Qt.Checked))
            self.connect(action_select_none, SIGNAL('triggered()'),
                         functools.partial(self._slot_set_select, logical_column, Qt.Unchecked))
            self.connect(action_select_invert, SIGNAL('triggered()'),
                         functools.partial(self._slot_set_select, logical_column, None))
            context_menu.addSeparator()

        fit_action = context_menu.addAction(self.tr('Fit Size'))
        fit_action.setCheckable(True)
        fit_action.setChecked(True if self.resizeMode(0) == QHeaderView.ResizeToContents else False)
        fit_action.toggled.connect(self._slot_set_resize_mode)
        for column in range(self.count()):
            action = context_menu.addAction(model.headerData(column, Qt.Horizontal, Qt.DisplayRole))
            action.setCheckable(True)
            action.setChecked(not self.isSectionHidden(column))
            action.toggled.connect(functools.partial(self._slot_set_section_visible, column))
        context_menu.exec_(QCursor.pos() + QPoint(10, 10))

    @Slot(int, int)
    def _slot_set_select(self, column, state):
        model = utils.real_model(self.model())
        model.beginResetModel()
        attr = '{}_checked'.format(model.header_list[column].get('key'))
        for row in range(model.rowCount()):
            if isinstance(model, QSortFilterProxyModel):
                real_index = model.mapToSource(model.index(row, column))
            else:
                real_index = model.index(row, column, QModelIndex())
            data_obj = real_index.internalPointer()
            if state is None:
                old_state = utils.get_obj_value(data_obj, attr)
                utils.set_obj_value(data_obj, attr, Qt.Unchecked if old_state == Qt.Checked else Qt.Checked)
            else:
                utils.set_obj_value(data_obj, attr, state)
        model.endResetModel()
        model.emit(SIGNAL('dataChanged(QModelIndex, QModelIndex)'), None, None)

    @Slot(QModelIndex, int)
    def _slot_set_section_visible(self, index, flag):
        self.setSectionHidden(index, not flag)

    @Slot(bool)
    def _slot_set_resize_mode(self, flag):
        if flag:
            self.resizeSections(QHeaderView.ResizeToContents)
        else:
            self.resizeSections(QHeaderView.Interactive)

    def setClickable(self, flag):
        try:
            QHeaderView.setSectionsClickable(self, flag)
        except AttributeError:
            QHeaderView.setClickable(self, flag)

    def setMovable(self, flag):
        try:
            QHeaderView.setSectionsMovable(self, flag)
        except AttributeError:
            QHeaderView.setMovable(self, flag)

    def resizeMode(self, index):
        try:
            QHeaderView.sectionResizeMode(self, index)
        except AttributeError:
            QHeaderView.resizeMode(self, index)

    def setResizeMode(self, mode):
        try:
            QHeaderView.setResizeMode(self, mode)
        except AttributeError:
            QHeaderView.setSectionResizeMode(self, mode)
