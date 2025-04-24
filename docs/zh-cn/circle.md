# MProgressCircle 环形进度

MProgressCircle 是一个环形进度组件，用于以环形方式展示操作的当前进度。它支持自定义颜色、尺寸，并且可以设置为仪表盘样式或添加自定义内容。

## 导入

```python
from dayu_widgets.progress_circle import MProgressCircle
```

## 代码示例

### 基本使用

MProgressCircle 可以创建一个简单的环形进度条，用于显示操作的进度。

```python
from dayu_widgets.progress_circle import MProgressCircle

# 创建一个环形进度条
progress_circle = MProgressCircle()
progress_circle.setValue(50)  # 设置进度为 50%
```

### 自定义颜色

MProgressCircle 支持自定义颜色，可以通过 `set_dayu_color` 方法设置。

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets import dayu_theme

# 创建一个自定义颜色的环形进度条
progress_circle = MProgressCircle()
progress_circle.set_dayu_color(dayu_theme.success_color)
progress_circle.setValue(80)

# 创建一个错误状态的环形进度条
error_circle = MProgressCircle()
error_circle.set_dayu_color(dayu_theme.error_color)
error_circle.setValue(40)
```

### 仪表盘样式

MProgressCircle 支持仪表盘样式，可以通过 `dashboard` 类方法创建。

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets import dayu_theme

# 创建一个仪表盘样式的环形进度条
dashboard = MProgressCircle.dashboard()
dashboard.setValue(75)

# 创建一个自定义颜色的仪表盘
custom_dashboard = MProgressCircle.dashboard()
custom_dashboard.set_dayu_color(dayu_theme.success_color)
custom_dashboard.setValue(100)
```

### 自定义尺寸

MProgressCircle 支持自定义尺寸，可以通过 `set_dayu_width` 方法设置。

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.qt import get_scale_factor

# 获取缩放因子
scale_x, _ = get_scale_factor()

# 创建一个小尺寸的环形进度条
small_circle = MProgressCircle()
small_circle.set_dayu_width(100 * scale_x)
small_circle.setValue(40)

# 创建一个默认尺寸的环形进度条
default_circle = MProgressCircle()
default_circle.setValue(40)

# 创建一个大尺寸的环形进度条
large_circle = MProgressCircle()
large_circle.set_dayu_width(160 * scale_x)
large_circle.setValue(40)
```

### 自定义格式

MProgressCircle 支持自定义文本格式，可以通过 `setFormat` 方法设置。

```python
from dayu_widgets.progress_circle import MProgressCircle

# 创建一个自定义格式的环形进度条
progress_circle = MProgressCircle()
progress_circle.setFormat("%p Days")
progress_circle.setValue(80)
```

### 自定义内容

MProgressCircle 支持添加自定义内容，可以通过 `set_widget` 方法设置。

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.label import MLabel
from dayu_widgets.divider import MDivider
from qtpy import QtWidgets
from qtpy import QtCore

# 创建自定义内容部件
custom_widget = QtWidgets.QWidget()
custom_layout = QtWidgets.QVBoxLayout()
custom_layout.setContentsMargins(20, 20, 20, 20)
custom_layout.addStretch()
custom_widget.setLayout(custom_layout)

# 添加标签
lab1 = MLabel(text="42,001,776").h3()
lab2 = MLabel(text="消费人群规模").secondary()
lab3 = MLabel(text="总占人数 75%").secondary()
lab1.setAlignment(QtCore.Qt.AlignCenter)
lab2.setAlignment(QtCore.Qt.AlignCenter)
lab3.setAlignment(QtCore.Qt.AlignCenter)
custom_layout.addWidget(lab1)
custom_layout.addWidget(lab2)
custom_layout.addWidget(MDivider())
custom_layout.addWidget(lab3)
custom_layout.addStretch()

# 创建环形进度条并设置自定义内容
custom_circle = MProgressCircle()
custom_circle.set_dayu_width(180)
custom_circle.setValue(75)
custom_circle.set_widget(custom_widget)
```

### 数据绑定

MProgressCircle 可以与 MFieldMixin 结合使用，实现数据绑定。

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.push_button import MPushButton
from dayu_widgets import dayu_theme
import functools


class ProgressCircleBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressCircleBindExample, self).__init__(parent)
        self._init_ui()
        
    def _init_ui(self):
        # 注册字段
        self.register_field("percent", 0)
        self.register_field("color", self.get_color)
        self.register_field("format", self.get_format)
        
        # 创建环形进度条
        circle = MProgressCircle()
        
        # 绑定数据
        self.bind("percent", circle, "value")
        self.bind("color", circle, "dayu_color")
        self.bind("format", circle, "format")
        
        # 创建按钮
        button_grp = QtWidgets.QHBoxLayout()
        plus_button = MPushButton(text="+")
        minus_button = MPushButton(text="-")
        plus_button.clicked.connect(functools.partial(self.slot_change_percent, 10))
        minus_button.clicked.connect(functools.partial(self.slot_change_percent, -10))
        button_grp.addWidget(plus_button)
        button_grp.addWidget(minus_button)
        
        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(circle)
        main_lay.addLayout(button_grp)
        self.setLayout(main_lay)
    
    def get_color(self):
        """根据百分比获取颜色"""
        p = self.field("percent")
        if p < 30:
            return dayu_theme.error_color
        if p < 60:
            return dayu_theme.warning_color
        if p < 100:
            return dayu_theme.primary_color
        return dayu_theme.success_color
    
    def get_format(self):
        """根据百分比获取格式"""
        p = self.field("percent")
        if p < 30:
            return ">_<"
        if p < 60:
            return "0_0"
        if p < 100:
            return "^_^"
        return "^o^"
    
    def slot_change_percent(self, value):
        """改变百分比"""
        self.set_field("percent", max(0, min(self.field("percent") + value, 100)))
```

### 完整示例

以下是一个完整的示例，展示了 MProgressCircle 的各种用法：

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import get_scale_factor


class ProgressCircleExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressCircleExample, self).__init__(parent)
        self.setWindowTitle("Examples for MProgressCircle")
        self._init_ui()

    def _init_ui(self):
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider("circle"))
        lay1 = QtWidgets.QHBoxLayout()
        circle_1 = MProgressCircle(parent=self)
        circle_1.setFormat("%p Days")
        circle_1.setValue(80)
        circle_2 = MProgressCircle(parent=self)
        circle_2.set_dayu_color(dayu_theme.success_color)
        circle_2.setValue(100)
        circle_3 = MProgressCircle(parent=self)
        circle_3.set_dayu_color(dayu_theme.error_color)
        circle_3.setValue(40)

        dashboard_1 = MProgressCircle.dashboard(parent=self)
        dashboard_1.setFormat("%p Days")
        dashboard_1.setValue(80)
        dashboard_2 = MProgressCircle.dashboard(parent=self)
        dashboard_2.set_dayu_color(dayu_theme.success_color)
        dashboard_2.setValue(100)
        dashboard_3 = MProgressCircle.dashboard(parent=self)
        dashboard_3.set_dayu_color(dayu_theme.error_color)
        dashboard_3.setValue(40)

        lay1.addWidget(circle_1)
        lay1.addWidget(circle_2)
        lay1.addWidget(circle_3)

        dashboard_lay = QtWidgets.QHBoxLayout()
        dashboard_lay.addWidget(dashboard_1)
        dashboard_lay.addWidget(dashboard_2)
        dashboard_lay.addWidget(dashboard_3)
        main_lay.addLayout(lay1)
        main_lay.addWidget(MDivider("dashboard"))
        main_lay.addLayout(dashboard_lay)
        main_lay.addWidget(MDivider("different radius"))

        scale_x, _ = get_scale_factor()
        circle_4 = MProgressCircle(parent=self)
        circle_4.set_dayu_width(100 * scale_x)
        circle_4.setValue(40)
        circle_5 = MProgressCircle(parent=self)
        circle_5.setValue(40)
        circle_6 = MProgressCircle(parent=self)
        circle_6.set_dayu_width(160 * scale_x)
        circle_6.setValue(40)
        lay2 = QtWidgets.QHBoxLayout()
        lay2.addWidget(circle_4)
        lay2.addWidget(circle_5)
        lay2.addWidget(circle_6)

        main_lay.addLayout(lay2)
        main_lay.addWidget(MDivider("data bind"))

        self.register_field("percent", 0)
        self.register_field("color", self.get_color)
        self.register_field("format", self.get_format)
        circle = MProgressCircle(parent=self)

        self.bind("percent", circle, "value")
        self.bind("color", circle, "dayu_color")
        self.bind("format", circle, "format")
        lay3 = QtWidgets.QHBoxLayout()
        button_grp = MPushButtonGroup()
        button_grp.set_dayu_type(MPushButton.DefaultType)
        button_grp.set_button_list(
            [
                {
                    "text": "+",
                    "clicked": functools.partial(self.slot_change_percent, 10),
                },
                {
                    "text": "-",
                    "clicked": functools.partial(self.slot_change_percent, -10),
                },
            ]
        )
        lay3.addWidget(circle)
        lay3.addWidget(button_grp)
        lay3.addStretch()
        main_lay.addLayout(lay3)

        custom_widget = QtWidgets.QWidget()
        custom_layout = QtWidgets.QVBoxLayout()
        custom_layout.setContentsMargins(20, 20, 20, 20)
        custom_layout.addStretch()
        custom_widget.setLayout(custom_layout)
        lab1 = MLabel(text="42,001,776").h3()
        lab2 = MLabel(text="消费人群规模").secondary()
        lab3 = MLabel(text="总占人数 75%").secondary()
        lab1.setAlignment(QtCore.Qt.AlignCenter)
        lab2.setAlignment(QtCore.Qt.AlignCenter)
        lab3.setAlignment(QtCore.Qt.AlignCenter)
        custom_layout.addWidget(lab1)
        custom_layout.addWidget(lab2)
        custom_layout.addWidget(MDivider())
        custom_layout.addWidget(lab3)
        custom_layout.addStretch()
        custom_circle = MProgressCircle()
        custom_circle.set_dayu_width(180 * scale_x)
        custom_circle.setValue(75)
        custom_circle.set_widget(custom_widget)

        main_lay.addWidget(MDivider("custom circle"))
        main_lay.addWidget(custom_circle)
        main_lay.addStretch()

    def get_color(self):
        p = self.field("percent")
        if p < 30:
            return dayu_theme.error_color
        if p < 60:
            return dayu_theme.warning_color
        if p < 100:
            return dayu_theme.primary_color
        return dayu_theme.success_color

    def get_format(self):
        p = self.field("percent")
        if p < 30:
            return ">_<"
        if p < 60:
            return "0_0"
        if p < 100:
            return "^_^"
        return "^o^"

    def slot_change_percent(self, value):
        self.set_field("percent", max(0, min(self.field("percent") + value, 100)))


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = ProgressCircleExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MProgressCircle(dashboard=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `dashboard` | 是否为仪表盘样式 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `get_dayu_width()` | 获取环形进度条的宽度 | 无 | `int` |
| `set_dayu_width(value)` | 设置环形进度条的宽度 | `value`: 宽度值 | 无 |
| `get_dayu_color()` | 获取环形进度条的颜色 | 无 | `str` |
| `set_dayu_color(value)` | 设置环形进度条的颜色 | `value`: 颜色值 | 无 |
| `set_widget(widget)` | 设置自定义内容部件 | `widget`: 内容部件 | 无 |

### 类方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `dashboard(parent=None)` | 创建仪表盘样式的环形进度条 | `parent`: 父部件 | `MProgressCircle` 实例 |

### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `dayu_width` | 环形进度条的宽度 | `int` | `dayu_theme.progress_circle_default_radius` |
| `dayu_color` | 环形进度条的颜色 | `str` | `dayu_theme.primary_color` |

### 继承的方法

MProgressCircle 继承自 QProgressBar，因此可以使用 QProgressBar 的所有方法，例如：

- `setValue(value)`: 设置当前值
- `value()`: 获取当前值
- `setRange(min, max)`: 设置范围
- `setMinimum(min)`: 设置最小值
- `setMaximum(max)`: 设置最大值
- `setFormat(format)`: 设置文本格式
- 更多方法请参考 Qt 文档

## 常见问题

### 如何创建仪表盘样式的环形进度条？

可以使用 `dashboard` 类方法创建仪表盘样式的环形进度条：

```python
from dayu_widgets.progress_circle import MProgressCircle

# 创建一个仪表盘样式的环形进度条
dashboard = MProgressCircle.dashboard()
dashboard.setValue(75)
```

### 如何自定义环形进度条的颜色？

可以使用 `set_dayu_color` 方法自定义环形进度条的颜色：

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets import dayu_theme

# 创建一个环形进度条
progress_circle = MProgressCircle()

# 设置为成功颜色
progress_circle.set_dayu_color(dayu_theme.success_color)

# 设置为错误颜色
progress_circle.set_dayu_color(dayu_theme.error_color)

# 设置为自定义颜色
progress_circle.set_dayu_color("#1890ff")
```

### 如何自定义环形进度条的尺寸？

可以使用 `set_dayu_width` 方法自定义环形进度条的尺寸：

```python
from dayu_widgets.progress_circle import MProgressCircle

# 创建一个环形进度条
progress_circle = MProgressCircle()

# 设置为小尺寸
progress_circle.set_dayu_width(80)

# 设置为大尺寸
progress_circle.set_dayu_width(160)
```

### 如何添加自定义内容到环形进度条中？

可以使用 `set_widget` 方法添加自定义内容到环形进度条中：

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.label import MLabel
from qtpy import QtWidgets
from qtpy import QtCore

# 创建自定义内容部件
custom_widget = QtWidgets.QWidget()
custom_layout = QtWidgets.QVBoxLayout()
custom_widget.setLayout(custom_layout)

# 添加标签
label = MLabel("自定义内容")
label.setAlignment(QtCore.Qt.AlignCenter)
custom_layout.addWidget(label)

# 创建环形进度条并设置自定义内容
progress_circle = MProgressCircle()
progress_circle.setValue(75)
progress_circle.set_widget(custom_widget)
```
