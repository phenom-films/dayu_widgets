# MDivider

MDivider is a divider component used to separate different content areas. It can be horizontal or vertical, and can include text within the divider.

## Import

```python
from dayu_widgets.divider import MDivider
```

## Examples

### Basic Usage

MDivider can create a simple horizontal divider.

```python
from dayu_widgets.divider import MDivider

# Create a simple horizontal divider
divider = MDivider()
```

### Divider with Text

MDivider can include text within the divider, and the text can be aligned to the left, center, or right.

```python
from dayu_widgets.divider import MDivider

# Create a divider with text (centered by default)
divider_with_text = MDivider("Divider with Text")

# Create a divider with left-aligned text
divider_left = MDivider.left("Left Text")

# Create a divider with center-aligned text
divider_center = MDivider.center("Center Text")

# Create a divider with right-aligned text
divider_right = MDivider.right("Right Text")
```

### Vertical Divider

MDivider can create vertical dividers to separate content horizontally.

```python
from dayu_widgets.divider import MDivider
from qtpy import QtCore

# Create a vertical divider
divider_vertical = MDivider(orientation=QtCore.Qt.Vertical)

# Or use the class method
divider_vertical = MDivider.vertical()
```

### Complete Example

![MDivider Demo](../_media/screenshots/divider.png)

Here's a complete example demonstrating various uses of MDivider:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel


class DividerExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(DividerExample, self).__init__(parent)
        self.setWindowTitle("Examples for MDivider")
        self._init_ui()

    def _init_ui(self):
        div1 = MDivider()
        div2 = MDivider("With Text")
        div3 = MDivider.left("Left Text")
        div4 = MDivider.center("Center Text")
        div5 = MDivider.right("Right Text")
        div6 = MDivider.vertical()
        div7 = MDivider.vertical()
        div8 = MDivider.left("orientation=Qt.Vertical")
        label1 = MLabel("Maya").strong()
        label2 = MLabel("Nuke").underline()
        label3 = MLabel("Houdini").mark()
        sub_lay = QtWidgets.QHBoxLayout()
        sub_lay.addWidget(label1)
        sub_lay.addWidget(div6)
        sub_lay.addWidget(label2)
        sub_lay.addWidget(div7)
        sub_lay.addWidget(label3)
        sub_lay.addStretch()

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MLabel("Default horizontal divider"))
        main_lay.addWidget(div1)
        main_lay.addWidget(MLabel("Horizontal divider with text"))
        main_lay.addWidget(div2)
        main_lay.addWidget(MLabel("Text position"))
        main_lay.addWidget(div3)
        main_lay.addWidget(div4)
        main_lay.addWidget(div5)
        main_lay.addWidget(MLabel("Vertical divider"))
        main_lay.addLayout(sub_lay)
        main_lay.addWidget(MLabel("Note: Vertical divider does not support text"))
        main_lay.addWidget(div8)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = DividerExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MDivider(text="", orientation=QtCore.Qt.Horizontal, alignment=QtCore.Qt.AlignCenter, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `text` | Text within the divider | `str` | `""` |
| `orientation` | Orientation of the divider | `QtCore.Qt.Orientation` | `QtCore.Qt.Horizontal` |
| `alignment` | Alignment of the text | `QtCore.Qt.Alignment` | `QtCore.Qt.AlignCenter` |
| `parent` | Parent widget | `QWidget` | `None` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_dayu_text(value)` | Set the text within the divider | `value`: Text content | None |
| `get_dayu_text()` | Get the text within the divider | None | `str` |

### Class Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `left(text="")` | Create a horizontal divider with left-aligned text | `text`: Text content | `MDivider` instance |
| `right(text="")` | Create a horizontal divider with right-aligned text | `text`: Text content | `MDivider` instance |
| `center(text="")` | Create a horizontal divider with center-aligned text | `text`: Text content | `MDivider` instance |
| `vertical()` | Create a vertical divider | None | `MDivider` instance |

### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `dayu_text` | Text within the divider | `str` | `""` |

## Frequently Asked Questions

### How to create dividers with different text alignments?

You can use MDivider's class methods to create dividers with different text alignments:

```python
from dayu_widgets.divider import MDivider

# Create a divider with left-aligned text
divider_left = MDivider.left("Left Text")

# Create a divider with center-aligned text
divider_center = MDivider.center("Center Text")

# Create a divider with right-aligned text
divider_right = MDivider.right("Right Text")
```

Or use the constructor and specify the `alignment` parameter:

```python
from dayu_widgets.divider import MDivider
from qtpy import QtCore

# Create a divider with left-aligned text
divider_left = MDivider("Left Text", alignment=QtCore.Qt.AlignLeft)

# Create a divider with center-aligned text
divider_center = MDivider("Center Text", alignment=QtCore.Qt.AlignCenter)

# Create a divider with right-aligned text
divider_right = MDivider("Right Text", alignment=QtCore.Qt.AlignRight)
```

### How to create a vertical divider?

You can use MDivider's `vertical` class method to create a vertical divider:

```python
from dayu_widgets.divider import MDivider

# Create a vertical divider
divider_vertical = MDivider.vertical()
```

Or use the constructor and specify the `orientation` parameter:

```python
from dayu_widgets.divider import MDivider
from qtpy import QtCore

# Create a vertical divider
divider_vertical = MDivider(orientation=QtCore.Qt.Vertical)
```

### Can vertical dividers include text?

No. Vertical dividers do not support including text. Even if text is set, it will not be displayed.

```python
from dayu_widgets.divider import MDivider

# Create a vertical divider
divider_vertical = MDivider.vertical()

# Try to set text (will not be displayed)
divider_vertical.set_dayu_text("This text will not be displayed")
```

### How to dynamically change the text of a divider?

You can use the `set_dayu_text` method to dynamically change the text of a divider:

```python
from dayu_widgets.divider import MDivider

# Create a divider
divider = MDivider("Initial Text")

# Change the text
divider.set_dayu_text("New Text")
```
