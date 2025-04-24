# MLabel

MLabel is a component for displaying text, based on Qt's QLabel class, providing richer text styling and formatting options.

## Import

```python
from dayu_widgets import MLabel
```

## Examples

### Basic Usage

MLabel can be set with different heading levels.

```python
from dayu_widgets.label import MLabel

# Create labels with different heading levels
h1_label = MLabel("H1 Title").h1()
h2_label = MLabel("H2 Title").h2()
h3_label = MLabel("H3 Title").h3()
h4_label = MLabel("H4 Title").h4()
```

### Different Types

MLabel supports various text types, including normal text, secondary text, warning text, and danger text.

```python
from dayu_widgets.label import MLabel

# Create labels with different types
normal_label = MLabel("Normal Text")
secondary_label = MLabel("Secondary Text").secondary()
warning_label = MLabel("Warning Text").warning()
danger_label = MLabel("Danger Text").danger()

# Create a disabled label
disabled_label = MLabel("Disabled Text")
disabled_label.setEnabled(False)
```

### Text Styles

MLabel supports various text styles, such as mark, code, underline, delete, and strong.

```python
from dayu_widgets.label import MLabel

# Create labels with different styles
mark_label = MLabel("Marked Text").mark()
code_label = MLabel("Code Text").code()
underline_label = MLabel("Underlined Text").underline()
delete_label = MLabel("Deleted Text").delete()
strong_label = MLabel("Strong Text").strong()
```

### Combined Styles

MLabel supports combining multiple styles to create richer text effects.

```python
from dayu_widgets.label import MLabel

# Create labels with combined styles
label1 = MLabel("Strong & Underline").strong().underline()
label2 = MLabel("Danger & Delete").danger().delete()
label3 = MLabel("Warning & Strong").warning().strong()
label4 = MLabel("H4 & Mark").h4().mark()
```

### Elide Mode

MLabel supports text elision, allowing you to set the elision position to left, middle, or right.

```python
from dayu_widgets.label import MLabel
from qtpy import QtCore

# Create labels with different elide modes
label_none = MLabel("This is a label with no elision, text will not be truncated.")

label_left = MLabel("This is a label with left elision, ellipsis will appear at the beginning of the text. This is some extra text.")
label_left.set_elide_mode(QtCore.Qt.ElideLeft)

label_middle = MLabel("This is a label with middle elision, ellipsis will appear in the middle of the text. This is some extra text.")
label_middle.set_elide_mode(QtCore.Qt.ElideMiddle)

label_right = MLabel("This is a label with right elision, ellipsis will appear at the end of the text. This is some extra text.")
label_right.set_elide_mode(QtCore.Qt.ElideRight)
```

### Hyperlinks

MLabel supports setting hyperlink text.

```python
from dayu_widgets.label import MLabel

# Create hyperlink labels
link_label1 = MLabel()
link_label1.set_link("https://google.com", text="Google")

link_label2 = MLabel()
link_label2.set_link("https://google.com")  # Use the link as display text

link_label3 = MLabel()
link_label3.set_link("https://github.com/phenom-films/dayu_widgets", text="Dayu Widgets")
```

### Complete Example

The following is a complete example that demonstrates all the features of MLabel:

```python
# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.push_button import MPushButton


class LabelExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(LabelExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLabel")
        self._init_ui()

    def _init_ui(self):
        title_lay = QtWidgets.QGridLayout()
        title_lay.addWidget(MLabel("一级标题").h1(), 0, 0)
        title_lay.addWidget(MLabel("二级标题").h2(), 1, 0)
        title_lay.addWidget(MLabel("三级标题").h3(), 2, 0)
        title_lay.addWidget(MLabel("四级标题").h4(), 3, 0)
        title_lay.addWidget(MLabel("h1 Level").h1(), 0, 1)
        title_lay.addWidget(MLabel("h2 Level").h2(), 1, 1)
        title_lay.addWidget(MLabel("h3 Level").h3(), 2, 1)
        title_lay.addWidget(MLabel("h4 Level").h4(), 3, 1)

        text_type_lay = QtWidgets.QHBoxLayout()
        text_type_lay.addWidget(MLabel("MLabel: Normal"))
        text_type_lay.addWidget(MLabel("MLabel: Secondary").secondary())
        text_type_lay.addWidget(MLabel("MLabel: Warning").warning())
        text_type_lay.addWidget(MLabel("MLabel: Danger").danger())
        disable_text = MLabel("MLabel: Disabled")
        disable_text.setEnabled(False)
        text_type_lay.addWidget(disable_text)

        text_attr_lay = QtWidgets.QHBoxLayout()
        text_attr_lay.addWidget(MLabel("MLabel: Mark").mark())
        text_attr_lay.addWidget(MLabel("MLabel: Code").code())
        text_attr_lay.addWidget(MLabel("MLabel: Underline").underline())
        text_attr_lay.addWidget(MLabel("MLabel: Delete").delete())
        text_attr_lay.addWidget(MLabel("MLabel: Strong").strong())

        text_mix_lay = QtWidgets.QHBoxLayout()
        text_mix_lay.addWidget(MLabel("MLabel: Strong & Underline").strong().underline())
        text_mix_lay.addWidget(MLabel("MLabel: Danger & Delete").danger().delete())
        text_mix_lay.addWidget(MLabel("MLabel: Warning & Strong").warning().strong())
        text_mix_lay.addWidget(MLabel("MLabel: H4 & Mark").h4().mark())

        lay_elide = QtWidgets.QVBoxLayout()
        label_none = MLabel("This is a elide NONE mode label. " "Ellipsis should NOT appear in the text.")
        label_left = MLabel(
            "This is a elide LEFT mode label. "
            "The ellipsis should appear at the beginning of the text. "
            "xiao mao xiao gou xiao ci wei"
        )
        label_left.set_elide_mode(QtCore.Qt.ElideLeft)
        label_middle = MLabel(
            "This is a elide MIDDLE mode label. "
            "The ellipsis should appear in the middle of the text. "
            "xiao mao xiao gou xiao ci wei"
        )
        label_middle.set_elide_mode(QtCore.Qt.ElideMiddle)
        label_right = MLabel()
        label_right.setText(
            "This is a elide RIGHT mode label. "
            "The ellipsis should appear at the end of the text. "
            "Some text to fill the line bala bala bala."
        )
        label_right.set_elide_mode(QtCore.Qt.ElideRight)
        lay_elide.addWidget(label_none)
        lay_elide.addWidget(label_left)
        lay_elide.addWidget(label_middle)
        lay_elide.addWidget(label_right)

        hyper_label_1 = MLabel()
        hyper_label_1.set_link("https://google.com", text="Google")
        hyper_label_2 = MLabel()
        hyper_label_2.set_link("https://google.com")
        hyper_label_3 = MLabel()
        hyper_label_3.set_link("https://github.com/phenom-films/dayu_widgets", text="Dayu Widgets")

        hyperlink_lay = QtWidgets.QVBoxLayout()
        hyperlink_lay.addWidget(hyper_label_1)
        hyperlink_lay.addWidget(hyper_label_2)
        hyperlink_lay.addWidget(hyper_label_3)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different level"))
        main_lay.addLayout(title_lay)
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(text_type_lay)
        main_lay.addWidget(MDivider("different property"))
        main_lay.addLayout(text_attr_lay)
        main_lay.addWidget(MDivider("mix"))
        main_lay.addLayout(text_mix_lay)
        main_lay.addWidget(MDivider("elide mode"))
        main_lay.addLayout(lay_elide)
        main_lay.addWidget(MDivider("hyperlink"))
        main_lay.addLayout(hyperlink_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = LabelExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `dayu_level` | Heading level | `int` | `0` |
| `dayu_type` | Text type | `str` | `""` |
| `dayu_underline` | Whether to show underline | `bool` | `False` |
| `dayu_delete` | Whether to show delete line | `bool` | `False` |
| `dayu_strong` | Whether to show bold text | `bool` | `False` |
| `dayu_mark` | Whether to show marked text | `bool` | `False` |
| `dayu_code` | Whether to show as code | `bool` | `False` |
| `dayu_elide_mod` | Elide mode | `QtCore.Qt.TextElideMode` | `QtCore.Qt.ElideNone` |

### Constants

| Constant | Value |
| --- | --- |
| `SecondaryType` | `"secondary"` |
| `WarningType` | `"warning"` |
| `DangerType` | `"danger"` |
| `H1Level` | `1` |
| `H2Level` | `2` |
| `H3Level` | `3` |
| `H4Level` | `4` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `h1()` | Set as h1 heading | None | Current label instance |
| `h2()` | Set as h2 heading | None | Current label instance |
| `h3()` | Set as h3 heading | None | Current label instance |
| `h4()` | Set as h4 heading | None | Current label instance |
| `secondary()` | Set as secondary text | None | Current label instance |
| `warning()` | Set as warning text | None | Current label instance |
| `danger()` | Set as danger text | None | Current label instance |
| `strong()` | Set as strong text | None | Current label instance |
| `mark()` | Set as marked text | None | Current label instance |
| `code()` | Set as code text | None | Current label instance |
| `delete()` | Set as deleted text | None | Current label instance |
| `underline()` | Set as underlined text | None | Current label instance |
| `set_elide_mode(mode)` | Set elide mode | `mode`: Elide mode, can be `QtCore.Qt.ElideNone`, `QtCore.Qt.ElideLeft`, `QtCore.Qt.ElideMiddle`, or `QtCore.Qt.ElideRight` | None |
| `set_link(href, text=None)` | Set hyperlink | `href`: Link address<br>`text`: Display text, defaults to the link address | None |

## Frequently Asked Questions

### How to set label styles?

MLabel provides various methods to set label styles, which can be combined through chained calls:

```python
# Set heading level
label1 = MLabel("H1 Title").h1()

# Set text type
label2 = MLabel("Warning Text").warning()

# Set text style
label3 = MLabel("Strong Text").strong()
label4 = MLabel("Underlined Text").underline()

# Combine multiple styles
label5 = MLabel("Strong Warning Text").warning().strong()
```

### How to handle long text?

MLabel supports text elision, which can be set using the `set_elide_mode` method:

```python
from dayu_widgets.label import MLabel
from qtpy import QtCore

# Left elision
label1 = MLabel("This is a very long text...")
label1.set_elide_mode(QtCore.Qt.ElideLeft)

# Middle elision
label2 = MLabel("This is a very long text...")
label2.set_elide_mode(QtCore.Qt.ElideMiddle)

# Right elision
label3 = MLabel("This is a very long text...")
label3.set_elide_mode(QtCore.Qt.ElideRight)
```

### How to create hyperlinks?

MLabel supports creating hyperlinks, which can be set using the `set_link` method:

```python
from dayu_widgets.label import MLabel

# Create a hyperlink with custom text
link_label1 = MLabel()
link_label1.set_link("https://github.com", text="GitHub")

# Create a hyperlink using the link as text
link_label2 = MLabel()
link_label2.set_link("https://github.com")
```
