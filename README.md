# dayu_widgets

<p align="center">
<a href="https://img.shields.io/pypi/pyversions/dayu_widgets">
<img src="https://img.shields.io/pypi/pyversions/dayu_widgets" alt="python version"></a>
<a href="https://badge.fury.io/py/dayu_widgets">
<img src="https://img.shields.io/pypi/v/dayu_widgets?color=green" alt="PyPI version"></a>
<img src="https://img.shields.io/pypi/dw/dayu_widgets" alt="Downloads Status">
<img src="https://img.shields.io/pypi/l/dayu_widgets" alt="License">
<img src="https://img.shields.io/pypi/format/dayu_widgets" alt="pypi format">
<img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance"></a>

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END --> 
</p>


Components for PySide

主要参考了 [AntDesign](https://ant.design/) 组件库，其他参考了 [iView](https://www.iviewui.com/) 组件库，微信基础组件。

更多在此基础上的组件插件：

* [dayu_widgets_tag](https://github.com/muyr/dayu_widgets_tag):  [中文](https://muyr.github.io/dayu_widgets_tag/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_tag/#/)
* [dayu_widgets_log](https://github.com/muyr/dayu_widgets_log):  [中文](https://muyr.github.io/dayu_widgets_log/#/zh-cn/) | [EN](https://muyr.github.io/dayu_widgets_log/#/)
* [dayu_widgets_overlay](https://github.com/FXTD-ODYSSEY/dayu_widgets_overlay)

提供**亮色(light)** 和 **暗色(dark)** 两种主题，每种主题可以设置主题颜色。
以下截图以：

* 亮色 #1890ff
* 暗色 #fa8c16

## General


### MPushButton(<- QPushButton)
![pageres](screenshots/push_button_light.png)![pageres](screenshots/push_button_dark.png)

### MLabel (<- QLabel)
![pageres](screenshots/label_light.png)![pageres](screenshots/label_dark.png)

### MLoading (<- QWidget)
![pageres](screenshots/loading_light.gif)![pageres](screenshots/loading_dark.gif)

### MToolButton (<- QToolButton)
![pageres](screenshots/tool_button_light.png)![pageres](screenshots/tool_button_dark.png)

## Navigation


### MBreadcrumb (<- QWidget)
![pageres](screenshots/breadcrumb_light.gif)![pageres](screenshots/breadcrumb_dark.gif)

### MMenuTabWidget (<- QWidget)
![pageres](screenshots/menu_tab_widget_light.png)![pageres](screenshots/menu_tab_widget_dark.png)

### MPage (<- QWidget)
![pageres](screenshots/page_light.png)![pageres](screenshots/page_dark.png)


## Data Entry


### MCheckBox <- QCheckBox
![pageres](screenshots/check_box_light.png)![pageres](screenshots/check_box_dark.png)

### MClickBrowserFilePushButton <- MPushButton
### MClickBrowserFileToolButton <- MToolButton
### MClickBrowserFolderPushButton <- MPushButton
### MClickBrowserFolderToolButton <- MToolButton
### MDragFileButton <- MToolButton
### MDragFolderButton <- MToolButton
![pageres](screenshots/browser_light.png)![pageres](screenshots/browser_dark.png)

### MLineEdit <- QLineEdit
![pageres](screenshots/line_edit_light.png)![pageres](screenshots/line_edit_dark.png)

### MRadioButton <- QRadioButton
![pageres](screenshots/radio_button_light.png)![pageres](screenshots/radio_button_dark.png)

### MSwitch <- QRadioButton
![pageres](screenshots/switch_light.png)![pageres](screenshots/switch_dark.png)

### MSilder <- QSlider
![pageres](screenshots/slider_light.png)![pageres](screenshots/slider_dark.png)

### MSpinBox <- QSpinBox
### MDoubleSpinBox  <- QDoubleSpinBox
### MDateTimeEdit <- QDateTimeEdit
### MDateEdit <- QDateEdit
### MTimeEdit <- QTimeEdit
![pageres](screenshots/spin_box_light.png)![pageres](screenshots/spin_box_dark.png)


## Data Display


### MAvatar <- QLabel
![pageres](screenshots/avatar_light.png)![pageres](screenshots/avatar_dark.png)

### MBadge <- QWidget
![pageres](screenshots/badge_light.png)![pageres](screenshots/badge_dark.png)


### MCarousel <- QGraphicsView
![pageres](screenshots/carousel_light.gif)![pageres](screenshots/carousel_dark.gif)

### MCard <- QWidget
![pageres](screenshots/card_light.png)![pageres](screenshots/card_dark.png)

### MCollapse <- QWidget
![pageres](screenshots/collapse_light.gif)![pageres](screenshots/collapse_dark.gif)

### MLineTabWidget <- QWidget
![pageres](screenshots/line_tab_widget_light.gif)![pageres](screenshots/line_tab_widget_dark.gif)

### MTag <- QLabel
### MCheckableTag <- QCheckBox
### MNewTag <- QWidget
![pageres](screenshots/tag_light.png)![pageres](screenshots/tag_dark.png)


## Feedback


### MAlert <- QWidget
![pageres](screenshots/alert_light.png)![pageres](screenshots/alert_dark.png)

### MDrawer <- QWidget
![pageres](screenshots/drawer_light.gif)![pageres](screenshots/drawer_dark.gif)

### MMessage <- QWidget
![pageres](screenshots/message_light.gif)![pageres](screenshots/message_dark.gif)

### MProgressBar <- QProgressBar
![pageres](screenshots/progressbar_light.gif)![pageres](screenshots/progressbar_dark.gif)

### MProgressCircle <- QProgressBar
![pageres](screenshots/progress_circle_light.png)![pageres](screenshots/progress_circle_dark.png)

### MToast <- QWidget
![pageres](screenshots/toast_light.gif)![pageres](screenshots/toast_dark.gif)

## Other

### MDivider <- QWidget
![pageres](screenshots/divider_light.png)![pageres](screenshots/divider_dark.png)


# 如何贡献代码

## 安装poetry
``shell
pip install poetry
``
## 安装依赖
```shell
poetry install
```

## 运行单元测试
```shell
poetry run pytest
```

## 运行 black检查
```shell
poetry run black dayu_widgets
```
## 运行isort
```shell
poetry run isort dayu_widgets
```

## 提交代码
```shell
poetry run cz commit
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/muyr"><img src="https://avatars.githubusercontent.com/u/1860334?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Yanru Mu</b></sub></a><br /><a href="https://github.com/phenom-films/dayu_widgets/commits?q=author%3Yanru Mu" itle="Code">💻</a></td>
    <td align="center"><a href="https://github.com/loonghao"><img src="https://avatars1.githubusercontent.com/u/13111745?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hal</b></sub></a><br /><a href="https://github.com/phenom-films/dayu_widgets/commits?author=loonghao" title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/FXTD-ODYSSEY"><img src="https://avatars.githubusercontent.com/u/40897360?v=4?s=100" width="100px;" alt=""/><br /><sub><b>FXTD-ODYSSEY</b></sub></a><br /><a href="https://github.com/phenom-films/dayu_widgets/commits?author=FXTD-ODYSSEY" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
