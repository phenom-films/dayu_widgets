#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2018.5
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.qt import *
from dayu_widgets.utils import display_formatter, apply_formatter, font_formatter, icon_formatter, \
    get_obj_value, set_obj_value

SETTING_MAP = {
    Qt.BackgroundRole: {'config': 'bg_color', 'formatter': QColor},
    Qt.DisplayRole: {'config': 'display', 'formatter': display_formatter},
    Qt.EditRole: {'config': 'edit', 'formatter': None},
    Qt.TextAlignmentRole: {'config': 'alignment',
                           'formatter': {'right': Qt.AlignRight, 'left': Qt.AlignLeft, 'center': Qt.AlignCenter}},
    Qt.ForegroundRole: {'config': 'color', 'formatter': QColor},
    Qt.FontRole: {'config': 'font', 'formatter': font_formatter},
    Qt.DecorationRole: {'config': 'icon', 'formatter': icon_formatter},
    Qt.ToolTipRole: {'config': 'tooltip', 'formatter': display_formatter},
    Qt.InitialSortOrderRole: {'config': 'order', 'formatter': {'asc': Qt.AscendingOrder, 'des': Qt.DescendingOrder}},
    Qt.SizeHintRole: {'config': 'size', 'formatter': lambda args: QSize(*args)},
    Qt.UserRole: {'config': 'data'},  # anything
}


class MTableModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super(MTableModel, self).__init__(parent)
        self.origin_count = 0
        self.root_item = {'name': 'root', 'children': []}
        self.data_generator = None
        self.header_list = []
        self.timer = QTimer(self)
        self.connect(self.timer, SIGNAL('timeout()'), self.fetchMore)

    def set_header_list(self, header_list):
        self.header_list = header_list

    def set_data_list(self, data_list):
        if hasattr(data_list, 'next'):
            self.beginResetModel()
            self.root_item['children'] = []
            self.endResetModel()
            self.data_generator = data_list
            self.origin_count = 0
            self.timer.start()
        else:
            self.beginResetModel()
            self.root_item['children'] = data_list if data_list is not None else []
            self.endResetModel()
            self.data_generator = None

    def clear(self):
        self.beginResetModel()
        self.root_item['children'] = []
        self.endResetModel()

    def get_data_list(self):
        return self.root_item['children']

    def append(self, data_dict):
        self.root_item['children'].append(data_dict)
        self.fetchMore()

    def remove(self, data_dict):
        row = self.root_item['children'].index(data_dict)
        self.beginRemoveRows(QModelIndex(), row, row)
        self.root_item['children'].remove(data_dict)
        self.endRemoveRows()

    def flags(self, index):
        result = QAbstractItemModel.flags(self, index)
        if not index.isValid():
            return Qt.ItemIsEnabled
        if self.header_list[index.column()].get('checkable', False):
            result |= Qt.ItemIsUserCheckable
        if self.header_list[index.column()].get('selectable', False):
            result |= Qt.ItemIsEditable
        if self.header_list[index.column()].get('editable', False):
            result |= Qt.ItemIsEditable
        if self.header_list[index.column()].get('draggable', False):
            result |= Qt.ItemIsDragEnabled
        if self.header_list[index.column()].get('droppable', False):
            result |= Qt.ItemIsDropEnabled
        return Qt.ItemFlags(result)

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Vertical:
            return super(MTableModel, self).headerData(section, orientation, role)
        if not self.header_list or section >= len(self.header_list):
            return None
        if role == Qt.DisplayRole:
            return self.header_list[section]['label']
        return None

    def index(self, row, column, parent_index=None):
        if parent_index and parent_index.isValid():
            parent_item = parent_index.internalPointer()
        else:
            parent_item = self.root_item

        children_list = get_obj_value(parent_item, 'children')
        if children_list and len(children_list) > row:
            child_item = children_list[row]
            if child_item:
                set_obj_value(child_item, '_parent', parent_item)
                return self.createIndex(row, column, child_item)
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        child_item = index.internalPointer()
        parent_item = get_obj_value(child_item, '_parent')

        if parent_item is None:
            return QModelIndex()

        grand_item = get_obj_value(parent_item, '_parent')
        if grand_item is None:
            return QModelIndex()
        parent_list = get_obj_value(grand_item, 'children')
        return self.createIndex(parent_list.index(parent_item), 0, parent_item)

    def rowCount(self, parent_index=None):
        if parent_index and parent_index.isValid():
            parent_item = parent_index.internalPointer()
        else:
            parent_item = self.root_item
        children_obj = get_obj_value(parent_item, 'children')
        return len(children_obj) if not hasattr(children_obj, 'next') else 0

    def hasChildren(self, parent_index=None):
        if parent_index and parent_index.isValid():
            parent_data = parent_index.internalPointer()
        else:
            parent_data = self.root_item
        children_obj = get_obj_value(parent_data, 'children')
        if children_obj is None:
            return False
        if hasattr(children_obj, 'next'):
            return True
        else:
            return len(children_obj)

    def columnCount(self, parent_index=None):
        return len(self.header_list)

    def canFetchMore(self, index):
        try:
            if self.data_generator:
                data = self.data_generator.next()
                self.root_item['children'].append(data)
                return True
            return False
        except StopIteration:
            if self.timer.isActive():
                self.timer.stop()
            return False

    def fetchMore(self, index=None):
        self.beginResetModel()
        self.endResetModel()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        attr_dict = self.header_list[index.column()]  # 获取该列字段的配置
        data_obj = index.internalPointer()
        attr = attr_dict.get('key')
        if role in SETTING_MAP.keys():
            role_key = SETTING_MAP[role].get('config')  # role 配置的关键字
            formatter_from_config = attr_dict.get(role_key)  # header中该role的配置
            if not formatter_from_config and role not in [Qt.DisplayRole, Qt.EditRole, Qt.ToolTipRole]:
                # 如果header中没有配置该role，而且也不是 DisplayRole/EditRole，直接返回None
                return None
            else:
                value = apply_formatter(formatter_from_config, get_obj_value(data_obj, attr), data_obj)
            formatter_from_model = SETTING_MAP[role].get('formatter', None)  # role 配置的转换函数
            result = apply_formatter(formatter_from_model, value)
            return result

        if role == Qt.CheckStateRole and attr_dict.get('checkable', False):
            state = get_obj_value(data_obj, attr + '_checked')
            return Qt.Unchecked if state is None else state
        return None

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role in [Qt.CheckStateRole, Qt.EditRole]:
            attr_dict = self.header_list[index.column()]
            key = attr_dict.get('key')
            data_obj = index.internalPointer()
            if role == Qt.CheckStateRole and attr_dict.get('checkable', False):
                key += '_checked'
                # 更新自己
                set_obj_value(data_obj, key, value)
                self.emit(SIGNAL('dataChanged(QModelIndex, QModelIndex)'), index, index)

                # 更新它的children
                for row, sub_obj in enumerate(get_obj_value(data_obj, 'children', [])):
                    set_obj_value(sub_obj, key, value)
                    sub_index = index.child(row, index.column())
                    self.emit(SIGNAL('dataChanged(QModelIndex, QModelIndex)'), sub_index, sub_index)

                # 更新它的parent
                parent_index = index.parent()
                if parent_index.isValid():
                    parent_obj = parent_index.internalPointer()
                    new_parent_value = value
                    old_parent_value = get_obj_value(parent_obj, key)
                    for sibling_obj in get_obj_value(get_obj_value(data_obj, '_parent'), 'children', []):
                        if value != get_obj_value(sibling_obj, key):
                            new_parent_value = 1
                            break
                    if new_parent_value != old_parent_value:
                        set_obj_value(parent_obj, key, new_parent_value)
                        self.emit(SIGNAL('dataChanged(QModelIndex, QModelIndex)'), parent_index, parent_index)
            else:
                set_obj_value(data_obj, key, value)
                # 采用 self.dataChanged.emit方式在houdini16里面会报错
                # TypeError: dataChanged(QModelIndex,QModelIndex,QVector<int>) only accepts 3 arguments, 3 given!
                # 所以临时使用旧式信号的发射方式
                self.emit(SIGNAL('dataChanged(QModelIndex, QModelIndex)'), index, index)
                # self.dataChanged.emit(index, index)
            return True
        else:
            return False


class MSortFilterModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super(MSortFilterModel, self).__init__(parent)
        self.header_list = []
        self.search_reg = QRegExp()
        self.search_reg.setCaseSensitivity(Qt.CaseInsensitive)
        self.search_reg.setPatternSyntax(QRegExp.Wildcard)

    def set_header_list(self, header_list):
        self.header_list = header_list
        for head in self.header_list:
            reg_exp = QRegExp()
            reg_exp.setCaseSensitivity(Qt.CaseInsensitive)
            reg_exp.setPatternSyntax(QRegExp.RegExp)
            head.update({'reg': reg_exp})

    def filterAcceptsRow(self, source_row, source_parent):
        # 如果search 栏有内容 先匹配 search 栏的内容
        if self.search_reg.pattern():
            for index, data_dict in enumerate(self.header_list):
                if data_dict.get('searchable', False):
                    model_index = self.sourceModel().index(source_row, index, source_parent)
                    value = self.sourceModel().data(model_index)
                    if self.search_reg.indexIn(value) != -1:
                        # 搜索匹配上了
                        break
            else:
                # 全部搜索完毕，没有一个匹配，直接返回 False
                return False

        # 再去匹配 filter 组合
        for index, data_dict in enumerate(self.header_list):
            model_index = self.sourceModel().index(source_row, index, source_parent)
            value = self.sourceModel().data(model_index)
            reg_exp = data_dict.get('reg', None)
            if reg_exp and reg_exp.pattern() and (not reg_exp.exactMatch(value)):
                # 不符合筛选，直接返回 False
                return False

        return True

    def set_search_pattern(self, pattern):
        self.search_reg.setPattern(pattern)
        self.invalidateFilter()

    def set_filter_attr_pattern(self, attr, pattern):
        for data_dict in self.header_list:
            if data_dict.get('key') == attr:
                data_dict.get('reg').setPattern(pattern)
                break
        self.invalidateFilter()
