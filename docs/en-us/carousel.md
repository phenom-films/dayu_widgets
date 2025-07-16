# MCarousel

MCarousel is a carousel component used to cycle through content of the same type, such as images or text, in a limited space. It provides automatic playback and manual switching functionality, suitable for displaying slideshows, advertisements, and other content.

## Import

```python
from dayu_widgets.carousel import MCarousel
```

## Examples

### Basic Usage

MCarousel can create a simple image carousel component.

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component
carousel = MCarousel(images, width=300, height=300)
```

### Autoplay

MCarousel enables autoplay by default, which can be controlled using the `set_autoplay` method.

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create an autoplay carousel component
carousel = MCarousel(images, autoplay=True, width=300, height=300)

# Stop autoplay
carousel.set_autoplay(False)

# Restart autoplay
carousel.set_autoplay(True)
```

### Setting the Interval

MCarousel can set the autoplay interval using the `set_interval` method.

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component
carousel = MCarousel(images, autoplay=True, width=300, height=300)

# Set the interval to 5 seconds
carousel.set_interval(5000)
```

### Manual Page Switching

MCarousel provides `next_page` and `pre_page` methods for manual page switching, as well as a `go_to_page` method for jumping to a specific page.

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap
from dayu_widgets.push_button import MPushButton
from qtpy import QtWidgets

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component
carousel = MCarousel(images, autoplay=False, width=300, height=300)

# Create control buttons
prev_button = MPushButton("Previous")
next_button = MPushButton("Next")
page1_button = MPushButton("Page 1")
page2_button = MPushButton("Page 2")
page3_button = MPushButton("Page 3")

# Connect signals
prev_button.clicked.connect(carousel.pre_page)
next_button.clicked.connect(carousel.next_page)
page1_button.clicked.connect(lambda: carousel.go_to_page(0))
page2_button.clicked.connect(lambda: carousel.go_to_page(1))
page3_button.clicked.connect(lambda: carousel.go_to_page(2))

# Create layout
button_layout = QtWidgets.QHBoxLayout()
button_layout.addWidget(prev_button)
button_layout.addWidget(page1_button)
button_layout.addWidget(page2_button)
button_layout.addWidget(page3_button)
button_layout.addWidget(next_button)

main_layout = QtWidgets.QVBoxLayout()
main_layout.addWidget(carousel)
main_layout.addLayout(button_layout)
```

### Interacting with Widgets

MCarousel can interact with other widgets, such as switches and sliders.

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap
from dayu_widgets.switch import MSwitch
from dayu_widgets.slider import MSlider
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component
carousel = MCarousel(images, autoplay=True, width=300, height=300)

# Create a control switch
switch = MSwitch()
switch.setChecked(True)
switch.toggled.connect(carousel.set_autoplay)

# Create an interval slider
slider = MSlider()
slider.setRange(1, 10)
slider.setValue(3)
slider.valueChanged.connect(lambda x: carousel.set_interval(x * 1000))

# Create layout
switch_layout = QtWidgets.QFormLayout()
switch_layout.addRow(MLabel("AutoPlay"), switch)
switch_layout.addRow(MLabel("Interval"), slider)

main_layout = QtWidgets.QVBoxLayout()
main_layout.addWidget(carousel)
main_layout.addLayout(switch_layout)
```

### Complete Example

![MCarousel Demo](../_media/screenshots/MCarousel.gif)

Here's a complete example demonstrating various uses of MCarousel:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.carousel import MCarousel
from dayu_widgets.label import MLabel
from dayu_widgets.qt import MPixmap
from dayu_widgets.slider import MSlider
from dayu_widgets.switch import MSwitch


class CarouselExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CarouselExample, self).__init__(parent)
        self.setWindowTitle("Examples for MCarousel")
        self._init_ui()

    def _init_ui(self):
        switch = MSwitch()
        switch.setChecked(True)
        slider = MSlider()
        slider.setRange(1, 10)
        switch_lay = QtWidgets.QFormLayout()
        switch_lay.addRow(MLabel("AutoPlay"), switch)
        switch_lay.addRow(MLabel("Interval"), slider)
        test = MCarousel(
            [MPixmap("app-{}.png".format(a)) for a in ["maya", "nuke", "houdini"]],
            width=300,
            height=300,
            autoplay=True,
        )
        switch.toggled.connect(test.set_autoplay)
        slider.valueChanged.connect(lambda x: test.set_interval(x * 1000))
        slider.setValue(3)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(test)
        main_lay.addLayout(switch_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = CarouselExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MCarousel(pix_list, autoplay=True, width=500, height=500, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `pix_list` | List of images | `List[QPixmap]` | - |
| `autoplay` | Whether to autoplay | `bool` | `True` |
| `width` | Component width | `int` | `500` |
| `height` | Component height | `int` | `500` |
| `parent` | Parent widget | `QWidget` | `None` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_autoplay(value)` | Set whether to autoplay | `value`: Boolean | None |
| `set_interval(ms)` | Set the autoplay interval | `ms`: Milliseconds | None |
| `next_page()` | Switch to the next page | None | None |
| `pre_page()` | Switch to the previous page | None | None |
| `go_to_page(index)` | Jump to a specific page | `index`: Page index | None |

### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `autoplay` | Whether to autoplay | `bool` | `True` |

## Frequently Asked Questions

### How to change the image size?

MCarousel automatically adjusts the image size to fit the component's width and height. You can specify the width and height when creating MCarousel:

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component with a specific size
carousel = MCarousel(images, width=400, height=300)
```

### How to control autoplay?

You can control autoplay using the `set_autoplay` method:

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component
carousel = MCarousel(images, autoplay=True)

# Stop autoplay
carousel.set_autoplay(False)

# Restart autoplay
carousel.set_autoplay(True)
```

### How to change the autoplay interval?

You can change the autoplay interval using the `set_interval` method:

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component
carousel = MCarousel(images, autoplay=True)

# Set the interval to 5 seconds
carousel.set_interval(5000)
```

### How to manually switch pages?

You can manually switch pages using the `next_page`, `pre_page`, and `go_to_page` methods:

```python
from dayu_widgets.carousel import MCarousel
from dayu_widgets.qt import MPixmap

# Create a list of images
images = [
    MPixmap("app-maya.png"),
    MPixmap("app-nuke.png"),
    MPixmap("app-houdini.png")
]

# Create a carousel component
carousel = MCarousel(images, autoplay=False)

# Switch to the next page
carousel.next_page()

# Switch to the previous page
carousel.pre_page()

# Jump to the second page (index starts from 0)
carousel.go_to_page(1)
```
