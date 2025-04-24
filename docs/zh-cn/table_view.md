# MTableView 表格视图

MTableView 是一个表格视图组件，用于展示结构化数据。它基于 Qt 的 QTableView 类，提供了更美观的样式和更好的交互体验，支持排序、筛选、自定义代理等功能。

## 导入

```python
from dayu_widgets.item_view import MTableView
```

## 代码示例

### 基本使用

MTableView 需要与 MTableModel 和 MSortFilterModel 一起使用，以展示和管理数据。

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_model import MSortFilterModel

# 创建模型
model = MTableModel()
model.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])

# 创建排序筛选模型
sort_filter_model = MSortFilterModel()
sort_filter_model.setSourceModel(model)

# 创建表格视图
table_view = MTableView()
table_view.setModel(sort_filter_model)
table_view.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])

# 设置数据
model.set_data_list([
    {"name": "张三", "age": 18, "city": "北京"},
    {"name": "李四", "age": 25, "city": "上海"},
    {"name": "王五", "age": 30, "city": "广州"}
])
```

### 不同尺寸

MTableView 支持不同的尺寸，可以通过 `size` 参数设置。

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets import dayu_theme

# 创建小尺寸的表格视图
table_small = MTableView(size=dayu_theme.small, show_row_count=True)

# 创建中等尺寸的表格视图（默认）
table_default = MTableView(size=dayu_theme.medium, show_row_count=True)

# 创建大尺寸的表格视图
table_large = MTableView(size=dayu_theme.large, show_row_count=False)
```

### 显示网格线

MTableView 默认不显示网格线，可以通过 `setShowGrid` 方法设置显示网格线。

```python
from dayu_widgets.item_view import MTableView

# 创建表格视图
table_grid = MTableView()

# 设置显示网格线
table_grid.setShowGrid(True)
```

### 搜索过滤

MTableView 可以与 MLineEdit 结合使用，实现搜索过滤功能。

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.line_edit import MLineEdit

# 创建模型和视图
model = MTableModel()
sort_filter_model = MSortFilterModel()
sort_filter_model.setSourceModel(model)
table_view = MTableView()
table_view.setModel(sort_filter_model)

# 创建搜索框
search_line_edit = MLineEdit().search().small()
search_line_edit.textChanged.connect(sort_filter_model.set_search_pattern)
```

### 加载状态

MTableView 可以与 MLoadingWrapper 结合使用，显示加载状态。

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.loading import MLoadingWrapper
import functools

# 创建表格视图
table_view = MTableView()

# 创建加载包装器
loading_wrapper = MLoadingWrapper(widget=table_view, loading=False)

# 模拟数据加载
def fetch_data():
    # 显示加载状态
    loading_wrapper.set_dayu_loading(True)

    # 模拟网络请求
    # ...

    # 隐藏加载状态
    loading_wrapper.set_dayu_loading(False)
```

### 自定义代理

MTableView 支持使用自定义代理来展示特定列的数据。

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.delegate import MPushButtonDelegate

# 创建模型和视图
model = MTableModel()
sort_filter_model = MSortFilterModel()
sort_filter_model.setSourceModel(model)
table_view = MTableView()
table_view.setModel(sort_filter_model)

# 创建按钮代理
button_delegate = MPushButtonDelegate(parent=table_view)
table_view.setItemDelegateForColumn(4, button_delegate)  # 为第5列设置按钮代理

# 连接按钮点击事件
button_delegate.sig_clicked.connect(lambda index: print("点击了按钮，行索引:", index.row()))
```

### 保存和恢复状态

MTableView 支持保存和恢复表头状态，包括列宽、列顺序等。

```python
from dayu_widgets.item_view import MTableView

# 创建表格视图
table_view = MTableView()

# 保存表头状态
table_view.save_state("my_table")

# 恢复表头状态
table_view.load_state("my_table")
```

### 完整示例

![MTableView 演示](../_media/screenshots/MTableView.png)

以下是一个完整的示例，展示了 MTableView 的各种用法：

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.alert import MAlert
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_view import MTableView
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton
import examples._mock_data as mock


class MFetchDataThread(QtCore.QThread):
    """A mock thread to fetch data"""
    sig_fetch_finished = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(MFetchDataThread, self).__init__(parent)
        self.size = 5

    def run(self, *args, **kwargs):
        self.msleep(800)
        self.sig_fetch_finished.emit(mock.data_list)


class TableViewExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(TableViewExample, self).__init__(parent)
        self.setWindowTitle("Examples for MTableView")
        self._init_ui()

    def _init_ui(self):
        model_1 = MTableModel()
        model_1.set_header_list(mock.header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)

        table_small = MTableView(size=dayu_theme.small, show_row_count=True)
        table_grid = MTableView(size=dayu_theme.small, show_row_count=True)
        table_grid.setShowGrid(True)
        table_default = MTableView(size=dayu_theme.medium, show_row_count=True)
        thread = MFetchDataThread(self)

        self.loading_wrapper = MLoadingWrapper(widget=table_default, loading=False)
        thread.started.connect(functools.partial(self.loading_wrapper.set_dayu_loading, True))
        thread.finished.connect(functools.partial(self.loading_wrapper.set_dayu_loading, False))
        thread.finished.connect(functools.partial(table_default.setModel, model_sort))
        button = MPushButton(text="获取数据: 4s")
        button.clicked.connect(thread.start)
        switch_lay = QtWidgets.QHBoxLayout()
        switch_lay.addWidget(button)
        switch_lay.addStretch()
        table_large = MTableView(size=dayu_theme.large, show_row_count=False)

        table_small.setModel(model_sort)
        table_grid.setModel(model_sort)
        table_large.setModel(model_sort)
        model_sort.set_header_list(mock.header_list)
        table_small.set_header_list(mock.header_list)
        table_grid.set_header_list(mock.header_list)
        table_default.set_header_list(mock.header_list)
        table_large.set_header_list(mock.header_list)
        model_1.set_data_list(mock.data_list)

        line_edit = MLineEdit().search().small()
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(line_edit)
        main_lay.addWidget(MDivider("小尺寸"))
        main_lay.addWidget(table_small)
        main_lay.addWidget(MDivider("默认尺寸"))
        main_lay.addLayout(switch_lay)
        main_lay.addWidget(self.loading_wrapper)
        main_lay.addWidget(MDivider("大尺寸（隐藏行数）"))
        main_lay.addWidget(table_large)
        main_lay.addWidget(MDivider("显示网格线"))
        main_lay.addWidget(table_grid)
        main_lay.addStretch()
        main_lay.addWidget(MAlert('简单使用 "MItemViewSet" 或 "MItemViewFullSet"'))
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = TableViewExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MTableView(size=None, show_row_count=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `size` | 表格尺寸 | `int` | `dayu_theme.default_size` |
| `show_row_count` | 是否显示行号 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_header_list(header_list)` | 设置表头列表 | `header_list`: 表头列表 | 无 |
| `save_state(name)` | 保存表头状态 | `name`: 状态名称 | 无 |
| `load_state(name)` | 加载表头状态 | `name`: 状态名称 | 无 |
| `enable_context_menu(enable)` | 启用右键菜单 | `enable`: 是否启用 | 无 |
| `slot_context_menu(point)` | 右键菜单槽函数 | `point`: 右键点击位置 | 无 |

### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_context_menu` | 右键菜单信号 | `object`: 右键菜单数据 |

### 继承的方法

MTableView 继承自 QTableView，因此可以使用 QTableView 的所有方法，例如：

- `setModel(model)`: 设置数据模型
- `setShowGrid(show)`: 设置是否显示网格线
- `setSelectionBehavior(behavior)`: 设置选择行为
- `setSelectionMode(mode)`: 设置选择模式
- `setSortingEnabled(enable)`: 设置是否启用排序
- 更多方法请参考 Qt 文档

## 常见问题

### 如何设置表头？

可以通过 `set_header_list` 方法设置表头，该方法接受一个列表，列表中的每个元素是一个字典，包含 `key` 和 `label` 等键：

```python
from dayu_widgets.item_view import MTableView

# 创建表格视图
table_view = MTableView()

# 设置表头
table_view.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄", "width": 80},
    {"key": "city", "label": "城市"}
])
```

### 如何设置数据？

数据需要通过 MTableModel 的 `set_data_list` 方法设置：

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_model import MSortFilterModel

# 创建模型
model = MTableModel()
model.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])

# 创建排序筛选模型
sort_filter_model = MSortFilterModel()
sort_filter_model.setSourceModel(model)

# 创建表格视图
table_view = MTableView()
table_view.setModel(sort_filter_model)
table_view.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])

# 设置数据
model.set_data_list([
    {"name": "张三", "age": 18, "city": "北京"},
    {"name": "李四", "age": 25, "city": "上海"},
    {"name": "王五", "age": 30, "city": "广州"}
])
```

### 如何实现搜索过滤？

可以通过 MSortFilterModel 的 `set_search_pattern` 方法实现搜索过滤：

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.line_edit import MLineEdit

# 创建模型和视图
model = MTableModel()
sort_filter_model = MSortFilterModel()
sort_filter_model.setSourceModel(model)
table_view = MTableView()
table_view.setModel(sort_filter_model)

# 创建搜索框
search_line_edit = MLineEdit().search().small()
search_line_edit.textChanged.connect(sort_filter_model.set_search_pattern)
```

### 如何使用 MItemViewSet 简化代码？

MItemViewSet 是一个封装了 MTableView、MTableModel 和 MSortFilterModel 的组件，可以简化代码：

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建表格视图集
item_view_set = MItemViewSet()

# 设置表头
item_view_set.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])

# 设置数据
item_view_set.set_data_list([
    {"name": "张三", "age": 18, "city": "北京"},
    {"name": "李四", "age": 25, "city": "上海"},
    {"name": "王五", "age": 30, "city": "广州"}
])
```

### 如何处理表格中的按钮点击事件？

可以使用 MPushButtonDelegate 为特定列设置按钮代理，并连接点击事件：

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.delegate import MPushButtonDelegate

# 创建表格视图
table_view = MTableView()

# 创建按钮代理
button_delegate = MPushButtonDelegate(parent=table_view)
table_view.setItemDelegateForColumn(4, button_delegate)  # 为第5列设置按钮代理

# 连接按钮点击事件
button_delegate.sig_clicked.connect(lambda index: print("点击了按钮，行索引:", index.row()))
```
