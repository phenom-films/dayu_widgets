# dayu_widgets3

A modern UI component library for [PySide](https://wiki.qt.io/PySide) with rich features and theme support.

## Features

* Support for Python 3.7 to 3.12
* Compatible with both PySide2 and PySide6
* Light and dark themes with customizable primary colors
* Rich component library including buttons, forms, navigation, data display, and more
* Comprehensive documentation and examples

## Design Reference

Inspired by [AntDesign](https://ant.design/) UI library, with additional references from [iView](https://www.iviewui.com/) and WeChat components.

## Themes

We provide **light** and **dark** themes. You can customize the primary color.
The screenshots in the documentation use:

* Light theme: #1890ff
* Dark theme: #fa8c16

## Installation

### Using pip

```shell
# Install with PySide6
pip install "dayu_widgets3[pyside6]"

# Install with PySide2
pip install "dayu_widgets3[pyside2]"
```

### Using uv (Recommended)

```shell
# Install uv (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install uv (Windows PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install with PySide6
uv pip install "dayu_widgets3[pyside6]"

# Install with PySide2
uv pip install "dayu_widgets3[pyside2]"
```

## Quick Start

```python
import dayu_widgets3
from dayu_widgets3.qt import QApplication
from dayu_widgets3 import dayu_theme
from dayu_widgets3.push_button import MPushButton

# Create application
app = QApplication([])

# Apply theme
dayu_theme.apply(style='light')  # or 'dark'

# Create a button
button = MPushButton('Hello World')
button.primary()
button.show()

# Run application
app.exec_()
```
