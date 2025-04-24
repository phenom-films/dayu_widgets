# MLineEdit

MLineEdit is a text input component used to get text input from users. It is based on Qt's QLineEdit class, providing a more attractive style and richer functionality.

## Import

```python
from dayu_widgets.line_edit import MLineEdit
```

## Examples

### Basic Usage

MLineEdit can create a simple text input field where users can enter text.

```python
from dayu_widgets.line_edit import MLineEdit

# Create an empty text input field
line_edit = MLineEdit()

# Create a text input field with default text
line_edit_with_text = MLineEdit(text="Default Text")

# Set placeholder text
line_edit.setPlaceholderText("Please enter...")
```

### Different Sizes

MLineEdit supports different sizes, which can be set through method chaining.

```python
from dayu_widgets.line_edit import MLineEdit

# Create a large size text input field
line_edit_large = MLineEdit().large()
line_edit_large.setPlaceholderText("Large Size")

# Create a medium size text input field (default)
line_edit_medium = MLineEdit().medium()
line_edit_medium.setPlaceholderText("Medium Size")

# Create a small size text input field
line_edit_small = MLineEdit().small()
line_edit_small.setPlaceholderText("Small Size")
```

### Password Input

MLineEdit can be set to password mode, where the entered text will be displayed as mask characters.

```python
from dayu_widgets.line_edit import MLineEdit

# Create a password input field
password_edit = MLineEdit().password()
password_edit.setPlaceholderText("Please enter password")
```

### Prefix and Suffix Widgets

MLineEdit supports adding custom widgets before and after the input field.

```python
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.push_button import MPushButton
from dayu_widgets.label import MLabel
from qtpy import QtCore

# Create a text input field with a prefix icon
line_edit_prefix = MLineEdit(text="With Prefix Icon")
line_edit_prefix.set_prefix_widget(MToolButton().svg("user_line.svg").icon_only())

# Create a text input field with a prefix label
line_edit_label = MLineEdit(text="With Prefix Label")
label = MLabel(text="User").mark().secondary()
label.setAlignment(QtCore.Qt.AlignCenter)
label.setFixedWidth(80)
line_edit_label.set_prefix_widget(label)

# Create a text input field with a suffix button
line_edit_suffix = MLineEdit(text="With Suffix Button")
button = MPushButton(text="Go").primary()
button.setFixedWidth(40)
line_edit_suffix.set_suffix_widget(button)
```

### Preset Styles

MLineEdit provides several preset styles that can be set through method chaining.

```python
from dayu_widgets.line_edit import MLineEdit

# Create a search box
search_edit = MLineEdit().search()
search_edit.setPlaceholderText("Enter keyword to search...")

# Create a search box with a search button
search_engine_edit = MLineEdit().search_engine("Search")
search_engine_edit.setPlaceholderText("Enter keyword to search...")

# Create a file selection box
file_edit = MLineEdit().file()
file_edit.setPlaceholderText("Click button to browse files")

# Create a file save box
save_file_edit = MLineEdit().save_file()
save_file_edit.setPlaceholderText("Click button to set save file")

# Create a folder selection box
folder_edit = MLineEdit().folder()
folder_edit.setPlaceholderText("Click button to browse folder")

# Create an error message box
error_edit = MLineEdit(text="Error: File d:/ddd/ccc.jpg does not exist.").error()
```

### Delayed Signal

MLineEdit provides a delayed signal `sig_delay_text_changed` that is triggered only after the user stops typing for a period of time, avoiding frequent signal triggering.

```python
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# Create a text input field and a label
line_edit = MLineEdit()
label = MLabel()

# Connect the delayed signal
line_edit.sig_delay_text_changed.connect(label.setText)

# Set the delay duration (milliseconds)
line_edit.set_delay_duration(1000)  # Default is 500 milliseconds
```

### Complete Example

![MLineEdit Demo](../_media/screenshots/MLineEdit.png?v=1)

Here's a complete example demonstrating various uses of MLineEdit:

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.menu import MMenu
from dayu_widgets.message import MMessage
from dayu_widgets.push_button import MPushButton
from dayu_widgets.tool_button import MToolButton


class LineEditExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LineEditExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLineEdit")
        self._init_ui()

    def _init_ui(self):
        size_lay = QtWidgets.QHBoxLayout()
        line_edit_l = MLineEdit().large()
        line_edit_l.setPlaceholderText("large size")
        line_edit_m = MLineEdit().medium()
        line_edit_m.setPlaceholderText("default size")
        line_edit_s = MLineEdit().small()
        line_edit_s.setPlaceholderText("small size")
        size_lay.addWidget(line_edit_l)
        size_lay.addWidget(line_edit_m)
        size_lay.addWidget(line_edit_s)

        line_edit_tool_button = MLineEdit(text="MToolButton")
        line_edit_tool_button.set_prefix_widget(MToolButton().svg("user_line.svg").icon_only())

        line_edit_label = MLineEdit(text="MLabel")
        tool_button = MLabel(text="User").mark().secondary()
        tool_button.setAlignment(QtCore.Qt.AlignCenter)
        tool_button.setFixedWidth(80)
        line_edit_label.set_prefix_widget(tool_button)

        line_edit_push_button = MLineEdit(text="MPushButton")
        push_button = MPushButton(text="Go").primary()
        push_button.setFixedWidth(60)
        line_edit_push_button.set_suffix_widget(push_button)

        search_engine_line_edit = MLineEdit().search_engine().large()
        search_engine_line_edit.returnPressed.connect(self.slot_search)

        line_edit_options = MLineEdit()
        combobox = MComboBox()
        option_menu = MMenu()
        option_menu.set_separator("|")
        option_menu.set_data([r"http://", r"https://"])
        combobox.set_menu(option_menu)
        combobox.set_value("http://")
        combobox.setFixedWidth(100)
        line_edit_options.set_prefix_widget(combobox)

        delay_line_editor = MLineEdit()
        delay_display_label = MLabel()
        delay_button = MPushButton("Click to Edit Text")
        delay_line_editor.sig_delay_text_changed.connect(delay_display_label.setText)
        delay_button.clicked.connect(functools.partial(delay_line_editor.setText, "Edited from code"))

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different size"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("custom prefix and suffix widget"))
        main_lay.addWidget(line_edit_tool_button)
        main_lay.addWidget(line_edit_label)
        main_lay.addWidget(line_edit_push_button)
        main_lay.addWidget(MDivider("preset"))

        main_lay.addWidget(MLabel("error"))
        main_lay.addWidget(MLineEdit(text="waring: file d:/ddd/ccc.jpg not exists.").error())
        main_lay.addWidget(MLabel("search"))
        main_lay.addWidget(MLineEdit().search().small())
        main_lay.addWidget(MLabel("search_engine"))
        main_lay.addWidget(search_engine_line_edit)
        main_lay.addWidget(MLabel("file"))
        main_lay.addWidget(MLineEdit().file().small())
        main_lay.addWidget(MLabel("folder"))
        main_lay.addWidget(MLineEdit().folder().small())
        main_lay.addWidget(MLabel("MLineEdit.options()"))
        main_lay.addWidget(line_edit_options)
        main_lay.addWidget(MDivider("Test delay Signal"))
        main_lay.addWidget(delay_line_editor)
        main_lay.addWidget(delay_display_label)
        main_lay.addWidget(delay_button)
        main_lay.addStretch()
        self.setLayout(main_lay)

    @QtCore.Slot()
    def slot_search(self):
        MMessage.info("No results found", parent=self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = LineEditExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MLineEdit(text="", parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `text` | Initial text for the input field | `str` | `""` |
| `parent` | Parent widget | `QWidget` | `None` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_dayu_size(value)` | Set the size of the input field | `value`: Size value | None |
| `get_dayu_size()` | Get the size of the input field | None | `int` |
| `set_delay_duration(millisecond)` | Set the trigger time for the delayed signal | `millisecond`: Milliseconds | None |
| `get_prefix_widget()` | Get the prefix widget | None | `QWidget` |
| `set_prefix_widget(widget)` | Set the prefix widget | `widget`: Widget to set | `QWidget` |
| `get_suffix_widget()` | Get the suffix widget | None | `QWidget` |
| `set_suffix_widget(widget)` | Set the suffix widget | `widget`: Widget to set | `QWidget` |
| `setText(text)` | Set text and save to history | `text`: Text to set | None |
| `clear()` | Clear text and history | None | None |
| `search()` | Set to search box style | None | `self` |
| `error()` | Set to error message box style | None | `self` |
| `search_engine(text="Search")` | Set to search box style with a search button | `text`: Button text | `self` |
| `file(filters=None)` | Set to file selection box style | `filters`: List of file filters | `self` |
| `save_file(filters=None)` | Set to file save box style | `filters`: List of file filters | `self` |
| `folder()` | Set to folder selection box style | None | `self` |
| `huge()` | Set to huge size | None | `self` |
| `large()` | Set to large size | None | `self` |
| `medium()` | Set to medium size | None | `self` |
| `small()` | Set to small size | None | `self` |
| `tiny()` | Set to tiny size | None | `self` |
| `password()` | Set to password input mode | None | `self` |

### Signals

| Signal | Description | Parameters |
| --- | --- | --- |
| `sig_delay_text_changed` | Triggered when the text changes and after a delay | `str`: Current text |

### Inherited Methods

MLineEdit inherits from QLineEdit, so you can use all methods of QLineEdit, such as:

- `text()`: Get the current text
- `setPlaceholderText(text)`: Set placeholder text
- `setReadOnly(bool)`: Set whether it's read-only
- `setMaxLength(int)`: Set maximum length
- `setAlignment(Qt.Alignment)`: Set text alignment
- For more methods, please refer to the Qt documentation

## Frequently Asked Questions

### How to listen for text changes?

You can listen for text changes by connecting to the `textChanged` signal:

```python
from dayu_widgets.line_edit import MLineEdit

# Create a text input field
line_edit = MLineEdit()

# Listen for text changes
line_edit.textChanged.connect(lambda text: print("Text changed:", text))
```

If you want to trigger only after the user stops typing for a period of time, you can use the `sig_delay_text_changed` signal:

```python
from dayu_widgets.line_edit import MLineEdit

# Create a text input field
line_edit = MLineEdit()

# Listen for delayed text changes
line_edit.sig_delay_text_changed.connect(lambda text: print("Delayed text changed:", text))

# Set the delay duration (milliseconds)
line_edit.set_delay_duration(1000)  # Default is 500 milliseconds
```

### How to set file filters for a file selection box?

You can set file filters through the `filters` parameter of the `file` method:

```python
from dayu_widgets.line_edit import MLineEdit

# Create a file selection box that only shows image files
line_edit = MLineEdit().file(filters=["Images (*.png *.jpg *.bmp)"])
```

### How to add a dropdown menu before the input field?

You can add a dropdown menu through the `set_prefix_widget` method:

```python
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.menu import MMenu

# Create a text input field
line_edit = MLineEdit()

# Create a dropdown menu
combobox = MComboBox()
option_menu = MMenu()
option_menu.set_data(["Option 1", "Option 2", "Option 3"])
combobox.set_menu(option_menu)
combobox.setFixedWidth(100)

# Set the prefix widget
line_edit.set_prefix_widget(combobox)
```

### How to create a search box with a search button?

You can use the `search_engine` method to create a search box with a search button:

```python
from dayu_widgets.line_edit import MLineEdit
from qtpy import QtCore

# Create a search box with a search button
search_edit = MLineEdit().search_engine("Search")

# Listen for the Enter key
search_edit.returnPressed.connect(lambda: print("Search:", search_edit.text()))
```
