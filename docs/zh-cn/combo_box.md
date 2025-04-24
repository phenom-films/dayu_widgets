# MComboBox 下拉框

MComboBox 是一个下拉选择框组件，用于从预定义的选项列表中选择一个或多个选项。它基于 Qt 的 QComboBox 类，提供了更美观的样式和更丰富的功能。

## 导入

```python
from dayu_widgets.combo_box import MComboBox
```

## 代码示例

### 基本使用

MComboBox 可以创建一个简单的下拉选择框，用户可以从中选择一个选项。

```python
from dayu_widgets.combo_box import MComboBox

# 创建一个下拉框
combo_box = MComboBox()

# 添加选项
combo_box.addItems(["北京", "上海", "广州", "深圳"])

# 设置默认选中项
combo_box.setCurrentIndex(0)  # 选中第一项
```

### 不同尺寸

MComboBox 支持不同的尺寸，可以通过方法链式调用设置。

```python
from dayu_widgets.combo_box import MComboBox

# 创建大尺寸的下拉框
combo_box_large = MComboBox().large()

# 创建中等尺寸的下拉框（默认）
combo_box_medium = MComboBox().medium()

# 创建小尺寸的下拉框
combo_box_small = MComboBox().small()
```

### 使用 MMenu

MComboBox 可以与 MMenu 结合使用，提供更丰富的功能，如多选、级联选择等。

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建一个单选菜单
menu = MMenu()
menu.set_data(["北京", "上海", "广州", "深圳"])

# 创建下拉框并设置菜单
combo_box = MComboBox()
combo_box.set_menu(menu)

# 监听值变化
combo_box.sig_value_changed.connect(lambda value: print("选中的值:", value))
```

### 多选下拉框

MComboBox 可以与 MMenu 结合实现多选功能。

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建一个多选菜单
menu = MMenu(exclusive=False)
menu.set_data(["北京", "上海", "广州", "深圳"])

# 创建下拉框并设置菜单
combo_box = MComboBox()
combo_box.set_menu(menu)

# 设置自定义格式化函数，用于显示多选结果
combo_box.set_formatter(lambda x: " & ".join(x))

# 监听值变化
combo_box.sig_value_changed.connect(lambda value: print("选中的值:", value))
```

### 级联选择

MComboBox 可以与 MMenu 结合实现级联选择功能。

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建一个级联菜单
menu = MMenu(cascader=True)
menu.set_data([
    "北京/朝阳区/三里屯",
    "北京/海淀区/中关村",
    "上海/浦东新区/陆家嘴",
    "上海/静安区/南京西路"
])

# 创建下拉框并设置菜单
combo_box = MComboBox()
combo_box.set_menu(menu)

# 设置自定义格式化函数，用于显示级联选择结果
combo_box.set_formatter(lambda x: " / ".join(x))

# 监听值变化
combo_box.sig_value_changed.connect(lambda value: print("选中的值:", value))
```

### 动态加载数据

MComboBox 可以通过 MMenu 的 `set_load_callback` 方法实现动态加载数据。

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 定义数据加载回调函数
def load_data():
    # 这里可以是从数据库或API获取数据
    return ["北京", "上海", "广州", "深圳", "杭州", "成都"]

# 创建菜单并设置数据加载回调
menu = MMenu()
menu.set_load_callback(load_data)

# 创建下拉框并设置菜单
combo_box = MComboBox()
combo_box.set_menu(menu)
```

### 可搜索的下拉框

MComboBox 支持搜索功能，可以通过设置 `searchable` 属性启用。

```python
from dayu_widgets.combo_box import MComboBox

# 创建一个可搜索的下拉框
combo_box = MComboBox()
combo_box.addItems(["北京", "上海", "广州", "深圳", "杭州", "成都", "南京", "武汉"])
combo_box.setProperty("searchable", True)
```

### 完整示例

以下是一个完整的示例，展示了 MComboBox 的各种用法：

```python
# Import built-in modules
import random

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.menu import MMenu


class ComboBoxExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ComboBoxExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        cities = ["北京", "上海", "广州", "深圳"]
        self.register_field("button1_selected", "北京")
        menu1 = MMenu(parent=self)
        menu1.set_data(cities)
        size_list = [
            ("大尺寸", dayu_theme.large),
            ("中等尺寸", dayu_theme.medium),
            ("小尺寸", dayu_theme.small),
        ]
        size_lay = QtWidgets.QHBoxLayout()
        for label, size in size_list:
            combo_box = MComboBox()
            combo_box.set_dayu_size(size)
            combo_box.set_menu(menu1)
            size_lay.addWidget(combo_box)
            self.bind("button1_selected", combo_box, "value", signal="sig_value_changed")

        self.register_field("button2_selected", ["北京"])
        menu2 = MMenu(exclusive=False, parent=self)
        menu2.set_data(cities)
        select2 = MComboBox()
        select2.set_menu(menu2)
        self.bind("button2_selected", select2, "value", signal="sig_value_changed")

        def dynamic_get_city():
            all_cities = cities + ["郑州", "石家庄"]
            count = random.randint(2, min(4, len(all_cities)))
            return random.sample(all_cities, count)

        self.register_field("button3_selected", "")
        menu3 = MMenu(parent=self)
        menu3.set_load_callback(dynamic_get_city)
        select3 = MComboBox()
        select3.set_menu(menu3)
        self.bind("button3_selected", select3, "value", signal="sig_value_changed")

        # 级联选择示例
        a = ["北京/朝阳区/三里屯", "北京/海淀区/中关村", "上海/浦东新区/陆家嘴", "上海/静安区/南京西路"]
        self.register_field("button4_selected", "")
        menu4 = MMenu(cascader=True, parent=self)
        menu4.set_data(a)
        select4 = MComboBox()
        select4.set_menu(menu4)
        select4.set_formatter(lambda x: " / ".join(x))
        self.bind("button4_selected", select4, "value", signal="sig_value_changed")

        self.register_field("button5_selected", "")
        menu5 = MMenu(exclusive=False, parent=self)
        menu5.set_data(cities)
        select5 = MComboBox()
        select5.set_menu(menu5)
        select5.set_formatter(lambda x: " & ".join(x))
        self.bind("button5_selected", select5, "value", signal="sig_value_changed")

        sub_lay1 = QtWidgets.QHBoxLayout()
        sub_lay1.addWidget(MLabel("单选:"))
        sub_lay1.addWidget(select2)
        sub_lay1.addStretch()

        sub_lay2 = QtWidgets.QHBoxLayout()
        sub_lay2.addWidget(MLabel("动态加载:"))
        sub_lay2.addWidget(select3)
        sub_lay2.addStretch()

        sub_lay3 = QtWidgets.QHBoxLayout()
        sub_lay3.addWidget(MLabel("级联选择:"))
        sub_lay3.addWidget(select4)
        sub_lay3.addStretch()

        sub_lay4 = QtWidgets.QHBoxLayout()
        sub_lay4.addWidget(MLabel("多选:"))
        sub_lay4.addWidget(select5)
        sub_lay4.addStretch()

        sub_lay5 = QtWidgets.QHBoxLayout()
        sub_lay5.addWidget(MLabel("可搜索:"))
        combo = MComboBox()
        items = cities[:]
        items += ["a" * i for i in range(20)]
        combo.addItems(items)
        combo.setProperty("searchable", True)
        sub_lay5.addWidget(combo)
        sub_lay5.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("不同尺寸"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("单选"))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(MDivider("动态加载"))
        main_lay.addLayout(sub_lay2)
        main_lay.addWidget(MDivider("级联选择"))
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider("多选"))
        main_lay.addLayout(sub_lay4)
        main_lay.addWidget(MDivider("可搜索"))
        main_lay.addLayout(sub_lay5)
        main_lay.addStretch()

        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = ComboBoxExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### 构造函数

```python
MComboBox(parent=None)
```

| 参数 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `parent` | 父部件 | `QWidget` | `None` |

### 方法

| 方法 | 描述 | 参数 | 返回值 |
| --- | --- | --- | --- |
| `set_menu(menu)` | 设置下拉菜单 | `menu`: MMenu 实例 | 无 |
| `set_formatter(func)` | 设置格式化函数 | `func`: 格式化函数 | 无 |
| `set_placeholder(text)` | 设置占位符文本 | `text`: 占位符文本 | 无 |
| `set_value(value)` | 设置当前值 | `value`: 当前值 | 无 |
| `set_dayu_size(value)` | 设置尺寸 | `value`: 尺寸值 | 无 |
| `huge()` | 设置为超大尺寸 | 无 | `self` |
| `large()` | 设置为大尺寸 | 无 | `self` |
| `medium()` | 设置为中等尺寸 | 无 | `self` |
| `small()` | 设置为小尺寸 | 无 | `self` |

### 继承的方法

MComboBox 继承自 QComboBox，因此可以使用 QComboBox 的所有方法，例如：

- `addItem(text, userData=None)`: 添加一个选项
- `addItems(texts)`: 添加多个选项
- `clear()`: 清空所有选项
- `count()`: 获取选项数量
- `currentIndex()`: 获取当前选中项的索引
- `currentText()`: 获取当前选中项的文本
- `setCurrentIndex(index)`: 设置当前选中项的索引
- `setCurrentText(text)`: 设置当前选中项的文本
- 更多方法请参考 Qt 文档

### 属性

| 属性 | 描述 | 类型 | 默认值 |
| --- | --- | --- | --- |
| `searchable` | 是否可搜索 | `bool` | `False` |
| `value` | 当前选中的值 | `str` 或 `list` | `""` |

### 信号

| 信号 | 描述 | 参数 |
| --- | --- | --- |
| `sig_value_changed` | 值变化时触发 | `value`: 新的值 |

## 常见问题

### 如何监听选中值的变化？

可以通过连接 `sig_value_changed` 信号来监听选中值的变化：

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建下拉框
menu = MMenu()
menu.set_data(["北京", "上海", "广州", "深圳"])
combo_box = MComboBox()
combo_box.set_menu(menu)

# 监听值变化
combo_box.sig_value_changed.connect(lambda value: print("选中的值:", value))
```

### 如何设置默认选中的值？

可以通过 `set_value` 方法设置默认选中的值：

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建下拉框
menu = MMenu()
menu.set_data(["北京", "上海", "广州", "深圳"])
combo_box = MComboBox()
combo_box.set_menu(menu)

# 设置默认选中的值
combo_box.set_value("上海")
```

对于多选下拉框，可以传入一个列表：

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建多选下拉框
menu = MMenu(exclusive=False)
menu.set_data(["北京", "上海", "广州", "深圳"])
combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " & ".join(x))

# 设置默认选中的值
combo_box.set_value(["北京", "上海"])
```

### 如何自定义显示格式？

可以通过 `set_formatter` 方法自定义显示格式：

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# 创建下拉框
menu = MMenu(cascader=True)
menu.set_data(["北京/朝阳区/三里屯", "北京/海淀区/中关村", "上海/浦东新区/陆家嘴", "上海/静安区/南京西路"])
combo_box = MComboBox()
combo_box.set_menu(menu)

# 自定义显示格式
combo_box.set_formatter(lambda x: " > ".join(x))
```

### 如何禁用下拉框？

可以通过 `setEnabled` 方法禁用下拉框：

```python
from dayu_widgets.combo_box import MComboBox

# 创建下拉框
combo_box = MComboBox()
combo_box.addItems(["北京", "上海", "广州", "深圳"])

# 禁用下拉框
combo_box.setEnabled(False)
```
