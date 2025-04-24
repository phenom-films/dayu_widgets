# MCascader

MCascader is a cascading selection component used to select from a set of related data sets, such as provinces/cities/districts, company hierarchies, or item categories. It is implemented based on the MMenu and MComboBox components.

## Import

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox
```

## Examples

### Basic Usage

MCascader can be implemented by combining MMenu and MComboBox, where MMenu needs to be set with `cascader=True`.

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox
from qtpy import QtWidgets

# Create a cascader component
menu = MMenu(cascader=True)
menu.set_data(["Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing", "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden"])

combo_box = MComboBox()
combo_box.set_menu(menu)

# Set display format
combo_box.set_formatter(lambda x: " / ".join(x))

# Listen for value changes
menu.sig_value_changed.connect(lambda value: print("Selected value:", value))
```

### Custom Separator

MCascader uses `/` as the default data separator. You can customize the separator using the `set_separator` method.

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# Create a cascader component
menu = MMenu(cascader=True)
menu.set_separator("-")
menu.set_data(["China-Beijing-Chaoyang", "China-Beijing-Haidian", "China-Shanghai-Pudong", "China-Shanghai-Jing'an"])

combo_box = MComboBox()
combo_box.set_menu(menu)
```

### Using with Data Binding

MCascader can be used with MFieldMixin for data binding.

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
        # Create cascader component
        menu = MMenu(cascader=True)
        menu.set_data(["Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing", "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden"])

        combo_box = MComboBox()
        combo_box.set_menu(menu)
        combo_box.set_formatter(lambda x: " / ".join(x))

        # Create label to display selected value
        label = MLabel()

        # Register fields and bind
        self.register_field("selected_value", "")
        self.register_field("selected_text", lambda: " / ".join(self.field("selected_value")) if isinstance(self.field("selected_value"), list) else "")
        self.bind("selected_value", menu, "value", signal="sig_value_changed")
        self.bind("selected_text", label, "text")

        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(combo_box)
        main_lay.addWidget(label)
        self.setLayout(main_lay)
```

### Dynamic Loading Data

MCascader supports dynamically loading data through a callback function.

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
        # Create cascader component
        menu = MMenu(cascader=True)
        menu.set_load_callback(self.load_data)

        combo_box = MComboBox()
        combo_box.set_menu(menu)
        combo_box.set_formatter(lambda x: " / ".join(x))

        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(combo_box)
        self.setLayout(main_lay)

    def load_data(self):
        # Simulate dynamic data loading
        locations = [
            "Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing",
            "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden",
            "Zhejiang/Hangzhou/West Lake", "Zhejiang/Ningbo/Tianyi Pavilion"
        ]
        # Randomly return a subset of data
        count = random.randint(3, len(locations))
        return random.sample(locations, count)
```

### Complete Example

![MCascader Demo](../_media/screenshots/MCascader.gif)

Here's a complete example demonstrating various uses of MCascader:

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
        # Basic example
        self.register_field("selected_value_1", "")
        self.register_field("selected_text_1", lambda: " / ".join(self.field("selected_value_1")) if isinstance(self.field("selected_value_1"), list) else "")

        menu1 = MMenu(cascader=True)
        menu1.set_data(["Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing", "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden"])

        combo_box1 = MComboBox()
        combo_box1.set_menu(menu1)
        combo_box1.set_formatter(lambda x: " / ".join(x))

        label1 = MLabel()

        self.bind("selected_value_1", menu1, "value", signal="sig_value_changed")
        self.bind("selected_text_1", label1, "text")

        # Custom separator example
        self.register_field("selected_value_2", "")
        self.register_field("selected_text_2", lambda: " > ".join(self.field("selected_value_2")) if isinstance(self.field("selected_value_2"), list) else "")

        menu2 = MMenu(cascader=True)
        menu2.set_separator("-")
        menu2.set_data(["China-Beijing-Chaoyang", "China-Beijing-Haidian", "China-Shanghai-Pudong", "China-Shanghai-Jing'an"])

        combo_box2 = MComboBox()
        combo_box2.set_menu(menu2)
        combo_box2.set_formatter(lambda x: " > ".join(x))

        label2 = MLabel()

        self.bind("selected_value_2", menu2, "value", signal="sig_value_changed")
        self.bind("selected_text_2", label2, "text")

        # Button cascader example
        self.register_field("selected_value_3", "")
        self.register_field("selected_text_3", lambda: " / ".join(self.field("selected_value_3")) if isinstance(self.field("selected_value_3"), list) else "")

        menu3 = MMenu(cascader=True)
        menu3.set_data(["Animals/Mammals/Dogs", "Animals/Mammals/Cats", "Animals/Reptiles/Snakes", "Plants/Flowers/Roses", "Plants/Flowers/Tulips", "Plants/Trees/Pine"])

        button3 = MPushButton(text="Cascader")
        button3.setMenu(menu3)
        button3.clicked.connect(button3.showMenu)

        label3 = MLabel()

        self.bind("selected_value_3", menu3, "value", signal="sig_value_changed")
        self.bind("selected_text_3", label3, "text")

        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic Example"))
        main_lay.addWidget(combo_box1)
        main_lay.addWidget(label1)
        main_lay.addWidget(MDivider("Custom Separator"))
        main_lay.addWidget(combo_box2)
        main_lay.addWidget(label2)
        main_lay.addWidget(MDivider("Button Cascader"))
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

#### Constructor

```python
MMenu(exclusive=True, cascader=False, title="", parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `exclusive` | Whether selection is exclusive | `bool` | `True` |
| `cascader` | Whether it's a cascader | `bool` | `False` |
| `title` | Menu title | `str` | `""` |
| `parent` | Parent widget | `QWidget` | `None` |

#### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_data(data_list)` | Set data list | `data_list`: Data list | None |
| `set_separator(chr)` | Set separator | `chr`: Separator character | None |
| `set_value(data)` | Set selected value | `data`: Selected value | None |
| `set_load_callback(func)` | Set data loading callback function | `func`: Callback function | None |

#### Signals

| Signal | Description | Parameters |
| --- | --- | --- |
| `sig_value_changed` | Triggered when value changes | `value`: New value |

### MComboBox

#### Constructor

```python
MComboBox(parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `parent` | Parent widget | `QWidget` | `None` |

#### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_menu(menu)` | Set menu | `menu`: MMenu instance | None |
| `set_formatter(formatter)` | Set formatter function | `formatter`: Formatter function | None |
| `set_dayu_size(size)` | Set size | `size`: Size value | None |

#### Signals

| Signal | Description | Parameters |
| --- | --- | --- |
| `sig_value_changed` | Triggered when value changes | `value`: New value |

## Frequently Asked Questions

### How to set the default selected value?

You can set the default selected value through the `set_value` method of MMenu:

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# Create a cascader component
menu = MMenu(cascader=True)
menu.set_data(["Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing", "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden"])

# Set default selected value
menu.set_value(["Beijing", "Temple of Heaven"])

combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " / ".join(x))
```

### How to customize the display format?

You can customize the display format through the `set_formatter` method of MComboBox:

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# Create a cascader component
menu = MMenu(cascader=True)
menu.set_data(["Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing", "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden"])

combo_box = MComboBox()
combo_box.set_menu(menu)

# Customize display format
combo_box.set_formatter(lambda x: " > ".join(x))
```

### How to dynamically load data?

You can set a data loading callback function through the `set_load_callback` method of MMenu:

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# Create a cascader component
menu = MMenu(cascader=True)

# Set data loading callback function
def load_data():
    # Load data from server or other data source
    return ["Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing", "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden"]

menu.set_load_callback(load_data)

combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " / ".join(x))
```

### How to listen for changes in the selected value?

You can listen for changes in the selected value by connecting to the `sig_value_changed` signal of MMenu:

```python
from dayu_widgets.menu import MMenu
from dayu_widgets.combo_box import MComboBox

# Create a cascader component
menu = MMenu(cascader=True)
menu.set_data(["Beijing/Forbidden City", "Beijing/Temple of Heaven", "Beijing/Wangfujing", "Jiangsu/Nanjing/Confucius Temple", "Jiangsu/Suzhou/Humble Administrator's Garden", "Jiangsu/Suzhou/Lion Grove Garden"])

combo_box = MComboBox()
combo_box.set_menu(menu)
combo_box.set_formatter(lambda x: " / ".join(x))

# Listen for changes in the selected value
menu.sig_value_changed.connect(lambda value: print("Selected value:", value))
```
