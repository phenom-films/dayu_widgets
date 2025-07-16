# MLoading

MLoading is a component for displaying loading animations, providing a rotating icon to indicate ongoing operations. Additionally, the MLoadingWrapper component can add a loading state mask to any widget.

## Import

```python
from dayu_widgets.loading import MLoading
from dayu_widgets.loading import MLoadingWrapper
```

## Examples

### Basic Usage

MLoading can be used directly, displaying a rotating loading icon by default.

```python
from dayu_widgets.loading import MLoading

# Create a loading animation with default size
loading = MLoading()
```

### Different Sizes

MLoading provides five sizes: tiny, small, medium (default), large, and huge.

```python
from dayu_widgets.loading import MLoading

# Create loading animations with different sizes
tiny_loading = MLoading.tiny()
small_loading = MLoading.small()
medium_loading = MLoading.medium()  # Same as MLoading()
large_loading = MLoading.large()
huge_loading = MLoading.huge()
```

### Custom Colors

MLoading supports custom colors, allowing you to set the color of the loading icon through parameters.

```python
from dayu_widgets.loading import MLoading

# Create loading animations with different colors
cyan_loading = MLoading.tiny(color="#13c2c2")
green_loading = MLoading.tiny(color="#52c41a")
magenta_loading = MLoading.tiny(color="#eb2f96")
red_loading = MLoading.tiny(color="#f5222d")
yellow_loading = MLoading.tiny(color="#fadb14")
volcano_loading = MLoading.tiny(color="#fa541c")
```

### Loading Wrapper

MLoadingWrapper can add a loading state mask to any widget. When set to loading state, it displays a semi-transparent mask and a loading animation.

```python
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.label import MLabel
from qtpy import QtWidgets

# Create a label
label = MLabel("This is a label")
label.setFixedSize(200, 200)

# Create a loading wrapper for the label
loading_wrapper = MLoadingWrapper(label, loading=False)

# Set to loading state
loading_wrapper.set_dayu_loading(True)

# Cancel loading state
loading_wrapper.set_dayu_loading(False)
```

### Using with Threads

MLoadingWrapper is often used with threads to display loading state during data loading.

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton

# Create a worker thread
class WorkThread(QtCore.QThread):
    def run(self):
        # Simulate time-consuming operation
        QtCore.QThread.sleep(3)

# Create a widget
widget = QtWidgets.QTableView()

# Create a loading wrapper
loading_wrapper = MLoadingWrapper(widget=widget, loading=False)

# Create a thread
thread = WorkThread()

# Connect signals
thread.started.connect(functools.partial(loading_wrapper.set_dayu_loading, True))
thread.finished.connect(functools.partial(loading_wrapper.set_dayu_loading, False))

# Create a button to start the thread
button = MPushButton(text="Load Data")
button.clicked.connect(thread.start)
```

### Complete Example

![MLoading Demo](../_media/screenshots/mloading.gif)

The following is a complete example that demonstrates all features of MLoading:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.loading import MLoading
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton


class LoadingExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(LoadingExample, self).__init__(parent)
        self.setWindowTitle("Examples for MLoading")
        self._init_ui()

    def _init_ui(self):
        size_lay = QtWidgets.QHBoxLayout()
        size_list = [
            ("Huge", MLoading.huge),
            ("Large", MLoading.large),
            ("Medium", MLoading.medium),
            ("Small", MLoading.small),
            ("Tiny", MLoading.tiny),
        ]
        for label, cls in size_list:
            size_lay.addWidget(MLabel(label))
            size_lay.addWidget(cls())
            size_lay.addSpacing(10)

        color_lay = QtWidgets.QHBoxLayout()
        color_list = [
            ("cyan", "#13c2c2"),
            ("green", "#52c41a"),
            ("magenta", "#eb2f96"),
            ("red", "#f5222d"),
            ("yellow", "#fadb14"),
            ("volcano", "#fa541c"),
        ]
        for label, color in color_list:
            color_lay.addWidget(MLabel(label))
            color_lay.addWidget(MLoading.tiny(color=color))
            color_lay.addSpacing(10)

        # Create a label for demonstrating MLoadingWrapper
        demo_label = MLabel("This is a label, click the button below to toggle loading state")
        demo_label.setFixedSize(300, 100)
        wrapper = MLoadingWrapper(demo_label, loading=False)

        # Create a button to control loading state
        button = MPushButton("Toggle Loading State")
        button.clicked.connect(lambda: wrapper.set_dayu_loading(not wrapper.get_dayu_loading()))

        wrapper_lay = QtWidgets.QVBoxLayout()
        wrapper_lay.addWidget(wrapper)
        wrapper_lay.addWidget(button)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Different Sizes"))
        main_lay.addLayout(size_lay)
        main_lay.addWidget(MDivider("Different Colors"))
        main_lay.addLayout(color_lay)
        main_lay.addWidget(MDivider("Loading Wrapper"))
        main_lay.addLayout(wrapper_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = LoadingExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### MLoading

#### Constructor

```python
MLoading(size=None, color=None, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `size` | Size of the loading animation | `int` | `dayu_theme.default_size` |
| `color` | Color of the loading animation | `str` | `dayu_theme.primary_color` |
| `parent` | Parent window | `QWidget` | `None` |

#### Class Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `tiny(color=None)` | Create a tiny loading animation | `color`: Color, optional | `MLoading` instance |
| `small(color=None)` | Create a small loading animation | `color`: Color, optional | `MLoading` instance |
| `medium(color=None)` | Create a medium loading animation | `color`: Color, optional | `MLoading` instance |
| `large(color=None)` | Create a large loading animation | `color`: Color, optional | `MLoading` instance |
| `huge(color=None)` | Create a huge loading animation | `color`: Color, optional | `MLoading` instance |

### MLoadingWrapper

#### Constructor

```python
MLoadingWrapper(widget, loading=True, parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `widget` | Widget to wrap | `QWidget` | - |
| `loading` | Initial loading state | `bool` | `True` |
| `parent` | Parent window | `QWidget` | `None` |

#### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_dayu_loading(loading)` | Set loading state | `loading`: Whether to show loading animation | `None` |
| `get_dayu_loading()` | Get current loading state | None | `bool` |

#### Properties

| Property | Description | Type | Default Value |
| --- | --- | --- | --- |
| `dayu_loading` | Current loading state | `bool` | - |

## Frequently Asked Questions

### How to change the color of the loading animation?

MLoading supports custom colors, which can be set through the `color` parameter when creating:

```python
from dayu_widgets.loading import MLoading

# Use hexadecimal color code
loading1 = MLoading(color="#1890ff")

# You can also set color when using class methods
loading2 = MLoading.tiny(color="#f5222d")
```

### How to display a loading animation when loading data?

MLoadingWrapper is often used with threads to display loading state during data loading:

```python
from dayu_widgets.loading import MLoadingWrapper
from qtpy import QtCore
import functools

# Create a widget
widget = QtWidgets.QTableView()

# Create a loading wrapper
loading_wrapper = MLoadingWrapper(widget=widget, loading=False)

# Create a thread
thread = QtCore.QThread()

# Connect signals
thread.started.connect(functools.partial(loading_wrapper.set_dayu_loading, True))
thread.finished.connect(functools.partial(loading_wrapper.set_dayu_loading, False))
```

### How to add loading state to custom widgets?

MLoadingWrapper can wrap any QWidget subclass to add loading state:

```python
from dayu_widgets.loading import MLoadingWrapper
from qtpy import QtWidgets

# Create a custom widget
custom_widget = QtWidgets.QWidget()
custom_layout = QtWidgets.QVBoxLayout()
custom_widget.setLayout(custom_layout)
custom_layout.addWidget(QtWidgets.QLabel("Custom Content"))

# Create a loading wrapper
wrapper = MLoadingWrapper(custom_widget, loading=False)

# Set to loading state
wrapper.set_dayu_loading(True)
```
