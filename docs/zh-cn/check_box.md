# MCheckBox 复选框

MCheckBox 是一个复选框组件，用于在一组选项中进行多项选择。它基于 Qt 的 QCheckBox 类，提供了更美观的样式和更好的交互体验。

## 导入

```python
from dayu_widgets.check_box import MCheckBox
```

## 代码示例

### 基本使用

MCheckBox 可以创建一个简单的复选框，用户可以选中或取消选中。

```python
from dayu_widgets.check_box import MCheckBox

# 创建一个复选框
checkbox = MCheckBox("选项 1")

# 创建一个默认选中的复选框
checkbox_checked = MCheckBox("选项 2")
checkbox_checked.setChecked(True)

# 创建一个禁用的复选框
checkbox_disabled = MCheckBox("禁用选项")
checkbox_disabled.setEnabled(False)
```

### 不同状态

MCheckBox 支持三种状态：未选中、选中和部分选中。

```python
from dayu_widgets.check_box import MCheckBox
from qtpy import QtCore

# 创建未选中状态的复选框
checkbox_unchecked = MCheckBox("未选中")
checkbox_unchecked.setCheckState(QtCore.Qt.Unchecked)

# 创建选中状态的复选框
checkbox_checked = MCheckBox("选中")
checkbox_checked.setCheckState(QtCore.Qt.Checked)

# 创建部分选中状态的复选框
checkbox_partially = MCheckBox("部分选中")
checkbox_partially.setCheckState(QtCore.Qt.PartiallyChecked)
```

### 带图标的复选框

MCheckBox 支持设置图标，可以在文本旁边显示一个图标。

```python
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.qt import MIcon

# 创建带图标的复选框
checkbox_icon = MCheckBox("Maya")
checkbox_icon.setIcon(MIcon("app-maya.png"))
```

### 数据绑定

MCheckBox 可以与 MFieldMixin 结合使用，实现数据绑定。

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton


class CheckBoxBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CheckBoxBindExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 创建复选框和标签
        checkbox = MCheckBox("数据绑定")
        label = MLabel()

        # 创建按钮用于改变状态
        button = MPushButton("改变状态")
        button.clicked.connect(lambda: self.set_field("checked", not self.field("checked")))

        # 注册字段和绑定
        self.register_field("checked", True)
        self.register_field("checked_text", lambda: "是！" if self.field("checked") else "否！！")
        self.bind("checked", checkbox, "checked", signal="stateChanged")
        self.bind("checked_text", label, "text")

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(checkbox)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        self.setLayout(main_lay)
```

### 复选框组

MCheckBoxGroup 是一个复选框组组件，可以方便地管理一组复选框。

```python
from dayu_widgets.button_group import MCheckBoxGroup
from qtpy import QtCore

# 创建水平布局的复选框组
checkbox_group_h = MCheckBoxGroup()
checkbox_group_h.set_button_list(["选项 1", "选项 2", "选项 3"])

# 创建垂直布局的复选框组
checkbox_group_v = MCheckBoxGroup(orientation=QtCore.Qt.Vertical)
checkbox_group_v.set_button_list(["选项 A", "选项 B", "选项 C"])

# 监听选中状态变化
checkbox_group_h.sig_checked_changed.connect(lambda checked_list: print("选中的选项:", checked_list))
```

### 带图标的复选框组

MCheckBoxGroup 支持为每个选项设置图标。

```python
from dayu_widgets.button_group import MCheckBoxGroup
from dayu_widgets.qt import MIcon

# 创建带图标的复选框组
checkbox_group = MCheckBoxGroup()
checkbox_group.set_button_list([
    {"text": "Maya", "icon": MIcon("app-maya.png")},
    {"text": "Nuke", "icon": MIcon("app-nuke.png")},
    {"text": "Houdini", "icon": MIcon("app-houdini.png")}
])
```

### 完整示例

![MCheckBox 演示](../_media/screenshots/MCheckBox.gif)

以下是一个完整的示例，展示了 MCheckBox 的各种用法：

```python
# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import MIcon


class CheckBoxExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CheckBoxExample, self).__init__(parent)
        self.setWindowTitle("Example for MCheckBox")
        self._init_ui()

    def _init_ui(self):
        grid_lay = QtWidgets.QGridLayout()

        for index, (text, state) in enumerate(
            [
                ("未选中", QtCore.Qt.Unchecked),
                ("选中", QtCore.Qt.Checked),
                ("部分选中", QtCore.Qt.PartiallyChecked),
            ]
        ):
            check_box_normal = MCheckBox(text)
            check_box_normal.setCheckState(state)

            check_box_disabled = MCheckBox(text)
            check_box_disabled.setCheckState(state)
            check_box_disabled.setEnabled(False)

            grid_lay.addWidget(check_box_normal, 0, index)
            grid_lay.addWidget(check_box_disabled, 1, index)

        icon_lay = QtWidgets.QHBoxLayout()
        for text, icon in [
            ("Maya", MIcon("app-maya.png")),
            ("Nuke", MIcon("app-nuke.png")),
            ("Houdini", MIcon("app-houdini.png")),
        ]:
            check_box_icon = MCheckBox(text)
            check_box_icon.setIcon(icon)
            icon_lay.addWidget(check_box_icon)

        check_box_bind = MCheckBox("数据绑定")
        label = MLabel()
        button = MPushButton(text="改变状态")
        button.clicked.connect(lambda: self.set_field("checked", not self.field("checked")))
        self.register_field("checked", True)
        self.register_field("checked_text", lambda: "是！" if self.field("checked") else "否！！")
        self.bind("checked", check_box_bind, "checked", signal="stateChanged")
        self.bind("checked_text", label, "text")

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("基本"))
        main_lay.addLayout(grid_lay)
        main_lay.addWidget(MDivider("图标"))
        main_lay.addLayout(icon_lay)
        main_lay.addWidget(MDivider("数据绑定"))
        main_lay.addWidget(check_box_bind)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = CheckBoxExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### MCheckBox

#### 构造函数

```python
MCheckBox(text="", parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `text` | 复选框显示的文本 | `str` | `""` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 继承的方法

MCheckBox 继承自 QCheckBox，因此可以使用 QCheckBox 的所有方法，例如：

- `setChecked(bool)`: 设置复选框是否选中
- `isChecked()`: 获取复选框是否选中
- `setCheckState(Qt.CheckState)`: 设置复选框的状态
- `checkState()`: 获取复选框的状态
- `setIcon(QIcon)`: 设置复选框的图标
- `setEnabled(bool)`: 设置复选框是否启用
- 更多方法请参考 Qt 文档

### MCheckBoxGroup

#### 构造函数

```python
MCheckBoxGroup(orientation=QtCore.Qt.Horizontal, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `orientation` | 布局方向 | `QtCore.Qt.Orientation` | `QtCore.Qt.Horizontal` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_button_list(data_list)` | 设置按钮列表 | `data_list`: 按钮数据列表 | 无 |
| `get_dayu_checked()` | 获取选中的按钮值列表 | 无 | `list` |
| `set_dayu_checked(value)` | 设置选中的按钮值列表 | `value`: 要选中的按钮值列表 | 无 |

#### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_checked_changed` | 选中状态变化时触发 | `list`: 选中的按钮值列表 |

#### 按钮数据

按钮数据可以是字符串或字典：

- 如果是字符串，则作为按钮的文本
- 如果是字典，可以包含以下键：
  - `text`: 按钮文本
  - `icon`: 按钮图标
  - `data`: 按钮数据，用于标识按钮
  - `checkable`: 按钮是否可选中
  - `checked`: 按钮是否默认选中

## 常见问题

### 如何创建三态复选框？

三态复选框可以显示三种状态：未选中、选中和部分选中。要创建三态复选框，需要先设置 `setTristate(True)`，然后可以使用 `setCheckState` 设置状态：

```python
from dayu_widgets.check_box import MCheckBox
from qtpy import QtCore

# 创建三态复选框
checkbox = MCheckBox("三态复选框")
checkbox.setTristate(True)

# 设置为部分选中状态
checkbox.setCheckState(QtCore.Qt.PartiallyChecked)
```

### 如何监听复选框状态变化？

可以通过连接 `stateChanged` 信号来监听复选框状态变化：

```python
from dayu_widgets.check_box import MCheckBox

# 创建复选框
checkbox = MCheckBox("选项")

# 监听状态变化
checkbox.stateChanged.connect(lambda state: print("状态变化:", state))
```

### 如何在 MCheckBoxGroup 中设置默认选中的选项？

可以通过 `set_dayu_checked` 方法设置默认选中的选项：

```python
from dayu_widgets.button_group import MCheckBoxGroup

# 创建复选框组
checkbox_group = MCheckBoxGroup()
checkbox_group.set_button_list(["选项 1", "选项 2", "选项 3", "选项 4"])

# 设置默认选中的选项
checkbox_group.set_dayu_checked(["选项 1", "选项 3"])
```

### 如何获取 MCheckBoxGroup 中选中的选项？

可以通过 `get_dayu_checked` 方法获取选中的选项：

```python
from dayu_widgets.button_group import MCheckBoxGroup

# 创建复选框组
checkbox_group = MCheckBoxGroup()
checkbox_group.set_button_list(["选项 1", "选项 2", "选项 3"])

# 获取选中的选项
checked_items = checkbox_group.get_dayu_checked()
print("选中的选项:", checked_items)
```
