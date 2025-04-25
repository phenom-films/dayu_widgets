# dayu_widgets

一个 [PySide](https://wiki.qt.io/PySide) 的组件库

主要参考了 [AntDesign](https://ant.design/) 组件库，其他参考了 [iView](https://www.iviewui.com/) 组件库，微信基础组件。


提供**亮色(light)** 和 **暗色(dark)** 两种主题，每种主题可以设置主题颜色。
以下截图以：

* 亮色 #1890ff
* 暗色 #fa8c16


## 安装

```shell
pip install dayu_widgets
```

## 运行示例程序

安装后，可以通过以下命令直接运行示例程序。注意，运行示例程序需要 Qt 环境（如 PySide2 或 PyQt5）：

```shell
# 使用 Python 模块方式运行（需要先安装 PySide2 或 PyQt5）
python -m dayu_widgets

# 使用 uvx 命令行工具运行（推荐方式，自动处理依赖）
uvx --python 3.10 --with pyside2 dayu_widgets
```

> **注意**：dayu_widgets 是一个 Qt 界面库，运行示例程序需要 Qt 环境。使用 `uvx` 命令时可以通过 `--with pyside2` 参数自动处理 Qt 依赖。

## 使用

```python
import dayu_widgets
```
