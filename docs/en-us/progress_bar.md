# MProgressBar

MProgressBar is a progress bar component used to display the current progress of an operation. It is based on Qt's QProgressBar class, providing a more attractive style and better interaction experience, supporting different states and auto-coloring functionality.

## Import

```python
from dayu_widgets.progress_bar import MProgressBar
```

## Examples

### Basic Usage

MProgressBar can create a simple progress bar to display the progress of an operation.

```python
from dayu_widgets.progress_bar import MProgressBar

# Create a progress bar
progress_bar = MProgressBar()
progress_bar.setValue(50)  # Set progress to 50%
```

### Different States

MProgressBar supports three different states: normal (primary), success, and error.

```python
from dayu_widgets.progress_bar import MProgressBar

# Create a normal state progress bar
normal_progress = MProgressBar()
normal_progress.setValue(30)

# Create a success state progress bar
success_progress = MProgressBar().success()
success_progress.setValue(100)

# Create an error state progress bar
error_progress = MProgressBar().error()
error_progress.setValue(50)
```

### Auto Coloring

MProgressBar supports auto-coloring based on progress, automatically changing to success state when the progress reaches the maximum value.

```python
from dayu_widgets.progress_bar import MProgressBar

# Create an auto-coloring progress bar
auto_color_progress = MProgressBar().auto_color()
auto_color_progress.setValue(50)  # Normal state
auto_color_progress.setValue(100)  # Automatically changes to success state
```

### Complete Example

![MProgressBar Demo](../_media/screenshots/progressbar.gif)

Here's a complete example demonstrating various uses of MProgressBar:

```python
# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.progress_bar import MProgressBar
from dayu_widgets.push_button import MPushButton


class ProgressBarExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressBarExample, self).__init__(parent)
        self.setWindowTitle("Examples for MProgressBar")
        self._init_ui()

    def _init_ui(self):
        progress_1 = MProgressBar()
        progress_1.setValue(10)
        progress_1.setAlignment(QtCore.Qt.AlignCenter)
        progress_2 = MProgressBar()
        progress_2.setValue(80)

        progress_normal = MProgressBar()
        progress_normal.setValue(30)
        progress_success = MProgressBar().success()
        progress_success.setValue(100)
        progress_error = MProgressBar().error()
        progress_error.setValue(50)
        form_lay = QtWidgets.QFormLayout()
        form_lay.addRow("Primary:", progress_normal)
        form_lay.addRow("Success:", progress_success)
        form_lay.addRow("Error:", progress_error)

        self.progress_count = 0
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.slot_timeout)
        run_button = MPushButton(text="Run Something")
        run_button.clicked.connect(self.slot_run)
        self.auto_color_progress = MProgressBar().auto_color()
        auto_color_lay = QtWidgets.QVBoxLayout()
        auto_color_lay.addWidget(run_button)
        auto_color_lay.addWidget(self.auto_color_progress)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic"))

        main_lay.addWidget(progress_1)
        main_lay.addWidget(progress_2)
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(form_lay)
        main_lay.addWidget(MDivider("auto color"))
        main_lay.addLayout(auto_color_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_run(self):
        self.timer.start()
        self.auto_color_progress.setValue(0)

    def slot_timeout(self):
        if self.auto_color_progress.value() > 99:
            self.timer.stop()
        else:
            self.auto_color_progress.setValue(self.auto_color_progress.value() + 1)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = ProgressBarExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MProgressBar(parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `parent` | Parent widget | `QWidget` | `None` |

### Class Constants

| Constant | Description | Value |
| --- | --- | --- |
| `ErrorStatus` | Error state | `"error"` |
| `NormalStatus` | Normal state | `"primary"` |
| `SuccessStatus` | Success state | `"success"` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `auto_color()` | Set to auto-coloring mode | None | `self` |
| `get_dayu_status()` | Get current state | None | `str` |
| `set_dayu_status(value)` | Set current state | `value`: State value | None |
| `normal()` | Set to normal state | None | `self` |
| `error()` | Set to error state | None | `self` |
| `success()` | Set to success state | None | `self` |

### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `dayu_status` | Current state | `str` | `NormalStatus` |

### Inherited Methods

MProgressBar inherits from QProgressBar, so you can use all methods of QProgressBar, such as:

- `setValue(value)`: Set current value
- `value()`: Get current value
- `setRange(min, max)`: Set range
- `setMinimum(min)`: Set minimum value
- `setMaximum(max)`: Set maximum value
- `setAlignment(alignment)`: Set alignment
- For more methods, please refer to the Qt documentation

## Frequently Asked Questions

### How to set the value of the progress bar?

You can set the value of the progress bar using the `setValue` method:

```python
from dayu_widgets.progress_bar import MProgressBar

# Create a progress bar
progress_bar = MProgressBar()

# Set progress to 50%
progress_bar.setValue(50)
```

### How to set the state of the progress bar?

You can set the state of the progress bar using the `set_dayu_status` method or chain methods:

```python
from dayu_widgets.progress_bar import MProgressBar

# Create a progress bar
progress_bar = MProgressBar()

# Using the set_dayu_status method
progress_bar.set_dayu_status(MProgressBar.SuccessStatus)

# Or using chain methods
progress_bar = MProgressBar().success()
progress_bar = MProgressBar().error()
progress_bar = MProgressBar().normal()
```

### How to implement auto-coloring?

You can set the progress bar to auto-coloring mode using the `auto_color` method, which automatically changes to success state when the progress reaches the maximum value:

```python
from dayu_widgets.progress_bar import MProgressBar

# Create an auto-coloring progress bar
auto_color_progress = MProgressBar().auto_color()
auto_color_progress.setValue(50)  # Normal state
auto_color_progress.setValue(100)  # Automatically changes to success state
```

### How to set the alignment of the progress bar?

You can set the alignment of the progress bar text using the `setAlignment` method:

```python
from dayu_widgets.progress_bar import MProgressBar
from qtpy import QtCore

# Create a progress bar
progress_bar = MProgressBar()

# Set text to center alignment
progress_bar.setAlignment(QtCore.Qt.AlignCenter)

# Set text to left alignment
progress_bar.setAlignment(QtCore.Qt.AlignLeft)

# Set text to right alignment
progress_bar.setAlignment(QtCore.Qt.AlignRight)
```
