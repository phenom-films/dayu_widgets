# Quick Guide

This guide will introduce how to use Dayu Widgets in your project, helping you quickly get started with developing PySide-based applications.

## Installation

### Requirements

- Python: >=3.7, <3.13
- Qt binding: PySide2 (>=5.15.2.1) or PySide6 (>=6.4.2)

> Note: PySide2 is no longer supported on Python 3.11+. If you are using Python 3.11 or higher, please use PySide6.

### Install with pip

```bash
# Install base package
pip install dayu_widgets

# Install with PySide2 (choose one)
pip install dayu_widgets[pyside2]

# Or install with PySide6 (choose one)
pip install dayu_widgets[pyside6]
```

### Install with poetry

```bash
# Install base package
poetry add dayu_widgets

# Install with PySide2 (choose one)
poetry add dayu_widgets[pyside2]

# Or install with PySide6 (choose one)
poetry add dayu_widgets[pyside6]
```

## Basic Usage

### Import Components

Dayu Widgets provides a rich set of components. You can import the components you need:

```python
# Import individual components
from dayu_widgets.push_button import MPushButton
from dayu_widgets.label import MLabel

# Or import all components from the main module
from dayu_widgets import MPushButton, MLabel
```

### Create an Application

Creating an application with Dayu Widgets is very simple. Here's a basic example:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.push_button import MPushButton
from dayu_widgets.label import MLabel
from dayu_widgets.qt import application


class MyApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.setWindowTitle("Dayu Widgets Example")
        self._init_ui()
        
    def _init_ui(self):
        # Create a label
        label = MLabel("Welcome to Dayu Widgets!")
        label.h3()
        
        # Create a button
        button = MPushButton("Click Me").primary()
        button.clicked.connect(self.slot_button_clicked)
        
        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)
        
    def slot_button_clicked(self):
        print("Button clicked!")


if __name__ == "__main__":
    # Use application context manager to create the app
    with application() as app:
        # Create main window
        window = MyApp()
        # Apply theme
        dayu_theme.apply(window)
        # Show window
        window.show()
```

### Apply Theme

Dayu Widgets provides light and dark themes, with dark theme as the default. You can apply the theme using the `dayu_theme` instance:

```python
from dayu_widgets import dayu_theme

# Apply theme to window
dayu_theme.apply(window)
```

You can also switch themes or customize the theme color:

```python
from dayu_widgets import dayu_theme
from dayu_widgets.theme import MTheme

# Switch to light theme
dayu_theme.set_theme("light")

# Set theme color to blue
dayu_theme.set_primary_color(MTheme.blue)

# Apply theme
dayu_theme.apply(window)
```

For more detailed information about themes, please refer to [Custom Theme](/en-us/custom_theme.md).

## Component Examples

### Buttons

```python
from dayu_widgets.push_button import MPushButton

# Create different types of buttons
default_button = MPushButton("Default Button")
primary_button = MPushButton("Primary Button").primary()
success_button = MPushButton("Success Button").success()
warning_button = MPushButton("Warning Button").warning()
danger_button = MPushButton("Danger Button").danger()

# Create different sizes of buttons
large_button = MPushButton("Large Button").large()
medium_button = MPushButton("Medium Button")  # Default medium size
small_button = MPushButton("Small Button").small()
```

### Labels

```python
from dayu_widgets.label import MLabel

# Create different heading levels
h1_label = MLabel("H1 Heading").h1()
h2_label = MLabel("H2 Heading").h2()
h3_label = MLabel("H3 Heading").h3()
h4_label = MLabel("H4 Heading").h4()

# Create different types of labels
normal_label = MLabel("Normal Text")
secondary_label = MLabel("Secondary Text").secondary()
warning_label = MLabel("Warning Text").warning()
danger_label = MLabel("Danger Text").danger()
```

### Input Fields

```python
from dayu_widgets.line_edit import MLineEdit

# Create basic input field
line_edit = MLineEdit()

# Create search field
search_edit = MLineEdit().search()

# Create password field
password_edit = MLineEdit().password()

# Create different sizes of input fields
large_edit = MLineEdit().large()
small_edit = MLineEdit().small()
```

### Table Views

```python
from dayu_widgets.item_view import MTableView
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_model import MSortFilterModel

# Create model
model = MTableModel()
model.set_header_list([
    {"key": "name", "label": "Name"},
    {"key": "age", "label": "Age"},
    {"key": "city", "label": "City"}
])

# Create sort filter model
sort_filter_model = MSortFilterModel()
sort_filter_model.setSourceModel(model)

# Create table view
table_view = MTableView()
table_view.setModel(sort_filter_model)
table_view.set_header_list([
    {"key": "name", "label": "Name"},
    {"key": "age", "label": "Age"},
    {"key": "city", "label": "City"}
])

# Set data
model.set_data_list([
    {"name": "John", "age": 18, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "London"},
    {"name": "Bob", "age": 30, "city": "Paris"}
])
```

### Simplify Code with View Sets

```python
from dayu_widgets.item_view_set import MItemViewSet

# Create table view set
item_view_set = MItemViewSet(view_type=MItemViewSet.TableViewType)

# Set header
item_view_set.set_header_list([
    {"key": "name", "label": "Name"},
    {"key": "age", "label": "Age"},
    {"key": "city", "label": "City"}
])

# Set data
item_view_set.setup_data([
    {"name": "John", "age": 18, "city": "New York"},
    {"name": "Jane", "age": 25, "city": "London"},
    {"name": "Bob", "age": 30, "city": "Paris"}
])

# Enable search functionality
item_view_set.searchable()
```

## Data Binding

Dayu Widgets provides the `MFieldMixin` class for data binding:

```python
from qtpy import QtWidgets
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton


class DataBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DataBindExample, self).__init__(parent)
        self._init_ui()
        
    def _init_ui(self):
        # Create label
        label = MLabel()
        
        # Create button
        button = MPushButton("Change Text").primary()
        button.clicked.connect(self.slot_change_text)
        
        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        self.setLayout(main_lay)
        
        # Register field and bind
        self.register_field("text", "Initial Text")
        self.bind("text", label, "text")
        
    def slot_change_text(self):
        self.set_field("text", "Text Changed")
```

## Complete Example

Here's a complete example showing how to create a simple form using Dayu Widgets:

```python
# Import third-party modules
from qtpy import QtWidgets
from qtpy import QtCore

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.button_group import MRadioButtonGroup
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.menu import MMenu
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import MIcon
from dayu_widgets.spin_box import MDateEdit
from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.switch import MSwitch


class FormExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(FormExample, self).__init__(parent)
        self.setWindowTitle("Form Example")
        self._init_ui()
        
    def _init_ui(self):
        # Create form layout
        form_lay = QtWidgets.QFormLayout()
        form_lay.setLabelAlignment(QtCore.Qt.AlignRight)
        
        # Name input
        name_edit = MLineEdit().small()
        form_lay.addRow("Name:", name_edit)
        
        # Gender radio buttons
        gender_grp = MRadioButtonGroup()
        gender_grp.set_button_list([
            {"text": "Female", "icon": MIcon("female.svg")},
            {"text": "Male", "icon": MIcon("male.svg")}
        ])
        form_lay.addRow("Gender:", gender_grp)
        
        # Age input
        age_spin = MSpinBox().small()
        form_lay.addRow("Age:", age_spin)
        
        # Password input
        password_edit = MLineEdit().small().password()
        form_lay.addRow("Password:", password_edit)
        
        # Country dropdown
        country_combo = MComboBox().small()
        country_menu = MMenu()
        country_menu.set_data(["China", "USA", "UK", "France", "Japan"])
        country_combo.set_menu(country_menu)
        form_lay.addRow("Country:", country_combo)
        
        # Birthday date picker
        date_edit = MDateEdit().small()
        date_edit.setCalendarPopup(True)
        form_lay.addRow("Birthday:", date_edit)
        
        # Switch
        switch = MSwitch()
        form_lay.addRow("Receive Notifications:", switch)
        
        # Checkbox
        check_box = MCheckBox("I accept the terms and conditions")
        
        # Buttons
        button_lay = QtWidgets.QHBoxLayout()
        button_lay.addStretch()
        button_lay.addWidget(MPushButton("Submit").primary())
        button_lay.addWidget(MPushButton("Cancel"))
        
        # Main layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("User Information"))
        main_lay.addLayout(form_lay)
        main_lay.addWidget(check_box)
        main_lay.addStretch()
        main_lay.addWidget(MDivider())
        main_lay.addLayout(button_lay)
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = FormExample()
        dayu_theme.apply(test)
        test.show()
```

<!-- Need to add screenshots for the form example -->
![Form Example](../_media/screenshots/quick_start_form_dark.png)
![Form Example](../_media/screenshots/quick_start_form_light.png)

## More Resources

- [Component Documentation](/en-us/README.md): View detailed documentation for all available components
- [Custom Theme](/en-us/custom_theme.md): Learn how to customize themes
- [GitHub Repository](https://github.com/muyr/dayu_widgets3): Access the project source code and examples

## FAQ

### How to switch between PySide2 and PySide6?

Dayu Widgets uses the `qtpy` library to achieve compatibility with different Qt bindings. You just need to install the corresponding Qt binding library and then import the Dayu Widgets components.

```python
# Use PySide2
pip install PySide2
from dayu_widgets import MPushButton

# Use PySide6
pip install PySide6
from dayu_widgets import MPushButton
```

### How to handle high-resolution screens?

Dayu Widgets automatically handles scaling for high-resolution screens. If you need to adjust manually, you can set Qt's high DPI scaling attributes before creating the application:

```python
from qtpy import QtCore

# Enable high DPI scaling
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
```

### How to contribute code?

If you want to contribute code to Dayu Widgets, please refer to the contribution guidelines in the [GitHub repository](https://github.com/muyr/dayu_widgets3). The basic steps are as follows:

1. Install poetry: `pip install poetry`
2. Install dependencies: `poetry install`
3. Run unit tests: `poetry run pytest`
4. Run code format check: `poetry run black dayu_widgets3`
5. Run import sorting: `poetry run isort dayu_widgets3`
6. Commit code: `poetry run cz commit`
