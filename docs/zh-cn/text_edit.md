# MTextEdit 文本编辑框

MTextEdit 是一个多行文本编辑框组件，用于输入和编辑多行文本。它基于 Qt 的 QTextEdit 类，提供了更美观的样式和更好的交互体验。

## 导入

```python
from dayu_widgets.text_edit import MTextEdit
```

## 代码示例

### 基本使用

MTextEdit 可以创建一个简单的多行文本编辑框，用户可以输入和编辑多行文本。

```python
from dayu_widgets.text_edit import MTextEdit
from qtpy import QtWidgets

# 创建一个多行文本编辑框
text_edit = MTextEdit()

# 创建一个带有默认文本的多行文本编辑框
text_edit_with_text = MTextEdit()
text_edit_with_text.setText("这是一段默认文本。\n可以包含多行内容。")

# 将文本编辑框添加到布局中
layout = QtWidgets.QVBoxLayout()
layout.addWidget(text_edit)
```

### 可调整大小

MTextEdit 支持在右下角添加一个大小调整手柄，用户可以通过拖动来调整文本编辑框的大小。

```python
from dayu_widgets.text_edit import MTextEdit

# 创建一个可调整大小的多行文本编辑框
text_edit = MTextEdit().resizeable()
```

### 自动调整大小

MTextEdit 支持根据内容自动调整大小（注意：此功能尚未完全实现）。

```python
from dayu_widgets.text_edit import MTextEdit

# 创建一个自动调整大小的多行文本编辑框
text_edit = MTextEdit().autosize()
```

### 完整示例

![MTextEdit 演示](../_media/screenshots/MTextEdit.png)

以下是一个完整的示例，展示了 MTextEdit 的各种用法：

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.push_button import MPushButton
from dayu_widgets.text_edit import MTextEdit


class TextEditExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TextEditExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        main_lay = QtWidgets.QVBoxLayout()

        main_lay.addWidget(MDivider("标准文本编辑框"))
        main_lay.addWidget(MTextEdit(self))
        main_lay.addWidget(MDivider("可调整大小的文本编辑框"))
        main_lay.addWidget(MTextEdit(self).resizeable())
        main_lay.addWidget(MPushButton("提交").primary())

        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = TextEditExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MTextEdit(parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `resizeable()` | 在右下角添加大小调整手柄 | 无 | `self` |
| `autosize()` | 根据内容自动调整大小（尚未完全实现） | 无 | `self` |

### 继承的方法

MTextEdit 继承自 QTextEdit，因此可以使用 QTextEdit 的所有方法，例如：

- `setText(text)`: 设置文本内容
- `text()`: 获取文本内容
- `setPlainText(text)`: 设置纯文本内容
- `toPlainText()`: 获取纯文本内容
- `setHtml(html)`: 设置 HTML 内容
- `toHtml()`: 获取 HTML 内容
- `setReadOnly(bool)`: 设置是否只读
- `isReadOnly()`: 获取是否只读
- `clear()`: 清空内容
- 更多方法请参考 Qt 文档

### 信号

MTextEdit 继承自 QTextEdit，因此可以使用 QTextEdit 的所有信号，例如：

- `textChanged()`: 当文本内容变化时触发
- `selectionChanged()`: 当选择区域变化时触发
- `copyAvailable(bool)`: 当复制操作可用时触发
- 更多信号请参考 Qt 文档

## 常见问题

### 如何监听文本变化？

可以通过连接 `textChanged` 信号来监听文本变化：

```python
from dayu_widgets.text_edit import MTextEdit

# 创建多行文本编辑框
text_edit = MTextEdit()

# 监听文本变化
text_edit.textChanged.connect(lambda: print("文本已变化:", text_edit.toPlainText()))
```

### 如何设置只读模式？

可以通过 `setReadOnly` 方法设置文本编辑框为只读模式：

```python
from dayu_widgets.text_edit import MTextEdit

# 创建多行文本编辑框
text_edit = MTextEdit()
text_edit.setText("这是一段只读文本，用户无法编辑。")

# 设置为只读模式
text_edit.setReadOnly(True)
```

### 如何设置占位符文本？

可以通过 `setPlaceholderText` 方法设置占位符文本：

```python
from dayu_widgets.text_edit import MTextEdit

# 创建多行文本编辑框
text_edit = MTextEdit()

# 设置占位符文本
text_edit.setPlaceholderText("请在此输入多行文本...")
```

### 如何限制文本编辑框的最大高度？

可以通过 `setMaximumHeight` 方法限制文本编辑框的最大高度：

```python
from dayu_widgets.text_edit import MTextEdit

# 创建多行文本编辑框
text_edit = MTextEdit()

# 限制最大高度为 200 像素
text_edit.setMaximumHeight(200)
```

### 如何在文本编辑框中使用语法高亮？

可以使用 QSyntaxHighlighter 类为 MTextEdit 添加语法高亮功能：

```python
from dayu_widgets.text_edit import MTextEdit
from qtpy import QtCore, QtGui

# 创建一个简单的语法高亮器
class SimpleHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(SimpleHighlighter, self).__init__(parent)
        self.keyword_format = QtGui.QTextCharFormat()
        self.keyword_format.setForeground(QtCore.Qt.blue)
        self.keyword_format.setFontWeight(QtGui.QFont.Bold)
        self.keywords = ["import", "from", "def", "class", "if", "else", "for", "while"]

    def highlightBlock(self, text):
        for word in text.split():
            if word in self.keywords:
                self.setFormat(text.indexOf(word), len(word), self.keyword_format)

# 创建多行文本编辑框
text_edit = MTextEdit()
text_edit.setText("import os\n\ndef hello():\n    print('Hello, World!')")

# 应用语法高亮
highlighter = SimpleHighlighter(text_edit.document())
```
