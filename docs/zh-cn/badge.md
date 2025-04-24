# MBadge 徽标

MBadge 是一个徽标组件，用于显示提醒数字、文本或状态点。它通常出现在通知图标、头像或按钮的右上角，用于显示未读消息数量或提醒用户注意某些内容。

## 导入

```python
from dayu_widgets.badge import MBadge
```

## 代码示例

### 基本使用

MBadge 可以独立使用，也可以包装其他组件。

```python
from dayu_widgets.badge import MBadge

# 创建一个独立的徽标，显示数字
badge_count = MBadge.count(20)

# 创建一个独立的徽标，显示红点
badge_dot = MBadge.dot(True)

# 创建一个独立的徽标，显示文本
badge_text = MBadge.text("new")
```

### 包装其他组件

MBadge 可以包装其他组件，在其右上角显示徽标。

```python
from dayu_widgets.badge import MBadge
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.avatar import MAvatar
from dayu_widgets.qt import MPixmap

# 创建一个带红点的按钮
button = MToolButton().svg("trash_line.svg")
badge_button = MBadge.dot(True, widget=button)

# 创建一个带红点的头像
avatar = MAvatar.large(MPixmap("avatar.png"))
badge_avatar = MBadge.dot(True, widget=avatar)

# 创建一个带数字的按钮
button_alert = MToolButton().svg("alert_fill.svg").large()
badge_count = MBadge.count(5, widget=button_alert)
```

### 数字徽标

MBadge 可以显示数字，当数字超过设定的最大值时，会显示为 "最大值+"。

```python
from dayu_widgets.badge import MBadge
from dayu_widgets.tool_button import MToolButton

# 创建一个带数字的按钮
button = MToolButton().svg("alert_fill.svg").large()
badge = MBadge.count(99, widget=button)

# 设置最大值为 10，当数字超过 10 时，显示为 "10+"
badge.set_dayu_overflow(10)
badge.set_dayu_count(15)  # 将显示为 "10+"
```

### 文本徽标

MBadge 可以显示文本，例如 "new"、"hot" 等。

```python
from dayu_widgets.badge import MBadge
from dayu_widgets.label import MLabel
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建一个带文本徽标的标签
label = MLabel("你的理想城市  ")
badge_hot = MBadge.text("hot", widget=label)

# 创建一个下拉菜单
menu = MMenu(parent=self)
menu.set_data(["北京", "上海", "广州", "深圳"])
select = MComboBox()
select.set_menu(menu)

# 将标签和下拉菜单放在一起
layout = QtWidgets.QHBoxLayout()
layout.addWidget(badge_hot)
layout.addWidget(select)
```

### 动态更改徽标

MBadge 的状态可以动态更改。

```python
from dayu_widgets.badge import MBadge
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.spin_box import MSpinBox

# 创建一个带红点的按钮
button = MToolButton().svg("trash_line.svg")
badge = MBadge.dot(True, widget=button)

# 点击按钮时隐藏红点
button.clicked.connect(lambda: badge.set_dayu_dot(False))

# 创建一个带数字的按钮
button_alert = MToolButton().svg("alert_fill.svg").large()
badge_count = MBadge.count(1, widget=button_alert)

# 创建一个数字输入框，用于更改徽标数字
spin_box = MSpinBox()
spin_box.setRange(0, 9999)
spin_box.valueChanged.connect(badge_count.set_dayu_count)
spin_box.setValue(1)
```

### 完整示例

![MBadge 演示](../_media/screenshots/MBadge.png)

以下是一个完整的示例，展示了 MBadge 的各种用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.avatar import MAvatar
from dayu_widgets.badge import MBadge
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.menu import MMenu
from dayu_widgets.qt import MPixmap
from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.tool_button import MToolButton


class BadgeExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(BadgeExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBadge")
        self._init_ui()

    def _init_ui(self):
        standalone_lay = QtWidgets.QHBoxLayout()
        standalone_lay.addWidget(MBadge.count(0))
        standalone_lay.addWidget(MBadge.count(20))
        standalone_lay.addWidget(MBadge.count(100))
        standalone_lay.addWidget(MBadge.dot(True))
        standalone_lay.addWidget(MBadge.text("new"))
        standalone_lay.addStretch()

        button = MToolButton().svg("trash_line.svg")
        avatar = MAvatar.large(MPixmap("avatar.png"))
        button_alert = MToolButton().svg("alert_fill.svg").large()
        badge_1 = MBadge.dot(True, widget=button)
        badge_2 = MBadge.dot(True, widget=avatar)
        badge_3 = MBadge.dot(True, widget=button_alert)
        button.clicked.connect(lambda: badge_1.set_dayu_dot(False))

        spin_box = MSpinBox()
        spin_box.setRange(0, 9999)
        spin_box.valueChanged.connect(badge_3.set_dayu_count)
        spin_box.setValue(1)

        self.register_field("button1_selected", "北京")
        menu1 = MMenu(parent=self)
        menu1.set_data(["北京", "上海", "广州", "深圳"])
        select1 = MComboBox()
        select1.set_menu(menu1)
        self.bind("button1_selected", select1, "value", signal="sig_value_changed")

        badge_hot = MBadge.text("hot", widget=MLabel("你的理想城市  "))

        sub_lay1 = QtWidgets.QHBoxLayout()
        sub_lay1.addWidget(badge_1)
        sub_lay1.addWidget(badge_2)
        sub_lay1.addWidget(badge_3)
        sub_lay1.addStretch()

        sub_lay2 = QtWidgets.QHBoxLayout()
        sub_lay2.addWidget(badge_hot)
        sub_lay2.addWidget(select1)
        sub_lay2.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("独立使用"))
        main_lay.addLayout(standalone_lay)
        main_lay.addWidget(MDivider("不同类型"))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(spin_box)
        main_lay.addWidget(MDivider("不同类型"))
        main_lay.addLayout(sub_lay2)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = BadgeExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MBadge(widget=None, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `widget` | 要包装的部件 | `QWidget` | `None` |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `get_dayu_overflow()` | 获取溢出数字 | 无 | `int` |
| `set_dayu_overflow(num)` | 设置溢出数字 | `num`: 最大显示数字 | 无 |
| `get_dayu_dot()` | 获取是否显示红点 | 无 | `bool` |
| `set_dayu_dot(show)` | 设置是否显示红点 | `show`: 是否显示 | 无 |
| `get_dayu_count()` | 获取当前数字 | 无 | `int` |
| `set_dayu_count(num)` | 设置当前数字 | `num`: 数字值 | 无 |
| `get_dayu_text()` | 获取当前文本 | 无 | `str` |
| `set_dayu_text(text)` | 设置当前文本 | `text`: 文本内容 | 无 |

### 类方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `dot(show=False, widget=None)` | 创建一个红点徽标 | `show`: 是否显示红点<br>`widget`: 要包装的部件 | `MBadge` 实例 |
| `count(count=0, widget=None)` | 创建一个数字徽标 | `count`: 数字值<br>`widget`: 要包装的部件 | `MBadge` 实例 |
| `text(text="", widget=None)` | 创建一个文本徽标 | `text`: 文本内容<br>`widget`: 要包装的部件 | `MBadge` 实例 |

### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `dayu_overflow` | 溢出数字 | `int` | `99` |
| `dayu_dot` | 是否显示红点 | `bool` | `False` |
| `dayu_count` | 当前数字 | `int` | `None` |
| `dayu_text` | 当前文本 | `str` | `None` |

## 常见问题

### 如何创建一个独立的徽标？

可以使用 MBadge 的类方法创建独立的徽标：

```python
from dayu_widgets.badge import MBadge

# 创建一个显示数字的徽标
badge_count = MBadge.count(20)

# 创建一个显示红点的徽标
badge_dot = MBadge.dot(True)

# 创建一个显示文本的徽标
badge_text = MBadge.text("new")
```

### 如何在组件上显示徽标？

可以通过在 MBadge 的类方法中传入 `widget` 参数来包装组件：

```python
from dayu_widgets.badge import MBadge
from dayu_widgets.tool_button import MToolButton

# 创建一个按钮
button = MToolButton().svg("alert_fill.svg")

# 在按钮上显示红点
badge = MBadge.dot(True, widget=button)

# 在按钮上显示数字
badge = MBadge.count(5, widget=button)

# 在按钮上显示文本
badge = MBadge.text("new", widget=button)
```

### 如何设置数字徽标的最大值？

可以通过 `set_dayu_overflow` 方法设置数字徽标的最大值：

```python
from dayu_widgets.badge import MBadge

# 创建一个数字徽标
badge = MBadge.count(100)

# 设置最大值为 99，当数字超过 99 时，显示为 "99+"
badge.set_dayu_overflow(99)

# 设置最大值为 10，当数字超过 10 时，显示为 "10+"
badge.set_dayu_overflow(10)
```

### 如何动态更改徽标的状态？

可以通过 MBadge 的方法动态更改徽标的状态：

```python
from dayu_widgets.badge import MBadge
from dayu_widgets.tool_button import MToolButton

# 创建一个带红点的按钮
button = MToolButton().svg("trash_line.svg")
badge = MBadge.dot(True, widget=button)

# 隐藏红点
badge.set_dayu_dot(False)

# 显示红点
badge.set_dayu_dot(True)

# 显示数字
badge.set_dayu_count(5)

# 显示文本
badge.set_dayu_text("new")
```
