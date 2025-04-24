# 自定义主题

Dayu Widgets 提供了灵活的主题定制功能，允许您根据自己的需求自定义组件的外观。您可以更改主题色、切换明暗主题，以及调整其他主题相关的属性。

## 主题系统概述

Dayu Widgets 的主题系统基于 `MTheme` 类实现，它提供了以下功能：

1. **明暗主题切换**：支持 "light"（明亮）和 "dark"（暗黑）两种主题模式
2. **主题色自定义**：可以自定义主题的主色调
3. **主题属性访问**：提供了丰富的主题属性，如颜色、尺寸、字体等
4. **主题应用**：可以将主题应用到整个应用程序或特定组件

## 导入

```python
from dayu_widgets import dayu_theme
```

## 代码示例

### 基本使用

默认情况下，Dayu Widgets 使用橙色作为主题色，暗黑模式作为默认主题。您可以直接使用 `dayu_theme` 实例来应用主题：

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton

with application() as app:
    button = MPushButton("测试按钮")
    dayu_theme.apply(button)
    button.show()
```

### 切换主题模式

您可以通过 `set_theme` 方法切换明暗主题：

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton

# 切换到明亮主题
dayu_theme.set_theme("light")

with application() as app:
    button = MPushButton("明亮主题按钮")
    dayu_theme.apply(button)
    button.show()
```

### 自定义主题色

您可以通过 `set_primary_color` 方法自定义主题色：

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton
from dayu_widgets.theme import MTheme

# 设置主题色为蓝色
dayu_theme.set_primary_color(MTheme.blue)

with application() as app:
    button = MPushButton("蓝色主题按钮").primary()
    dayu_theme.apply(button)
    button.show()
```

### 创建新的主题实例

您也可以创建一个全新的主题实例，而不是使用默认的 `dayu_theme`：

```python
from dayu_widgets.theme import MTheme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton

# 创建一个明亮主题，使用绿色作为主题色
custom_theme = MTheme("light", primary_color=MTheme.green)

with application() as app:
    button = MPushButton("自定义主题按钮").primary()
    custom_theme.apply(button)
    button.show()
```

### 完整示例

![主题切换演示](../_media/screenshots/custom_theme.gif)

以下是一个完整的示例，展示了如何创建一个主题切换器：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.theme import MTheme


class ThemeSwitcherExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ThemeSwitcherExample, self).__init__(parent)
        self.setWindowTitle("主题切换示例")
        self._init_ui()

    def _init_ui(self):
        # 创建主题实例
        self.dark_theme = MTheme("dark", primary_color=MTheme.orange)
        self.light_theme = MTheme("light", primary_color=MTheme.blue)

        # 当前主题
        self.current_theme = self.dark_theme

        # 创建主题切换按钮
        theme_button_grp = MPushButtonGroup()
        theme_button_grp.set_button_list([
            {"text": "暗黑主题", "clicked": self.slot_use_dark_theme},
            {"text": "明亮主题", "clicked": self.slot_use_light_theme}
        ])

        # 创建颜色切换按钮
        color_button_grp = MPushButtonGroup()
        color_button_grp.set_button_list([
            {"text": "蓝色", "clicked": lambda: self.slot_change_color(MTheme.blue)},
            {"text": "绿色", "clicked": lambda: self.slot_change_color(MTheme.green)},
            {"text": "红色", "clicked": lambda: self.slot_change_color(MTheme.red)},
            {"text": "橙色", "clicked": lambda: self.slot_change_color(MTheme.orange)},
            {"text": "紫色", "clicked": lambda: self.slot_change_color(MTheme.purple)}
        ])

        # 创建示例组件
        self.sample_button = MPushButton("示例按钮").primary()

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("主题切换"))
        main_lay.addWidget(theme_button_grp)
        main_lay.addWidget(MDivider("主题色切换"))
        main_lay.addWidget(color_button_grp)
        main_lay.addWidget(MDivider("示例组件"))
        main_lay.addWidget(self.sample_button)
        main_lay.addStretch()
        self.setLayout(main_lay)

        # 应用初始主题
        self.current_theme.apply(self)

    def slot_use_dark_theme(self):
        self.current_theme = self.dark_theme
        self.current_theme.apply(self)

    def slot_use_light_theme(self):
        self.current_theme = self.light_theme
        self.current_theme.apply(self)

    def slot_change_color(self, color):
        self.current_theme.set_primary_color(color)
        self.current_theme.apply(self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = ThemeSwitcherExample()
        test.show()
```

## API

### MTheme 类

#### 构造函数

```python
MTheme(theme="light", primary_color=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `theme` | 主题模式，可选 "light" 或 "dark" | `str` | `"light"` |
| `primary_color` | 主题色，如果为 None，则使用蓝色 | `str` | `None` |

#### 预定义颜色常量

MTheme 类提供了多种预定义的颜色常量，可以用作主题色：

| 常量 | 描述 | 值 |
| --- | --- | --- |
| `blue` | 蓝色 | `"#1890ff"` |
| `purple` | 紫色 | `"#722ed1"` |
| `cyan` | 青色 | `"#13c2c2"` |
| `green` | 绿色 | `"#52c41a"` |
| `magenta` | 洋红色 | `"#eb2f96"` |
| `pink` | 粉色 | `"#ef5b97"` |
| `red` | 红色 | `"#f5222d"` |
| `orange` | 橙色 | `"#fa8c16"` |
| `yellow` | 黄色 | `"#fadb14"` |
| `volcano` | 火山色 | `"#fa541c"` |
| `geekblue` | 极客蓝 | `"#2f54eb"` |
| `lime` | 酸橙色 | `"#a0d911"` |
| `gold` | 金色 | `"#faad14"` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_theme(theme)` | 设置主题模式 | `theme`: "light" 或 "dark" | 无 |
| `set_primary_color(color)` | 设置主题色 | `color`: 颜色值，如 "#1890ff" | 无 |
| `apply(widget)` | 将主题应用到组件 | `widget`: 要应用主题的组件 | 无 |
| `deco(cls)` | 装饰器，将主题应用到类 | `cls`: 要装饰的类 | 装饰后的类 |

#### 主题属性

MTheme 实例提供了丰富的主题属性，可以在自定义样式时使用：

##### 颜色属性

| 属性 | 描述 |
| --- | --- |
| `primary_color` | 主题色 |
| `primary_1` 到 `primary_10` | 主题色的不同深浅变体 |
| `info_color` | 信息色 |
| `success_color` | 成功色 |
| `warning_color` | 警告色 |
| `error_color` | 错误色 |
| `title_color` | 标题文本颜色 |
| `primary_text_color` | 主要文本颜色 |
| `secondary_text_color` | 次要文本颜色 |
| `disable_color` | 禁用状态颜色 |
| `border_color` | 边框颜色 |
| `divider_color` | 分割线颜色 |
| `background_color` | 背景颜色 |
| `background_selected_color` | 选中状态背景颜色 |
| `item_hover_bg` | 悬停状态背景颜色 |

##### 尺寸属性

| 属性 | 描述 |
| --- | --- |
| `huge` | 超大尺寸 |
| `large` | 大尺寸 |
| `medium` | 中等尺寸 |
| `small` | 小尺寸 |
| `tiny` | 超小尺寸 |
| `huge_icon` | 超大图标尺寸 |
| `large_icon` | 大图标尺寸 |
| `medium_icon` | 中等图标尺寸 |
| `small_icon` | 小图标尺寸 |
| `tiny_icon` | 超小图标尺寸 |

##### 字体属性

| 属性 | 描述 |
| --- | --- |
| `font_family` | 字体族 |
| `font_size_base` | 基础字体大小 |
| `font_size_large` | 大字体大小 |
| `font_size_small` | 小字体大小 |
| `h1_size` | 一级标题大小 |
| `h2_size` | 二级标题大小 |
| `h3_size` | 三级标题大小 |
| `h4_size` | 四级标题大小 |

## 常见问题

### 如何在整个应用程序中应用主题？

要在整个应用程序中应用主题，可以在创建应用程序后，显示主窗口前应用主题：

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from my_app import MyMainWindow

with application() as app:
    main_window = MyMainWindow()
    dayu_theme.apply(main_window)
    main_window.show()
```

### 如何在运行时切换主题？

要在运行时切换主题，可以调用 `set_theme` 方法，然后重新应用主题：

```python
def switch_to_dark_theme(self):
    dayu_theme.set_theme("dark")
    dayu_theme.apply(self)

def switch_to_light_theme(self):
    dayu_theme.set_theme("light")
    dayu_theme.apply(self)
```

### 如何使用自定义颜色作为主题色？

除了使用预定义的颜色常量外，您还可以使用任何有效的颜色值作为主题色：

```python
# 使用十六进制颜色值
dayu_theme.set_primary_color("#FF5733")

# 或者使用 RGB 颜色值
dayu_theme.set_primary_color("rgb(255, 87, 51)")
```

### 如何同时使用多个主题？

如果您需要在应用程序的不同部分使用不同的主题，可以创建多个 MTheme 实例：

```python
from dayu_widgets.theme import MTheme

# 创建两个不同的主题
dark_theme = MTheme("dark", primary_color=MTheme.blue)
light_theme = MTheme("light", primary_color=MTheme.green)

# 将不同的主题应用到不同的组件
dark_theme.apply(widget1)
light_theme.apply(widget2)
```
