# MCard

MCard is a card component used to display content, which can include a title, icon, and content area. It provides a clean way to organize and present information, suitable for various scenarios.

## Import

```python
from dayu_widgets.card import MCard
from dayu_widgets.card import MMeta
```

## Examples

### Basic Usage

MCard can create a simple card with a title and content.

```python
from dayu_widgets.card import MCard
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# Create a card with a title
card = MCard(title="Card Title")

# Create content widget
content_widget = QtWidgets.QWidget()
content_layout = QtWidgets.QVBoxLayout()
content_layout.setContentsMargins(15, 15, 15, 15)
content_widget.setLayout(content_layout)

# Add content
for i in range(4):
    content_layout.addWidget(MLabel("Card Content {}".format(i + 1)))

# Set card content
card.set_widget(content_widget)
```

### Different Sizes

MCard supports different sizes, which can be set through the `size` parameter.

```python
from dayu_widgets.card import MCard
from dayu_widgets import dayu_theme

# Create a small size card
card_small = MCard(title="Small Card", size=dayu_theme.small)

# Create a medium size card (default)
card_medium = MCard(title="Medium Card", size=dayu_theme.medium)

# Create a large size card
card_large = MCard(title="Large Card", size=dayu_theme.large)
```

### Card with Icon

MCard supports displaying an icon next to the title.

```python
from dayu_widgets.card import MCard
from dayu_widgets.qt import MPixmap

# Create a card with an icon
card = MCard(title="Card with Icon", image=MPixmap("app-houdini.png"))
```

### Card with Extra Action

MCard supports adding an extra action button on the right side of the title.

```python
from dayu_widgets.card import MCard

# Create a card with an extra action
card = MCard(title="Card with Extra Action", extra="More")

# Get the more button and connect click event
more_button = card.get_more_button()
more_button.clicked.connect(lambda: print("More button clicked"))
```

### Card with Border

MCard supports displaying a border.

```python
from dayu_widgets.card import MCard

# Create a card with a border
card = MCard(title="Card with Border").border()
```

### Meta Card (MMeta)

MMeta is a special type of card used to display metadata information, such as cover image, avatar, title, and description.

```python
from dayu_widgets.card import MMeta
from dayu_widgets.qt import MPixmap

# Create a meta card
meta_card = MMeta()
meta_card.setup_data({
    "title": "Houdini",
    "description": "Side Effects Software's flagship product, an effective tool for creating advanced visual effects",
    "avatar": MPixmap("user_line.svg"),
    "cover": MPixmap("app-houdini.png")
})
```

### Meta Card with Extra Action

MMeta also supports adding an extra action button.

```python
from dayu_widgets.card import MMeta
from dayu_widgets.qt import MPixmap

# Create a meta card with an extra action
meta_card = MMeta(extra=True)
meta_card.setup_data({
    "title": "Task A",
    "description": "demo pl_0010 Animation \n2019/04/01 - 2019/04/09",
    "avatar": MPixmap("success_line.svg", dayu_theme.success_color)
})

# Get the more button and connect click event
more_button = meta_card.get_more_button()
more_button.clicked.connect(lambda: print("More button clicked"))
```

### Complete Example

![MCard Demo](../_media/screenshots/MCard.png)

Here's a complete example demonstrating various uses of MCard and MMeta:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.card import MCard
from dayu_widgets.card import MMeta
from dayu_widgets.divider import MDivider
from dayu_widgets.flow_layout import MFlowLayout
from dayu_widgets.label import MLabel
from dayu_widgets.qt import MPixmap


class CardExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CardExample, self).__init__(parent)
        self.setWindowTitle("Examples for MCard")
        self._init_ui()

    def _init_ui(self):
        basic_card_lay = MFlowLayout()
        basic_card_lay.setSpacing(20)
        for setting in [
            {
                "title": "",
            },
            {"title": "Card Title", "size": dayu_theme.small},
            {"title": "Card Title", "image": MPixmap("app-houdini.png")},
            {
                "title": "Card Title",
                "extra": "More",
                "image": MPixmap("app-houdini.png"),
            },
            {
                "title": "Card Title",
                "extra": "More",
            },
        ]:
            card_0 = MCard(**setting)
            content_widget_0 = QtWidgets.QWidget()
            content_lay_0 = QtWidgets.QVBoxLayout()
            content_lay_0.setContentsMargins(15, 15, 15, 15)
            content_widget_0.setLayout(content_lay_0)
            for i in range(4):
                content_lay_0.addWidget(MLabel("Card Content {}".format(i + 1)))
            card_0.set_widget(content_widget_0)

            basic_card_lay.addWidget(card_0)

        meta_card_lay = MFlowLayout()
        meta_card_lay.setSpacing(20)
        for setting in [
            {
                "title": "Houdini",
                "description": "Side Effects Software's flagship product, an effective tool for creating advanced visual effects",
                "avatar": MPixmap("user_line.svg"),
                "cover": MPixmap("app-houdini.png"),
            },
            {
                "title": "Autodesk Maya",
                "description": "The world's leading software application for 3D digital animation and visual effects",
                "cover": MPixmap("app-maya.png"),
            },
        ]:
            meta_card = MMeta()
            meta_card.setup_data(setting)
            meta_card_lay.addWidget(meta_card)

        task_card_lay = QtWidgets.QVBoxLayout()
        for setting in [
            {
                "title": "Task A",
                "description": "demo pl_0010 Animation \n2019/04/01 - 2019/04/09",
                "avatar": MPixmap("success_line.svg", dayu_theme.success_color),
            },
            {
                "title": "Task B",
                "description": "#2 closed by xiao hua.",
                "avatar": MPixmap("error_line.svg", dayu_theme.error_color),
            },
            {
                "title": "Task C",
                "description": "#3 closed by xiao hua.",
                "avatar": MPixmap("warning_line.svg", dayu_theme.warning_color),
            },
        ]:
            meta_card = MMeta(extra=True)
            meta_card.setup_data(setting)
            task_card_lay.addWidget(meta_card)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic Card"))
        main_lay.addLayout(basic_card_lay)
        main_lay.addWidget(MDivider("Meta Card"))
        main_lay.addLayout(meta_card_lay)
        main_lay.addWidget(MDivider("Task Card"))
        main_lay.addLayout(task_card_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = CardExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### MCard

#### Constructor

```python
MCard(title=None, image=None, size=None, extra=None, type=None, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `title` | Card title | `str` | `None` |
| `image` | Icon next to the title | `QPixmap` | `None` |
| `size` | Card size | `int` | `dayu_theme.default_size` |
| `extra` | Text for extra action | `str` | `None` |
| `type` | Card type | `str` | `None` |
| `parent` | Parent widget | `QWidget` | `None` |

#### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `get_more_button()` | Get the more button | None | `MToolButton` |
| `set_widget(widget)` | Set the card content widget | `widget`: Content widget | None |
| `border()` | Set the card to display a border | None | `self` |

### MMeta

#### Constructor

```python
MMeta(cover=None, avatar=None, title=None, description=None, extra=False, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `cover` | Cover image | `QPixmap` | `None` |
| `avatar` | Avatar icon | `QPixmap` | `None` |
| `title` | Title | `str` | `None` |
| `description` | Description | `str` | `None` |
| `extra` | Whether to show extra action button | `bool` | `False` |
| `parent` | Parent widget | `QWidget` | `None` |

#### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `get_more_button()` | Get the more button | None | `MToolButton` |
| `setup_data(data_dict)` | Set the card data | `data_dict`: Data dictionary | None |

#### Data Dictionary

The `setup_data` method accepts a data dictionary that can contain the following keys:

| Key | Description | Type | Required |
| --- | --- | --- | --- |
| `cover` | Cover image | `QPixmap` | No |
| `avatar` | Avatar icon | `QPixmap` | No |
| `title` | Title | `str` | No |
| `description` | Description | `str` | No |

## Frequently Asked Questions

### How to add custom content to a card?

You can set the card's content widget using the `set_widget` method:

```python
from dayu_widgets.card import MCard
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# Create a card
card = MCard(title="Custom Content")

# Create content widget
content_widget = QtWidgets.QWidget()
content_layout = QtWidgets.QVBoxLayout()
content_layout.setContentsMargins(15, 15, 15, 15)
content_widget.setLayout(content_layout)

# Add custom content
content_layout.addWidget(MLabel("This is custom content"))
content_layout.addWidget(QtWidgets.QPushButton("Click Me"))

# Set card content
card.set_widget(content_widget)
```

### How to handle extra action button click events?

You can get the more button using the `get_more_button` method and then connect the click event:

```python
from dayu_widgets.card import MCard

# Create a card with an extra action
card = MCard(title="Card with Extra Action", extra="More")

# Get the more button and connect click event
more_button = card.get_more_button()
more_button.clicked.connect(lambda: print("More button clicked"))
```

### How to create different styles of cards?

MCard and MMeta provide different style options:

1. Basic card: Use MCard to create a basic card
2. Card with border: Use the `border()` method to create a card with a border
3. Card with icon: Set the `image` parameter to create a card with an icon
4. Card with extra action: Set the `extra` parameter to create a card with an extra action
5. Meta card: Use MMeta to create a meta card
6. Task card: Use MMeta and set different avatar icons to create a task card

```python
from dayu_widgets.card import MCard
from dayu_widgets.card import MMeta
from dayu_widgets.qt import MPixmap
from dayu_widgets import dayu_theme

# Basic card
basic_card = MCard(title="Basic Card")

# Card with border
border_card = MCard(title="Card with Border").border()

# Card with icon
icon_card = MCard(title="Card with Icon", image=MPixmap("app-houdini.png"))

# Card with extra action
extra_card = MCard(title="Card with Extra Action", extra="More")

# Meta card
meta_card = MMeta()
meta_card.setup_data({
    "title": "Houdini",
    "description": "Side Effects Software's flagship product",
    "cover": MPixmap("app-houdini.png")
})

# Task card
task_card = MMeta(extra=True)
task_card.setup_data({
    "title": "Task A",
    "description": "demo pl_0010 Animation",
    "avatar": MPixmap("success_line.svg", dayu_theme.success_color)
})
```
