# Custom Theme

Dayu Widgets provides flexible theme customization features, allowing you to customize the appearance of components according to your needs. You can change the theme color, switch between light and dark themes, and adjust other theme-related properties.

## Theme System Overview

The theme system of Dayu Widgets is implemented based on the `MTheme` class, which provides the following features:

1. **Light/Dark Theme Switching**: Supports "light" and "dark" theme modes
2. **Theme Color Customization**: Allows customization of the primary color
3. **Theme Property Access**: Provides rich theme properties such as colors, sizes, fonts, etc.
4. **Theme Application**: Can apply the theme to the entire application or specific components

## Import

```python
from dayu_widgets import dayu_theme
```

## Examples

### Basic Usage

By default, Dayu Widgets uses orange as the theme color and dark mode as the default theme. You can directly use the `dayu_theme` instance to apply the theme:

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton

with application() as app:
    button = MPushButton("Test Button")
    dayu_theme.apply(button)
    button.show()
```

### Switching Theme Mode

You can switch between light and dark themes using the `set_theme` method:

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton

# Switch to light theme
dayu_theme.set_theme("light")

with application() as app:
    button = MPushButton("Light Theme Button")
    dayu_theme.apply(button)
    button.show()
```

### Customizing Theme Color

You can customize the theme color using the `set_primary_color` method:

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton
from dayu_widgets.theme import MTheme

# Set theme color to blue
dayu_theme.set_primary_color(MTheme.blue)

with application() as app:
    button = MPushButton("Blue Theme Button").primary()
    dayu_theme.apply(button)
    button.show()
```

### Creating a New Theme Instance

You can also create a brand new theme instance instead of using the default `dayu_theme`:

```python
from dayu_widgets.theme import MTheme
from dayu_widgets.qt import application
from dayu_widgets.push_button import MPushButton

# Create a light theme with green as the primary color
custom_theme = MTheme("light", primary_color=MTheme.green)

with application() as app:
    button = MPushButton("Custom Theme Button").primary()
    custom_theme.apply(button)
    button.show()
```

### Complete Example

Here is a complete example showing how to create a theme switcher:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.button_group import MButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.theme import MTheme


class ThemeSwitcherExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ThemeSwitcherExample, self).__init__(parent)
        self.setWindowTitle("Theme Switcher Example")
        self._init_ui()
        
    def _init_ui(self):
        # Create theme instances
        self.dark_theme = MTheme("dark", primary_color=MTheme.orange)
        self.light_theme = MTheme("light", primary_color=MTheme.blue)
        
        # Current theme
        self.current_theme = self.dark_theme
        
        # Create theme switching buttons
        theme_button_grp = MButtonGroup()
        theme_button_grp.set_button_list([
            {"text": "Dark Theme", "clicked": self.slot_use_dark_theme},
            {"text": "Light Theme", "clicked": self.slot_use_light_theme}
        ])
        
        # Create color switching buttons
        color_button_grp = MButtonGroup()
        color_button_grp.set_button_list([
            {"text": "Blue", "clicked": lambda: self.slot_change_color(MTheme.blue)},
            {"text": "Green", "clicked": lambda: self.slot_change_color(MTheme.green)},
            {"text": "Red", "clicked": lambda: self.slot_change_color(MTheme.red)},
            {"text": "Orange", "clicked": lambda: self.slot_change_color(MTheme.orange)},
            {"text": "Purple", "clicked": lambda: self.slot_change_color(MTheme.purple)}
        ])
        
        # Create sample components
        self.sample_button = MPushButton("Sample Button").primary()
        
        # Create layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Theme Switching"))
        main_lay.addWidget(theme_button_grp)
        main_lay.addWidget(MDivider("Theme Color Switching"))
        main_lay.addWidget(color_button_grp)
        main_lay.addWidget(MDivider("Sample Components"))
        main_lay.addWidget(self.sample_button)
        main_lay.addStretch()
        self.setLayout(main_lay)
        
        # Apply initial theme
        self.current_theme.apply(self)
        
    def slot_use_dark_theme(self):
        self.current_theme = self.dark_theme
        self.current_theme.apply(self)
        
    def slot_use_light_theme(self):
        self.current_theme = self.light_theme
        self.current_theme.apply(self)
        
    def slot_change_color(self, color):
        self.current_theme.set_primary_color(color)
        self.current_theme.apply(self)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets.qt import application

    with application() as app:
        test = ThemeSwitcherExample()
        test.show()
```

<!-- Need to add screenshots for theme switching -->
![Theme Switching](../_media/screenshots/custom_theme_dark.png)
![Theme Switching](../_media/screenshots/custom_theme_light.png)

## API

### MTheme Class

#### Constructor

```python
MTheme(theme="light", primary_color=None)
```

| Parameter | Description | Type | Default |
| --- | --- | --- | --- |
| `theme` | Theme mode, can be "light" or "dark" | `str` | `"light"` |
| `primary_color` | Theme color, if None, blue is used | `str` | `None` |

#### Predefined Color Constants

The MTheme class provides various predefined color constants that can be used as theme colors:

| Constant | Description | Value |
| --- | --- | --- |
| `blue` | Blue | `"#1890ff"` |
| `purple` | Purple | `"#722ed1"` |
| `cyan` | Cyan | `"#13c2c2"` |
| `green` | Green | `"#52c41a"` |
| `magenta` | Magenta | `"#eb2f96"` |
| `pink` | Pink | `"#ef5b97"` |
| `red` | Red | `"#f5222d"` |
| `orange` | Orange | `"#fa8c16"` |
| `yellow` | Yellow | `"#fadb14"` |
| `volcano` | Volcano | `"#fa541c"` |
| `geekblue` | Geek Blue | `"#2f54eb"` |
| `lime` | Lime | `"#a0d911"` |
| `gold` | Gold | `"#faad14"` |

#### Methods

| Method | Description | Parameters | Return |
| --- | --- | --- | --- |
| `set_theme(theme)` | Set theme mode | `theme`: "light" or "dark" | None |
| `set_primary_color(color)` | Set theme color | `color`: Color value, e.g., "#1890ff" | None |
| `apply(widget)` | Apply theme to component | `widget`: Component to apply theme to | None |
| `deco(cls)` | Decorator to apply theme to class | `cls`: Class to decorate | Decorated class |

#### Theme Properties

MTheme instances provide rich theme properties that can be used when customizing styles:

##### Color Properties

| Property | Description |
| --- | --- |
| `primary_color` | Theme color |
| `primary_1` to `primary_10` | Different shades of the theme color |
| `info_color` | Information color |
| `success_color` | Success color |
| `warning_color` | Warning color |
| `error_color` | Error color |
| `title_color` | Title text color |
| `primary_text_color` | Primary text color |
| `secondary_text_color` | Secondary text color |
| `disable_color` | Disabled state color |
| `border_color` | Border color |
| `divider_color` | Divider color |
| `background_color` | Background color |
| `background_selected_color` | Selected state background color |
| `item_hover_bg` | Hover state background color |

##### Size Properties

| Property | Description |
| --- | --- |
| `huge` | Huge size |
| `large` | Large size |
| `medium` | Medium size |
| `small` | Small size |
| `tiny` | Tiny size |
| `huge_icon` | Huge icon size |
| `large_icon` | Large icon size |
| `medium_icon` | Medium icon size |
| `small_icon` | Small icon size |
| `tiny_icon` | Tiny icon size |

##### Font Properties

| Property | Description |
| --- | --- |
| `font_family` | Font family |
| `font_size_base` | Base font size |
| `font_size_large` | Large font size |
| `font_size_small` | Small font size |
| `h1_size` | H1 heading size |
| `h2_size` | H2 heading size |
| `h3_size` | H3 heading size |
| `h4_size` | H4 heading size |

## FAQ

### How to apply a theme to the entire application?

To apply a theme to the entire application, you can apply the theme after creating the application and before showing the main window:

```python
from dayu_widgets import dayu_theme
from dayu_widgets.qt import application
from my_app import MyMainWindow

with application() as app:
    main_window = MyMainWindow()
    dayu_theme.apply(main_window)
    main_window.show()
```

### How to switch themes at runtime?

To switch themes at runtime, you can call the `set_theme` method and then reapply the theme:

```python
def switch_to_dark_theme(self):
    dayu_theme.set_theme("dark")
    dayu_theme.apply(self)
    
def switch_to_light_theme(self):
    dayu_theme.set_theme("light")
    dayu_theme.apply(self)
```

### How to use a custom color as the theme color?

In addition to using predefined color constants, you can use any valid color value as the theme color:

```python
# Use hexadecimal color value
dayu_theme.set_primary_color("#FF5733")

# Or use RGB color value
dayu_theme.set_primary_color("rgb(255, 87, 51)")
```

### How to use multiple themes simultaneously?

If you need to use different themes in different parts of your application, you can create multiple MTheme instances:

```python
from dayu_widgets.theme import MTheme

# Create two different themes
dark_theme = MTheme("dark", primary_color=MTheme.blue)
light_theme = MTheme("light", primary_color=MTheme.green)

# Apply different themes to different components
dark_theme.apply(widget1)
light_theme.apply(widget2)
```
