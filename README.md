# dayu_widgets3

这是一个现代化的 PySide 组件库，提供丰富的 UI 组件和主题支持。

## 特性

* 支持 Python 3.7 到 3.12
* 同时支持 PySide2 和 PySide6
* 提供亮色和暗色两种主题，可自定义主题颜色
* 丰富的组件库，包括按钮、表单、导航、数据展示等
* 完善的文档和示例

## 兼容性

使用 `qtpy` 实现跨 Qt 绑定兼容，主要支持：
* PySide2 (Python 3.7-3.10)
* PySide6 (Python 3.7-3.12)

其他 Qt 绑定如 PyQt4、PyQt5 可自行测试。

## 设计参考

主要参考了 [AntDesign](https://ant.design/) 组件库，其他参考了 [iView](https://www.iviewui.com/) 组件库和微信基础组件。

## 文档

* [中文文档](https://xiaonuoandy.github.io/dayu_widgets3/#/zh-cn/)
* [English Documentation](https://xiaonuoandy.github.io/dayu_widgets3/#/en-us/)

## 扩展组件

以下是基于 dayu_widgets 的扩展组件库：

* [dayu_widgets_tag](https://github.com/muyr/dayu_widgets_tag): [中文](https://muyr.github.io/dayu_widgets_tag/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_tag/#/)
* [dayu_widgets_log](https://github.com/muyr/dayu_widgets_log): [中文](https://muyr.github.io/dayu_widgets_log/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_log/#/)
* [dayu_widgets_overlay](https://github.com/FXTD-ODYSSEY/dayu_widgets_overlay)


## 安装

### 使用 pip 安装

```shell
# 安装基础包（不包含 Qt 绑定）
pip install dayu_widgets3

# 安装带 PySide2 的版本
pip install "dayu_widgets3[pyside2]"

# 安装带 PySide6 的版本
pip install "dayu_widgets3[pyside6]"
```

### 使用 uv 安装（推荐）

[uv](https://github.com/astral-sh/uv) 是一个快速的 Python 包安装器和解析器，可以替代传统的 pip。

```shell
# 安装 uv（Linux/macOS）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装 uv（Windows PowerShell）
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# 安装基础包（不包含 Qt 绑定）
uv pip install dayu_widgets3

# 安装带 PySide2 的版本
uv pip install "dayu_widgets3[pyside2]"

# 安装带 PySide6 的版本
uv pip install "dayu_widgets3[pyside6]"
```

### 从源码安装

```shell
# 克隆仓库
git clone https://github.com/xiaonuoAndy/dayu_widgets3.git
cd dayu_widgets3

# 使用 uv 安装开发版本
uv pip install -e ".[pyside6]"  # 使用 PySide6
# 或者
uv pip install -e ".[pyside2]"  # 使用 PySide2
```

注意：依赖里并未强制要求安装任何 Qt 的 Python 绑定库，可根据自己的需要，选择手动安装 PySide2、PySide6、PyQt4、PyQt5。

## 开发指南

### 开发环境设置

#### 使用 poetry（传统方式）

```shell
# 安装 poetry
pip install poetry

# 安装依赖
poetry install

# 激活虚拟环境
poetry shell
```

#### 使用 uv（推荐）

```shell
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh  # Linux/macOS
# 或
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"  # Windows

# 创建虚拟环境并安装依赖
uv venv
uv pip install -e ".[pyside6]"  # 或 ".[pyside2]"

# 安装开发依赖
uv pip install pytest black isort commitizen
```

### 代码质量工具

#### 运行单元测试

```shell
# 使用 poetry
poetry run pytest

# 使用 uv
uv run pytest
```

#### 代码格式化

```shell
# 使用 poetry
poetry run black dayu_widgets3
poetry run isort dayu_widgets3

# 使用 uv
uv run black dayu_widgets3
uv run isort dayu_widgets3
```

#### 运行 nox 测试

```shell
# 安装 nox
uv pip install nox

# 列出可用的 nox 会话
nox -l

# 运行特定的测试
nox -s test -- --qt-binding=pyside6
```

### 提交代码

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范进行代码提交。

```shell
# 使用 poetry
poetry run cz commit

# 使用 uv
uv run cz commit
```

### 文档开发

文档使用 [docsify](https://docsify.js.org/) 构建，支持中英文两种语言。

```shell
# 安装 docsify
npm install -g docsify-cli

# 本地预览文档
docsify serve docs
```

然后访问 http://localhost:3000 查看文档。
