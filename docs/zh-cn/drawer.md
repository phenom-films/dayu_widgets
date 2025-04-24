# MDrawer 抽屉

MDrawer 是一个抽屉组件，用于从屏幕边缘滑出的浮层，可以替代模态对话框，承载更多内容。它可以从屏幕的上、右、下、左四个方向滑出，并且可以包含各种自定义内容。

## 导入

```python
from dayu_widgets.drawer import MDrawer
```

## 代码示例

### 基本使用

MDrawer 可以创建一个简单的抽屉，从屏幕边缘滑出。

```python
from dayu_widgets.drawer import MDrawer
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# 创建一个抽屉
drawer = MDrawer("基本抽屉", parent=self)

# 创建自定义内容
custom_widget = QtWidgets.QWidget()
custom_lay = QtWidgets.QVBoxLayout()
custom_lay.addWidget(MLabel("这是抽屉的内容..."))
custom_lay.addWidget(MLabel("这是抽屉的内容..."))
custom_lay.addWidget(MLabel("这是抽屉的内容..."))
custom_widget.setLayout(custom_lay)

# 设置抽屉内容
drawer.set_widget(custom_widget)

# 显示抽屉
drawer.show()
```

### 不同位置

MDrawer 支持从屏幕的上、右、下、左四个方向滑出。

```python
from dayu_widgets.drawer import MDrawer

# 创建一个从右侧滑出的抽屉（默认）
drawer_right = MDrawer("右侧抽屉", position=MDrawer.RightPos, parent=self)
# 或者使用链式调用
drawer_right = MDrawer("右侧抽屉", parent=self).right()

# 创建一个从左侧滑出的抽屉
drawer_left = MDrawer("左侧抽屉", position=MDrawer.LeftPos, parent=self)
# 或者使用链式调用
drawer_left = MDrawer("左侧抽屉", parent=self).left()

# 创建一个从顶部滑出的抽屉
drawer_top = MDrawer("顶部抽屉", position=MDrawer.TopPos, parent=self)
# 或者使用链式调用
drawer_top = MDrawer("顶部抽屉", parent=self).top()

# 创建一个从底部滑出的抽屉
drawer_bottom = MDrawer("底部抽屉", position=MDrawer.BottomPos, parent=self)
# 或者使用链式调用
drawer_bottom = MDrawer("底部抽屉", parent=self).bottom()
```

### 自定义尺寸

MDrawer 支持自定义宽度或高度，取决于抽屉的位置。

```python
from dayu_widgets.drawer import MDrawer
from dayu_widgets.qt import get_scale_factor

# 获取缩放因子
scale_x, _ = get_scale_factor()

# 创建一个自定义宽度的抽屉
drawer = MDrawer("自定义宽度", parent=self)
drawer.setFixedWidth(300 * scale_x)  # 设置宽度为 300 像素（考虑缩放因子）

# 创建一个自定义高度的抽屉
drawer_top = MDrawer("自定义高度", position=MDrawer.TopPos, parent=self)
drawer_top.setFixedHeight(200 * scale_x)  # 设置高度为 200 像素（考虑缩放因子）
```

### 添加底部按钮

MDrawer 支持在底部添加按钮，如确认、取消等。

```python
from dayu_widgets.drawer import MDrawer
from dayu_widgets.push_button import MPushButton

# 创建一个抽屉
drawer = MDrawer("带底部按钮的抽屉", parent=self)

# 创建底部按钮
cancel_button = MPushButton("取消")
submit_button = MPushButton("提交").primary()

# 连接按钮点击事件
cancel_button.clicked.connect(drawer.close)
submit_button.clicked.connect(lambda: (print("提交成功"), drawer.close()))

# 添加按钮到抽屉底部
drawer.add_widget_to_bottom(cancel_button)
drawer.add_widget_to_bottom(submit_button)
```

### 表单提交示例

MDrawer 常用于表单提交场景，以下是一个完整的表单提交示例：

```python
from dayu_widgets.drawer import MDrawer
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.spin_box import MDateEdit
from dayu_widgets.push_button import MPushButton
from qtpy import QtWidgets

# 创建一个抽屉
drawer = MDrawer("新建账户", parent=self)

# 创建表单内容
custom_widget = QtWidgets.QWidget()
custom_lay = QtWidgets.QFormLayout()
custom_lay.addRow("姓名", MLineEdit())
custom_lay.addRow("年龄", MSpinBox())
custom_lay.addRow("生日", MDateEdit())
custom_widget.setLayout(custom_lay)

# 创建底部按钮
cancel_button = MPushButton("取消")
submit_button = MPushButton("提交").primary()

# 连接按钮点击事件
cancel_button.clicked.connect(drawer.close)
submit_button.clicked.connect(lambda: (print("提交成功"), drawer.close()))

# 设置抽屉内容和底部按钮
drawer.set_widget(custom_widget)
drawer.add_widget_to_bottom(cancel_button)
drawer.add_widget_to_bottom(submit_button)

# 设置抽屉宽度
from dayu_widgets.qt import get_scale_factor
scale_x, _ = get_scale_factor()
drawer.setFixedWidth(300 * scale_x)

# 显示抽屉
drawer.show()
```

### 完整示例

![MDrawer 演示](../_media/screenshots/drawer.gif)

以下是一个完整的示例，展示了 MDrawer 的各种用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.button_group import MRadioButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.drawer import MDrawer
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import MIcon
from dayu_widgets.qt import get_scale_factor
from dayu_widgets.spin_box import MDateEdit
from dayu_widgets.spin_box import MSpinBox


class DrawerExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(DrawerExample, self).__init__(parent)
        self.setWindowTitle("Examples for MDrawer")
        self._init_ui()

    def _init_ui(self):
        scale_x, _ = get_scale_factor()
        self.button_grp = MRadioButtonGroup()
        self.button_grp.set_button_list(["top", {"text": "right", "checked": True}, "bottom", "left"])

        open_button_2 = MPushButton("打开").primary()
        open_button_2.clicked.connect(self.slot_open_button_2)
        placement_lay = QtWidgets.QHBoxLayout()
        placement_lay.addWidget(self.button_grp)
        placement_lay.addSpacing(20 * scale_x)
        placement_lay.addWidget(open_button_2)
        placement_lay.addStretch()

        new_account_button = MPushButton(text="新建账户", icon=MIcon("add_line.svg", "#fff")).primary()
        new_account_button.clicked.connect(self.slot_new_account)
        new_account_lay = QtWidgets.QHBoxLayout()
        new_account_lay.addWidget(MLabel("在抽屉中提交表单"))
        new_account_lay.addWidget(new_account_button)
        new_account_lay.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("自定义位置"))
        main_lay.addLayout(placement_lay)
        main_lay.addWidget(MDivider("在抽屉中提交表单"))
        main_lay.addLayout(new_account_lay)

        main_lay.addWidget(MDivider("预览抽屉"))
        self.setLayout(main_lay)

    def slot_open_button_2(self):
        custom_widget = QtWidgets.QWidget()
        custom_lay = QtWidgets.QVBoxLayout()
        custom_lay.addWidget(MLabel("一些内容..."))
        custom_lay.addWidget(MLabel("一些内容..."))
        custom_lay.addWidget(MLabel("一些内容..."))
        custom_widget.setLayout(custom_lay)

        drawer = MDrawer("基本抽屉", parent=self)
        drawer.set_dayu_position(self.button_grp.get_button_group().checkedButton().text())

        scale_x, _ = get_scale_factor()
        drawer.setFixedWidth(300 * scale_x)
        drawer.set_widget(custom_widget)
        drawer.show()

    def slot_new_account(self):
        custom_widget = QtWidgets.QWidget()
        custom_lay = QtWidgets.QFormLayout()
        custom_lay.addRow("姓名", MLineEdit())
        custom_lay.addRow("年龄", MSpinBox())
        custom_lay.addRow("生日", MDateEdit())
        custom_widget.setLayout(custom_lay)

        drawer = MDrawer("新建账户", parent=self)
        submit_button = MPushButton("提交").primary()
        submit_button.clicked.connect(drawer.close)
        drawer.add_widget_to_bottom(MPushButton("取消"))
        drawer.add_widget_to_bottom(submit_button)
        scale_x, _ = get_scale_factor()
        drawer.setFixedWidth(300 * scale_x)
        drawer.set_widget(custom_widget)
        drawer.show()


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = DrawerExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MDrawer(title, position="right", closable=True, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `title` | 抽屉标题 | `str` | 必填 |
| `position` | 抽屉位置 | `str` | `"right"` |
| `closable` | 是否可关闭 | `bool` | `True` |
| `parent` | 父部件 | `QWidget` | `None` |

### 类常量

| 常量 | 描述 | 值 |
| --- | --- | --- |
| `LeftPos` | 左侧位置 | `"left"` |
| `RightPos` | 右侧位置 | `"right"` |
| `TopPos` | 顶部位置 | `"top"` |
| `BottomPos` | 底部位置 | `"bottom"` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_widget(widget)` | 设置抽屉内容部件 | `widget`: 内容部件 | 无 |
| `add_widget_to_bottom(widget)` | 添加部件到抽屉底部 | `widget`: 底部部件 | 无 |
| `set_dayu_position(value)` | 设置抽屉位置 | `value`: 位置值 | 无 |
| `get_dayu_position()` | 获取抽屉位置 | 无 | `str` |
| `left()` | 设置抽屉位置为左侧 | 无 | `self` |
| `right()` | 设置抽屉位置为右侧 | 无 | `self` |
| `top()` | 设置抽屉位置为顶部 | 无 | `self` |
| `bottom()` | 设置抽屉位置为底部 | 无 | `self` |
| `show()` | 显示抽屉 | 无 | 无 |
| `close()` | 关闭抽屉 | 无 | 无 |

### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `dayu_position` | 抽屉位置 | `str` | `"right"` |

### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_closed` | 抽屉关闭时触发 | 无 |

## 常见问题

### 如何设置抽屉的位置？

可以在创建抽屉时通过 `position` 参数设置位置，或者使用链式方法调用：

```python
from dayu_widgets.drawer import MDrawer

# 使用 position 参数
drawer_right = MDrawer("右侧抽屉", position=MDrawer.RightPos, parent=self)
drawer_left = MDrawer("左侧抽屉", position=MDrawer.LeftPos, parent=self)
drawer_top = MDrawer("顶部抽屉", position=MDrawer.TopPos, parent=self)
drawer_bottom = MDrawer("底部抽屉", position=MDrawer.BottomPos, parent=self)

# 使用链式方法调用
drawer_right = MDrawer("右侧抽屉", parent=self).right()
drawer_left = MDrawer("左侧抽屉", parent=self).left()
drawer_top = MDrawer("顶部抽屉", parent=self).top()
drawer_bottom = MDrawer("底部抽屉", parent=self).bottom()
```

### 如何设置抽屉的尺寸？

可以使用 `setFixedWidth` 或 `setFixedHeight` 方法设置抽屉的尺寸，取决于抽屉的位置：

```python
from dayu_widgets.drawer import MDrawer
from dayu_widgets.qt import get_scale_factor

# 获取缩放因子
scale_x, _ = get_scale_factor()

# 对于左侧和右侧抽屉，设置宽度
drawer_right = MDrawer("右侧抽屉", parent=self).right()
drawer_right.setFixedWidth(300 * scale_x)

# 对于顶部和底部抽屉，设置高度
drawer_top = MDrawer("顶部抽屉", parent=self).top()
drawer_top.setFixedHeight(200 * scale_x)
```

### 如何在抽屉中添加底部按钮？

可以使用 `add_widget_to_bottom` 方法添加底部按钮：

```python
from dayu_widgets.drawer import MDrawer
from dayu_widgets.push_button import MPushButton

# 创建一个抽屉
drawer = MDrawer("带底部按钮的抽屉", parent=self)

# 创建底部按钮
cancel_button = MPushButton("取消")
submit_button = MPushButton("提交").primary()

# 连接按钮点击事件
cancel_button.clicked.connect(drawer.close)
submit_button.clicked.connect(lambda: (print("提交成功"), drawer.close()))

# 添加按钮到抽屉底部
drawer.add_widget_to_bottom(cancel_button)
drawer.add_widget_to_bottom(submit_button)
```

### 如何监听抽屉的关闭事件？

可以连接抽屉的 `sig_closed` 信号来监听关闭事件：

```python
from dayu_widgets.drawer import MDrawer

# 创建一个抽屉
drawer = MDrawer("抽屉", parent=self)

# 连接关闭信号
drawer.sig_closed.connect(lambda: print("抽屉已关闭"))
```
