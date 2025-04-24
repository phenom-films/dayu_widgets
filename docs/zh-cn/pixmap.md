# MPixmap 图像

MPixmap 是一个用于加载和管理图像的组件，它基于 Qt 的 QPixmap 类，提供了更便捷的图像加载和颜色管理功能。

## 导入

```python
from dayu_widgets.qt import MPixmap
```

## 代码示例

### 基本使用

MPixmap 可以加载 SVG 或 PNG 格式的图像。

```python
from dayu_widgets.qt import MPixmap
from qtpy import QtWidgets

# 创建一个图像
pixmap = MPixmap("avatar.png")

# 创建一个 SVG 图像
svg_pixmap = MPixmap("success_line.svg")

# 在标签中使用图像
label = QtWidgets.QLabel()
label.setPixmap(pixmap)
```

### 自定义颜色

MPixmap 支持为 SVG 图像设置自定义颜色。

```python
from dayu_widgets.qt import MPixmap
from dayu_widgets import dayu_theme

# 使用十六进制颜色代码
colored_pixmap = MPixmap("success_line.svg", "#1890ff")

# 使用主题颜色
primary_pixmap = MPixmap("success_line.svg", dayu_theme.primary_color)
success_pixmap = MPixmap("success_line.svg", dayu_theme.success_color)
warning_pixmap = MPixmap("warning_line.svg", dayu_theme.warning_color)
error_pixmap = MPixmap("error_line.svg", dayu_theme.error_color)
```

### 在组件中使用

MPixmap 可以与 dayu_widgets 中的其他组件一起使用，如 MAvatar、MCard 等。

```python
from dayu_widgets.qt import MPixmap
from dayu_widgets.avatar import MAvatar
from dayu_widgets.card import MCard

# 在 MAvatar 中使用
avatar = MAvatar()
avatar.set_dayu_image(MPixmap("avatar.png"))

# 在 MCard 中使用
card = MCard(title="Card Title", image=MPixmap("app-houdini.png"))
```

### 缓存机制

MPixmap 使用缓存机制，相同路径和颜色的图像只会加载一次，提高性能。

```python
from dayu_widgets.qt import MPixmap

# 这两个变量引用的是同一个图像对象
pixmap1 = MPixmap("avatar.png")
pixmap2 = MPixmap("avatar.png")

# 这两个变量引用的是不同的图像对象，因为颜色不同
colored_pixmap1 = MPixmap("success_line.svg", "#1890ff")
colored_pixmap2 = MPixmap("success_line.svg", "#52c41a")
```

### 完整示例

![MPixmap 演示](../_media/screenshots/mpixmap.png)

以下是一个完整的示例，展示了 MPixmap 的各种用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.avatar import MAvatar
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.qt import MPixmap


class PixmapExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(PixmapExample, self).__init__(parent)
        self.setWindowTitle("Examples for MPixmap")
        self._init_ui()

    def _init_ui(self):
        basic_lay = QtWidgets.QHBoxLayout()

        # 基本图像
        label1 = QtWidgets.QLabel()
        label1.setPixmap(MPixmap("app-maya.png"))
        basic_lay.addWidget(label1)

        label2 = QtWidgets.QLabel()
        label2.setPixmap(MPixmap("app-nuke.png"))
        basic_lay.addWidget(label2)

        label3 = QtWidgets.QLabel()
        label3.setPixmap(MPixmap("app-houdini.png"))
        basic_lay.addWidget(label3)

        basic_lay.addStretch()

        # 不同颜色的 SVG 图像
        color_lay = QtWidgets.QHBoxLayout()
        color_list = [
            ("primary", dayu_theme.primary_color),
            ("success", dayu_theme.success_color),
            ("warning", dayu_theme.warning_color),
            ("error", dayu_theme.error_color),
        ]

        for label_text, color in color_list:
            label = QtWidgets.QLabel()
            label.setPixmap(MPixmap("success_line.svg", color))
            color_lay.addWidget(MLabel(label_text))
            color_lay.addWidget(label)
            color_lay.addSpacing(10)

        color_lay.addStretch()

        # 在 MAvatar 中使用
        avatar_lay = QtWidgets.QHBoxLayout()

        avatar1 = MAvatar()
        avatar1.set_dayu_image(MPixmap("avatar.png"))
        avatar_lay.addWidget(avatar1)

        avatar2 = MAvatar()
        avatar2.set_dayu_image(MPixmap("app-maya.png"))
        avatar_lay.addWidget(avatar2)

        avatar3 = MAvatar()
        avatar3.set_dayu_image(MPixmap("app-nuke.png"))
        avatar_lay.addWidget(avatar3)

        avatar4 = MAvatar()
        avatar4.set_dayu_image(MPixmap("app-houdini.png"))
        avatar_lay.addWidget(avatar4)

        avatar_lay.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("基本图像"))
        main_lay.addLayout(basic_lay)
        main_lay.addWidget(MDivider("不同颜色的 SVG 图像"))
        main_lay.addLayout(color_lay)
        main_lay.addWidget(MDivider("在 MAvatar 中使用"))
        main_lay.addLayout(avatar_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = PixmapExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MPixmap(path, color=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `path` | 图像路径，相对于静态资源目录 | `str` | - |
| `color` | 图像颜色，仅对 SVG 图像有效 | `str` | `None` |

### 静态资源路径

MPixmap 会在以下路径中查找图像文件：

1. 默认路径：`dayu_widgets/static/`
2. 自定义路径：通过 `dayu_widgets.CUSTOM_STATIC_FOLDERS` 设置

### 继承的方法

MPixmap 继承自 QPixmap，因此可以使用 QPixmap 的所有方法，例如：

- `width()`: 获取图像宽度
- `height()`: 获取图像高度
- `size()`: 获取图像大小
- `scaled()`: 缩放图像
- `scaledToWidth()`: 按宽度缩放图像
- `scaledToHeight()`: 按高度缩放图像
- 更多方法请参考 Qt 文档

## 常见问题

### 如何使用自定义图像？

MPixmap 默认会在 `dayu_widgets/static/` 目录下查找图像文件。如果你想使用自定义图像，可以通过以下方式：

1. 将图像文件放在 `dayu_widgets/static/` 目录下
2. 或者设置自定义路径：

```python
import dayu_widgets
dayu_widgets.CUSTOM_STATIC_FOLDERS.append("path/to/your/images")
```

### 如何更改 SVG 图像颜色？

MPixmap 支持在创建时指定 SVG 图像颜色：

```python
# 使用十六进制颜色代码
pixmap1 = MPixmap("success_line.svg", "#1890ff")

# 使用主题颜色
pixmap2 = MPixmap("success_line.svg", dayu_theme.primary_color)
```

### 支持哪些图像格式？

MPixmap 支持 SVG 和 PNG 格式的图像：

- SVG 格式：支持通过 `color` 参数更改颜色
- PNG 格式：不支持更改颜色，但支持透明度

### 如何在组件中使用图像？

许多 dayu_widgets 组件都支持设置图像：

```python
# 在 MAvatar 中使用
avatar = MAvatar()
avatar.set_dayu_image(MPixmap("avatar.png"))

# 在 MCard 中使用
card = MCard(title="Card Title", image=MPixmap("app-houdini.png"))

# 在 MMeta 中使用
meta = MMeta()
meta.setup_data({
    "title": "Houdini",
    "description": "Side Effects Software的旗舰级产品",
    "avatar": MPixmap("user_line.svg"),
    "cover": MPixmap("app-houdini.png"),
})
```
