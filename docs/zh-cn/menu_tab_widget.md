# MMenuTabWidget 菜单形式的导航栏

MMenuTabWidget 是一个菜单形式的导航栏组件，可以用于创建应用程序的主导航菜单。它支持水平和垂直两种布局方式，可以添加图标和文本，并且可以在两端插入自定义部件。

## 导入

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
```

## 代码示例

### 基本使用

MMenuTabWidget 可以通过 `add_menu` 方法添加菜单项。每个菜单项是一个字典，可以包含以下键：

- `text`: 显示的文本
- `svg`: 图标的 SVG 文件名
- `icon`: 图标对象
- `clicked`: 点击时触发的回调函数

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
import functools
from dayu_widgets.message import MMessage

# 创建一个菜单导航栏
menu_tab = MMenuTabWidget()

# 添加菜单项
menu_tab.add_menu({
    "text": "首页",
    "svg": "home_line.svg",
    "clicked": functools.partial(MMessage.info, "点击了首页")
})
menu_tab.add_menu({
    "text": "用户",
    "svg": "user_line.svg",
    "clicked": functools.partial(MMessage.info, "点击了用户")
})
menu_tab.add_menu({
    "text": "设置",
    "svg": "setting_line.svg",
    "clicked": functools.partial(MMessage.info, "点击了设置")
})

# 设置默认选中的菜单项
menu_tab.tool_button_group.set_dayu_checked(0)
```

### 不同尺寸

MMenuTabWidget 支持设置不同的尺寸，可以通过 `set_dayu_size` 方法设置：

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets import dayu_theme

# 创建默认尺寸的菜单导航栏
menu_tab_default = MMenuTabWidget()

# 创建大尺寸的菜单导航栏
menu_tab_large = MMenuTabWidget()
menu_tab_large.set_dayu_size(dayu_theme.large)

# 创建超大尺寸的菜单导航栏
menu_tab_huge = MMenuTabWidget()
menu_tab_huge.set_dayu_size(dayu_theme.huge)
```

### 垂直布局

MMenuTabWidget 支持垂直布局，可以在创建时指定 `orientation` 参数：

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from qtpy import QtCore

# 创建垂直布局的菜单导航栏
menu_tab_vertical = MMenuTabWidget(orientation=QtCore.Qt.Vertical)
```

### 插入和追加部件

MMenuTabWidget 支持在导航栏的两端插入自定义部件：

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.label import MLabel
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.badge import MBadge

# 创建菜单导航栏
menu_tab = MMenuTabWidget()

# 在左侧插入标签
menu_tab.tool_bar_insert_widget(MLabel("Logo").h4().strong())

# 在右侧追加带徽标的按钮
badge_button = MBadge.dot(show=True, widget=MToolButton().icon_only().svg("user_fill.svg").large())
menu_tab.tool_bar_append_widget(badge_button)
```

### 完整示例

![MMenuTabWidget 演示](../_media/screenshots/MMenuTabWidget.gif)

以下是一个完整的示例，展示了 MMenuTabWidget 的各种用法：

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.badge import MBadge
from dayu_widgets.label import MLabel
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.message import MMessage
from dayu_widgets.tool_button import MToolButton


class MenuTabWidgetExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MenuTabWidgetExample, self).__init__(parent)
        self.setWindowTitle("Examples for MMenuTabWidget")
        self._init_ui()

    def _init_ui(self):
        item_list = [
            {
                "text": "概览",
                "svg": "home_line.svg",
                "clicked": functools.partial(MMessage.info, "首页", parent=self),
            },
            {
                "text": "我的",
                "svg": "user_line.svg",
                "clicked": functools.partial(MMessage.info, "编辑账户", parent=self),
            },
            {
                "text": "通知",
                "svg": "alert_line.svg",
                "clicked": functools.partial(MMessage.info, "查看通知", parent=self),
            },
        ]

        # 水平布局，默认尺寸
        tool_bar = MMenuTabWidget()
        tool_bar.tool_bar_insert_widget(MLabel("DaYu").h4().secondary().strong())
        tool_bar.tool_bar_append_widget(
            MBadge.dot(show=True, widget=MToolButton().icon_only().svg("user_fill.svg").large())
        )
        for index, data_dict in enumerate(item_list):
            tool_bar.add_menu(data_dict, index)
        tool_bar.tool_button_group.set_dayu_checked(0)

        # 水平布局，超大尺寸
        tool_bar_huge = MMenuTabWidget()
        tool_bar_huge.set_dayu_size(dayu_theme.huge)
        tool_bar_huge.tool_bar_insert_widget(MLabel("DaYu").h4().secondary().strong())
        for index, data_dict in enumerate(item_list):
            tool_bar_huge.add_menu(data_dict, index)
        tool_bar_huge.tool_button_group.set_dayu_checked(0)

        # 垂直布局，超大尺寸
        tool_bar_huge_v = MMenuTabWidget(orientation=QtCore.Qt.Vertical)
        tool_bar_huge_v.set_dayu_size(dayu_theme.huge)
        dayu_icon = MLabel("DaYu").h4().secondary().strong()
        dayu_icon.setContentsMargins(10, 10, 10, 10)
        tool_bar_huge_v.tool_bar_insert_widget(dayu_icon)
        for index, data_dict in enumerate(item_list):
            tool_bar_huge_v.add_menu(data_dict, index)
        tool_bar_huge_v.tool_button_group.set_dayu_checked(0)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)

        main_lay.addWidget(MLabel("菜单导航栏 (大尺寸)"))
        main_lay.addWidget(tool_bar)

        main_lay.addWidget(MLabel("菜单导航栏 (超大尺寸)"))
        main_lay.addWidget(tool_bar_huge)

        main_lay.addWidget(MLabel("垂直菜单导航栏 (超大尺寸)"))
        main_lay.addWidget(tool_bar_huge_v)

        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = MenuTabWidgetExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MMenuTabWidget(orientation=QtCore.Qt.Horizontal, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `orientation` | 布局方向 | `QtCore.Qt.Orientation` | `QtCore.Qt.Horizontal` |
| `parent` | 父部件 | `QWidget` | `None` |

### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `dayu_size` | 导航栏尺寸 | `int` | `dayu_theme.large` |
| `tool_button_group` | 按钮组对象 | `MBlockButtonGroup` | - |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `add_menu(data_dict, index=None)` | 添加一个菜单项 | `data_dict`: 菜单项字典<br>`index`: 插入位置，默认为末尾 | 无 |
| `tool_bar_append_widget(widget)` | 在导航栏右侧追加部件 | `widget`: 要追加的部件 | 无 |
| `tool_bar_insert_widget(widget)` | 在导航栏左侧插入部件 | `widget`: 要插入的部件 | 无 |
| `set_dayu_size(value)` | 设置导航栏尺寸 | `value`: 尺寸值 | 无 |
| `get_dayu_size()` | 获取导航栏尺寸 | 无 | `int` |

### 菜单项字典

每个菜单项是一个字典，可以包含以下键：

| 键 | 描述 | 类型 | 是否必须 |
| --- | --- | --- | --- |
| `text` | 显示的文本 | `str` | 否 |
| `svg` | 图标的 SVG 文件名 | `str` | 否 |
| `icon` | 图标对象 | `QIcon` | 否 |
| `clicked` | 点击时触发的回调函数 | `callable` | 否 |

## 常见问题

### 如何设置默认选中的菜单项？

可以通过 `tool_button_group.set_dayu_checked` 方法设置默认选中的菜单项：

```python
menu_tab = MMenuTabWidget()
# 添加菜单项...
menu_tab.tool_button_group.set_dayu_checked(0)  # 选中第一个菜单项
```

### 如何获取当前选中的菜单项？

可以通过 `tool_button_group.get_dayu_checked` 方法获取当前选中的菜单项的索引：

```python
menu_tab = MMenuTabWidget()
# 添加菜单项...
current_index = menu_tab.tool_button_group.get_dayu_checked()
```

### 如何在菜单项中只显示图标？

如果只想显示图标而不显示文本，可以只设置 `svg` 或 `icon` 键，不设置 `text` 键：

```python
menu_tab.add_menu({
    "svg": "home_line.svg",
    "clicked": functools.partial(MMessage.info, "点击了首页")
})
```

### 如何在菜单项中只显示文本？

如果只想显示文本而不显示图标，可以只设置 `text` 键，不设置 `svg` 和 `icon` 键：

```python
menu_tab.add_menu({
    "text": "首页",
    "clicked": functools.partial(MMessage.info, "点击了首页")
})
```

### 如何监听菜单项的选中状态变化？

可以通过 `tool_button_group.sig_checked_changed` 信号监听菜单项的选中状态变化：

```python
menu_tab = MMenuTabWidget()
# 添加菜单项...
menu_tab.tool_button_group.sig_checked_changed.connect(lambda index: print(f"选中了第 {index} 个菜单项"))
```
