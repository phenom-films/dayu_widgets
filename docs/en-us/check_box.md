# MCheckBox

MCheckBox is a checkbox component used for selecting multiple options from a set. It is based on Qt's QCheckBox class, providing a more attractive style and better interaction experience.

## Import

```python
from dayu_widgets.check_box import MCheckBox
```

## Examples

### Basic Usage

MCheckBox can create a simple checkbox that users can check or uncheck.

```python
from dayu_widgets.check_box import MCheckBox

# Create a checkbox
checkbox = MCheckBox("Option 1")

# Create a checked checkbox
checkbox_checked = MCheckBox("Option 2")
checkbox_checked.setChecked(True)

# Create a disabled checkbox
checkbox_disabled = MCheckBox("Disabled Option")
checkbox_disabled.setEnabled(False)
```

### Different States

MCheckBox supports three states: unchecked, checked, and partially checked.

```python
from dayu_widgets.check_box import MCheckBox
from qtpy import QtCore

# Create an unchecked checkbox
checkbox_unchecked = MCheckBox("Unchecked")
checkbox_unchecked.setCheckState(QtCore.Qt.Unchecked)

# Create a checked checkbox
checkbox_checked = MCheckBox("Checked")
checkbox_checked.setCheckState(QtCore.Qt.Checked)

# Create a partially checked checkbox
checkbox_partially = MCheckBox("Partially Checked")
checkbox_partially.setCheckState(QtCore.Qt.PartiallyChecked)
```

### Checkbox with Icon

MCheckBox supports setting an icon that will be displayed next to the text.

```python
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.qt import MIcon

# Create a checkbox with an icon
checkbox_icon = MCheckBox("Maya")
checkbox_icon.setIcon(MIcon("app-maya.png"))
```

### Data Binding

MCheckBox can be used with MFieldMixin for data binding.

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton


class CheckBoxBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CheckBoxBindExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # Create checkbox and label
        checkbox = MCheckBox("Data Bind")
        label = MLabel()

        # Create button to change state
        button = MPushButton("Change State")
        button.clicked.connect(lambda: self.set_field("checked", not self.field("checked")))

        # Register fields and bind
        self.register_field("checked", True)
        self.register_field("checked_text", lambda: "Yes!" if self.field("checked") else "No!!")
        self.bind("checked", checkbox, "checked", signal="stateChanged")
        self.bind("checked_text", label, "text")

        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(checkbox)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        self.setLayout(main_lay)
```

### Checkbox Group

MCheckBoxGroup is a checkbox group component that can easily manage a group of checkboxes.

```python
from dayu_widgets.button_group import MCheckBoxGroup
from qtpy import QtCore

# Create a horizontal checkbox group
checkbox_group_h = MCheckBoxGroup()
checkbox_group_h.set_button_list(["Option 1", "Option 2", "Option 3"])

# Create a vertical checkbox group
checkbox_group_v = MCheckBoxGroup(orientation=QtCore.Qt.Vertical)
checkbox_group_v.set_button_list(["Option A", "Option B", "Option C"])

# Listen for checked state changes
checkbox_group_h.sig_checked_changed.connect(lambda checked_list: print("Checked options:", checked_list))
```

### Checkbox Group with Icons

MCheckBoxGroup supports setting icons for each option.

```python
from dayu_widgets.button_group import MCheckBoxGroup
from dayu_widgets.qt import MIcon

# Create a checkbox group with icons
checkbox_group = MCheckBoxGroup()
checkbox_group.set_button_list([
    {"text": "Maya", "icon": MIcon("app-maya.png")},
    {"text": "Nuke", "icon": MIcon("app-nuke.png")},
    {"text": "Houdini", "icon": MIcon("app-houdini.png")}
])
```

### Complete Example

![MCheckBox Demo](../_media/screenshots/MCheckBox.gif)

Here's a complete example demonstrating various uses of MCheckBox:

```python
# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import MIcon


class CheckBoxExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(CheckBoxExample, self).__init__(parent)
        self.setWindowTitle("Example for MCheckBox")
        self._init_ui()

    def _init_ui(self):
        grid_lay = QtWidgets.QGridLayout()

        for index, (text, state) in enumerate(
            [
                ("Unchecked", QtCore.Qt.Unchecked),
                ("Checked", QtCore.Qt.Checked),
                ("Partially", QtCore.Qt.PartiallyChecked),
            ]
        ):
            check_box_normal = MCheckBox(text)
            check_box_normal.setCheckState(state)

            check_box_disabled = MCheckBox(text)
            check_box_disabled.setCheckState(state)
            check_box_disabled.setEnabled(False)

            grid_lay.addWidget(check_box_normal, 0, index)
            grid_lay.addWidget(check_box_disabled, 1, index)

        icon_lay = QtWidgets.QHBoxLayout()
        for text, icon in [
            ("Maya", MIcon("app-maya.png")),
            ("Nuke", MIcon("app-nuke.png")),
            ("Houdini", MIcon("app-houdini.png")),
        ]:
            check_box_icon = MCheckBox(text)
            check_box_icon.setIcon(icon)
            icon_lay.addWidget(check_box_icon)

        check_box_bind = MCheckBox("Data Bind")
        label = MLabel()
        button = MPushButton(text="Change State")
        button.clicked.connect(lambda: self.set_field("checked", not self.field("checked")))
        self.register_field("checked", True)
        self.register_field("checked_text", lambda: "Yes!" if self.field("checked") else "No!!")
        self.bind("checked", check_box_bind, "checked", signal="stateChanged")
        self.bind("checked_text", label, "text")

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic"))
        main_lay.addLayout(grid_lay)
        main_lay.addWidget(MDivider("Icon"))
        main_lay.addLayout(icon_lay)
        main_lay.addWidget(MDivider("Data Bind"))
        main_lay.addWidget(check_box_bind)
        main_lay.addWidget(label)
        main_lay.addWidget(button)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = CheckBoxExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### MCheckBox

#### Constructor

```python
MCheckBox(text="", parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `text` | Text displayed by the checkbox | `str` | `""` |
| `parent` | Parent widget | `QWidget` | `None` |

#### Inherited Methods

MCheckBox inherits from QCheckBox, so you can use all methods of QCheckBox, such as:

- `setChecked(bool)`: Set whether the checkbox is checked
- `isChecked()`: Get whether the checkbox is checked
- `setCheckState(Qt.CheckState)`: Set the checkbox state
- `checkState()`: Get the checkbox state
- `setIcon(QIcon)`: Set the checkbox icon
- `setEnabled(bool)`: Set whether the checkbox is enabled
- For more methods, please refer to the Qt documentation

### MCheckBoxGroup

#### Constructor

```python
MCheckBoxGroup(orientation=QtCore.Qt.Horizontal, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `orientation` | Layout orientation | `QtCore.Qt.Orientation` | `QtCore.Qt.Horizontal` |
| `parent` | Parent widget | `QWidget` | `None` |

#### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_button_list(data_list)` | Set the button list | `data_list`: List of button data | None |
| `get_dayu_checked()` | Get the list of checked button values | None | `list` |
| `set_dayu_checked(value)` | Set the list of checked button values | `value`: List of button values to check | None |

#### Signals

| Signal | Description | Parameters |
| --- | --- | --- |
| `sig_checked_changed` | Triggered when the checked state changes | `list`: List of checked button values |

#### Button Data

Button data can be a string or a dictionary:

- If it's a string, it will be used as the button text
- If it's a dictionary, it can contain the following keys:
  - `text`: Button text
  - `icon`: Button icon
  - `data`: Button data, used to identify the button
  - `checkable`: Whether the button is checkable
  - `checked`: Whether the button is checked by default

## Frequently Asked Questions

### How to create a tri-state checkbox?

A tri-state checkbox can display three states: unchecked, checked, and partially checked. To create a tri-state checkbox, you need to set `setTristate(True)` first, then you can use `setCheckState` to set the state:

```python
from dayu_widgets.check_box import MCheckBox
from qtpy import QtCore

# Create a tri-state checkbox
checkbox = MCheckBox("Tri-state Checkbox")
checkbox.setTristate(True)

# Set to partially checked state
checkbox.setCheckState(QtCore.Qt.PartiallyChecked)
```

### How to listen for checkbox state changes?

You can listen for checkbox state changes by connecting to the `stateChanged` signal:

```python
from dayu_widgets.check_box import MCheckBox

# Create a checkbox
checkbox = MCheckBox("Option")

# Listen for state changes
checkbox.stateChanged.connect(lambda state: print("State changed:", state))
```

### How to set default checked options in MCheckBoxGroup?

You can set default checked options using the `set_dayu_checked` method:

```python
from dayu_widgets.button_group import MCheckBoxGroup

# Create a checkbox group
checkbox_group = MCheckBoxGroup()
checkbox_group.set_button_list(["Option 1", "Option 2", "Option 3", "Option 4"])

# Set default checked options
checkbox_group.set_dayu_checked(["Option 1", "Option 3"])
```

### How to get checked options in MCheckBoxGroup?

You can get checked options using the `get_dayu_checked` method:

```python
from dayu_widgets.button_group import MCheckBoxGroup

# Create a checkbox group
checkbox_group = MCheckBoxGroup()
checkbox_group.set_button_list(["Option 1", "Option 2", "Option 3"])

# Get checked options
checked_items = checkbox_group.get_dayu_checked()
print("Checked options:", checked_items)
```
