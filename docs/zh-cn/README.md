# dayu_widgets3

一个现代化的 [PySide](https://wiki.qt.io/PySide) 组件库，提供丰富的 UI 组件和主题支持。

## 特性

* 支持 Python 3.7 到 3.12
* 同时兼容 PySide2 和 PySide6
* 提供亮色和暗色两种主题，可自定义主题颜色
* 丰富的组件库，包括按钮、表单、导航、数据展示等
* 完善的文档和示例

## 设计参考

主要参考了 [AntDesign](https://ant.design/) 组件库，其他参考了 [iView](https://www.iviewui.com/) 组件库和微信基础组件。

## 主题

提供**亮色(light)** 和 **暗色(dark)** 两种主题，每种主题可以设置主题颜色。
文档中的截图使用以下颜色：

* 亮色主题：#1890ff
* 暗色主题：#fa8c16

## 安装

### 使用 pip 安装

```shell
# 安装带 PySide6 的版本
pip install "dayu_widgets3[pyside6]"

# 安装带 PySide2 的版本
pip install "dayu_widgets3[pyside2]"
```

### 使用 uv 安装（推荐）

```shell
# 安装 uv（Linux/macOS）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装 uv（Windows PowerShell）
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 安装带 PySide6 的版本
uv pip install "dayu_widgets3[pyside6]"

# 安装带 PySide2 的版本
uv pip install "dayu_widgets3[pyside2]"
```

## 快速开始

```python
import dayu_widgets3
from dayu_widgets3.qt import QApplication
from dayu_widgets3 import dayu_theme
from dayu_widgets3.push_button import MPushButton

# 创建应用
app = QApplication([])

# 应用主题
dayu_theme.apply(style='light')  # 或 'dark'

# 创建一个按钮
button = MPushButton('你好，世界')
button.primary()
button.show()

# 运行应用
app.exec_()
```
