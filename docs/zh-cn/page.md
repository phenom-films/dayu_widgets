# MPage 分页

MPage 是一个分页组件，用于将长列表数据分成多个页面显示，每次只加载一页数据，提高应用程序的性能和用户体验。

## 导入

```python
from dayu_widgets.page import MPage
```

## 代码示例

### 基本使用

MPage 可以通过 `set_total` 方法设置总数据条数，并通过 `sig_page_changed` 信号监听页码变化：

```python
from dayu_widgets.page import MPage

# 创建一个分页组件
page = MPage()

# 设置总数据条数
page.set_total(255)

# 监听页码变化
page.sig_page_changed.connect(lambda page_size, current_page: print(f"每页 {page_size} 条，当前第 {current_page} 页"))
```

### 自定义每页条数选项

MPage 默认提供了每页 25、50、75、100 条数据的选项，你可以通过 `set_page_config` 方法自定义这些选项：

```python
from dayu_widgets.page import MPage

# 创建一个分页组件
page = MPage()

# 设置总数据条数
page.set_total(255)

# 自定义每页条数选项
page.set_page_config([
    {"label": "10 条/页", "value": 10},
    {"label": "20 条/页", "value": 20},
    {"label": "30 条/页", "value": 30},
    {"label": "50 条/页", "value": 50}
])
```

### 与数据表格结合使用

MPage 通常与数据表格结合使用，以下是一个简单的示例：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.page import MPage
from dayu_widgets.table_view import MTableView


class PageTableExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PageTableExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 创建表格
        self.table_view = MTableView()
        self.model = QtWidgets.QStandardItemModel()
        self.table_view.setModel(self.model)

        # 创建分页组件
        self.page = MPage()
        self.page.set_total(255)
        self.page.sig_page_changed.connect(self.slot_page_changed)

        # 初始化布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(self.table_view)
        main_lay.addWidget(self.page)
        self.setLayout(main_lay)

        # 加载第一页数据
        self.slot_page_changed(self.page.field("page_size_selected"), 1)

    def slot_page_changed(self, page_size, current_page):
        # 清空表格
        self.model.clear()

        # 设置表头
        self.model.setHorizontalHeaderLabels(["ID", "名称", "描述"])

        # 计算当前页的起始索引
        start_index = (current_page - 1) * page_size

        # 加载当前页的数据
        for i in range(page_size):
            index = start_index + i
            if index < self.page.field("total"):
                self.model.appendRow([
                    QtWidgets.QStandardItem(str(index + 1)),
                    QtWidgets.QStandardItem(f"项目 {index + 1}"),
                    QtWidgets.QStandardItem(f"这是项目 {index + 1} 的描述")
                ])
```

### 完整示例

![MPage 演示](../_media/screenshots/MPage.gif)

以下是一个完整的示例，展示了 MPage 的基本用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.page import MPage


class PageExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PageExample, self).__init__(parent)
        self.setWindowTitle("Examples for MPage")
        self._init_ui()

    def _init_ui(self):
        # 创建第一个分页组件
        page_1 = MPage()
        page_1.set_total(255)
        page_1.sig_page_changed.connect(self.slot_page_changed)

        # 创建第二个分页组件，自定义每页条数选项
        page_2 = MPage()
        page_2.set_total(100)
        page_2.set_page_config([
            {"label": "10 条/页", "value": 10},
            {"label": "20 条/页", "value": 20},
            {"label": "30 条/页", "value": 30}
        ])
        page_2.sig_page_changed.connect(self.slot_page_changed)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("基本示例"))
        main_lay.addWidget(page_1)
        main_lay.addWidget(MDivider("自定义每页条数"))
        main_lay.addWidget(page_2)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_page_changed(self, page_size, current_page):
        print(f"每页 {page_size} 条，当前第 {current_page} 页")


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = PageExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MPage(parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_total(value)` | 设置总数据条数 | `value`: 总数据条数 | 无 |
| `set_page_config(data_list)` | 设置每页条数选项 | `data_list`: 每页条数选项列表 | 无 |
| `field(name)` | 获取字段值 | `name`: 字段名称 | 字段值 |
| `set_field(name, value)` | 设置字段值 | `name`: 字段名称<br>`value`: 字段值 | 无 |

### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_page_changed` | 页码变化时触发 | `page_size`: 每页条数<br>`current_page`: 当前页码 |

### 字段

MPage 使用 MFieldMixin 来管理内部状态，以下是主要的字段：

| 字段 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `page_size_selected` | 当前选择的每页条数 | `int` | `25` |
| `page_size_list` | 每页条数选项列表 | `list` | 预设的选项列表 |
| `total` | 总数据条数 | `int` | `0` |
| `current_page` | 当前页码 | `int` | `0` |
| `total_page` | 总页数 | `int` | 计算得出 |
| `display_text` | 显示文本 | `str` | 计算得出 |

## 常见问题

### 如何获取当前页码和每页条数？

可以通过 `field` 方法获取当前页码和每页条数：

```python
page = MPage()
page.set_total(255)

# 获取当前页码
current_page = page.field("current_page")

# 获取每页条数
page_size = page.field("page_size_selected")
```

### 如何手动设置当前页码？

可以通过 `set_field` 方法设置当前页码：

```python
page = MPage()
page.set_total(255)

# 设置当前页码为 3
page.set_field("current_page", 3)
```

### 如何计算总页数？

总页数是根据总数据条数和每页条数自动计算的，可以通过 `field` 方法获取：

```python
page = MPage()
page.set_total(255)

# 获取总页数
total_page = page.field("total_page")
```

### 如何自定义每页条数选项的显示文本？

可以在 `set_page_config` 方法中设置每个选项的 `label` 和 `value`：

```python
page = MPage()
page.set_page_config([
    {"label": "10 - 最快", "value": 10},
    {"label": "20 - 较快", "value": 20},
    {"label": "50 - 中等", "value": 50},
    {"label": "100 - 较慢", "value": 100}
])
```
