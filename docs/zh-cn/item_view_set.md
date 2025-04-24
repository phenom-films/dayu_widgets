# MItemViewSet 视图集

MItemViewSet 是一个视图集组件，它封装了 MTableView、MListView、MTreeView 和 MBigView 等视图组件，以及 MTableModel 和 MSortFilterModel 模型组件，提供了一个统一的接口来管理和展示数据。

## 导入

```python
from dayu_widgets.item_view_set import MItemViewSet
```

## 代码示例

### 基本使用

MItemViewSet 可以通过 `view_type` 参数指定要使用的视图类型。

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建表格视图集
table_view_set = MItemViewSet(view_type=MItemViewSet.TableViewType)

# 设置表头
table_view_set.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])

# 设置数据
table_view_set.setup_data([
    {"name": "张三", "age": 18, "city": "北京"},
    {"name": "李四", "age": 25, "city": "上海"},
    {"name": "王五", "age": 30, "city": "广州"}
])
```

### 不同视图类型

MItemViewSet 支持四种视图类型：TableViewType、ListViewType、TreeViewType 和 BigViewType。

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建表格视图集
table_view_set = MItemViewSet(view_type=MItemViewSet.TableViewType)

# 创建列表视图集
list_view_set = MItemViewSet(view_type=MItemViewSet.ListViewType)

# 创建树形视图集
tree_view_set = MItemViewSet(view_type=MItemViewSet.TreeViewType)

# 创建大图视图集
big_view_set = MItemViewSet(view_type=MItemViewSet.BigViewType)
```

### 启用搜索功能

MItemViewSet 可以通过 `searchable` 方法启用搜索功能。

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建表格视图集
table_view_set = MItemViewSet(view_type=MItemViewSet.TableViewType)

# 启用搜索功能
table_view_set.searchable()
```

### 插入自定义部件

MItemViewSet 可以通过 `insert_widget` 方法插入自定义部件。

```python
from dayu_widgets.item_view_set import MItemViewSet
from dayu_widgets.push_button import MPushButton

# 创建树形视图集
tree_view_set = MItemViewSet(view_type=MItemViewSet.TreeViewType)

# 创建展开和折叠按钮
expand_button = MPushButton("展开全部")
expand_button.clicked.connect(tree_view_set.item_view.expandAll)

collapse_button = MPushButton("折叠全部")
collapse_button.clicked.connect(tree_view_set.item_view.collapseAll)

# 插入自定义部件
tree_view_set.insert_widget(expand_button)
tree_view_set.insert_widget(collapse_button)
```

### 完整示例

![MItemViewSet 演示](../_media/screenshots/MItemViewSet.png)

以下是一个完整的示例，展示了 MItemViewSet 的各种用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import utils
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_view_set import MItemViewSet
from dayu_widgets.push_button import MPushButton
import examples._mock_data as mock


@utils.add_settings("DaYu", "DaYuExample", event_name="hideEvent")
class ItemViewSetExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ItemViewSetExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 创建表格视图集
        item_view_set_table = MItemViewSet(view_type=MItemViewSet.TableViewType)
        item_view_set_table.set_header_list(mock.header_list)

        # 创建列表视图集
        item_view_set_list = MItemViewSet(view_type=MItemViewSet.ListViewType)
        item_view_set_list.set_header_list(mock.header_list)

        # 创建树形视图集
        item_view_set_tree = MItemViewSet(view_type=MItemViewSet.TreeViewType)
        item_view_set_tree.set_header_list(mock.header_list)

        # 创建大图视图集
        item_view_set_thumbnail = MItemViewSet(view_type=MItemViewSet.BigViewType)
        item_view_set_thumbnail.set_header_list(mock.header_list)

        # 创建带搜索功能的树形视图集
        item_view_set_search = MItemViewSet(view_type=MItemViewSet.TreeViewType)
        item_view_set_search.set_header_list(mock.header_list)
        item_view_set_search.searchable()

        # 添加展开和折叠按钮
        expand_button = MPushButton("展开全部")
        expand_button.clicked.connect(item_view_set_search.item_view.expandAll)
        coll_button = MPushButton("折叠全部")
        coll_button.clicked.connect(item_view_set_search.item_view.collapseAll)
        item_view_set_search.insert_widget(coll_button)
        item_view_set_search.insert_widget(expand_button)

        # 设置树形数据
        item_view_set_tree.setup_data(mock.tree_data_list)
        item_view_set_search.setup_data(mock.tree_data_list)

        # 保存视图列表，用于后续更新数据
        self.view_list = [
            item_view_set_table,
            item_view_set_list,
            item_view_set_thumbnail,
        ]

        # 绑定表头状态
        self.bind(
            "item_view_set_example_header_state",
            item_view_set_table.item_view.header_view,
            "state",
        )

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("表格视图"))
        main_lay.addWidget(item_view_set_table)
        main_lay.addWidget(MDivider("列表视图"))
        main_lay.addWidget(item_view_set_list)
        main_lay.addWidget(MDivider("大图视图"))
        main_lay.addWidget(item_view_set_thumbnail)
        main_lay.addWidget(MDivider("树形视图"))
        main_lay.addWidget(item_view_set_tree)
        main_lay.addWidget(MDivider("带搜索功能的树形视图"))
        main_lay.addWidget(item_view_set_search)
        self.setLayout(main_lay)

        # 更新数据
        self.slot_update_data()

    def slot_update_data(self):
        for view in self.view_list:
            view.setup_data(mock.data_list)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = ItemViewSetExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MItemViewSet(view_type=None, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `view_type` | 视图类型 | `class` | `MItemViewSet.TableViewType` |
| `parent` | 父部件 | `QWidget` | `None` |

### 类属性

| 属性 | 描述 | 类型 |
| --- | --- | --- |
| `TableViewType` | 表格视图类型 | `class` |
| `ListViewType` | 列表视图类型 | `class` |
| `TreeViewType` | 树形视图类型 | `class` |
| `BigViewType` | 大图视图类型 | `class` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_header_list(header_list)` | 设置表头列表 | `header_list`: 表头列表 | 无 |
| `setup_data(data_list)` | 设置数据列表 | `data_list`: 数据列表 | 无 |
| `get_data()` | 获取数据列表 | 无 | `list`: 数据列表 |
| `searchable()` | 启用搜索功能 | 无 | `self`: 当前实例 |
| `insert_widget(widget)` | 插入自定义部件 | `widget`: 要插入的部件 | 无 |

### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_double_clicked` | 双击信号 | `QModelIndex`: 被双击的索引 |
| `sig_left_clicked` | 左键点击信号 | `QModelIndex`: 被点击的索引 |

## 常见问题

### 如何设置表头？

可以通过 `set_header_list` 方法设置表头，该方法接受一个列表，列表中的每个元素是一个字典，包含 `key` 和 `label` 等键：

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建视图集
item_view_set = MItemViewSet()

# 设置表头
item_view_set.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])
```

### 如何设置数据？

可以通过 `setup_data` 方法设置数据，该方法接受一个列表，列表中的每个元素是一个字典，包含与表头对应的键值对：

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建视图集
item_view_set = MItemViewSet()

# 设置表头
item_view_set.set_header_list([
    {"key": "name", "label": "姓名"},
    {"key": "age", "label": "年龄"},
    {"key": "city", "label": "城市"}
])

# 设置数据
item_view_set.setup_data([
    {"name": "张三", "age": 18, "city": "北京"},
    {"name": "李四", "age": 25, "city": "上海"},
    {"name": "王五", "age": 30, "city": "广州"}
])
```

### 如何获取数据？

可以通过 `get_data` 方法获取数据：

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建视图集
item_view_set = MItemViewSet()

# 设置数据
item_view_set.setup_data([
    {"name": "张三", "age": 18, "city": "北京"},
    {"name": "李四", "age": 25, "city": "上海"},
    {"name": "王五", "age": 30, "city": "广州"}
])

# 获取数据
data = item_view_set.get_data()
print(data)  # 输出数据列表
```

### 如何监听双击事件？

可以通过连接 `sig_double_clicked` 信号来监听双击事件：

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建视图集
item_view_set = MItemViewSet()

# 监听双击事件
item_view_set.sig_double_clicked.connect(lambda index: print("双击了行:", index.row()))
```

### 如何监听左键点击事件？

可以通过连接 `sig_left_clicked` 信号来监听左键点击事件：

```python
from dayu_widgets.item_view_set import MItemViewSet

# 创建视图集
item_view_set = MItemViewSet()

# 监听左键点击事件
item_view_set.sig_left_clicked.connect(lambda index: print("点击了行:", index.row()))
```
