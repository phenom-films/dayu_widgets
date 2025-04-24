# [施工中....请勿使用]

# dayu_widgets3

这是一个 PySide 组件库。

* Python: >=3.7, <=3.12
* PySide2/PySide6

使用`qtpy` 来做兼容，支持 `PySide2` 和 `PySide6`，至于 `PyQt4`、`PyQt5`，可自行测试。

主要参考了 [AntDesign](https://ant.design/) 组件库，其他参考了 [iView](https://www.iviewui.com/) 组件库，微信基础组件。

更多在此基础上的组件插件：

* [dayu_widgets_tag](https://github.com/muyr/dayu_widgets_tag):  [中文](https://muyr.github.io/dayu_widgets_tag/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_tag/#/)
* [dayu_widgets_log](https://github.com/muyr/dayu_widgets_log):  [中文](https://muyr.github.io/dayu_widgets_log/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_log/#/)
* [dayu_widgets_overlay](https://github.com/FXTD-ODYSSEY/dayu_widgets_overlay)


## 如何贡献代码

### 使用 poetry 安装
```shell
pip install poetry
```

### 使用 poetry 安装依赖
```shell
poetry install
```

### 使用 uv 安装
```shell
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装依赖
uv pip install -e ".[pyside6]"  # 使用 PySide6
# 或者
uv pip install -e ".[pyside2]"  # 使用 PySide2
```

注意，依赖里并未强制要求安装任何 Qt 的python 绑定库，可根据自己的需要，选择手动安装 PySide2、PySide6、PyQt4、PyQt5。

### 运行单元测试
```shell
# 使用 poetry
poetry run pytest

# 使用 uv
uv run pytest
```

### 运行 black检查
```shell
# 使用 poetry
poetry run black dayu_widgets3

# 使用 uv
uv run black dayu_widgets3
```

### 运行isort
```shell
# 使用 poetry
poetry run isort dayu_widgets3

# 使用 uv
uv run isort dayu_widgets3
```

### 提交代码
```shell
# 使用 poetry
poetry run cz commit

# 使用 uv
uv run cz commit
```
