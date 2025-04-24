# MLoading 加载动画

MLoading 是一个用于显示加载动画的组件，它提供了一个旋转的图标来指示正在进行的操作。此外，MLoadingWrapper 组件可以为任何小部件添加加载状态遮罩。

## 导入

```python
from dayu_widgets.loading import MLoading
from dayu_widgets.loading import MLoadingWrapper
```

## 代码示例

### 基本使用

MLoading 可以直接使用，默认显示一个旋转的加载图标。

```python
from dayu_widgets.loading import MLoading

# 创建默认大小的加载动画
loading = MLoading()
```

### 不同尺寸

MLoading 提供了五种尺寸：tiny、small、medium（默认）、large 和 huge。

```python
from dayu_widgets.loading import MLoading

# 创建不同尺寸的加载动画
tiny_loading = MLoading.tiny()
small_loading = MLoading.small()
medium_loading = MLoading.medium()  # 等同于 MLoading()
large_loading = MLoading.large()
huge_loading = MLoading.huge()
```

### 自定义颜色

MLoading 支持自定义颜色，可以通过参数设置加载图标的颜色。

```python
from dayu_widgets.loading import MLoading

# 创建不同颜色的加载动画
cyan_loading = MLoading.tiny(color="#13c2c2")
green_loading = MLoading.tiny(color="#52c41a")
magenta_loading = MLoading.tiny(color="#eb2f96")
red_loading = MLoading.tiny(color="#f5222d")
yellow_loading = MLoading.tiny(color="#fadb14")
volcano_loading = MLoading.tiny(color="#fa541c")
```

### 加载包装器

MLoadingWrapper 可以为任何小部件添加加载状态遮罩，当设置为加载状态时，会显示一个半透明遮罩和加载动画。

```python
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# 创建一个标签
label = MLabel("这是一个标签")
label.setFixedSize(200, 200)

# 创建一个加载包装器，包装标签
loading_wrapper = MLoadingWrapper(label, loading=False)

# 设置为加载状态
loading_wrapper.set_dayu_loading(True)

# 取消加载状态
loading_wrapper.set_dayu_loading(False)
```

### 与线程结合使用

MLoadingWrapper 通常与线程结合使用，在数据加载过程中显示加载状态。

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton

# 创建一个工作线程
class WorkThread(QtCore.QThread):
    def run(self):
        # 模拟耗时操作
        QtCore.QThread.sleep(3)

# 创建一个小部件
widget = QtWidgets.QTableView()

# 创建加载包装器
loading_wrapper = MLoadingWrapper(widget=widget, loading=False)

# 创建线程
thread = WorkThread()

# 连接信号
thread.started.connect(functools.partial(loading_wrapper.set_dayu_loading, True))
thread.finished.connect(functools.partial(loading_wrapper.set_dayu_loading, False))

# 创建按钮启动线程
button = MPushButton(text="加载数据")
button.clicked.connect(thread.start)
```

### 完整示例

![MLoading 演示](../_media/screenshots/mloading.gif)

以下是一个完整的示例，展示了 MLoading 的所有功能：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.loading import MLoading
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton


class LoadingExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(LoadingExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLoading")
        self._init_ui()

    def _init_ui(self):
        size_lay = QtWidgets.QHBoxLayout()
        size_list = [
            ("Huge", MLoading.huge),
            ("Large", MLoading.large),
            ("Medium", MLoading.medium),
            ("Small", MLoading.small),
            ("Tiny", MLoading.tiny),
        ]
        for label, cls in size_list:
            size_lay.addWidget(MLabel(label))
            size_lay.addWidget(cls())
            size_lay.addSpacing(10)

        color_lay = QtWidgets.QHBoxLayout()
        color_list = [
            ("cyan", "#13c2c2"),
            ("green", "#52c41a"),
            ("magenta", "#eb2f96"),
            ("red", "#f5222d"),
            ("yellow", "#fadb14"),
            ("volcano", "#fa541c"),
        ]
        for label, color in color_list:
            color_lay.addWidget(MLabel(label))
            color_lay.addWidget(MLoading.tiny(color=color))
            color_lay.addSpacing(10)

        # 创建一个标签用于演示 MLoadingWrapper
        demo_label = MLabel("这是一个标签，点击下方按钮切换加载状态")
        demo_label.setFixedSize(300, 100)
        wrapper = MLoadingWrapper(demo_label, loading=False)

        # 创建按钮控制加载状态
        button = MPushButton("切换加载状态")
        button.clicked.connect(lambda: wrapper.set_dayu_loading(not wrapper.get_dayu_loading()))

        wrapper_lay = QtWidgets.QVBoxLayout()
        wrapper_lay.addWidget(wrapper)
        wrapper_lay.addWidget(button)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("不同尺寸"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("不同颜色"))
        main_lay.addLayout(color_lay)
        main_lay.addWidget(MDivider("加载包装器"))
        main_lay.addLayout(wrapper_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = LoadingExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### MLoading

#### 构造函数

```python
MLoading(size=None, color=None, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `size` | 加载动画的大小 | `int` | `dayu_theme.default_size` |
| `color` | 加载动画的颜色 | `str` | `dayu_theme.primary_color` |
| `parent` | 父窗口 | `QWidget` | `None` |

#### 类方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `tiny(color=None)` | 创建超小尺寸的加载动画 | `color`: 颜色，可选 | `MLoading` 实例 |
| `small(color=None)` | 创建小尺寸的加载动画 | `color`: 颜色，可选 | `MLoading` 实例 |
| `medium(color=None)` | 创建中等尺寸的加载动画 | `color`: 颜色，可选 | `MLoading` 实例 |
| `large(color=None)` | 创建大尺寸的加载动画 | `color`: 颜色，可选 | `MLoading` 实例 |
| `huge(color=None)` | 创建超大尺寸的加载动画 | `color`: 颜色，可选 | `MLoading` 实例 |

### MLoadingWrapper

#### 构造函数

```python
MLoadingWrapper(widget, loading=True, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `widget` | 要包装的小部件 | `QWidget` | - |
| `loading` | 初始加载状态 | `bool` | `True` |
| `parent` | 父窗口 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_dayu_loading(loading)` | 设置加载状态 | `loading`: 是否显示加载动画 | `None` |
| `get_dayu_loading()` | 获取当前加载状态 | 无 | `bool` |

#### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `dayu_loading` | 当前加载状态 | `bool` | - |

## 常见问题

### 如何更改加载动画的颜色？

MLoading 支持自定义颜色，可以在创建时通过 `color` 参数设置：

```python
from dayu_widgets.loading import MLoading

# 使用十六进制颜色代码
loading1 = MLoading(color="#1890ff")

# 使用类方法时也可以设置颜色
loading2 = MLoading.tiny(color="#f5222d")
```

### 如何在加载数据时显示加载动画？

MLoadingWrapper 通常与线程结合使用，在数据加载过程中显示加载状态：

```python
from dayu_widgets.loading import MLoadingWrapper
from qtpy import QtCore
import functools

# 创建一个小部件
widget = QtWidgets.QTableView()

# 创建加载包装器
loading_wrapper = MLoadingWrapper(widget=widget, loading=False)

# 创建线程
thread = QtCore.QThread()

# 连接信号
thread.started.connect(functools.partial(loading_wrapper.set_dayu_loading, True))
thread.finished.connect(functools.partial(loading_wrapper.set_dayu_loading, False))
```

### 如何为自定义小部件添加加载状态？

MLoadingWrapper 可以包装任何 QWidget 子类，为其添加加载状态：

```python
from dayu_widgets.loading import MLoadingWrapper
from qtpy import QtWidgets

# 创建自定义小部件
custom_widget = QtWidgets.QWidget()
custom_layout = QtWidgets.QVBoxLayout()
custom_widget.setLayout(custom_layout)
custom_layout.addWidget(QtWidgets.QLabel("自定义内容"))

# 创建加载包装器
wrapper = MLoadingWrapper(custom_widget, loading=False)

# 设置为加载状态
wrapper.set_dayu_loading(True)
```
