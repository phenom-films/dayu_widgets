# MMenuTabWidget

MMenuTabWidget is a menu-style navigation bar component that can be used to create the main navigation menu for applications. It supports both horizontal and vertical layouts, can include icons and text, and allows inserting custom widgets at both ends.

## Import

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
```

## Examples

### Basic Usage

MMenuTabWidget can add menu items through the `add_menu` method. Each menu item is a dictionary that can contain the following keys:

- `text`: The display text
- `svg`: The SVG icon filename
- `icon`: The icon object
- `clicked`: The callback function triggered on click

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
import functools
from dayu_widgets.message import MMessage

# Create a menu navigation bar
menu_tab = MMenuTabWidget()

# Add menu items
menu_tab.add_menu({
    "text": "Home",
    "svg": "home_line.svg",
    "clicked": functools.partial(MMessage.info, "Home clicked")
})
menu_tab.add_menu({
    "text": "User",
    "svg": "user_line.svg",
    "clicked": functools.partial(MMessage.info, "User clicked")
})
menu_tab.add_menu({
    "text": "Settings",
    "svg": "setting_line.svg",
    "clicked": functools.partial(MMessage.info, "Settings clicked")
})

# Set the default selected menu item
menu_tab.tool_button_group.set_dayu_checked(0)
```

### Different Sizes

MMenuTabWidget supports setting different sizes through the `set_dayu_size` method:

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets import dayu_theme

# Create a menu navigation bar with default size
menu_tab_default = MMenuTabWidget()

# Create a menu navigation bar with large size
menu_tab_large = MMenuTabWidget()
menu_tab_large.set_dayu_size(dayu_theme.large)

# Create a menu navigation bar with huge size
menu_tab_huge = MMenuTabWidget()
menu_tab_huge.set_dayu_size(dayu_theme.huge)
```

### Vertical Layout

MMenuTabWidget supports vertical layout by specifying the `orientation` parameter when creating:

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from qtpy import QtCore

# Create a vertical menu navigation bar
menu_tab_vertical = MMenuTabWidget(orientation=QtCore.Qt.Vertical)
```

### Inserting and Appending Widgets

MMenuTabWidget supports inserting custom widgets at both ends of the navigation bar:

```python
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.label import MLabel
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.badge import MBadge

# Create a menu navigation bar
menu_tab = MMenuTabWidget()

# Insert a label on the left
menu_tab.tool_bar_insert_widget(MLabel("Logo").h4().strong())

# Append a button with badge on the right
badge_button = MBadge.dot(show=True, widget=MToolButton().icon_only().svg("user_fill.svg").large())
menu_tab.tool_bar_append_widget(badge_button)
```

### Complete Example

![MMenuTabWidget Demo](../_media/screenshots/MMenuTabWidget.gif)

Here's a complete example demonstrating various uses of MMenuTabWidget:

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.badge import MBadge
from dayu_widgets.label import MLabel
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.message import MMessage
from dayu_widgets.tool_button import MToolButton


class MenuTabWidgetExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MenuTabWidgetExample, self).__init__(parent)
        self.setWindowTitle("Examples for MMenuTabWidget")
        self._init_ui()

    def _init_ui(self):
        item_list = [
            {
                "text": "Overview",
                "svg": "home_line.svg",
                "clicked": functools.partial(MMessage.info, "Home", parent=self),
            },
            {
                "text": "My Account",
                "svg": "user_line.svg",
                "clicked": functools.partial(MMessage.info, "Edit Account", parent=self),
            },
            {
                "text": "Notice",
                "svg": "alert_line.svg",
                "clicked": functools.partial(MMessage.info, "View Notifications", parent=self),
            },
        ]

        # Horizontal layout, default size
        tool_bar = MMenuTabWidget()
        tool_bar.tool_bar_insert_widget(MLabel("DaYu").h4().secondary().strong())
        tool_bar.tool_bar_append_widget(
            MBadge.dot(show=True, widget=MToolButton().icon_only().svg("user_fill.svg").large())
        )
        for index, data_dict in enumerate(item_list):
            tool_bar.add_menu(data_dict, index)
        tool_bar.tool_button_group.set_dayu_checked(0)

        # Horizontal layout, huge size
        tool_bar_huge = MMenuTabWidget()
        tool_bar_huge.set_dayu_size(dayu_theme.huge)
        tool_bar_huge.tool_bar_insert_widget(MLabel("DaYu").h4().secondary().strong())
        for index, data_dict in enumerate(item_list):
            tool_bar_huge.add_menu(data_dict, index)
        tool_bar_huge.tool_button_group.set_dayu_checked(0)

        # Vertical layout, huge size
        tool_bar_huge_v = MMenuTabWidget(orientation=QtCore.Qt.Vertical)
        tool_bar_huge_v.set_dayu_size(dayu_theme.huge)
        dayu_icon = MLabel("DaYu").h4().secondary().strong()
        dayu_icon.setContentsMargins(10, 10, 10, 10)
        tool_bar_huge_v.tool_bar_insert_widget(dayu_icon)
        for index, data_dict in enumerate(item_list):
            tool_bar_huge_v.add_menu(data_dict, index)
        tool_bar_huge_v.tool_button_group.set_dayu_checked(0)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)

        main_lay.addWidget(MLabel("Menu Tab Widget (Large)"))
        main_lay.addWidget(tool_bar)

        main_lay.addWidget(MLabel("Menu Tab Widget (Huge)"))
        main_lay.addWidget(tool_bar_huge)

        main_lay.addWidget(MLabel("Menu Vertical Tab Widget (Huge)"))
        main_lay.addWidget(tool_bar_huge_v)

        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = MenuTabWidgetExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MMenuTabWidget(orientation=QtCore.Qt.Horizontal, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `orientation` | Layout orientation | `QtCore.Qt.Orientation` | `QtCore.Qt.Horizontal` |
| `parent` | Parent widget | `QWidget` | `None` |

### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `dayu_size` | Navigation bar size | `int` | `dayu_theme.large` |
| `tool_button_group` | Button group object | `MBlockButtonGroup` | - |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `add_menu(data_dict, index=None)` | Add a menu item | `data_dict`: Menu item dictionary<br>`index`: Insert position, default is at the end | None |
| `tool_bar_append_widget(widget)` | Append a widget to the right side of the navigation bar | `widget`: Widget to append | None |
| `tool_bar_insert_widget(widget)` | Insert a widget to the left side of the navigation bar | `widget`: Widget to insert | None |
| `set_dayu_size(value)` | Set the navigation bar size | `value`: Size value | None |
| `get_dayu_size()` | Get the navigation bar size | None | `int` |

### Menu Item Dictionary

Each menu item is a dictionary that can contain the following keys:

| Key | Description | Type | Required |
| --- | --- | --- | --- |
| `text` | Display text | `str` | No |
| `svg` | SVG icon filename | `str` | No |
| `icon` | Icon object | `QIcon` | No |
| `clicked` | Callback function triggered on click | `callable` | No |

## Frequently Asked Questions

### How to set the default selected menu item?

You can set the default selected menu item through the `tool_button_group.set_dayu_checked` method:

```python
menu_tab = MMenuTabWidget()
# Add menu items...
menu_tab.tool_button_group.set_dayu_checked(0)  # Select the first menu item
```

### How to get the currently selected menu item?

You can get the index of the currently selected menu item through the `tool_button_group.get_dayu_checked` method:

```python
menu_tab = MMenuTabWidget()
# Add menu items...
current_index = menu_tab.tool_button_group.get_dayu_checked()
```

### How to show only icons in menu items?

If you want to show only icons without text, you can set only the `svg` or `icon` key without setting the `text` key:

```python
menu_tab.add_menu({
    "svg": "home_line.svg",
    "clicked": functools.partial(MMessage.info, "Home clicked")
})
```

### How to show only text in menu items?

If you want to show only text without icons, you can set only the `text` key without setting the `svg` and `icon` keys:

```python
menu_tab.add_menu({
    "text": "Home",
    "clicked": functools.partial(MMessage.info, "Home clicked")
})
```

### How to listen for changes in the selected menu item?

You can listen for changes in the selected menu item through the `tool_button_group.sig_checked_changed` signal:

```python
menu_tab = MMenuTabWidget()
# Add menu items...
menu_tab.tool_button_group.sig_checked_changed.connect(lambda index: print(f"Selected menu item {index}"))
```
