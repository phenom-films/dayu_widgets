# MSwitch 开关

MSwitch 是一个开关组件，用于在两种状态之间进行切换。它基于 Qt 的 QRadioButton 类，但提供了更美观的样式和更好的交互体验。

## 导入

```python
from dayu_widgets.switch import MSwitch
```

## 代码示例

### 基本使用

MSwitch 可以创建一个简单的开关，用户可以点击切换状态。

```python
from dayu_widgets.switch import MSwitch

# 创建一个开关
switch = MSwitch()

# 创建一个默认选中的开关
switch_checked = MSwitch()
switch_checked.setChecked(True)

# 创建一个禁用的开关
switch_disabled = MSwitch()
switch_disabled.setEnabled(False)
```

### 不同尺寸

MSwitch 支持不同的尺寸，可以通过方法链式调用设置。

```python
from dayu_widgets.switch import MSwitch

# 创建超大尺寸的开关
switch_huge = MSwitch().huge()

# 创建大尺寸的开关
switch_large = MSwitch().large()

# 创建中等尺寸的开关（默认）
switch_medium = MSwitch().medium()

# 创建小尺寸的开关
switch_small = MSwitch().small()

# 创建超小尺寸的开关
switch_tiny = MSwitch().tiny()
```

### 监听状态变化

MSwitch 可以通过连接 `toggled` 信号来监听状态变化。

```python
from dayu_widgets.switch import MSwitch
from qtpy import QtWidgets

# 创建一个开关和标签
switch = MSwitch()
label = QtWidgets.QLabel("关闭")

# 监听状态变化
switch.toggled.connect(lambda checked: label.setText("开启" if checked else "关闭"))
```

### 数据绑定

MSwitch 可以与 MFieldMixin 结合使用，实现数据绑定。

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.switch import MSwitch
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel


class SwitchBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(SwitchBindExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 创建开关和标签
        switch = MSwitch()
        label = MLabel()

        # 注册字段和绑定
        self.register_field("is_on", False)
        self.register_field("status_text", lambda: "开启" if self.field("is_on") else "关闭")
        self.bind("is_on", switch, "checked", signal="toggled")
        self.bind("status_text", label, "text")

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(switch)
        main_lay.addWidget(label)
        self.setLayout(main_lay)
```

### 在表单中使用

MSwitch 常用于表单中作为开关选项。

```python
from dayu_widgets.switch import MSwitch
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# 创建表单布局
form_layout = QtWidgets.QFormLayout()

# 添加开关选项
form_layout.addRow(MLabel("自动保存:"), MSwitch())
form_layout.addRow(MLabel("夜间模式:"), MSwitch())
form_layout.addRow(MLabel("通知提醒:"), MSwitch())
```

### 完整示例

![MSwitch 演示](../_media/screenshots/MSwitch.png)

以下是一个完整的示例，展示了 MSwitch 的各种用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.switch import MSwitch


class SwitchExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(SwitchExample, self).__init__(parent)
        self.setWindowTitle("Examples for MSwitch")
        self._init_ui()

    def _init_ui(self):
        # 基本开关
        switch_1 = MSwitch()
        switch_1.setChecked(True)
        switch_2 = MSwitch()
        switch_3 = MSwitch()
        switch_3.setEnabled(False)
        basic_lay = QtWidgets.QHBoxLayout()
        basic_lay.addWidget(switch_1)
        basic_lay.addWidget(switch_2)
        basic_lay.addWidget(switch_3)
        basic_lay.addStretch()

        # 不同尺寸
        size_lay = QtWidgets.QFormLayout()
        size_lay.addRow("超大尺寸", MSwitch().huge())
        size_lay.addRow("大尺寸", MSwitch().large())
        size_lay.addRow("中等尺寸", MSwitch().medium())
        size_lay.addRow("小尺寸", MSwitch().small())
        size_lay.addRow("超小尺寸", MSwitch().tiny())

        # 数据绑定
        self.register_field("is_on", False)
        self.register_field("status_text", lambda: "开启状态" if self.field("is_on") else "关闭状态")

        switch_bind = MSwitch()
        status_label = MLabel()

        self.bind("is_on", switch_bind, "checked", signal="toggled")
        self.bind("status_text", status_label, "text")

        bind_lay = QtWidgets.QHBoxLayout()
        bind_lay.addWidget(switch_bind)
        bind_lay.addWidget(status_label)
        bind_lay.addStretch()

        # 主布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("基本"))
        main_lay.addLayout(basic_lay)
        main_lay.addWidget(MDivider("不同尺寸"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("数据绑定"))
        main_lay.addLayout(bind_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = SwitchExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MSwitch(parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_dayu_size(value)` | 设置开关的尺寸 | `value`: 尺寸值 | 无 |
| `get_dayu_size()` | 获取开关的尺寸 | 无 | `int` |
| `huge()` | 设置为超大尺寸 | 无 | `self` |
| `large()` | 设置为大尺寸 | 无 | `self` |
| `medium()` | 设置为中等尺寸 | 无 | `self` |
| `small()` | 设置为小尺寸 | 无 | `self` |
| `tiny()` | 设置为超小尺寸 | 无 | `self` |

### 继承的方法

MSwitch 继承自 QRadioButton，因此可以使用 QRadioButton 的所有方法，例如：

- `setChecked(bool)`: 设置开关是否选中
- `isChecked()`: 获取开关是否选中
- `setEnabled(bool)`: 设置开关是否启用
- 更多方法请参考 Qt 文档

### 信号

MSwitch 继承自 QRadioButton，因此可以使用 QRadioButton 的所有信号，例如：

- `toggled(bool)`: 当开关状态变化时触发
- 更多信号请参考 Qt 文档

## 常见问题

### 如何监听开关状态变化？

可以通过连接 `toggled` 信号来监听开关状态变化：

```python
from dayu_widgets.switch import MSwitch

# 创建开关
switch = MSwitch()

# 监听状态变化
switch.toggled.connect(lambda checked: print("开关状态:", "开启" if checked else "关闭"))
```

### 如何设置开关的默认状态？

可以通过 `setChecked` 方法设置开关的默认状态：

```python
from dayu_widgets.switch import MSwitch

# 创建开关
switch = MSwitch()

# 设置为选中状态
switch.setChecked(True)
```

### 如何禁用开关？

可以通过 `setEnabled` 方法禁用开关：

```python
from dayu_widgets.switch import MSwitch

# 创建开关
switch = MSwitch()

# 禁用开关
switch.setEnabled(False)
```

### 如何在表单中使用开关？

可以将开关添加到表单布局中：

```python
from dayu_widgets.switch import MSwitch
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# 创建表单布局
form_layout = QtWidgets.QFormLayout()

# 添加开关选项
form_layout.addRow(MLabel("自动保存:"), MSwitch())
form_layout.addRow(MLabel("夜间模式:"), MSwitch())
form_layout.addRow(MLabel("通知提醒:"), MSwitch())

# 创建部件并设置布局
widget = QtWidgets.QWidget()
widget.setLayout(form_layout)
```
