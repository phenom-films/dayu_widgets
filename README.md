# dayu_widgets3

这是一个 PySide 组件库。

* Python: >=3.6, <3.11
* PySide2/PySide6

使用`qtpy` 来做兼容，支持 `PySide2` 和 `PySide6`，至于 `PyQt4`、`PyQt5`，可自行测试。

主要参考了 [AntDesign](https://ant.design/) 组件库，其他参考了 [iView](https://www.iviewui.com/) 组件库，微信基础组件。

更多在此基础上的组件插件：

* [dayu_widgets_tag](https://github.com/muyr/dayu_widgets_tag):  [中文](https://muyr.github.io/dayu_widgets_tag/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_tag/#/)
* [dayu_widgets_log](https://github.com/muyr/dayu_widgets_log):  [中文](https://muyr.github.io/dayu_widgets_log/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_log/#/)
* [dayu_widgets_overlay](https://github.com/FXTD-ODYSSEY/dayu_widgets_overlay)


## 如何贡献代码

### 安装poetry
``shell
pip install poetry
``

### 安装依赖
```shell
poetry install
```
注意，依赖里并未强制要求安装任何 Qt 的python 绑定库，可根据自己的需要，选择手动安装 PySide2、PySide6、PyQt4、PyQt5。

### 运行单元测试
```shell
poetry run pytest
```

### 运行 black检查
```shell
poetry run black dayu_widgets3
```

### 运行isort
```shell
poetry run isort dayu_widgets3
```

### 提交代码
```shell
poetry run cz commit
```
