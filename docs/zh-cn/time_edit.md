# MTimeEdit 时间编辑框

MTimeEdit 是一个时间编辑框组件，用于输入和编辑时间。它基于 Qt 的 QTimeEdit 类，提供了更美观的样式和更好的交互体验。

## 导入

```python
from dayu_widgets.spin_box import MTimeEdit
```

## 代码示例

### 基本使用

MTimeEdit 可以创建一个简单的时间输入框，用户可以通过点击上下按钮或直接输入来设置时间。

```python
# Import built-in modules
import datetime

# Import local modules
from dayu_widgets.spin_box import MTimeEdit

# 创建一个时间输入框
time_edit = MTimeEdit()
time_edit.setTime(datetime.datetime.now().time())
```

### 不同尺寸

MTimeEdit 支持不同的尺寸，可以通过方法链式调用设置。

```python
from dayu_widgets.spin_box import MTimeEdit

# 创建超大尺寸的时间输入框
time_edit_huge = MTimeEdit().huge()

# 创建大尺寸的时间输入框
time_edit_large = MTimeEdit().large()

# 创建中等尺寸的时间输入框（默认）
time_edit_medium = MTimeEdit().medium()

# 创建小尺寸的时间输入框
time_edit_small = MTimeEdit().small()

# 创建超小尺寸的时间输入框
time_edit_tiny = MTimeEdit().tiny()
```

### 设置时间范围

MTimeEdit 支持设置时间范围。

```python
# Import built-in modules
import datetime

# Import local modules
from dayu_widgets.spin_box import MTimeEdit

# 创建时间输入框并设置范围
time_edit = MTimeEdit()
time_edit.setTimeRange(
    datetime.time(9, 0, 0),
    datetime.time(18, 0, 0)
)
```

### 设置显示格式

MTimeEdit 支持设置显示格式。

```python
from dayu_widgets.spin_box import MTimeEdit

# 创建时间输入框并设置显示格式
time_edit = MTimeEdit()
time_edit.setDisplayFormat("hh时mm分ss秒")
```

### 监听时间变化

MTimeEdit 可以通过连接 `timeChanged` 信号来监听时间变化。

```python
# Import built-in modules
import datetime

# Import local modules
from dayu_widgets.spin_box import MTimeEdit

# 创建时间输入框
time_edit = MTimeEdit()
time_edit.setTime(datetime.datetime.now().time())

# 监听时间变化
time_edit.timeChanged.connect(lambda time: print("当前时间:", time))
```

### 完整示例

![MTimeEdit 演示](../_media/screenshots/MTimeEdit.png)

以下是一个完整的示例，展示了 MTimeEdit 的各种用法：

```python
# Import built-in modules
import datetime

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.spin_box import MTimeEdit
from dayu_widgets.label import MLabel


class TimeEditExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TimeEditExample, self).__init__(parent)
        self.setWindowTitle("Examples for MTimeEdit")
        self._init_ui()

    def _init_ui(self):
        main_lay = QtWidgets.QVBoxLayout()

        # 基本使用
        main_lay.addWidget(MDivider("基本使用"))
        basic_lay = QtWidgets.QHBoxLayout()
        basic_time_edit = MTimeEdit()
        basic_time_edit.setTime(datetime.datetime.now().time())
        basic_lay.addWidget(MLabel("基本时间输入框:"))
        basic_lay.addWidget(basic_time_edit)
        basic_lay.addStretch()
        main_lay.addLayout(basic_lay)

        # 不同尺寸
        main_lay.addWidget(MDivider("不同尺寸"))
        size_lay = QtWidgets.QFormLayout()
        size_lay.addRow("超大尺寸", MTimeEdit().huge())
        size_lay.addRow("大尺寸", MTimeEdit().large())
        size_lay.addRow("中等尺寸", MTimeEdit().medium())
        size_lay.addRow("小尺寸", MTimeEdit().small())
        size_lay.addRow("超小尺寸", MTimeEdit().tiny())
        main_lay.addLayout(size_lay)

        # 设置时间范围
        main_lay.addWidget(MDivider("设置时间范围"))
        range_lay = QtWidgets.QHBoxLayout()
        range_time_edit = MTimeEdit()
        range_time_edit.setTimeRange(
            datetime.time(9, 0, 0),
            datetime.time(18, 0, 0)
        )
        range_lay.addWidget(MLabel("时间范围 09:00:00 到 18:00:00:"))
        range_lay.addWidget(range_time_edit)
        range_lay.addStretch()
        main_lay.addLayout(range_lay)

        # 设置显示格式
        main_lay.addWidget(MDivider("设置显示格式"))
        format_lay = QtWidgets.QHBoxLayout()
        format_time_edit = MTimeEdit()
        format_time_edit.setDisplayFormat("hh时mm分ss秒")
        format_lay.addWidget(MLabel("自定义显示格式:"))
        format_lay.addWidget(format_time_edit)
        format_lay.addStretch()
        main_lay.addLayout(format_lay)

        # 监听时间变化
        main_lay.addWidget(MDivider("监听时间变化"))
        time_changed_lay = QtWidgets.QHBoxLayout()
        time_changed_time_edit = MTimeEdit()
        time_changed_time_edit.setTime(datetime.datetime.now().time())
        time_changed_label = MLabel("当前时间: {}".format(datetime.datetime.now().time().strftime("%H:%M:%S")))
        time_changed_time_edit.timeChanged.connect(
            lambda time: time_changed_label.setText("当前时间: {}".format(time.toString("hh:mm:ss")))
        )
        time_changed_lay.addWidget(time_changed_time_edit)
        time_changed_lay.addWidget(time_changed_label)
        time_changed_lay.addStretch()
        main_lay.addLayout(time_changed_lay)

        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = TimeEditExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MTimeEdit(time=None, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `time` | 初始时间 | `datetime.datetime` 或 `datetime.time` | `None` |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_dayu_size(value)` | 设置输入框的尺寸 | `value`: 尺寸值 | 无 |
| `get_dayu_size()` | 获取输入框的尺寸 | 无 | `int` |
| `huge()` | 设置为超大尺寸 | 无 | `self` |
| `large()` | 设置为大尺寸 | 无 | `self` |
| `medium()` | 设置为中等尺寸 | 无 | `self` |
| `small()` | 设置为小尺寸 | 无 | `self` |
| `tiny()` | 设置为超小尺寸 | 无 | `self` |

### 继承的方法

MTimeEdit 继承自 QTimeEdit，因此可以使用 QTimeEdit 的所有方法，例如：

- `setTime(time)`: 设置时间
- `time()`: 获取时间
- `setTimeRange(min, max)`: 设置时间范围
- `setMinimumTime(time)`: 设置最小时间
- `setMaximumTime(time)`: 设置最大时间
- `setDisplayFormat(format)`: 设置显示格式
- 更多方法请参考 Qt 文档

### 信号

MTimeEdit 继承自 QTimeEdit，因此可以使用 QTimeEdit 的所有信号，例如：

- `timeChanged(time)`: 当时间变化时触发
- 更多信号请参考 Qt 文档

## 常见问题

### 如何设置时间格式？

可以通过 `setDisplayFormat` 方法设置时间格式：

```python
from dayu_widgets.spin_box import MTimeEdit

# 创建时间输入框
time_edit = MTimeEdit()

# 设置显示格式
time_edit.setDisplayFormat("hh:mm:ss")
```

格式字符串使用以下占位符：

- `h`：小时（0-23）
- `hh`：小时（00-23）
- `m`：分钟（0-59）
- `mm`：分钟（00-59）
- `s`：秒（0-59）
- `ss`：秒（00-59）
- `AP`：使用 AM/PM 显示
- `ap`：使用 am/pm 显示

### 如何设置时间范围？

可以通过 `setTimeRange` 方法设置时间范围：

```python
# Import built-in modules
import datetime

# Import local modules
from dayu_widgets.spin_box import MTimeEdit

# 创建时间输入框
time_edit = MTimeEdit()

# 设置时间范围
time_edit.setTimeRange(
    datetime.time(9, 0, 0),
    datetime.time(18, 0, 0)
)
```

也可以单独设置最小和最大时间：

```python
# Import built-in modules
import datetime

# Import local modules
from dayu_widgets.spin_box import MTimeEdit

# 创建时间输入框
time_edit = MTimeEdit()

# 设置最小时间
time_edit.setMinimumTime(datetime.time(9, 0, 0))

# 设置最大时间
time_edit.setMaximumTime(datetime.time(18, 0, 0))
```

### 如何禁用时间输入框？

可以通过 `setEnabled` 方法禁用时间输入框：

```python
from dayu_widgets.spin_box import MTimeEdit

# 创建时间输入框
time_edit = MTimeEdit()

# 禁用时间输入框
time_edit.setEnabled(False)
```
