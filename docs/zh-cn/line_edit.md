# MLineEdit 文本输入框

MLineEdit 是一个文本输入框组件，用于获取用户的文本输入。它基于 Qt 的 QLineEdit 类，提供了更美观的样式和更丰富的功能。

## 导入

```python
from dayu_widgets.line_edit import MLineEdit
```

## 代码示例

### 基本使用

MLineEdit 可以创建一个简单的文本输入框，用户可以输入文本。

```python
from dayu_widgets.line_edit import MLineEdit

# 创建一个空的文本输入框
line_edit = MLineEdit()

# 创建一个带有默认文本的文本输入框
line_edit_with_text = MLineEdit(text="默认文本")

# 设置占位符文本
line_edit.setPlaceholderText("请输入...")
```

### 不同尺寸

MLineEdit 支持不同的尺寸，可以通过方法链式调用设置。

```python
from dayu_widgets.line_edit import MLineEdit

# 创建大尺寸的文本输入框
line_edit_large = MLineEdit().large()
line_edit_large.setPlaceholderText("大尺寸")

# 创建中等尺寸的文本输入框（默认）
line_edit_medium = MLineEdit().medium()
line_edit_medium.setPlaceholderText("中等尺寸")

# 创建小尺寸的文本输入框
line_edit_small = MLineEdit().small()
line_edit_small.setPlaceholderText("小尺寸")
```

### 密码输入框

MLineEdit 可以设置为密码输入模式，输入的文本将显示为掩码字符。

```python
from dayu_widgets.line_edit import MLineEdit

# 创建密码输入框
password_edit = MLineEdit().password()
password_edit.setPlaceholderText("请输入密码")
```

### 前缀和后缀部件

MLineEdit 支持在输入框的前面和后面添加自定义部件。

```python
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.push_button import MPushButton
from dayu_widgets.label import MLabel
from qtpy import QtCore

# 创建带有前缀图标的文本输入框
line_edit_prefix = MLineEdit(text="带有前缀图标")
line_edit_prefix.set_prefix_widget(MToolButton().svg("user_line.svg").icon_only())

# 创建带有前缀标签的文本输入框
line_edit_label = MLineEdit(text="带有前缀标签")
label = MLabel(text="用户").mark().secondary()
label.setAlignment(QtCore.Qt.AlignCenter)
label.setFixedWidth(80)
line_edit_label.set_prefix_widget(label)

# 创建带有后缀按钮的文本输入框
line_edit_suffix = MLineEdit(text="带有后缀按钮")
button = MPushButton(text="确定").primary()
button.setFixedWidth(40)
line_edit_suffix.set_suffix_widget(button)
```

### 预设样式

MLineEdit 提供了多种预设样式，可以通过方法链式调用设置。

```python
from dayu_widgets.line_edit import MLineEdit

# 创建搜索框
search_edit = MLineEdit().search()
search_edit.setPlaceholderText("输入关键词搜索...")

# 创建带搜索按钮的搜索框
search_engine_edit = MLineEdit().search_engine("搜索")
search_engine_edit.setPlaceholderText("输入关键词搜索...")

# 创建文件选择框
file_edit = MLineEdit().file()
file_edit.setPlaceholderText("点击按钮浏览文件")

# 创建文件保存框
save_file_edit = MLineEdit().save_file()
save_file_edit.setPlaceholderText("点击按钮设置保存文件")

# 创建文件夹选择框
folder_edit = MLineEdit().folder()
folder_edit.setPlaceholderText("点击按钮浏览文件夹")

# 创建错误信息框
error_edit = MLineEdit(text="错误：文件 d:/ddd/ccc.jpg 不存在。").error()
```

### 延迟信号

MLineEdit 提供了一个延迟信号 `sig_delay_text_changed`，当用户停止输入一段时间后才会触发，避免频繁触发信号。

```python
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# 创建文本输入框和标签
line_edit = MLineEdit()
label = MLabel()

# 连接延迟信号
line_edit.sig_delay_text_changed.connect(label.setText)

# 设置延迟时间（毫秒）
line_edit.set_delay_duration(1000)  # 默认为 500 毫秒
```

### 完整示例

![MLineEdit 演示](../_media/screenshots/MLineEdit.png?v=1)

以下是一个完整的示例，展示了 MLineEdit 的各种用法：

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.menu import MMenu
from dayu_widgets.message import MMessage
from dayu_widgets.push_button import MPushButton
from dayu_widgets.tool_button import MToolButton


class LineEditExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LineEditExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLineEdit")
        self._init_ui()

    def _init_ui(self):
        size_lay = QtWidgets.QHBoxLayout()
        line_edit_l = MLineEdit().large()
        line_edit_l.setPlaceholderText("大尺寸")
        line_edit_m = MLineEdit().medium()
        line_edit_m.setPlaceholderText("默认尺寸")
        line_edit_s = MLineEdit().small()
        line_edit_s.setPlaceholderText("小尺寸")
        size_lay.addWidget(line_edit_l)
        size_lay.addWidget(line_edit_m)
        size_lay.addWidget(line_edit_s)

        line_edit_tool_button = MLineEdit(text="带工具按钮")
        line_edit_tool_button.set_prefix_widget(MToolButton().svg("user_line.svg").icon_only())

        line_edit_label = MLineEdit(text="带标签")
        tool_button = MLabel(text="用户").mark().secondary()
        tool_button.setAlignment(QtCore.Qt.AlignCenter)
        tool_button.setFixedWidth(80)
        line_edit_label.set_prefix_widget(tool_button)

        line_edit_push_button = MLineEdit(text="带按钮")
        push_button = MPushButton(text="确定").primary()
        push_button.setFixedWidth(60)
        line_edit_push_button.set_suffix_widget(push_button)

        search_engine_line_edit = MLineEdit().search_engine().large()
        search_engine_line_edit.returnPressed.connect(self.slot_search)

        line_edit_options = MLineEdit()
        combobox = MComboBox()
        option_menu = MMenu()
        option_menu.set_separator("|")
        option_menu.set_data([r"http://", r"https://"])
        combobox.set_menu(option_menu)
        combobox.set_value("http://")
        combobox.setFixedWidth(100)
        line_edit_options.set_prefix_widget(combobox)

        delay_line_editor = MLineEdit()
        delay_display_label = MLabel()
        delay_button = MPushButton("点击编辑文本")
        delay_line_editor.sig_delay_text_changed.connect(delay_display_label.setText)
        delay_button.clicked.connect(functools.partial(delay_line_editor.setText, "从代码中编辑"))

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("不同尺寸"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("自定义前缀和后缀部件"))
        main_lay.addWidget(line_edit_tool_button)
        main_lay.addWidget(line_edit_label)
        main_lay.addWidget(line_edit_push_button)
        main_lay.addWidget(MDivider("预设样式"))

        main_lay.addWidget(MLabel("错误"))
        main_lay.addWidget(MLineEdit(text="警告：文件 d:/ddd/ccc.jpg 不存在。").error())
        main_lay.addWidget(MLabel("搜索"))
        main_lay.addWidget(MLineEdit().search().small())
        main_lay.addWidget(MLabel("搜索引擎"))
        main_lay.addWidget(search_engine_line_edit)
        main_lay.addWidget(MLabel("文件"))
        main_lay.addWidget(MLineEdit().file().small())
        main_lay.addWidget(MLabel("文件夹"))
        main_lay.addWidget(MLineEdit().folder().small())
        main_lay.addWidget(MLabel("选项"))
        main_lay.addWidget(line_edit_options)
        main_lay.addWidget(MDivider("延迟信号测试"))
        main_lay.addWidget(delay_line_editor)
        main_lay.addWidget(delay_display_label)
        main_lay.addWidget(delay_button)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @QtCore.Slot()
    def slot_search(self):
        MMessage.info("查无此人", parent=self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = LineEditExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MLineEdit(text="", parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `text` | 输入框的初始文本 | `str` | `""` |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_dayu_size(value)` | 设置输入框的尺寸 | `value`: 尺寸值 | 无 |
| `get_dayu_size()` | 获取输入框的尺寸 | 无 | `int` |
| `set_delay_duration(millisecond)` | 设置延迟信号的触发时间 | `millisecond`: 毫秒数 | 无 |
| `get_prefix_widget()` | 获取前缀部件 | 无 | `QWidget` |
| `set_prefix_widget(widget)` | 设置前缀部件 | `widget`: 要设置的部件 | `QWidget` |
| `get_suffix_widget()` | 获取后缀部件 | 无 | `QWidget` |
| `set_suffix_widget(widget)` | 设置后缀部件 | `widget`: 要设置的部件 | `QWidget` |
| `setText(text)` | 设置文本并保存到历史记录 | `text`: 要设置的文本 | 无 |
| `clear()` | 清除文本和历史记录 | 无 | 无 |
| `search()` | 设置为搜索框样式 | 无 | `self` |
| `error()` | 设置为错误信息框样式 | 无 | `self` |
| `search_engine(text="Search")` | 设置为带搜索按钮的搜索框样式 | `text`: 按钮文本 | `self` |
| `file(filters=None)` | 设置为文件选择框样式 | `filters`: 文件过滤器列表 | `self` |
| `save_file(filters=None)` | 设置为文件保存框样式 | `filters`: 文件过滤器列表 | `self` |
| `folder()` | 设置为文件夹选择框样式 | 无 | `self` |
| `huge()` | 设置为超大尺寸 | 无 | `self` |
| `large()` | 设置为大尺寸 | 无 | `self` |
| `medium()` | 设置为中等尺寸 | 无 | `self` |
| `small()` | 设置为小尺寸 | 无 | `self` |
| `tiny()` | 设置为超小尺寸 | 无 | `self` |
| `password()` | 设置为密码输入模式 | 无 | `self` |

### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_delay_text_changed` | 当文本变化且经过延迟后触发 | `str`: 当前文本 |

### 继承的方法

MLineEdit 继承自 QLineEdit，因此可以使用 QLineEdit 的所有方法，例如：

- `text()`: 获取当前文本
- `setPlaceholderText(text)`: 设置占位符文本
- `setReadOnly(bool)`: 设置是否只读
- `setMaxLength(int)`: 设置最大长度
- `setAlignment(Qt.Alignment)`: 设置文本对齐方式
- 更多方法请参考 Qt 文档

## 常见问题

### 如何监听文本变化？

可以通过连接 `textChanged` 信号来监听文本变化：

```python
from dayu_widgets.line_edit import MLineEdit

# 创建文本输入框
line_edit = MLineEdit()

# 监听文本变化
line_edit.textChanged.connect(lambda text: print("文本变化:", text))
```

如果希望在用户停止输入一段时间后再触发，可以使用 `sig_delay_text_changed` 信号：

```python
from dayu_widgets.line_edit import MLineEdit

# 创建文本输入框
line_edit = MLineEdit()

# 监听延迟文本变化
line_edit.sig_delay_text_changed.connect(lambda text: print("延迟文本变化:", text))

# 设置延迟时间（毫秒）
line_edit.set_delay_duration(1000)  # 默认为 500 毫秒
```

### 如何设置文件选择框的文件过滤器？

可以通过 `file` 方法的 `filters` 参数设置文件过滤器：

```python
from dayu_widgets.line_edit import MLineEdit

# 创建文件选择框，只显示图片文件
line_edit = MLineEdit().file(filters=["Images (*.png *.jpg *.bmp)"])
```

### 如何在输入框前面添加下拉菜单？

可以通过 `set_prefix_widget` 方法添加下拉菜单：

```python
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建文本输入框
line_edit = MLineEdit()

# 创建下拉菜单
combobox = MComboBox()
option_menu = MMenu()
option_menu.set_data(["选项1", "选项2", "选项3"])
combobox.set_menu(option_menu)
combobox.setFixedWidth(100)

# 设置前缀部件
line_edit.set_prefix_widget(combobox)
```

### 如何创建带有搜索按钮的搜索框？

可以使用 `search_engine` 方法创建带有搜索按钮的搜索框：

```python
from dayu_widgets.line_edit import MLineEdit
from qtpy import QtCore

# 创建带搜索按钮的搜索框
search_edit = MLineEdit().search_engine("搜索")

# 监听回车键
search_edit.returnPressed.connect(lambda: print("搜索:", search_edit.text()))
```
