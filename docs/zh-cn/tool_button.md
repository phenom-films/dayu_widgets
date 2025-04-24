# MToolButton 工具按钮

工具按钮是一种轻量级的按钮控件，通常用于工具栏或需要图标按钮的场景。它支持多种显示模式，可以只显示图标、只显示文本，或者同时显示图标和文本。

## 导入

```python
from dayu_widgets import MToolButton
```

## 代码示例

### 基本使用

MToolButton 可以设置 SVG 图标，并支持多种显示模式。

```python
from dayu_widgets.tool_button import MToolButton

# 创建只显示图标的工具按钮
icon_only_button = MToolButton().svg("left_line.svg").icon_only()

# 创建只显示文本的工具按钮
text_only_button = MToolButton().text_only()
text_only_button.setText("文本按钮")

# 创建图标在文本旁边的工具按钮
text_beside_icon_button = MToolButton().svg("user_line.svg").text_beside_icon()
text_beside_icon_button.setText("用户")

# 创建图标在文本上方的工具按钮
text_under_icon_button = MToolButton().svg("calendar_line.svg").text_under_icon()
text_under_icon_button.setText("日历")
```

### 不同尺寸

MToolButton 有五种尺寸：tiny、small、medium（默认）、large 和 huge。

```python
from dayu_widgets.tool_button import MToolButton

# 创建不同尺寸的工具按钮
huge_button = MToolButton().svg("left_line.svg").icon_only().huge()
large_button = MToolButton().svg("right_line.svg").icon_only().large()
medium_button = MToolButton().svg("up_line.svg").icon_only()  # 默认是 medium 尺寸
small_button = MToolButton().svg("up_line.svg").icon_only().small()
tiny_button = MToolButton().svg("down_line.svg").icon_only().tiny()
```

### 禁用状态

使用 `setEnabled(False)` 可以设置按钮为禁用状态。

```python
from dayu_widgets.tool_button import MToolButton

# 创建禁用的工具按钮
disabled_button = MToolButton().svg("detail_line.svg").icon_only()
disabled_button.setEnabled(False)
```

### 可选中状态

MToolButton 支持可选中状态，当按钮被选中时，图标会变为主题色。

```python
from dayu_widgets.tool_button import MToolButton

# 创建可选中的工具按钮
checkable_button = MToolButton().svg("trash_line.svg").icon_only()
checkable_button.setCheckable(True)
```

### 完整示例

以下是一个完整的示例，展示了 MToolButton 的所有功能：

![工具按钮演示](../_media/screenshots/tool_button_dark.png)

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.tool_button import MToolButton


class ToolButtonExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ToolButtonExample, self).__init__(parent)
        self.setWindowTitle("Examples for MToolButton")
        self._init_ui()

    def _init_ui(self):
        size_lay = QtWidgets.QVBoxLayout()
        sub_lay1 = QtWidgets.QHBoxLayout()
        sub_lay1.addWidget(MToolButton().svg("left_line.svg").icon_only().huge())
        sub_lay1.addWidget(MToolButton().svg("right_line.svg").icon_only().large())
        sub_lay1.addWidget(MToolButton().svg("up_line.svg").icon_only())
        sub_lay1.addWidget(MToolButton().svg("up_line.svg").icon_only().small())
        sub_lay1.addWidget(MToolButton().svg("down_line.svg").icon_only().tiny())
        sub_lay1.addStretch()
        size_lay.addLayout(sub_lay1)

        button2 = MToolButton().svg("detail_line.svg").icon_only()
        button2.setEnabled(False)
        button7 = MToolButton().svg("trash_line.svg").icon_only()
        button7.setCheckable(True)
        state_lay = QtWidgets.QHBoxLayout()
        state_lay.addWidget(button2)
        state_lay.addWidget(button7)
        state_lay.addStretch()

        button_trash = MToolButton().svg("trash_line.svg").text_beside_icon()
        button_trash.setText("删除")
        button_login = MToolButton().svg("user_line.svg").text_beside_icon()
        button_login.setText("登录")

        button_lay = QtWidgets.QHBoxLayout()
        button_lay.addWidget(button_trash)
        button_lay.addWidget(button_login)
        button_lay.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("不同尺寸"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("禁用和可选中状态"))
        main_lay.addLayout(state_lay)
        main_lay.addWidget(MDivider("文本和图标"))
        main_lay.addLayout(button_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = ToolButtonExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `dayu_size` | 按钮尺寸 | `int` | `dayu_theme.default_size` |
| `dayu_svg` | SVG 图标路径 | `str` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `svg(path)` | 设置 SVG 图标路径 | `path`: SVG 图标路径 | 当前按钮实例 |
| `icon_only()` | 设置按钮只显示图标 | 无 | 当前按钮实例 |
| `text_only()` | 设置按钮只显示文本 | 无 | 当前按钮实例 |
| `text_beside_icon()` | 设置文本显示在图标旁边 | 无 | 当前按钮实例 |
| `text_under_icon()` | 设置文本显示在图标下方 | 无 | 当前按钮实例 |
| `huge()` | 设置按钮为超大尺寸 | 无 | 当前按钮实例 |
| `large()` | 设置按钮为大尺寸 | 无 | 当前按钮实例 |
| `medium()` | 设置按钮为中等尺寸 | 无 | 当前按钮实例 |
| `small()` | 设置按钮为小尺寸 | 无 | 当前按钮实例 |
| `tiny()` | 设置按钮为超小尺寸 | 无 | 当前按钮实例 |

### 继承的信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `clicked` | 当按钮被点击时触发 | 无 |
| `toggled` | 当按钮状态改变时触发（仅当按钮可选中时） | `bool`: 是否选中 |

## 常见问题

### 如何设置按钮样式？

MToolButton 的样式由 dayu_theme 统一管理，你可以通过设置不同的尺寸来改变按钮样式，而不需要手动设置样式表。

### 如何使用 SVG 图标？

MToolButton 支持使用 SVG 图标，你可以通过 `svg()` 方法设置图标路径。SVG 图标文件应该放在项目的资源目录中。

```python
button = MToolButton().svg("icon_name.svg").icon_only()
```

### 如何同时显示图标和文本？

MToolButton 支持多种显示模式，你可以使用 `text_beside_icon()` 或 `text_under_icon()` 方法来同时显示图标和文本。

```python
# 文本在图标旁边
button1 = MToolButton().svg("user_line.svg").text_beside_icon()
button1.setText("用户")

# 文本在图标下方
button2 = MToolButton().svg("calendar_line.svg").text_under_icon()
button2.setText("日历")
```
