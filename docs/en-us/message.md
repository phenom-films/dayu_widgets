# MMessage

MMessage is a global message component used to display operation feedback information. It appears centered at the top of the page and automatically disappears, suitable for lightweight prompts that don't interrupt user operations.

## Import

```python
from dayu_widgets.message import MMessage
```

## Examples

### Basic Usage

MMessage provides four different types of global messages: information, success, warning, and error.

```python
from dayu_widgets.message import MMessage

# Display an information message
MMessage.info("This is an information message", parent=self)

# Display a success message
MMessage.success("This is a success message", parent=self)

# Display a warning message
MMessage.warning("This is a warning message", parent=self)

# Display an error message
MMessage.error("This is an error message", parent=self)
```

### Custom Display Duration

MMessage automatically disappears after 2 seconds by default, but you can customize the display duration using the `duration` parameter.

```python
from dayu_widgets.message import MMessage

# Display a message that disappears after 5 seconds
MMessage.info("This message will be displayed for 5 seconds", parent=self, duration=5)
```

### Closable Message

MMessage supports creating closable messages that users can close early by clicking the close button.

```python
from dayu_widgets.message import MMessage

# Display a closable message
MMessage.info("This is a closable message", parent=self, closable=True)
```

### Loading Message

MMessage supports displaying messages with a loading animation, suitable for feedback during asynchronous operations.

```python
from dayu_widgets.message import MMessage
import functools

# Display a loading message
loading_message = MMessage.loading("Loading...", parent=self)

# Simulate completion of an asynchronous operation
# In a real application, you would close the loading message and display a result message in the callback of the asynchronous operation
loading_message.sig_closed.connect(functools.partial(MMessage.success, "Loading successful", self))
```

### Global Configuration

MMessage supports global configuration of the default display duration and distance from the top.

```python
from dayu_widgets.message import MMessage

# Set the default display duration to 1 second
MMessage.config(duration=1)

# Set the distance from the top to 50 pixels
MMessage.config(top=50)

# Set both the display duration and distance from the top
MMessage.config(duration=3, top=30)
```

### Complete Example

![MMessage Demo](../_media/screenshots/message.gif)

Here's a complete example demonstrating various uses of MMessage:

```python
# Import built-in modules
import functools

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel
from dayu_widgets.message import MMessage
from dayu_widgets.push_button import MPushButton


class MessageExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MessageExample, self).__init__(parent)
        self.setWindowTitle("Examples for MMessage")
        self._init_ui()

    def _init_ui(self):
        button3 = MPushButton(text="Normal Message").primary()
        button4 = MPushButton(text="Success Message").success()
        button5 = MPushButton(text="Warning Message").warning()
        button6 = MPushButton(text="Error Message").danger()
        button3.clicked.connect(functools.partial(self.slot_show_message, MMessage.info, {"text": "This is a normal message"}))
        button4.clicked.connect(functools.partial(self.slot_show_message, MMessage.success, {"text": "Congratulations, success!"}))
        button5.clicked.connect(functools.partial(self.slot_show_message, MMessage.warning, {"text": "I'm warning you!"}))
        button6.clicked.connect(functools.partial(self.slot_show_message, MMessage.error, {"text": "Failed!"}))

        sub_lay1 = QtWidgets.QHBoxLayout()
        sub_lay1.addWidget(button3)
        sub_lay1.addWidget(button4)
        sub_lay1.addWidget(button5)
        sub_lay1.addWidget(button6)

        button_duration = MPushButton(text="Show 5s Message")
        button_duration.clicked.connect(
            functools.partial(
                self.slot_show_message,
                MMessage.info,
                {"text": "This message will be displayed for 5 seconds", "duration": 5},
            )
        )
        button_closable = MPushButton(text="Closable Message")
        button_closable.clicked.connect(
            functools.partial(
                self.slot_show_message,
                MMessage.info,
                {"text": "This message can be closed manually", "closable": True},
            )
        )
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("different type"))
        main_lay.addLayout(sub_lay1)
        main_lay.addWidget(MLabel("Different message types: normal, success, warning, error. Default disappears after 2 seconds"))
        main_lay.addWidget(MDivider("set duration"))
        main_lay.addWidget(button_duration)
        main_lay.addWidget(MLabel("Custom duration, set duration value in config, unit is seconds"))

        main_lay.addWidget(MDivider("set closable"))
        main_lay.addWidget(button_closable)
        main_lay.addWidget(MLabel("Set whether it can be closed, set closable to True in config"))

        button_grp = MPushButtonGroup()
        button_grp.set_button_list(
            [
                {
                    "text": "set duration to 1s",
                    "clicked": functools.partial(self.slot_set_config, MMessage.config, {"duration": 1}),
                },
                {
                    "text": "set duration to 10s",
                    "clicked": functools.partial(self.slot_set_config, MMessage.config, {"duration": 10}),
                },
                {
                    "text": "set top to 5",
                    "clicked": functools.partial(self.slot_set_config, MMessage.config, {"top": 5}),
                },
                {
                    "text": "set top to 50",
                    "clicked": functools.partial(self.slot_set_config, MMessage.config, {"top": 50}),
                },
            ]
        )
        loading_button = MPushButton("Display a loading indicator")
        loading_button.clicked.connect(self.slot_show_loading)
        main_lay.addWidget(MDivider("set global setting"))
        main_lay.addWidget(button_grp)
        main_lay.addWidget(MLabel("Global setting default duration (default 2 seconds); top (distance from parent top, default 24px)"))
        main_lay.addWidget(loading_button)

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(parent=self, **config)

    def slot_set_config(self, func, config):
        func(**config)

    def slot_show_loading(self):
        msg = MMessage.loading("Loading...", parent=self)
        msg.sig_closed.connect(functools.partial(MMessage.success, "Loading successful!!", self))


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = MessageExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Class Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `info(text, parent, duration=None, closable=None)` | Display an information message | `text`: Message text<br>`parent`: Parent widget<br>`duration`: Display duration (seconds)<br>`closable`: Whether closable | `MMessage` instance |
| `success(text, parent, duration=None, closable=None)` | Display a success message | `text`: Message text<br>`parent`: Parent widget<br>`duration`: Display duration (seconds)<br>`closable`: Whether closable | `MMessage` instance |
| `warning(text, parent, duration=None, closable=None)` | Display a warning message | `text`: Message text<br>`parent`: Parent widget<br>`duration`: Display duration (seconds)<br>`closable`: Whether closable | `MMessage` instance |
| `error(text, parent, duration=None, closable=None)` | Display an error message | `text`: Message text<br>`parent`: Parent widget<br>`duration`: Display duration (seconds)<br>`closable`: Whether closable | `MMessage` instance |
| `loading(text, parent)` | Display a loading message | `text`: Message text<br>`parent`: Parent widget | `MMessage` instance |
| `config(duration=None, top=None)` | Global configuration | `duration`: Default display duration (seconds)<br>`top`: Distance from the top (pixels) | None |

### Class Constants

| Constant | Description | Value |
| --- | --- | --- |
| `InfoType` | Information type | `"info"` |
| `SuccessType` | Success type | `"success"` |
| `WarningType` | Warning type | `"warning"` |
| `ErrorType` | Error type | `"error"` |
| `LoadingType` | Loading type | `"loading"` |

### Signals

| Signal | Description | Parameters |
| --- | --- | --- |
| `sig_closed` | Triggered when the message is closed | None |

### Default Configuration

| Configuration Item | Description | Default Value |
| --- | --- | --- |
| `duration` | Default display duration (seconds) | `2` |
| `top` | Distance from the top (pixels) | `24` |

## Frequently Asked Questions

### How to display different types of messages?

You can display different types of messages using MMessage's class methods:

```python
from dayu_widgets.message import MMessage

# Display an information message
MMessage.info("This is an information message", parent=self)

# Display a success message
MMessage.success("This is a success message", parent=self)

# Display a warning message
MMessage.warning("This is a warning message", parent=self)

# Display an error message
MMessage.error("This is an error message", parent=self)
```

### How to customize the display duration of a message?

You can customize the display duration of a message using the `duration` parameter:

```python
from dayu_widgets.message import MMessage

# Display a message that disappears after 5 seconds
MMessage.info("This message will be displayed for 5 seconds", parent=self, duration=5)
```

### How to create a closable message?

You can create a closable message using the `closable` parameter:

```python
from dayu_widgets.message import MMessage

# Display a closable message
MMessage.info("This is a closable message", parent=self, closable=True)
```

### How to globally configure the default behavior of messages?

You can globally configure the default behavior of messages using the `config` method:

```python
from dayu_widgets.message import MMessage

# Set the default display duration to 1 second
MMessage.config(duration=1)

# Set the distance from the top to 50 pixels
MMessage.config(top=50)

# Set both the display duration and distance from the top
MMessage.config(duration=3, top=30)
```

### How to display a result message after an asynchronous operation is completed?

You can use the `sig_closed` signal to display a result message after an asynchronous operation is completed:

```python
from dayu_widgets.message import MMessage
import functools

# Display a loading message
loading_message = MMessage.loading("Loading...", parent=self)

# Simulate an asynchronous operation
def async_operation():
    # Close the loading message and display a result message after the asynchronous operation is completed
    loading_message.close()
    MMessage.success("Operation successful", parent=self)

# Or use signal connection
loading_message.sig_closed.connect(functools.partial(MMessage.success, "Operation successful", self))
```
