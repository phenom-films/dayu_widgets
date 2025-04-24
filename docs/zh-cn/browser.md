# Upload 上传

Upload 组件提供了多种文件和文件夹上传方式，包括点击选择和拖拽上传。它基于 Qt 的文件对话框和拖放功能，提供了更美观的样式和更好的交互体验。

## 导入

```python
from dayu_widgets.browser import MClickBrowserFilePushButton
from dayu_widgets.browser import MClickBrowserFileToolButton
from dayu_widgets.browser import MClickBrowserFolderPushButton
from dayu_widgets.browser import MClickBrowserFolderToolButton
from dayu_widgets.browser import MDragFileButton
from dayu_widgets.browser import MDragFolderButton
```

## 代码示例

### 点击选择文件

MClickBrowserFilePushButton 和 MClickBrowserFileToolButton 提供了点击选择文件的功能。

```python
from dayu_widgets.browser import MClickBrowserFilePushButton
from dayu_widgets.browser import MClickBrowserFileToolButton
from dayu_widgets.label import MLabel

# 创建一个文件选择按钮
file_button = MClickBrowserFilePushButton(text="选择文件")

# 创建一个显示选择文件路径的标签
file_label = MLabel()
file_button.sig_file_changed.connect(file_label.setText)

# 创建一个文件选择工具按钮
file_tool_button = MClickBrowserFileToolButton()
file_tool_button.sig_file_changed.connect(file_label.setText)
```

### 点击选择文件夹

MClickBrowserFolderPushButton 和 MClickBrowserFolderToolButton 提供了点击选择文件夹的功能。

```python
from dayu_widgets.browser import MClickBrowserFolderPushButton
from dayu_widgets.browser import MClickBrowserFolderToolButton
from dayu_widgets.label import MLabel

# 创建一个文件夹选择按钮
folder_button = MClickBrowserFolderPushButton(text="选择文件夹")

# 创建一个显示选择文件夹路径的标签
folder_label = MLabel()
folder_button.sig_folder_changed.connect(folder_label.setText)

# 创建一个文件夹选择工具按钮
folder_tool_button = MClickBrowserFolderToolButton()
folder_tool_button.sig_folder_changed.connect(folder_label.setText)
```

### 多选文件

MClickBrowserFilePushButton 和 MClickBrowserFileToolButton 支持多选文件。

```python
from dayu_widgets.browser import MClickBrowserFilePushButton
from dayu_widgets.label import MLabel

# 创建一个多选文件按钮
multi_file_button = MClickBrowserFilePushButton(text="选择多个文件", multiple=True)

# 创建一个显示选择文件数量的标签
file_count_label = MLabel()
multi_file_button.sig_files_changed.connect(lambda files: file_count_label.setText("已选择 {} 个文件".format(len(files))))
```

### 拖拽上传文件

MDragFileButton 提供了拖拽上传文件的功能。

```python
from dayu_widgets.browser import MDragFileButton
from dayu_widgets.label import MLabel

# 创建一个拖拽文件按钮
drag_file_button = MDragFileButton(text="点击或拖拽文件到此处")

# 创建一个显示选择文件路径的标签
file_label = MLabel()
drag_file_button.sig_file_changed.connect(file_label.setText)
```

### 拖拽上传文件夹

MDragFolderButton 提供了拖拽上传文件夹的功能。

```python
from dayu_widgets.browser import MDragFolderButton
from dayu_widgets.label import MLabel

# 创建一个拖拽文件夹按钮
drag_folder_button = MDragFolderButton()

# 创建一个显示选择文件夹路径的标签
folder_label = MLabel()
drag_folder_button.sig_folder_changed.connect(folder_label.setText)
```

### 设置文件过滤器

MClickBrowserFilePushButton、MClickBrowserFileToolButton 和 MDragFileButton 支持设置文件过滤器。

```python
from dayu_widgets.browser import MClickBrowserFilePushButton
from dayu_widgets.browser import MDragFileButton

# 创建一个只选择图片文件的按钮
image_button = MClickBrowserFilePushButton(text="选择图片")
image_button.set_dayu_filters([".jpg", ".png", ".gif"])

# 创建一个只接受视频文件的拖拽按钮
video_button = MDragFileButton(text="点击或拖拽视频文件到此处")
video_button.set_dayu_svg("media_line.svg")
video_button.set_dayu_filters([".mov", ".mp4", ".avi"])
```

### 自定义图标

MDragFileButton 和 MDragFolderButton 支持自定义图标。

```python
from dayu_widgets.browser import MDragFileButton
from dayu_widgets.browser import MDragFolderButton

# 创建一个自定义图标的拖拽文件按钮
custom_file_button = MDragFileButton(text="点击或拖拽文件到此处")
custom_file_button.set_dayu_svg("attachment_line.svg")

# 创建一个自定义图标的拖拽文件夹按钮
custom_folder_button = MDragFolderButton()
custom_folder_button.set_dayu_svg("folder_fill.svg")
```

### 数据绑定

Upload 组件可以与 MFieldMixin 结合使用，实现数据绑定。

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.browser import MDragFileButton
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel


class UploadBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(UploadBindExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 创建拖拽文件按钮
        file_button = MDragFileButton(text="点击或拖拽文件到此处")
        file_button.set_dayu_svg("media_line.svg")
        file_button.set_dayu_filters([".mov", ".mp4"])

        # 创建标签
        file_label = MLabel()
        file_label.set_elide_mode(QtCore.Qt.ElideRight)

        # 注册字段和绑定
        self.register_field("current_file", "")
        self.bind("current_file", file_button, "dayu_path", signal="sig_file_changed")
        self.bind("current_file", file_label, "text")

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(file_button)
        main_lay.addWidget(file_label)
        self.setLayout(main_lay)
```

### 完整示例

![Upload 演示](../_media/screenshots/Upload.png)

以下是一个完整的示例，展示了 Upload 组件的各种用法：

```python
# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.browser import MClickBrowserFilePushButton
from dayu_widgets.browser import MClickBrowserFileToolButton
from dayu_widgets.browser import MClickBrowserFolderPushButton
from dayu_widgets.browser import MClickBrowserFolderToolButton
from dayu_widgets.browser import MDragFileButton
from dayu_widgets.browser import MDragFolderButton
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.qt import MIcon


class BrowserExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(BrowserExample, self).__init__(parent)
        self.setWindowTitle("Examples for Browser")
        self._init_ui()

    def _init_ui(self):
        browser_1 = MClickBrowserFilePushButton(text="选择文件").primary()
        browser_2 = MClickBrowserFolderPushButton(text="选择文件夹")
        browser_2.setIcon(MIcon("upload_line.svg"))
        browser_3 = MClickBrowserFilePushButton(text="选择多个文件", multiple=True).primary()
        lay_1 = QtWidgets.QHBoxLayout()
        lay_1.addWidget(browser_1)
        lay_1.addWidget(browser_2)
        lay_1.addWidget(browser_3)

        browser_4 = MClickBrowserFileToolButton().huge()
        label_4 = MLabel()
        label_4.set_elide_mode(QtCore.Qt.ElideMiddle)
        browser_4.sig_file_changed.connect(label_4.setText)

        browser_5 = MClickBrowserFolderToolButton().huge()
        label_5 = MLabel()
        label_5.set_elide_mode(QtCore.Qt.ElideMiddle)
        browser_5.sig_folder_changed.connect(label_5.setText)

        lay_2 = QtWidgets.QHBoxLayout()
        lay_2.addWidget(label_4)
        lay_2.addWidget(browser_4)
        lay_2.addWidget(label_5)
        lay_2.addWidget(browser_5)

        browser_6 = MDragFileButton(text="点击或拖拽文件到此处")
        browser_6.set_dayu_svg("attachment_line.svg")
        label_6 = MLabel()
        label_6.set_elide_mode(QtCore.Qt.ElideMiddle)
        browser_6.sig_file_changed.connect(label_6.setText)

        browser_7 = MDragFolderButton()
        label_7 = MLabel()
        label_7.set_elide_mode(QtCore.Qt.ElideRight)
        browser_7.sig_folder_changed.connect(label_7.setText)

        lay_3 = QtWidgets.QGridLayout()
        lay_3.addWidget(browser_6, 2, 0)
        lay_3.addWidget(browser_7, 2, 1)
        lay_3.addWidget(label_6, 3, 0)
        lay_3.addWidget(label_7, 3, 1)

        browser_8 = MDragFileButton(text="点击或拖拽媒体文件到此处", multiple=False)
        browser_8.set_dayu_svg("media_line.svg")
        browser_8.set_dayu_filters([".mov", ".mp4"])
        browser_8_label = MLabel()
        browser_8_label.set_elide_mode(QtCore.Qt.ElideRight)
        self.register_field("current_file", "")
        self.bind("current_file", browser_8, "dayu_path", signal="sig_file_changed")
        self.bind("current_file", browser_8_label, "text")

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("MClickBrowser*PushButton"))
        main_lay.addLayout(lay_1)
        main_lay.addWidget(MDivider("MClickBrowser*ToolButton"))
        main_lay.addLayout(lay_2)
        main_lay.addWidget(MDivider("MDragBrowser*ToolButton"))
        main_lay.addLayout(lay_3)
        main_lay.addWidget(MDivider("数据绑定"))
        main_lay.addWidget(browser_8)
        main_lay.addWidget(browser_8_label)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = BrowserExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### MClickBrowserFilePushButton

#### 构造函数

```python
MClickBrowserFilePushButton(text="Browser", multiple=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `text` | 按钮文本 | `str` | `"Browser"` |
| `multiple` | 是否支持多选文件 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `get_dayu_filters()` | 获取文件过滤器 | 无 | `list` |
| `set_dayu_filters(value)` | 设置文件过滤器 | `value`: 文件扩展名列表 | 无 |
| `get_dayu_path()` | 获取当前路径 | 无 | `str` |
| `set_dayu_path(value)` | 设置当前路径 | `value`: 路径字符串 | 无 |

#### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_file_changed` | 当选择单个文件时触发 | `str`: 文件路径 |
| `sig_files_changed` | 当选择多个文件时触发 | `list`: 文件路径列表 |

### MClickBrowserFileToolButton

#### 构造函数

```python
MClickBrowserFileToolButton(multiple=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `multiple` | 是否支持多选文件 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

与 MClickBrowserFilePushButton 相同。

#### 信号

与 MClickBrowserFilePushButton 相同。

### MClickBrowserFolderPushButton

#### 构造函数

```python
MClickBrowserFolderPushButton(text="Browser", multiple=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `text` | 按钮文本 | `str` | `"Browser"` |
| `multiple` | 是否支持多选文件夹 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `get_dayu_path()` | 获取当前路径 | 无 | `str` |
| `set_dayu_path(value)` | 设置当前路径 | `value`: 路径字符串 | 无 |

#### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_folder_changed` | 当选择单个文件夹时触发 | `str`: 文件夹路径 |
| `sig_folders_changed` | 当选择多个文件夹时触发 | `list`: 文件夹路径列表 |

### MClickBrowserFolderToolButton

#### 构造函数

```python
MClickBrowserFolderToolButton(multiple=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `multiple` | 是否支持多选文件夹 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

与 MClickBrowserFolderPushButton 相同。

#### 信号

与 MClickBrowserFolderPushButton 相同。

### MDragFileButton

#### 构造函数

```python
MDragFileButton(text="", multiple=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `text` | 按钮文本 | `str` | `""` |
| `multiple` | 是否支持多选文件 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `get_dayu_filters()` | 获取文件过滤器 | 无 | `list` |
| `set_dayu_filters(value)` | 设置文件过滤器 | `value`: 文件扩展名列表 | 无 |
| `get_dayu_path()` | 获取当前路径 | 无 | `str` |
| `set_dayu_path(value)` | 设置当前路径 | `value`: 路径字符串 | 无 |
| `get_dayu_multiple()` | 获取是否支持多选 | 无 | `bool` |
| `set_dayu_multiple(value)` | 设置是否支持多选 | `value`: 布尔值 | 无 |
| `set_dayu_svg(path)` | 设置 SVG 图标 | `path`: SVG 文件名 | 无 |

#### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_file_changed` | 当选择单个文件时触发 | `str`: 文件路径 |
| `sig_files_changed` | 当选择多个文件时触发 | `list`: 文件路径列表 |

### MDragFolderButton

#### 构造函数

```python
MDragFolderButton(multiple=False, parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `multiple` | 是否支持多选文件夹 | `bool` | `False` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `get_dayu_path()` | 获取当前路径 | 无 | `str` |
| `set_dayu_path(value)` | 设置当前路径 | `value`: 路径字符串 | 无 |
| `get_dayu_multiple()` | 获取是否支持多选 | 无 | `bool` |
| `set_dayu_multiple(value)` | 设置是否支持多选 | `value`: 布尔值 | 无 |
| `set_dayu_svg(path)` | 设置 SVG 图标 | `path`: SVG 文件名 | 无 |

#### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_folder_changed` | 当选择单个文件夹时触发 | `str`: 文件夹路径 |
| `sig_folders_changed` | 当选择多个文件夹时触发 | `list`: 文件夹路径列表 |

## 常见问题

### 如何限制可选择的文件类型？

可以通过 `set_dayu_filters` 方法设置文件过滤器：

```python
from dayu_widgets.browser import MClickBrowserFilePushButton

# 创建一个只选择图片文件的按钮
image_button = MClickBrowserFilePushButton(text="选择图片")
image_button.set_dayu_filters([".jpg", ".png", ".gif"])
```

### 如何获取选择的文件路径？

可以通过连接 `sig_file_changed` 或 `sig_files_changed` 信号来获取选择的文件路径：

```python
from dayu_widgets.browser import MClickBrowserFilePushButton
from dayu_widgets.label import MLabel

# 创建一个文件选择按钮
file_button = MClickBrowserFilePushButton(text="选择文件")

# 创建一个显示选择文件路径的标签
file_label = MLabel()
file_button.sig_file_changed.connect(file_label.setText)
```

### 如何自定义拖拽按钮的图标？

可以通过 `set_dayu_svg` 方法设置拖拽按钮的图标：

```python
from dayu_widgets.browser import MDragFileButton

# 创建一个自定义图标的拖拽文件按钮
custom_file_button = MDragFileButton(text="点击或拖拽文件到此处")
custom_file_button.set_dayu_svg("attachment_line.svg")
```

### 如何在 MLineEdit 中添加文件选择按钮？

可以使用 MLineEdit 的 `file` 方法添加文件选择按钮：

```python
from dayu_widgets.line_edit import MLineEdit

# 创建一个带文件选择按钮的输入框
file_input = MLineEdit().file()

# 创建一个带文件选择按钮的输入框，并限制文件类型
image_input = MLineEdit().file(filters=[".jpg", ".png", ".gif"])
```
