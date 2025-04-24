# MBreadcrumb

MBreadcrumb is a breadcrumb navigation component that displays the current location within a hierarchy and allows going back to states higher up in the hierarchy.

## Import

```python
from dayu_widgets.breadcrumb import MBreadcrumb
```

## Examples

### Basic Usage

MBreadcrumb can set navigation items through the `set_item_list` method. Each navigation item is a dictionary that can contain the following keys:

- `text`: The display text
- `svg`: The SVG icon filename
- `icon`: The icon object
- `tooltip`: The tooltip text shown on hover
- `clicked`: The callback function triggered on click

```python
from dayu_widgets.breadcrumb import MBreadcrumb
import functools

# Create a breadcrumb navigation
breadcrumb = MBreadcrumb()

# Set the navigation item list
item_list = [
    {
        "svg": "home_line.svg",  # Use SVG icon
        "clicked": functools.partial(print, "Home clicked")
    },
    {
        "text": "Project",  # Display text
        "svg": "folder_line.svg",  # Use SVG icon
        "clicked": functools.partial(print, "Project clicked")
    },
    {
        "text": "Task",  # Display text
        "clicked": functools.partial(print, "Task clicked")
    }
]

breadcrumb.set_item_list(item_list)
```

### Custom Separator

MBreadcrumb uses `/` as the default separator, but you can specify a custom separator when creating it:

```python
from dayu_widgets.breadcrumb import MBreadcrumb

# Create a breadcrumb navigation with > as separator
breadcrumb = MBreadcrumb(separator=">")

# Create a breadcrumb navigation with => as separator
breadcrumb_arrow = MBreadcrumb(separator="=>")
```

### Using with Message Notifications

MBreadcrumb is often used with click callback functions. Here's an example combined with MMessage:

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.breadcrumb import MBreadcrumb
from dayu_widgets.divider import MDivider
from dayu_widgets.message import MMessage


class BreadcrumbExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(BreadcrumbExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBreadcrumb")
        self._init_ui()

    def _init_ui(self):
        MMessage.config(duration=1)
        entity_list = [
            {
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Home Page"'),
                "svg": "home_line.svg",
            },
            {
                "text": "Project",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Project"'),
                "svg": "user_line.svg",
            },
            {
                "text": "Task",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Task"'),
            },
        ]
        no_icon_eg = MBreadcrumb()
        no_icon_eg.set_item_list(entity_list)

        separator_eg = MBreadcrumb(separator="=>")
        separator_eg.set_item_list(entity_list)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Default Separator"))
        main_lay.addWidget(no_icon_eg)
        main_lay.addWidget(MDivider("Custom Separator: =>"))
        main_lay.addWidget(separator_eg)

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(config, parent=self)
```

### Complete Example

![MBreadcrumb Demo](../_media/screenshots/MBreadcrumb.gif)

Here's a complete example demonstrating various uses of MBreadcrumb:

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.breadcrumb import MBreadcrumb
from dayu_widgets.divider import MDivider
from dayu_widgets.message import MMessage


class BreadcrumbExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(BreadcrumbExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBreadcrumb")
        self._init_ui()

    def _init_ui(self):
        MMessage.config(duration=1)

        # Basic example
        basic_list = [
            {
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Home Page"'),
                "svg": "home_line.svg",
            },
            {
                "text": "Project",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Project"'),
                "svg": "user_line.svg",
            },
            {
                "text": "Task",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Task"'),
            },
        ]
        basic_breadcrumb = MBreadcrumb()
        basic_breadcrumb.set_item_list(basic_list)

        # Custom separator example
        separator_breadcrumb = MBreadcrumb(separator="=>")
        separator_breadcrumb.set_item_list(basic_list)

        # Text-only example
        text_only_list = [
            {
                "text": "Home",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Home"'),
            },
            {
                "text": "Settings",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Settings"'),
            },
            {
                "text": "Profile",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Profile"'),
            },
        ]
        text_only_breadcrumb = MBreadcrumb()
        text_only_breadcrumb.set_item_list(text_only_list)

        # With tooltip example
        tooltip_list = [
            {
                "text": "Home",
                "tooltip": "Return to home page",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Home"'),
                "svg": "home_line.svg",
            },
            {
                "text": "Documentation",
                "tooltip": "View documentation",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Documentation"'),
                "svg": "file_line.svg",
            },
            {
                "text": "Components",
                "tooltip": "View component documentation",
                "clicked": functools.partial(self.slot_show_message, MMessage.info, 'Go to "Components"'),
            },
        ]
        tooltip_breadcrumb = MBreadcrumb()
        tooltip_breadcrumb.set_item_list(tooltip_list)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic Example"))
        main_lay.addWidget(basic_breadcrumb)
        main_lay.addWidget(MDivider("Custom Separator: =>"))
        main_lay.addWidget(separator_breadcrumb)
        main_lay.addWidget(MDivider("Text Only"))
        main_lay.addWidget(text_only_breadcrumb)
        main_lay.addWidget(MDivider("With Tooltip"))
        main_lay.addWidget(tooltip_breadcrumb)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(config, parent=self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = BreadcrumbExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MBreadcrumb(separator="/", parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `separator` | Separator character | `str` | `"/"` |
| `parent` | Parent widget | `QWidget` | `None` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_item_list(data_list)` | Set the navigation item list | `data_list`: List of navigation items, each is a dictionary | None |
| `add_item(data_dict, index=None)` | Add a navigation item | `data_dict`: Navigation item dictionary<br>`index`: Insert position, default is at the end | None |

### Navigation Item Dictionary

Each navigation item is a dictionary that can contain the following keys:

| Key | Description | Type | Required |
| --- | --- | --- | --- |
| `text` | Display text | `str` | No |
| `svg` | SVG icon filename | `str` | No |
| `icon` | Icon object | `QIcon` | No |
| `tooltip` | Tooltip text shown on hover | `str` | No |
| `clicked` | Callback function triggered on click | `callable` | No |

## Frequently Asked Questions

### How to show only icons in the breadcrumb?

If you want to show only icons without text, you can set only the `svg` or `icon` key without setting the `text` key:

```python
item_list = [
    {
        "svg": "home_line.svg",
        "clicked": functools.partial(print, "Home clicked")
    },
    # Other navigation items...
]
```

### How to show only text in the breadcrumb?

If you want to show only text without icons, you can set only the `text` key without setting the `svg` and `icon` keys:

```python
item_list = [
    {
        "text": "Home",
        "clicked": functools.partial(print, "Home clicked")
    },
    # Other navigation items...
]
```

### How to dynamically update the breadcrumb?

You can update the breadcrumb navigation items by calling the `set_item_list` method again:

```python
# Initial navigation items
initial_list = [
    {"text": "Home", "svg": "home_line.svg"},
    {"text": "Project", "svg": "folder_line.svg"}
]
breadcrumb.set_item_list(initial_list)

# Updated navigation items
updated_list = [
    {"text": "Home", "svg": "home_line.svg"},
    {"text": "Project", "svg": "folder_line.svg"},
    {"text": "Task", "svg": "task_line.svg"}
]
breadcrumb.set_item_list(updated_list)
```
