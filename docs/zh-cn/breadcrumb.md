# MBreadcrumb 面包屑

MBreadcrumb 是一个面包屑导航组件，用于显示当前页面在系统层级结构中的位置，并能够返回之前的任何一个层级。

## 导入

```python
from dayu_widgets.breadcrumb import MBreadcrumb
```

## 代码示例

### 基本使用

MBreadcrumb 可以通过 `set_item_list` 方法设置导航项列表。每个导航项是一个字典，可以包含以下键：

- `text`: 显示的文本
- `svg`: 图标的 SVG 文件名
- `icon`: 图标对象
- `tooltip`: 鼠标悬停时显示的提示文本
- `clicked`: 点击时触发的回调函数

```python
from dayu_widgets.breadcrumb import MBreadcrumb
import functools

# 创建一个面包屑导航
breadcrumb = MBreadcrumb()

# 设置导航项列表
item_list = [
    {
        "svg": "home_line.svg",  # 使用 SVG 图标
        "clicked": functools.partial(print, "点击了首页")
    },
    {
        "text": "项目",  # 显示文本
        "svg": "folder_line.svg",  # 使用 SVG 图标
        "clicked": functools.partial(print, "点击了项目")
    },
    {
        "text": "任务",  # 显示文本
        "clicked": functools.partial(print, "点击了任务")
    }
]

breadcrumb.set_item_list(item_list)
```

### 自定义分隔符

MBreadcrumb 默认使用 `/` 作为分隔符，你可以在创建时指定自定义分隔符：

```python
from dayu_widgets.breadcrumb import MBreadcrumb

# 创建一个使用 > 作为分隔符的面包屑导航
breadcrumb = MBreadcrumb(separator=">")

# 创建一个使用 => 作为分隔符的面包屑导航
breadcrumb_arrow = MBreadcrumb(separator="=>")
```

### 与消息提示结合使用

MBreadcrumb 通常与点击回调函数结合使用，以下是一个与 MMessage 结合的示例：

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.breadcrumb import MBreadcrumb
from dayu_widgets.divider import MDivider
from dayu_widgets.message import MMessage


class BreadcrumbExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(BreadcrumbExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBreadcrumb")
        self._init_ui()

    def _init_ui(self):
        MMessage.config(duration=1)
        entity_list = [
            {
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"首页"'),
                "svg": "home_line.svg",
            },
            {
                "text": "项目",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"项目"'),
                "svg": "user_line.svg",
            },
            {
                "text": "任务",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"任务"'),
            },
        ]
        no_icon_eg = MBreadcrumb()
        no_icon_eg.set_item_list(entity_list)

        separator_eg = MBreadcrumb(separator="=>")
        separator_eg.set_item_list(entity_list)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("默认分隔符"))
        main_lay.addWidget(no_icon_eg)
        main_lay.addWidget(MDivider("自定义分隔符: =>"))
        main_lay.addWidget(separator_eg)

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(config, parent=self)
```

### 完整示例

![MBreadcrumb 演示](../_media/screenshots/MBreadcrumb.gif)

以下是一个完整的示例，展示了 MBreadcrumb 的各种用法：

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.breadcrumb import MBreadcrumb
from dayu_widgets.divider import MDivider
from dayu_widgets.message import MMessage


class BreadcrumbExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(BreadcrumbExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBreadcrumb")
        self._init_ui()

    def _init_ui(self):
        MMessage.config(duration=1)

        # 基本示例
        basic_list = [
            {
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"首页"'),
                "svg": "home_line.svg",
            },
            {
                "text": "项目",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"项目"'),
                "svg": "user_line.svg",
            },
            {
                "text": "任务",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"任务"'),
            },
        ]
        basic_breadcrumb = MBreadcrumb()
        basic_breadcrumb.set_item_list(basic_list)

        # 自定义分隔符示例
        separator_breadcrumb = MBreadcrumb(separator="=>")
        separator_breadcrumb.set_item_list(basic_list)

        # 只有文本的示例
        text_only_list = [
            {
                "text": "首页",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"首页"'),
            },
            {
                "text": "设置",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"设置"'),
            },
            {
                "text": "个人信息",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"个人信息"'),
            },
        ]
        text_only_breadcrumb = MBreadcrumb()
        text_only_breadcrumb.set_item_list(text_only_list)

        # 带提示的示例
        tooltip_list = [
            {
                "text": "首页",
                "tooltip": "返回首页",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"首页"'),
                "svg": "home_line.svg",
            },
            {
                "text": "文档",
                "tooltip": "查看文档",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"文档"'),
                "svg": "file_line.svg",
            },
            {
                "text": "组件",
                "tooltip": "查看组件文档",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, '跳转到"组件"'),
            },
        ]
        tooltip_breadcrumb = MBreadcrumb()
        tooltip_breadcrumb.set_item_list(tooltip_list)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("基本示例"))
        main_lay.addWidget(basic_breadcrumb)
        main_lay.addWidget(MDivider("自定义分隔符: =>"))
        main_lay.addWidget(separator_breadcrumb)
        main_lay.addWidget(MDivider("只有文本"))
        main_lay.addWidget(text_only_breadcrumb)
        main_lay.addWidget(MDivider("带提示"))
        main_lay.addWidget(tooltip_breadcrumb)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(config, parent=self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = BreadcrumbExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MBreadcrumb(separator="/", parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `separator` | 分隔符 | `str` | `"/"` |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_item_list(data_list)` | 设置导航项列表 | `data_list`: 导航项列表，每项是一个字典 | 无 |
| `add_item(data_dict, index=None)` | 添加一个导航项 | `data_dict`: 导航项字典<br>`index`: 插入位置，默认为末尾 | 无 |

### 导航项字典

每个导航项是一个字典，可以包含以下键：

| 键 | 描述 | 类型 | 是否必须 |
| --- | --- | --- | --- |
| `text` | 显示的文本 | `str` | 否 |
| `svg` | 图标的 SVG 文件名 | `str` | 否 |
| `icon` | 图标对象 | `QIcon` | 否 |
| `tooltip` | 鼠标悬停时显示的提示文本 | `str` | 否 |
| `clicked` | 点击时触发的回调函数 | `callable` | 否 |

## 常见问题

### 如何在面包屑中只显示图标？

如果只想显示图标而不显示文本，可以只设置 `svg` 或 `icon` 键，不设置 `text` 键：

```python
item_list = [
    {
        "svg": "home_line.svg",
        "clicked": functools.partial(print, "点击了首页")
    },
    # 其他导航项...
]
```

### 如何在面包屑中只显示文本？

如果只想显示文本而不显示图标，可以只设置 `text` 键，不设置 `svg` 和 `icon` 键：

```python
item_list = [
    {
        "text": "首页",
        "clicked": functools.partial(print, "点击了首页")
    },
    # 其他导航项...
]
```

### 如何动态更新面包屑？

可以通过再次调用 `set_item_list` 方法来更新面包屑的导航项：

```python
# 初始导航项
initial_list = [
    {"text": "首页", "svg": "home_line.svg"},
    {"text": "项目", "svg": "folder_line.svg"}
]
breadcrumb.set_item_list(initial_list)

# 更新导航项
updated_list = [
    {"text": "首页", "svg": "home_line.svg"},
    {"text": "项目", "svg": "folder_line.svg"},
    {"text": "任务", "svg": "task_line.svg"}
]
breadcrumb.set_item_list(updated_list)
```
