#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################
from qt import *
from MTheme import global_theme
from MHeaderView import MHeaderView
import MItemModel
from MMenu import MMenu
import utils
from . import STATIC_FOLDERS

qss = '''
QTableView{{
    {text_font}
    background-color: white;
    alternate-background-color: {background};
    selection-background-color: rgba(45, 140, 240, 50);
    selection-color:#1e1e1e;
    border: 1px solid {border};
    padding: 0;
    gridline-color: {border};
}}

QTableView::item:hover{{
    background-color: rgba(45, 140, 240, 50);
}}
QTableView::item:selected{{
    background-color: rgba(45, 140, 240, 50);
}}

QTableView QTableCornerButton::section {{
    background-color: {background_selected};
    border: 0px solid {border};
    border-right: 1px solid {border};
    border-bottom: 1px solid {border};
    padding: 1px 6px;
}}

QTableView::indicator{{
    width: 13px;
    height: 13px;
    border-radius: 2px;
    border: 1px solid {border};
    background-color: white;
}}
QTableView::indicator:disabled{{
    border: 1px solid {border};
    background-color: {background_selected};
}}

QTableView::indicator:hover{{
    border: 1px solid {primary_light};
    background-color: white;
}}

QTableView::indicator:checked{{
    background-color: {primary};
    image: url(check.svg);
}}

QTableView::indicator:checked:disabled{{
    background-color: {disabled};
}}

QTableView::indicator:indeterminate {{
    background-color: {primary};
    image: url(minus.svg);
}}

QTableView::indicator:indeterminate:disabled {{
    background-color: {disabled};
}}


QScrollBar:horizontal {{
    border: 0 solid {border};
    height: 9px;
    margin: 0 32px 0 0;
    background-color: {border};
}}

QScrollBar::handle:horizontal {{
    background-color: {background_dark};
    min-width: 10px;
}}

QScrollBar::add-line:horizontal {{
    subcontrol-origin: margin;
    subcontrol-position: right center;
    background: {border};
    width: 15px;
}}

QScrollBar::sub-line:horizontal {{
    subcontrol-origin: margin;
    subcontrol-position: right center;
    background: {border};
    width: 15px;
    right: 16px;
}}

QScrollBar::left-arrow:horizontal {{
    width: 9px;
    height: 9px;
    position: relative;
    image: url(left_fill.svg)
}}

QScrollBar::right-arrow:horizontal {{
    width: 9px;
    height: 9px;
    position: relative;
    image: url(right_fill.svg)
}}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
    background: none;
}}

QScrollBar:vertical {{
    border: 0 solid {border};
    width: 9px;
    margin: 0 0 32px 0 ;
    background-color: {border};
}}

QScrollBar::handle:vertical {{
    background-color: {background_dark};
    min-height: 10px;
}}

QScrollBar::add-line:vertical {{
    subcontrol-origin: margin;
    subcontrol-position: center bottom;
    background: {border};
    height: 15px;
}}

QScrollBar::sub-line:vertical {{
    subcontrol-origin: margin;
    subcontrol-position: center bottom;
    background: {border};
    height: 15px;
    bottom: 16px;
}}

QScrollBar::up-arrow:vertical {{
    width: 9px;
    height: 9px;
    position: relative;
    image: url(up_fill.svg)
}}

QScrollBar::down-arrow:vertical {{
    width: 9px;
    height: 9px;
    position: relative;
    image: url(down_fill.svg)
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
    background: none;
}}
'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


class MOptionDelegate(QItemDelegate):
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
        super(MOptionDelegate, self).paint(painter, option, index)
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(Qt.white))
        pix = MPixmap('down_fill.svg')
        h = option.rect.height()
        pix = pix.scaledToWidth(h * 0.5, Qt.SmoothTransformation)
        painter.drawPixmap(option.rect.x() + option.rect.width() - h,
                           option.rect.y() + h / 4, pix)
        painter.restore()

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


class MTableView(QTableView):
    sig_context_menu = Signal(object)

    def __init__(self, size=None, show_row_count=False, parent=None):
        super(MTableView, self).__init__(parent)
        size = size or MView.DefaultSize
        ver_header_view = self.verticalHeader()
        ver_header_view.setDefaultSectionSize(global_theme.get(size + '_size'))
        self.header_list = []
        self.header_view = MHeaderView(Qt.Horizontal)
        self.header_view.setProperty('line_size', size)
        if not show_row_count:
            ver_header_view.hide()
        else:
            ver_header_view.setProperty('orientation', 'vertical')
            ver_header_view.setStyleSheet(self.header_view.styleSheet())
        self.setHorizontalHeader(self.header_view)
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setAlternatingRowColors(True)
        self.setShowGrid(False)
        self.setStyleSheet(qss)

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
        #     'title': attr.title(),  # 选填，显示在界面的该列的名字
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

    def save_state(self, name):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'DAYU', 'dayu_widgets')
        settings.setValue('{}/headerState'.format(name, self.header_view.saveState()))

    def load_state(self, name):
        settings = QSettings(QSettings.IniFormat, QSettings.UserScope, 'DAYU', 'dayu_widgets')
        if settings.value('{}/headerState'.format(name)):
            self.header_view.restoreState(settings.value('{}/headerState'.format(name)))
