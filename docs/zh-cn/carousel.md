# MCarousel 走马灯

MCarousel 是一个走马灯组件，用于在有限空间内循环播放同一类型的内容，如图片、文本等。它提供了自动播放和手动切换功能，适用于展示轮播图、广告等内容。

## 导入

```python
from dayu_widgets.carousel import MCarousel
```

## 代码示例

### 基本使用

MCarousel 可以创建一个简单的图片轮播组件。

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个走马灯组件
carousel = MCarousel(images, width=300, height=300)
```

### 自动播放

MCarousel 默认启用自动播放功能，可以通过 `set_autoplay` 方法控制。

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个自动播放的走马灯组件
carousel = MCarousel(images, autoplay=True, width=300, height=300)

# 停止自动播放
carousel.set_autoplay(False)

# 重新启动自动播放
carousel.set_autoplay(True)
```

### 设置播放间隔

MCarousel 可以通过 `set_interval` 方法设置自动播放的间隔时间。

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个走马灯组件
carousel = MCarousel(images, autoplay=True, width=300, height=300)

# 设置播放间隔为 5 秒
carousel.set_interval(5000)
```

### 手动切换页面

MCarousel 提供了 `next_page` 和 `pre_page` 方法用于手动切换页面，以及 `go_to_page` 方法用于跳转到指定页面。

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap
from dayu_widgets.push_button import MPushButton
from qtpy import QtWidgets

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个走马灯组件
carousel = MCarousel(images, autoplay=False, width=300, height=300)

# 创建控制按钮
prev_button = MPushButton("上一页")
next_button = MPushButton("下一页")
page1_button = MPushButton("第 1 页")
page2_button = MPushButton("第 2 页")
page3_button = MPushButton("第 3 页")

# 连接信号
prev_button.clicked.connect(carousel.pre_page)
next_button.clicked.connect(carousel.next_page)
page1_button.clicked.connect(lambda: carousel.go_to_page(0))
page2_button.clicked.connect(lambda: carousel.go_to_page(1))
page3_button.clicked.connect(lambda: carousel.go_to_page(2))

# 创建布局
button_layout = QtWidgets.QHBoxLayout()
button_layout.addWidget(prev_button)
button_layout.addWidget(page1_button)
button_layout.addWidget(page2_button)
button_layout.addWidget(page3_button)
button_layout.addWidget(next_button)

main_layout = QtWidgets.QVBoxLayout()
main_layout.addWidget(carousel)
main_layout.addLayout(button_layout)
```

### 与控件交互

MCarousel 可以与其他控件交互，例如开关和滑块。

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap
from dayu_widgets.switch import MSwitch
from dayu_widgets.slider import MSlider
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个走马灯组件
carousel = MCarousel(images, autoplay=True, width=300, height=300)

# 创建控制开关
switch = MSwitch()
switch.setChecked(True)
switch.toggled.connect(carousel.set_autoplay)

# 创建间隔滑块
slider = MSlider()
slider.setRange(1, 10)
slider.setValue(3)
slider.valueChanged.connect(lambda x: carousel.set_interval(x * 1000))

# 创建布局
switch_layout = QtWidgets.QFormLayout()
switch_layout.addRow(MLabel("自动播放"), switch)
switch_layout.addRow(MLabel("播放间隔"), slider)

main_layout = QtWidgets.QVBoxLayout()
main_layout.addWidget(carousel)
main_layout.addLayout(switch_layout)
```

### 完整示例

![MCarousel 演示](../_media/screenshots/MCarousel.gif)

以下是一个完整的示例，展示了 MCarousel 的各种用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.carousel import MCarousel
from dayu_widgets.label import MLabel
from dayu_widgets.qt import MPixmap
from dayu_widgets.slider import MSlider
from dayu_widgets.switch import MSwitch


class CarouselExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CarouselExample, self).__init__(parent)
        self.setWindowTitle("Examples for MCarousel")
        self._init_ui()

    def _init_ui(self):
        switch = MSwitch()
        switch.setChecked(True)
        slider = MSlider()
        slider.setRange(1, 10)
        switch_lay = QtWidgets.QFormLayout()
        switch_lay.addRow(MLabel("自动播放"), switch)
        switch_lay.addRow(MLabel("播放间隔"), slider)
        test = MCarousel(
            [MPixmap("app-{}.png".format(a)) for a in ["maya", "nuke", "houdini"]],
            width=300,
            height=300,
            autoplay=True,
        )
        switch.toggled.connect(test.set_autoplay)
        slider.valueChanged.connect(lambda x: test.set_interval(x * 1000))
        slider.setValue(3)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(test)
        main_lay.addLayout(switch_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = CarouselExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MCarousel(pix_list, autoplay=True, width=500, height=500, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `pix_list` | 图片列表 | `List[QPixmap]` | - |
| `autoplay` | 是否自动播放 | `bool` | `True` |
| `width` | 组件宽度 | `int` | `500` |
| `height` | 组件高度 | `int` | `500` |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_autoplay(value)` | 设置是否自动播放 | `value`: 布尔值 | 无 |
| `set_interval(ms)` | 设置自动播放的间隔时间 | `ms`: 毫秒数 | 无 |
| `next_page()` | 切换到下一页 | 无 | 无 |
| `pre_page()` | 切换到上一页 | 无 | 无 |
| `go_to_page(index)` | 跳转到指定页面 | `index`: 页面索引 | 无 |

### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `autoplay` | 是否自动播放 | `bool` | `True` |

## 常见问题

### 如何更改图片大小？

MCarousel 会自动调整图片大小以适应组件的宽度和高度。您可以在创建 MCarousel 时指定宽度和高度：

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个指定大小的走马灯组件
carousel = MCarousel(images, width=400, height=300)
```

### 如何控制自动播放？

可以通过 `set_autoplay` 方法控制自动播放：

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个走马灯组件
carousel = MCarousel(images, autoplay=True)

# 停止自动播放
carousel.set_autoplay(False)

# 重新启动自动播放
carousel.set_autoplay(True)
```

### 如何更改自动播放的间隔时间？

可以通过 `set_interval` 方法更改自动播放的间隔时间：

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个走马灯组件
carousel = MCarousel(images, autoplay=True)

# 设置播放间隔为 5 秒
carousel.set_interval(5000)
```

### 如何手动切换页面？

可以使用 `next_page`、`pre_page` 和 `go_to_page` 方法手动切换页面：

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# 创建一个图片列表
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# 创建一个走马灯组件
carousel = MCarousel(images, autoplay=False)

# 切换到下一页
carousel.next_page()

# 切换到上一页
carousel.pre_page()

# 跳转到第二页（索引从 0 开始）
carousel.go_to_page(1)
```
