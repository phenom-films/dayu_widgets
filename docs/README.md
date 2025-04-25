# dayu_widgets

[PySide](https://wiki.qt.io/PySide) UI library `dayu_widgets`

reference of [AntDesign](https://ant.design/) UI library, [iView](https://www.iviewui.com/) and wechat


We provide **light** 和 **dark** themes. You can custom the primary color
The screenshots in docs used:

* Light: #1890ff
* Dark: #fa8c16


## Installation

```shell
pip install dayu_widgets
```

## Run Demo

After installation, you can run the demo application with the following commands. Note that running the demo requires a Qt environment (like PySide2 or PyQt5):

```shell
# Run as a Python module (requires PySide2 or PyQt5 to be installed)
python -m dayu_widgets

# Or use the uvx command line tool (recommended, handles dependencies automatically)
uvx --python 3.10 --with pyside2 dayu_widgets
```

> **Note**: dayu_widgets is a Qt UI library, so running the demo requires a Qt environment. When using the `uvx` command, you can automatically handle Qt dependencies with the `--with pyside2` parameter.

## Usage

```python
import dayu_widgets
```
