#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
import dayu_widgets.utils as utils
from dayu_widgets.MHeaderView import MHeaderView
from dayu_widgets.MItemModel import MTableModel, MSortFilterModel
from dayu_widgets.MMenu import MMenu
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import loading_mixin
from dayu_widgets.qt import *


class MOptionDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(MOptionDelegate, self).__init__(parent)
        self.editor = None
        self.showed = False
        self.exclusive = True
        self.parent_widget = None
        self.arrow_space = 20
        self.arrow_height = 6

    def set_exclusive(self, flag):
        self.exclusive = flag

    def createEditor(self, parent, option, index):
        self.parent_widget = parent
        self.editor = MMenu(exclusive=self.exclusive, parent=parent)
        self.editor.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        model = utils.real_model(index)
        real_index = utils.real_index(index)
        data_obj = real_index.internalPointer()
        attr = '{}_list'.format(model.header_list[real_index.column()].get('key'))

        self.editor.set_data(utils.get_obj_value(data_obj, attr, []))
        self.editor.sig_value_changed.connect(self._slot_finish_edit)
        return self.editor

    def setEditorData(self, editor, index):
        editor.set_value(index.data(Qt.EditRole))

    def setModelData(self, editor, model, index):
        model.setData(index, editor.property('value'))

    def updateEditorGeometry(self, editor, option, index):
        editor.move(self.parent_widget.mapToGlobal(QPoint(option.rect.x(), option.rect.y() + option.rect.height())))

    def paint(self, painter, option, index):
        painter.save()
        if option.state & QStyle.State_MouseOver:
            painter.fillRect(option.rect, dayu_theme.color.primary_opacity)
        if option.state & QStyle.State_Selected:
            painter.fillRect(option.rect, dayu_theme.color.primary)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.white))
        pix = MPixmap('down_fill.svg', dayu_theme.color.icon)
        h = option.rect.height()
        pix = pix.scaledToWidth(h * 0.5, Qt.SmoothTransformation)
        painter.drawPixmap(option.rect.x() + option.rect.width() - h,
                           option.rect.y() + h / 4, pix)
        painter.restore()
        super(MOptionDelegate, self).paint(painter, option, index)

    @Slot(object)
    def _slot_finish_edit(self, obj):
        self.commitData.emit(self.editor)

    def sizeHint(self, option, index):
        orig = super(MOptionDelegate, self).sizeHint(option, index)
        return QSize(orig.width() + self.arrow_space, orig.height())

    # def eventFilter(self, obj, event):
    #     if obj is self.editor:
    #         print event.type(), obj.size()
    #     return super(MOptionDelegate, self).eventFilter(obj, event)


def set_header_list(self, header_list):
    self.header_list = header_list
    if self.header_view:
        self.header_view.setSortIndicator(-1, Qt.AscendingOrder)
        for index, i in enumerate(header_list):
            self.header_view.setSectionHidden(index, i.get('hide', False))
            self.header_view.resizeSection(index, i.get('width', 100))
            if i.get('order', None) is not None:
                self.header_view.setSortIndicator(index, i.get('order'))
            if i.get('selectable', False):
                delegate = MOptionDelegate(parent=self)
                delegate.set_exclusive(i.get('exclusive', True))
                self.setItemDelegateForColumn(index, delegate)
            elif self.itemDelegateForColumn(index):
                self.setItemDelegateForColumn(index, None)


def enable_context_menu(self, enable):
    if enable:
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.slot_context_menu)
    else:
        self.setContextMenuPolicy(Qt.NoContextMenu)


@Slot(QPoint)
def slot_context_menu(self, point):
    proxy_index = self.indexAt(point)
    if proxy_index.isValid():
        need_map = isinstance(self.model(), QSortFilterProxyModel)
        selection = []
        for index in self.selectionModel().selectedRows() or self.selectionModel().selectedIndexes():
            data_obj = self.model().mapToSource(index).internalPointer() if need_map else index.internalPointer()
            selection.append(data_obj)
        event = utils.ItemViewMenuEvent(view=self, selection=selection, extra={})
        self.sig_context_menu.emit(event)
    else:
        event = utils.ItemViewMenuEvent(view=self, selection=[], extra={})
        self.sig_context_menu.emit(event)


def drawEmptyText(self, text):
    model = utils.real_model(self.model())
    if model and isinstance(model, MTableModel):
        if not model.get_data_list():
            painter = QPainter(self.viewport())
            font_metrics = painter.fontMetrics()
            painter.setPen(QPen(dayu_theme.color.text_help))
            painter.drawText(self.width() / 2 - font_metrics.width(text) / 2, self.height() / 2 - 10, text)
            painter.end()


@loading_mixin
class MTableView(QTableView):
    sig_context_menu = Signal(object)
    _no_data_text = 'No Data'

    def __init__(self, size=None, show_row_count=False, parent=None):
        super(MTableView, self).__init__(parent)
        size = size or dayu_theme.default_size
        ver_header_view = MHeaderView(Qt.Vertical, parent=self)
        ver_header_view.setDefaultSectionSize(size)
        self.setVerticalHeader(ver_header_view)
        self.header_list = []
        self.header_view = MHeaderView(Qt.Horizontal, parent=self)
        self.header_view.setFixedHeight(size)
        if not show_row_count:
            ver_header_view.hide()
        else:
            ver_header_view.setProperty('orientation', 'vertical')
        self.setHorizontalHeader(self.header_view)
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setAlternatingRowColors(True)
        self.setShowGrid(False)

    def set_no_data_text(self, text):
        self._no_data_text = text

    def setShowGrid(self, flag):
        self.header_view.setProperty('grid', flag)
        self.verticalHeader().setProperty('grid', flag)
        self.header_view.style().polish(self.header_view)

        return super(MTableView, self).setShowGrid(flag)

    def set_header_list(self, header_list):
        self.header_list = header_list
        if self.header_view:
            self.header_view.setSortIndicator(-1, Qt.AscendingOrder)
            for index, i in enumerate(header_list):
                self.header_view.setSectionHidden(index, i.get('hide', False))
                self.header_view.resizeSection(index, i.get('width', 100))
                if i.get('order', None) is not None:
                    self.header_view.setSortIndicator(index, i.get('order'))
                if i.get('selectable', False):
                    # self.setIndexWidget()
                    delegate = MOptionDelegate(parent=self)
                    delegate.set_exclusive(i.get('exclusive', True))
                    self.setItemDelegateForColumn(index, delegate)
                # elif self.itemDelegateForColumn(index):
                #     self.setItemDelegateForColumn(index, None)

        # setting = {
        #     'key': attr,  # 必填，用来读取 model后台数据结构的属性
        #     'label': attr.title(),  # 选填，显示在界面的该列的名字
        #     'width': 100,  # 选填，单元格默认的宽度
        #     'default_filter': False,  # 选填，如果有组合的filter组件，该属性默认是否显示，默认False
        #     'searchable': False,  # 选填，如果有搜索组件，该属性是否可以被搜索，默认False
        #     'editable': False,  # 选填，该列是否可以双击编辑，默认False
        #     'selectable': False,  # 选填，该列是否可以双击编辑，且使用下拉列表选择。该下拉框的选项们，是通过 data 拿数据的
        #     'checkable': False,  # 选填，该单元格是否要加checkbox，默认False
        #     'exclusive': True,  # 配合selectable，如果是可以多选的则为 False，如果是单选，则为True
        #     'order': None,  # 选填，初始化时，该列的排序方式, 0 升序，1 降序
        #     # 下面的是每个单元格的设置，主要用来根据本单元格数据，动态设置样式
        #     'color': None,  # QColor选填，该单元格文字的颜色，例如根据百分比数据大小，大于100%显示红色，小于100%显示绿色
        #     'bg_color': None,  # 选填，该单元格的背景色，例如根据bool数据，True显示绿色，False显示红色
        #     'display': None,  # 选填，该单元显示的内容，例如数据是以分钟为单位，可以在这里给转换成按小时为单位
        #     'align': None,  # 选填，该单元格文字的对齐方式
        #     'font': None,  # 选填，该单元格文字的格式，例如加下划线、加粗等等
        #     'icon': None,  # 选填，该单格元的图标，注意，当 QListView 使用图标模式时，每个item的图片也是在这里设置
        #     'tooltip': None,  # 选填，鼠标指向该单元格时，显示的提示信息
        #     'size': None,  # 选填，该列的 hint size，设置
        #     'data': None,
        #     'edit': None
        # }

    def paintEvent(self, event):
        drawEmptyText(self, self._no_data_text)
        return super(MTableView, self).paintEvent(event)

    def save_state(self, name):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'DAYU', 'dayu_widgets')
        settings.setValue('{}/headerState'.format(name, self.header_view.saveState()))

    def load_state(self, name):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'DAYU', 'dayu_widgets')
        if settings.value('{}/headerState'.format(name)):
            self.header_view.restoreState(settings.value('{}/headerState'.format(name)))


class MTreeView(QTreeView):
    set_header_list = set_header_list
    enable_context_menu = enable_context_menu
    slot_context_menu = slot_context_menu
    sig_context_menu = Signal(object)
    _no_data_text = 'No Data'

    def __init__(self, parent=None):
        super(MTreeView, self).__init__(parent)
        self.header_list = []
        self.header_view = MHeaderView(Qt.Horizontal)
        self.setHeader(self.header_view)
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)

    def paintEvent(self, event):
        drawEmptyText(self, self._no_data_text)
        return super(MTreeView, self).paintEvent(event)

    def set_no_data_text(self, text):
        self._no_data_text = text


class MBigView(QListView):
    set_header_list = set_header_list
    enable_context_menu = enable_context_menu
    slot_context_menu = slot_context_menu
    sig_context_menu = Signal(object)
    _no_data_text = 'No Data'

    def __init__(self, parent=None):
        super(MBigView, self).__init__(parent)
        self.header_list = []
        self.header_view = None
        self.setViewMode(QListView.IconMode)
        self.setResizeMode(QListView.Adjust)
        self.setMovement(QListView.Static)
        self.setSpacing(10)
        self.setIconSize(QSize(128, 128))

    def wheelEvent(self, event):
        if event.modifiers() == Qt.ControlModifier:
            num_degrees = event.delta() / 8.0
            num_steps = num_degrees / 15.0
            factor = pow(1.125, num_steps)
            new_size = self.iconSize() * factor
            if new_size.width() > 200:
                new_size = QSize(200, 200)
            elif new_size.width() < 24:
                new_size = QSize(24, 24)
            self.setIconSize(new_size)
        else:
            super(MBigView, self).wheelEvent(event)

    def paintEvent(self, event):
        drawEmptyText(self, self._no_data_text)
        return super(MBigView, self).paintEvent(event)

    def set_no_data_text(self, text):
        self._no_data_text = text


class MListView(QListView):
    set_header_list = set_header_list
    enable_context_menu = enable_context_menu
    slot_context_menu = slot_context_menu
    sig_context_menu = Signal(object)
    _no_data_text = 'No Data'

    def __init__(self, parent=None):
        super(MListView, self).__init__(parent)
        self.header_list = []
        self.header_view = None
        self.setModelColumn(0)
        self.setAlternatingRowColors(True)

    def set_show_column(self, attr):
        for index, attr_dict in enumerate(self.header_list):
            if attr_dict.get('key') == attr:
                self.setModelColumn(index)
                break
        else:
            self.setModelColumn(0)

    def paintEvent(self, event):
        drawEmptyText(self, self._no_data_text)
        return super(MListView, self).paintEvent(event)

    def set_no_data_text(self, text):
        self._no_data_text = text

    def minimumSizeHint(self, *args, **kwargs):
        return QSize(200, 50)
