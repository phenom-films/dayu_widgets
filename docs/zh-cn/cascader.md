# MCascader 级联选择

MCascader 是一个级联选择组件，用于从一组相关联的数据集合中进行选择，例如省市区、公司层级、事物分类等。它基于 MMenu 和 MComboBox 组件实现。

## 导入

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox
```

## 代码示例

### 基本使用

MCascader 可以通过组合 MMenu 和 MComboBox 来实现，其中 MMenu 需要设置 `cascader=True`。

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox
from qtpy import QtWidgets

# 创建一个级联选择组件
menu = MMenu(cascader=True)
menu.set_data(["北京/故宫", "北京/天坛", "北京/王府井", "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林"])

combo_box = MComboBox()
combo_box.set_menu(menu)

# 设置显示格式
combo_box.set_formatter(lambda x: " / ".join(x))

# 监听值变化
menu.sig_value_changed.connect(lambda value: print("选中的值:", value))
```

### 自定义分隔符

MCascader 默认使用 `/` 作为数据的分隔符，你可以通过 `set_separator` 方法自定义分隔符。

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# 创建一个级联选择组件
menu = MMenu(cascader=True)
menu.set_separator("-")
menu.set_data(["中国-北京-朝阳", "中国-北京-海淀", "中国-上海-浦东", "中国-上海-静安"])

combo_box = MComboBox()
combo_box.set_menu(menu)
```

### 与数据绑定结合使用

MCascader 可以与 MFieldMixin 结合使用，实现数据绑定。

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel


class CascaderBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CascaderBindExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 创建级联选择组件
        menu = MMenu(cascader=True)
        menu.set_data(["北京/故宫", "北京/天坛", "北京/王府井", "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林"])

        combo_box = MComboBox()
        combo_box.set_menu(menu)
        combo_box.set_formatter(lambda x: " / ".join(x))

        # 创建标签显示选中的值
        label = MLabel()

        # 注册字段和绑定
        self.register_field("selected_value", "")
        self.register_field("selected_text", lambda: " / ".join(self.field("selected_value")) if isinstance(self.field("selected_value"), list) else "")
        self.bind("selected_value", menu, "value", signal="sig_value_changed")
        self.bind("selected_text", label, "text")

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(combo_box)
        main_lay.addWidget(label)
        self.setLayout(main_lay)
```

### 动态加载数据

MCascader 支持通过回调函数动态加载数据。

```python
# Import built-in modules
import random

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox


class CascaderDynamicExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CascaderDynamicExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # 创建级联选择组件
        menu = MMenu(cascader=True)
        menu.set_load_callback(self.load_data)

        combo_box = MComboBox()
        combo_box.set_menu(menu)
        combo_box.set_formatter(lambda x: " / ".join(x))

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(combo_box)
        self.setLayout(main_lay)

    def load_data(self):
        # 模拟动态加载数据
        locations = [
            "北京/故宫", "北京/天坛", "北京/王府井",
            "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林",
            "浙江/杭州/西湖", "浙江/宁波/天一阁"
        ]
        # 随机返回一部分数据
        count = random.randint(3, len(locations))
        return random.sample(locations, count)
```

### 完整示例

![MCascader 演示](../_media/screenshots/MCascader.gif)

以下是一个完整的示例，展示了 MCascader 的各种用法：

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.menu import MMenu
from dayu_widgets.push_button import MPushButton


class CascaderExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CascaderExample, self).__init__(parent)
        self.setWindowTitle("Example for MCascader")
        self._init_ui()

    def _init_ui(self):
        # 基本示例
        self.register_field("selected_value_1", "")
        self.register_field("selected_text_1", lambda: " / ".join(self.field("selected_value_1")) if isinstance(self.field("selected_value_1"), list) else "")

        menu1 = MMenu(cascader=True)
        menu1.set_data(["北京/故宫", "北京/天坛", "北京/王府井", "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林"])

        combo_box1 = MComboBox()
        combo_box1.set_menu(menu1)
        combo_box1.set_formatter(lambda x: " / ".join(x))

        label1 = MLabel()

        self.bind("selected_value_1", menu1, "value", signal="sig_value_changed")
        self.bind("selected_text_1", label1, "text")

        # 自定义分隔符示例
        self.register_field("selected_value_2", "")
        self.register_field("selected_text_2", lambda: " > ".join(self.field("selected_value_2")) if isinstance(self.field("selected_value_2"), list) else "")

        menu2 = MMenu(cascader=True)
        menu2.set_separator("-")
        menu2.set_data(["中国-北京-朝阳", "中国-北京-海淀", "中国-上海-浦东", "中国-上海-静安"])

        combo_box2 = MComboBox()
        combo_box2.set_menu(menu2)
        combo_box2.set_formatter(lambda x: " > ".join(x))

        label2 = MLabel()

        self.bind("selected_value_2", menu2, "value", signal="sig_value_changed")
        self.bind("selected_text_2", label2, "text")

        # 按钮级联选择示例
        self.register_field("selected_value_3", "")
        self.register_field("selected_text_3", lambda: " / ".join(self.field("selected_value_3")) if isinstance(self.field("selected_value_3"), list) else "")

        menu3 = MMenu(cascader=True)
        menu3.set_data(["动物/哺乳动物/狗", "动物/哺乳动物/猫", "动物/爬行动物/蛇", "植物/花卉/玫瑰", "植物/花卉/郁金香", "植物/树木/松树"])

        button3 = MPushButton(text="级联选择")
        button3.setMenu(menu3)
        button3.clicked.connect(button3.showMenu)

        label3 = MLabel()

        self.bind("selected_value_3", menu3, "value", signal="sig_value_changed")
        self.bind("selected_text_3", label3, "text")

        # 创建布局
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("基本示例"))
        main_lay.addWidget(combo_box1)
        main_lay.addWidget(label1)
        main_lay.addWidget(MDivider("自定义分隔符"))
        main_lay.addWidget(combo_box2)
        main_lay.addWidget(label2)
        main_lay.addWidget(MDivider("按钮级联选择"))
        main_lay.addWidget(button3)
        main_lay.addWidget(label3)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = CascaderExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### MMenu (cascader=True)

#### 构造函数

```python
MMenu(exclusive=True, cascader=False, title="", parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `exclusive` | 是否互斥选择 | `bool` | `True` |
| `cascader` | 是否为级联选择 | `bool` | `False` |
| `title` | 菜单标题 | `str` | `""` |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_data(data_list)` | 设置数据列表 | `data_list`: 数据列表 | 无 |
| `set_separator(chr)` | 设置分隔符 | `chr`: 分隔符字符 | 无 |
| `set_value(data)` | 设置选中的值 | `data`: 选中的值 | 无 |
| `set_load_callback(func)` | 设置数据加载回调函数 | `func`: 回调函数 | 无 |

#### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_value_changed` | 值变化时触发 | `value`: 新的值 |

### MComboBox

#### 构造函数

```python
MComboBox(parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `parent` | 父部件 | `QWidget` | `None` |

#### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_menu(menu)` | 设置菜单 | `menu`: MMenu 实例 | 无 |
| `set_formatter(formatter)` | 设置格式化函数 | `formatter`: 格式化函数 | 无 |
| `set_dayu_size(size)` | 设置尺寸 | `size`: 尺寸值 | 无 |

#### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_value_changed` | 值变化时触发 | `value`: 新的值 |

## 常见问题

### 如何设置默认选中的值？

可以通过 MMenu 的 `set_value` 方法设置默认选中的值：

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# 创建级联选择组件
menu = MMenu(cascader=True)
menu.set_data(["北京/故宫", "北京/天坛", "北京/王府井", "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林"])

# 设置默认选中的值
menu.set_value(["北京", "天坛"])

combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " / ".join(x))
```

### 如何自定义显示格式？

可以通过 MComboBox 的 `set_formatter` 方法自定义显示格式：

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# 创建级联选择组件
menu = MMenu(cascader=True)
menu.set_data(["北京/故宫", "北京/天坛", "北京/王府井", "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林"])

combo_box = MComboBox()
combo_box.set_menu(menu)

# 自定义显示格式
combo_box.set_formatter(lambda x: " > ".join(x))
```

### 如何动态加载数据？

可以通过 MMenu 的 `set_load_callback` 方法设置数据加载回调函数：

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# 创建级联选择组件
menu = MMenu(cascader=True)

# 设置数据加载回调函数
def load_data():
    # 从服务器或其他数据源加载数据
    return ["北京/故宫", "北京/天坛", "北京/王府井", "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林"]

menu.set_load_callback(load_data)

combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " / ".join(x))
```

### 如何监听选中值的变化？

可以通过连接 MMenu 的 `sig_value_changed` 信号来监听选中值的变化：

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# 创建级联选择组件
menu = MMenu(cascader=True)
menu.set_data(["北京/故宫", "北京/天坛", "北京/王府井", "江苏/南京/夫子庙", "江苏/苏州/拙政园", "江苏/苏州/狮子林"])

combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " / ".join(x))

# 监听选中值的变化
menu.sig_value_changed.connect(lambda value: print("选中的值:", value))
```
