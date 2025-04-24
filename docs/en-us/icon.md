# MIcon

MIcon is a component for displaying icons, based on Qt's QIcon class, providing more convenient icon loading and color management features.

## Import

```python
from dayu_widgets.qt import MIcon
```

## Examples

### Basic Usage

MIcon can load icons in SVG or PNG format and supports custom colors.

```python
from dayu_widgets.qt import MIcon
from qtpy import QtWidgets

# Create an icon
icon = MIcon("add_line.svg")

# Create an icon with custom color
colored_icon = MIcon("add_line.svg", "#1890ff")

# Use the icon in a button
button = QtWidgets.QPushButton()
button.setIcon(icon)
```

### Using with Components

MIcon can be used with other components in dayu_widgets, such as MPushButton, MToolButton, MRadioButton, etc.

```python
from dayu_widgets.qt import MIcon
from dayu_widgets.push_button import MPushButton
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.radio_button import MRadioButton

# Use in MPushButton
button = MPushButton(text="Add", icon=MIcon("add_line.svg", "#fff"))

# Use in MToolButton
tool_button = MToolButton().svg("user_line.svg")

# Use in MRadioButton
radio_button = MRadioButton("Folder")
radio_button.setIcon(MIcon("folder_fill.svg"))
```

### Icons with Different Colors

MIcon supports custom icon colors by passing a color value when creating the icon.

```python
from dayu_widgets.qt import MIcon
from dayu_widgets import dayu_theme
from qtool_widgets import MPushButton

# Use theme colors
primary_icon = MIcon("check_line.svg", dayu_theme.primary_color)
success_icon = MIcon("check_circle_line.svg", dayu_theme.success_color)
warning_icon = MIcon("warning_fill.svg", dayu_theme.warning_color)
error_icon = MIcon("close_circle_fill.svg", dayu_theme.error_color)

# Use custom color
custom_icon = MIcon("star_fill.svg", "#ff5500")

# Use in buttons
primary_button = MPushButton(icon=primary_icon, text="Primary Button").primary()
success_button = MPushButton(icon=success_icon, text="Success Button").success()
warning_button = MPushButton(icon=warning_icon, text="Warning Button").warning()
error_button = MPushButton(icon=error_button, text="Error Button").danger()
```

### Complete Example

The following is a complete example that demonstrates various uses of MIcon:

```python
# Import third-party modules
from qtpy import QtWidgets
from qtpy import QtCore

# Import local modules
from dayu_widgets.qt import MIcon
from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.push_button import MPushButton
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.radio_button import MRadioButton
from dayu_widgets.check_box import MCheckBox


class MIconExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MIconExample, self).__init__(parent)
        self.setWindowTitle("Examples for MIcon")
        self._init_ui()

    def _init_ui(self):
        # Basic icon examples
        basic_lay = QtWidgets.QHBoxLayout()
        basic_lay.addWidget(MToolButton().svg("add_line.svg").icon_only())
        basic_lay.addWidget(MToolButton().svg("delete_line.svg").icon_only())
        basic_lay.addWidget(MToolButton().svg("success_line.svg").icon_only())
        basic_lay.addWidget(MToolButton().svg("error_line.svg").icon_only())
        basic_lay.addWidget(MToolButton().svg("info_line.svg").icon_only())
        basic_lay.addWidget(MToolButton().svg("warning_line.svg").icon_only())
        basic_lay.addStretch()

        # Icons with different colors
        color_lay = QtWidgets.QHBoxLayout()
        color_lay.addWidget(MToolButton().svg("star_fill.svg").icon_only())

        # Using theme primary color
        primary_button = MToolButton().icon_only()
        primary_button.setIcon(MIcon("star_fill.svg", dayu_theme.primary_color))
        color_lay.addWidget(primary_button)

        # Using success color
        success_button = MToolButton().icon_only()
        success_button.setIcon(MIcon("star_fill.svg", dayu_theme.success_color))
        color_lay.addWidget(success_button)

        # Using warning color
        warning_button = MToolButton().icon_only()
        warning_button.setIcon(MIcon("star_fill.svg", dayu_theme.warning_color))
        color_lay.addWidget(warning_button)

        # Using error color
        error_button = MToolButton().icon_only()
        error_button.setIcon(MIcon("star_fill.svg", dayu_theme.error_color))
        color_lay.addWidget(error_button)

        # Using custom colors
        custom_button1 = MToolButton().icon_only()
        custom_button1.setIcon(MIcon("star_fill.svg", "#5d00ff"))
        color_lay.addWidget(custom_button1)

        custom_button2 = MToolButton().icon_only()
        custom_button2.setIcon(MIcon("star_fill.svg", "#ff00ff"))
        color_lay.addWidget(custom_button2)

        color_lay.addStretch()

        # Using in different components
        components_lay = QtWidgets.QHBoxLayout()
        components_lay.addWidget(MPushButton(icon=MIcon("trash_line.svg", "#fff"), text="Delete").primary())

        radio_button = MRadioButton("Folder")
        radio_button.setIcon(MIcon("folder_fill.svg"))
        components_lay.addWidget(radio_button)

        check_box = MCheckBox("Favorite")
        check_box.setIcon(MIcon("star_fill.svg"))
        components_lay.addWidget(check_box)

        components_lay.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic Icons"))
        main_lay.addLayout(basic_lay)
        main_lay.addWidget(MDivider("Icons with Different Colors"))
        main_lay.addLayout(color_lay)
        main_lay.addWidget(MDivider("Using in Different Components"))
        main_lay.addLayout(components_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = MIconExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MIcon(path, color=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `path` | Icon path, relative to the static resource directory | `str` | - |
| `color` | Icon color, can be a hexadecimal color code or theme color variable | `str` | `None` |

### Static Resource Path

MIcon will look for icon files in the following paths:

1. Default path: `dayu_widgets/static/`
2. Custom paths: set through `dayu_widgets.CUSTOM_STATIC_FOLDERS`

## Frequently Asked Questions

### How to use custom icons?

MIcon will look for icon files in the `dayu_widgets/static/` directory by default. If you want to use custom icons, you can:

1. Place the icon files in the `dayu_widgets/static/` directory
2. Or set a custom path:

```python
import dayu_widgets
dayu_widgets.CUSTOM_STATIC_FOLDERS.append("path/to/your/icons")
```

### How to change the icon color?

MIcon supports specifying the icon color when creating it:

```python
# Use hexadecimal color code
icon1 = MIcon("star_fill.svg", "#ff5500")

# Use theme color
icon2 = MIcon("star_fill.svg", dayu_theme.primary_color)
```

### What icon formats are supported?

MIcon supports icons in SVG and PNG formats:

- SVG format: supports changing color through the `color` parameter
- PNG format: does not support changing color

### How to use icons in components?

Most dayu_widgets components support setting icons:

```python
# Use in MPushButton
button = MPushButton(icon=MIcon("add_line.svg"))

# Use in MToolButton
tool_button = MToolButton().svg("user_line.svg")

# Use in MRadioButton
radio_button = MRadioButton("Option")
radio_button.setIcon(MIcon("check_circle_fill.svg"))
```
