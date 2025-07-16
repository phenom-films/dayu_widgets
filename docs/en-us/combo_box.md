# MComboBox

MComboBox is a dropdown selection component used for selecting one or more options from a predefined list. It is based on Qt's QComboBox class, providing a more attractive style and richer functionality.

## Import

```python
from dayu_widgets.combo_box import MComboBox
```

## Examples

### Basic Usage

MComboBox can create a simple dropdown selection box where users can select an option.

```python
from dayu_widgets.combo_box import MComboBox

# Create a combo box
combo_box = MComboBox()

# Add options
combo_box.addItems(["Beijing", "Shanghai", "Guangzhou", "Shenzhen"])

# Set default selected item
combo_box.setCurrentIndex(0)  # Select the first item
```

### Different Sizes

MComboBox supports different sizes, which can be set through method chaining.

```python
from dayu_widgets.combo_box import MComboBox

# Create a large size combo box
combo_box_large = MComboBox().large()

# Create a medium size combo box (default)
combo_box_medium = MComboBox().medium()

# Create a small size combo box
combo_box_small = MComboBox().small()
```

### Using MMenu

MComboBox can be used with MMenu to provide richer functionality, such as multi-selection, cascading selection, etc.

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a single-selection menu
menu = MMenu()
menu.set_data(["Beijing", "Shanghai", "Guangzhou", "Shenzhen"])

# Create a combo box and set the menu
combo_box = MComboBox()
combo_box.set_menu(menu)

# Listen for value changes
combo_box.sig_value_changed.connect(lambda value: print("Selected value:", value))
```

### Multi-selection Combo Box

MComboBox can be combined with MMenu to implement multi-selection functionality.

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a multi-selection menu
menu = MMenu(exclusive=False)
menu.set_data(["Beijing", "Shanghai", "Guangzhou", "Shenzhen"])

# Create a combo box and set the menu
combo_box = MComboBox()
combo_box.set_menu(menu)

# Set a custom formatter for displaying multi-selection results
combo_box.set_formatter(lambda x: " & ".join(x))

# Listen for value changes
combo_box.sig_value_changed.connect(lambda value: print("Selected values:", value))
```

### Cascading Selection

MComboBox can be combined with MMenu to implement cascading selection functionality.

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a cascading menu
menu = MMenu(cascader=True)
menu.set_data([
    "Beijing/Chaoyang District/Sanlitun",
    "Beijing/Haidian District/Zhongguancun",
    "Shanghai/Pudong New District/Lujiazui",
    "Shanghai/Jing'an District/West Nanjing Road"
])

# Create a combo box and set the menu
combo_box = MComboBox()
combo_box.set_menu(menu)

# Set a custom formatter for displaying cascading selection results
combo_box.set_formatter(lambda x: " / ".join(x))

# Listen for value changes
combo_box.sig_value_changed.connect(lambda value: print("Selected value:", value))
```

### Dynamic Data Loading

MComboBox can implement dynamic data loading through the `set_load_callback` method of MMenu.

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Define a data loading callback function
def load_data():
    # This could be data from a database or API
    return ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou", "Chengdu"]

# Create a menu and set the data loading callback
menu = MMenu()
menu.set_load_callback(load_data)

# Create a combo box and set the menu
combo_box = MComboBox()
combo_box.set_menu(menu)
```

### Searchable Combo Box

MComboBox supports search functionality, which can be enabled by setting the `searchable` property.

```python
from dayu_widgets.combo_box import MComboBox

# Create a searchable combo box
combo_box = MComboBox()
combo_box.addItems(["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou", "Chengdu", "Nanjing", "Wuhan"])
combo_box.setProperty("searchable", True)
```

### Complete Example

Here's a complete example demonstrating various uses of MComboBox:

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
        cities = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"]
        self.register_field("button1_selected", "Beijing")
        menu1 = MMenu(parent=self)
        menu1.set_data(cities)
        size_list = [
            ("Large", dayu_theme.large),
            ("Medium", dayu_theme.medium),
            ("Small", dayu_theme.small),
        ]
        size_lay = QtWidgets.QHBoxLayout()
        for label, size in size_list:
            combo_box = MComboBox()
            combo_box.set_dayu_size(size)
            combo_box.set_menu(menu1)
            size_lay.addWidget(combo_box)
            self.bind("button1_selected", combo_box, "value", signal="sig_value_changed")

        self.register_field("button2_selected", ["Beijing"])
        menu2 = MMenu(exclusive=False, parent=self)
        menu2.set_data(cities)
        select2 = MComboBox()
        select2.set_menu(menu2)
        self.bind("button2_selected", select2, "value", signal="sig_value_changed")

        def dynamic_get_city():
            all_cities = cities + ["Zhengzhou", "Shijiazhuang"]
            count = random.randint(2, min(4, len(all_cities)))
            return random.sample(all_cities, count)

        self.register_field("button3_selected", "")
        menu3 = MMenu(parent=self)
        menu3.set_load_callback(dynamic_get_city)
        select3 = MComboBox()
        select3.set_menu(menu3)
        self.bind("button3_selected", select3, "value", signal="sig_value_changed")

        # Cascading selection example
        a = ["Beijing/Chaoyang District/Sanlitun", "Beijing/Haidian District/Zhongguancun", "Shanghai/Pudong New District/Lujiazui", "Shanghai/Jing'an District/West Nanjing Road"]
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
        sub_lay1.addWidget(MLabel("Single Selection:"))
        sub_lay1.addWidget(select2)
        sub_lay1.addStretch()

        sub_lay2 = QtWidgets.QHBoxLayout()
        sub_lay2.addWidget(MLabel("Dynamic Loading:"))
        sub_lay2.addWidget(select3)
        sub_lay2.addStretch()

        sub_lay3 = QtWidgets.QHBoxLayout()
        sub_lay3.addWidget(MLabel("Cascading Selection:"))
        sub_lay3.addWidget(select4)
        sub_lay3.addStretch()

        sub_lay4 = QtWidgets.QHBoxLayout()
        sub_lay4.addWidget(MLabel("Multi Selection:"))
        sub_lay4.addWidget(select5)
        sub_lay4.addStretch()

        sub_lay5 = QtWidgets.QHBoxLayout()
        sub_lay5.addWidget(MLabel("Searchable:"))
        combo = MComboBox()
        items = cities[:]
        items += ["a" * i for i in range(20)]
        combo.addItems(items)
        combo.setProperty("searchable", True)
        sub_lay5.addWidget(combo)
        sub_lay5.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Different Sizes"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("Single Selection"))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(MDivider("Dynamic Loading"))
        main_lay.addLayout(sub_lay2)
        main_lay.addWidget(MDivider("Cascading Selection"))
        main_lay.addLayout(sub_lay3)
        main_lay.addWidget(MDivider("Multi Selection"))
        main_lay.addLayout(sub_lay4)
        main_lay.addWidget(MDivider("Searchable"))
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

### Constructor

```python
MComboBox(parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `parent` | Parent widget | `QWidget` | `None` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_menu(menu)` | Set the dropdown menu | `menu`: MMenu instance | None |
| `set_formatter(func)` | Set the formatter function | `func`: Formatter function | None |
| `set_placeholder(text)` | Set the placeholder text | `text`: Placeholder text | None |
| `set_value(value)` | Set the current value | `value`: Current value | None |
| `set_dayu_size(value)` | Set the size | `value`: Size value | None |
| `huge()` | Set to huge size | None | `self` |
| `large()` | Set to large size | None | `self` |
| `medium()` | Set to medium size | None | `self` |
| `small()` | Set to small size | None | `self` |

### Inherited Methods

MComboBox inherits from QComboBox, so you can use all methods of QComboBox, such as:

- `addItem(text, userData=None)`: Add an option
- `addItems(texts)`: Add multiple options
- `clear()`: Clear all options
- `count()`: Get the number of options
- `currentIndex()`: Get the index of the current selected item
- `currentText()`: Get the text of the current selected item
- `setCurrentIndex(index)`: Set the index of the current selected item
- `setCurrentText(text)`: Set the text of the current selected item
- For more methods, please refer to the Qt documentation

### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `searchable` | Whether the combo box is searchable | `bool` | `False` |
| `value` | The current selected value | `str` or `list` | `""` |

### Signals

| Signal | Description | Parameters |
| --- | --- | --- |
| `sig_value_changed` | Triggered when the value changes | `value`: New value |

## Frequently Asked Questions

### How to listen for changes in the selected value?

You can listen for changes in the selected value by connecting to the `sig_value_changed` signal:

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a combo box
menu = MMenu()
menu.set_data(["Beijing", "Shanghai", "Guangzhou", "Shenzhen"])
combo_box = MComboBox()
combo_box.set_menu(menu)

# Listen for value changes
combo_box.sig_value_changed.connect(lambda value: print("Selected value:", value))
```

### How to set the default selected value?

You can set the default selected value using the `set_value` method:

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a combo box
menu = MMenu()
menu.set_data(["Beijing", "Shanghai", "Guangzhou", "Shenzhen"])
combo_box = MComboBox()
combo_box.set_menu(menu)

# Set the default selected value
combo_box.set_value("Shanghai")
```

For a multi-selection combo box, you can pass a list:

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a multi-selection combo box
menu = MMenu(exclusive=False)
menu.set_data(["Beijing", "Shanghai", "Guangzhou", "Shenzhen"])
combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " & ".join(x))

# Set the default selected values
combo_box.set_value(["Beijing", "Shanghai"])
```

### How to customize the display format?

You can customize the display format using the `set_formatter` method:

```python
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a combo box
menu = MMenu(cascader=True)
menu.set_data(["Beijing/Chaoyang District/Sanlitun", "Beijing/Haidian District/Zhongguancun", "Shanghai/Pudong New District/Lujiazui", "Shanghai/Jing'an District/West Nanjing Road"])
combo_box = MComboBox()
combo_box.set_menu(menu)

# Customize the display format
combo_box.set_formatter(lambda x: " > ".join(x))
```

### How to disable the combo box?

You can disable the combo box using the `setEnabled` method:

```python
from dayu_widgets.combo_box import MComboBox

# Create a combo box
combo_box = MComboBox()
combo_box.addItems(["Beijing", "Shanghai", "Guangzhou", "Shenzhen"])

# Disable the combo box
combo_box.setEnabled(False)
```
