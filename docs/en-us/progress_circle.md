# MProgressCircle

MProgressCircle is a circular progress component used to display the current progress of an operation in a circular manner. It supports custom colors, sizes, and can be set to dashboard style or have custom content added.

## Import

```python
from dayu_widgets.progress_circle import MProgressCircle
```

## Examples

### Basic Usage

MProgressCircle can create a simple circular progress bar to display the progress of an operation.

```python
from dayu_widgets.progress_circle import MProgressCircle

# Create a circular progress bar
progress_circle = MProgressCircle()
progress_circle.setValue(50)  # Set progress to 50%
```

### Custom Colors

MProgressCircle supports custom colors, which can be set using the `set_dayu_color` method.

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets import dayu_theme

# Create a circular progress bar with custom color
progress_circle = MProgressCircle()
progress_circle.set_dayu_color(dayu_theme.success_color)
progress_circle.setValue(80)

# Create a circular progress bar with error color
error_circle = MProgressCircle()
error_circle.set_dayu_color(dayu_theme.error_color)
error_circle.setValue(40)
```

### Dashboard Style

MProgressCircle supports dashboard style, which can be created using the `dashboard` class method.

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets import dayu_theme

# Create a dashboard style circular progress bar
dashboard = MProgressCircle.dashboard()
dashboard.setValue(75)

# Create a dashboard with custom color
custom_dashboard = MProgressCircle.dashboard()
custom_dashboard.set_dayu_color(dayu_theme.success_color)
custom_dashboard.setValue(100)
```

### Custom Sizes

MProgressCircle supports custom sizes, which can be set using the `set_dayu_width` method.

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.qt import get_scale_factor

# Get scale factor
scale_x, _ = get_scale_factor()

# Create a small circular progress bar
small_circle = MProgressCircle()
small_circle.set_dayu_width(100 * scale_x)
small_circle.setValue(40)

# Create a default size circular progress bar
default_circle = MProgressCircle()
default_circle.setValue(40)

# Create a large circular progress bar
large_circle = MProgressCircle()
large_circle.set_dayu_width(160 * scale_x)
large_circle.setValue(40)
```

### Custom Format

MProgressCircle supports custom text format, which can be set using the `setFormat` method.

```python
from dayu_widgets.progress_circle import MProgressCircle

# Create a circular progress bar with custom format
progress_circle = MProgressCircle()
progress_circle.setFormat("%p Days")
progress_circle.setValue(80)
```

### Custom Content

MProgressCircle supports adding custom content, which can be set using the `set_widget` method.

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.label import MLabel
from dayu_widgets.divider import MDivider
from qtpy import QtWidgets
from qtpy import QtCore

# Create custom content widget
custom_widget = QtWidgets.QWidget()
custom_layout = QtWidgets.QVBoxLayout()
custom_layout.setContentsMargins(20, 20, 20, 20)
custom_layout.addStretch()
custom_widget.setLayout(custom_layout)

# Add labels
lab1 = MLabel(text="42,001,776").h3()
lab2 = MLabel(text="Consumer Group Size").secondary()
lab3 = MLabel(text="Total 75% of Population").secondary()
lab1.setAlignment(QtCore.Qt.AlignCenter)
lab2.setAlignment(QtCore.Qt.AlignCenter)
lab3.setAlignment(QtCore.Qt.AlignCenter)
custom_layout.addWidget(lab1)
custom_layout.addWidget(lab2)
custom_layout.addWidget(MDivider())
custom_layout.addWidget(lab3)
custom_layout.addStretch()

# Create circular progress bar and set custom content
custom_circle = MProgressCircle()
custom_circle.set_dayu_width(180)
custom_circle.setValue(75)
custom_circle.set_widget(custom_widget)
```

### Data Binding

MProgressCircle can be used with MFieldMixin for data binding.

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.push_button import MPushButton
from dayu_widgets import dayu_theme
import functools


class ProgressCircleBindExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressCircleBindExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # Register fields
        self.register_field("percent", 0)
        self.register_field("color", self.get_color)
        self.register_field("format", self.get_format)

        # Create circular progress bar
        circle = MProgressCircle()

        # Bind data
        self.bind("percent", circle, "value")
        self.bind("color", circle, "dayu_color")
        self.bind("format", circle, "format")

        # Create buttons
        button_grp = QtWidgets.QHBoxLayout()
        plus_button = MPushButton(text="+")
        minus_button = MPushButton(text="-")
        plus_button.clicked.connect(functools.partial(self.slot_change_percent, 10))
        minus_button.clicked.connect(functools.partial(self.slot_change_percent, -10))
        button_grp.addWidget(plus_button)
        button_grp.addWidget(minus_button)

        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(circle)
        main_lay.addLayout(button_grp)
        self.setLayout(main_lay)

    def get_color(self):
        """Get color based on percentage"""
        p = self.field("percent")
        if p < 30:
            return dayu_theme.error_color
        if p < 60:
            return dayu_theme.warning_color
        if p < 100:
            return dayu_theme.primary_color
        return dayu_theme.success_color

    def get_format(self):
        """Get format based on percentage"""
        p = self.field("percent")
        if p < 30:
            return ">_<"
        if p < 60:
            return "0_0"
        if p < 100:
            return "^_^"
        return "^o^"

    def slot_change_percent(self, value):
        """Change percentage"""
        self.set_field("percent", max(0, min(self.field("percent") + value, 100)))
```

### Complete Example

![MProgressCircle Demo](../_media/screenshots/progress_circle.png)

Here's a complete example demonstrating various uses of MProgressCircle:

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import get_scale_factor


class ProgressCircleExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ProgressCircleExample, self).__init__(parent)
        self.setWindowTitle("Examples for MProgressCircle")
        self._init_ui()

    def _init_ui(self):
        main_lay = QtWidgets.QVBoxLayout()
        self.setLayout(main_lay)
        main_lay.addWidget(MDivider("circle"))
        lay1 = QtWidgets.QHBoxLayout()
        circle_1 = MProgressCircle(parent=self)
        circle_1.setFormat("%p Days")
        circle_1.setValue(80)
        circle_2 = MProgressCircle(parent=self)
        circle_2.set_dayu_color(dayu_theme.success_color)
        circle_2.setValue(100)
        circle_3 = MProgressCircle(parent=self)
        circle_3.set_dayu_color(dayu_theme.error_color)
        circle_3.setValue(40)

        dashboard_1 = MProgressCircle.dashboard(parent=self)
        dashboard_1.setFormat("%p Days")
        dashboard_1.setValue(80)
        dashboard_2 = MProgressCircle.dashboard(parent=self)
        dashboard_2.set_dayu_color(dayu_theme.success_color)
        dashboard_2.setValue(100)
        dashboard_3 = MProgressCircle.dashboard(parent=self)
        dashboard_3.set_dayu_color(dayu_theme.error_color)
        dashboard_3.setValue(40)

        lay1.addWidget(circle_1)
        lay1.addWidget(circle_2)
        lay1.addWidget(circle_3)

        dashboard_lay = QtWidgets.QHBoxLayout()
        dashboard_lay.addWidget(dashboard_1)
        dashboard_lay.addWidget(dashboard_2)
        dashboard_lay.addWidget(dashboard_3)
        main_lay.addLayout(lay1)
        main_lay.addWidget(MDivider("dashboard"))
        main_lay.addLayout(dashboard_lay)
        main_lay.addWidget(MDivider("different radius"))

        scale_x, _ = get_scale_factor()
        circle_4 = MProgressCircle(parent=self)
        circle_4.set_dayu_width(100 * scale_x)
        circle_4.setValue(40)
        circle_5 = MProgressCircle(parent=self)
        circle_5.setValue(40)
        circle_6 = MProgressCircle(parent=self)
        circle_6.set_dayu_width(160 * scale_x)
        circle_6.setValue(40)
        lay2 = QtWidgets.QHBoxLayout()
        lay2.addWidget(circle_4)
        lay2.addWidget(circle_5)
        lay2.addWidget(circle_6)

        main_lay.addLayout(lay2)
        main_lay.addWidget(MDivider("data bind"))

        self.register_field("percent", 0)
        self.register_field("color", self.get_color)
        self.register_field("format", self.get_format)
        circle = MProgressCircle(parent=self)

        self.bind("percent", circle, "value")
        self.bind("color", circle, "dayu_color")
        self.bind("format", circle, "format")
        lay3 = QtWidgets.QHBoxLayout()
        button_grp = MPushButtonGroup()
        button_grp.set_dayu_type(MPushButton.DefaultType)
        button_grp.set_button_list(
            [
                {
                    "text": "+",
                    "clicked": functools.partial(self.slot_change_percent, 10),
                },
                {
                    "text": "-",
                    "clicked": functools.partial(self.slot_change_percent, -10),
                },
            ]
        )
        lay3.addWidget(circle)
        lay3.addWidget(button_grp)
        lay3.addStretch()
        main_lay.addLayout(lay3)

        custom_widget = QtWidgets.QWidget()
        custom_layout = QtWidgets.QVBoxLayout()
        custom_layout.setContentsMargins(20, 20, 20, 20)
        custom_layout.addStretch()
        custom_widget.setLayout(custom_layout)
        lab1 = MLabel(text="42,001,776").h3()
        lab2 = MLabel(text="Consumer Group Size").secondary()
        lab3 = MLabel(text="Total 75% of Population").secondary()
        lab1.setAlignment(QtCore.Qt.AlignCenter)
        lab2.setAlignment(QtCore.Qt.AlignCenter)
        lab3.setAlignment(QtCore.Qt.AlignCenter)
        custom_layout.addWidget(lab1)
        custom_layout.addWidget(lab2)
        custom_layout.addWidget(MDivider())
        custom_layout.addWidget(lab3)
        custom_layout.addStretch()
        custom_circle = MProgressCircle()
        custom_circle.set_dayu_width(180 * scale_x)
        custom_circle.setValue(75)
        custom_circle.set_widget(custom_widget)

        main_lay.addWidget(MDivider("custom circle"))
        main_lay.addWidget(custom_circle)
        main_lay.addStretch()

    def get_color(self):
        p = self.field("percent")
        if p < 30:
            return dayu_theme.error_color
        if p < 60:
            return dayu_theme.warning_color
        if p < 100:
            return dayu_theme.primary_color
        return dayu_theme.success_color

    def get_format(self):
        p = self.field("percent")
        if p < 30:
            return ">_<"
        if p < 60:
            return "0_0"
        if p < 100:
            return "^_^"
        return "^o^"

    def slot_change_percent(self, value):
        self.set_field("percent", max(0, min(self.field("percent") + value, 100)))


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = ProgressCircleExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MProgressCircle(dashboard=False, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `dashboard` | Whether it's dashboard style | `bool` | `False` |
| `parent` | Parent widget | `QWidget` | `None` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `get_dayu_width()` | Get the width of the circular progress bar | None | `int` |
| `set_dayu_width(value)` | Set the width of the circular progress bar | `value`: Width value | None |
| `get_dayu_color()` | Get the color of the circular progress bar | None | `str` |
| `set_dayu_color(value)` | Set the color of the circular progress bar | `value`: Color value | None |
| `set_widget(widget)` | Set custom content widget | `widget`: Content widget | None |

### Class Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `dashboard(parent=None)` | Create a dashboard style circular progress bar | `parent`: Parent widget | `MProgressCircle` instance |

### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `dayu_width` | Width of the circular progress bar | `int` | `dayu_theme.progress_circle_default_radius` |
| `dayu_color` | Color of the circular progress bar | `str` | `dayu_theme.primary_color` |

### Inherited Methods

MProgressCircle inherits from QProgressBar, so you can use all methods of QProgressBar, such as:

- `setValue(value)`: Set current value
- `value()`: Get current value
- `setRange(min, max)`: Set range
- `setMinimum(min)`: Set minimum value
- `setMaximum(max)`: Set maximum value
- `setFormat(format)`: Set text format
- For more methods, please refer to the Qt documentation

## Frequently Asked Questions

### How to create a dashboard style circular progress bar?

You can create a dashboard style circular progress bar using the `dashboard` class method:

```python
from dayu_widgets.progress_circle import MProgressCircle

# Create a dashboard style circular progress bar
dashboard = MProgressCircle.dashboard()
dashboard.setValue(75)
```

### How to customize the color of the circular progress bar?

You can customize the color of the circular progress bar using the `set_dayu_color` method:

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets import dayu_theme

# Create a circular progress bar
progress_circle = MProgressCircle()

# Set to success color
progress_circle.set_dayu_color(dayu_theme.success_color)

# Set to error color
progress_circle.set_dayu_color(dayu_theme.error_color)

# Set to custom color
progress_circle.set_dayu_color("#1890ff")
```

### How to customize the size of the circular progress bar?

You can customize the size of the circular progress bar using the `set_dayu_width` method:

```python
from dayu_widgets.progress_circle import MProgressCircle

# Create a circular progress bar
progress_circle = MProgressCircle()

# Set to small size
progress_circle.set_dayu_width(80)

# Set to large size
progress_circle.set_dayu_width(160)
```

### How to add custom content to the circular progress bar?

You can add custom content to the circular progress bar using the `set_widget` method:

```python
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.label import MLabel
from qtpy import QtWidgets
from qtpy import QtCore

# Create custom content widget
custom_widget = QtWidgets.QWidget()
custom_layout = QtWidgets.QVBoxLayout()
custom_widget.setLayout(custom_layout)

# Add label
label = MLabel("Custom Content")
label.setAlignment(QtCore.Qt.AlignCenter)
custom_layout.addWidget(label)

# Create circular progress bar and set custom content
progress_circle = MProgressCircle()
progress_circle.setValue(75)
progress_circle.set_widget(custom_widget)
```
