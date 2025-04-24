# MPage

MPage is a pagination component used to divide long list data into multiple pages, loading only one page of data at a time, improving application performance and user experience.

## Import

```python
from dayu_widgets.page import MPage
```

## Examples

### Basic Usage

MPage can set the total number of data items through the `set_total` method and listen for page changes through the `sig_page_changed` signal:

```python
from dayu_widgets.page import MPage

# Create a pagination component
page = MPage()

# Set the total number of data items
page.set_total(255)

# Listen for page changes
page.sig_page_changed.connect(lambda page_size, current_page: print(f"{page_size} items per page, current page {current_page}"))
```

### Custom Page Size Options

MPage provides default options for 25, 50, 75, and 100 items per page. You can customize these options through the `set_page_config` method:

```python
from dayu_widgets.page import MPage

# Create a pagination component
page = MPage()

# Set the total number of data items
page.set_total(255)

# Customize page size options
page.set_page_config([
    {"label": "10 items/page", "value": 10},
    {"label": "20 items/page", "value": 20},
    {"label": "30 items/page", "value": 30},
    {"label": "50 items/page", "value": 50}
])
```

### Using with Data Tables

MPage is often used with data tables. Here's a simple example:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.page import MPage
from dayu_widgets.table_view import MTableView


class PageTableExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PageTableExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        # Create table
        self.table_view = MTableView()
        self.model = QtWidgets.QStandardItemModel()
        self.table_view.setModel(self.model)

        # Create pagination component
        self.page = MPage()
        self.page.set_total(255)
        self.page.sig_page_changed.connect(self.slot_page_changed)

        # Initialize layout
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(self.table_view)
        main_lay.addWidget(self.page)
        self.setLayout(main_lay)

        # Load first page data
        self.slot_page_changed(self.page.field("page_size_selected"), 1)

    def slot_page_changed(self, page_size, current_page):
        # Clear table
        self.model.clear()

        # Set headers
        self.model.setHorizontalHeaderLabels(["ID", "Name", "Description"])

        # Calculate start index for current page
        start_index = (current_page - 1) * page_size

        # Load current page data
        for i in range(page_size):
            index = start_index + i
            if index < self.page.field("total"):
                self.model.appendRow([
                    QtWidgets.QStandardItem(str(index + 1)),
                    QtWidgets.QStandardItem(f"Item {index + 1}"),
                    QtWidgets.QStandardItem(f"This is the description for item {index + 1}")
                ])
```

### Complete Example

![MPage Demo](../_media/screenshots/MPage.gif)

Here's a complete example demonstrating the basic usage of MPage:

```python
# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets.divider import MDivider
from dayu_widgets.page import MPage


class PageExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PageExample, self).__init__(parent)
        self.setWindowTitle("Examples for MPage")
        self._init_ui()

    def _init_ui(self):
        # Create first pagination component
        page_1 = MPage()
        page_1.set_total(255)
        page_1.sig_page_changed.connect(self.slot_page_changed)

        # Create second pagination component with custom page size options
        page_2 = MPage()
        page_2.set_total(100)
        page_2.set_page_config([
            {"label": "10 items/page", "value": 10},
            {"label": "20 items/page", "value": 20},
            {"label": "30 items/page", "value": 30}
        ])
        page_2.sig_page_changed.connect(self.slot_page_changed)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Basic Example"))
        main_lay.addWidget(page_1)
        main_lay.addWidget(MDivider("Custom Page Size"))
        main_lay.addWidget(page_2)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_page_changed(self, page_size, current_page):
        print(f"{page_size} items per page, current page {current_page}")


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = PageExample()
        dayu_theme.apply(test)
        test.show()
```

## API

### Constructor

```python
MPage(parent=None)
```

| Parameter | Description | Type | Default Value |
| --- | --- | --- | --- |
| `parent` | Parent widget | `QWidget` | `None` |

### Methods

| Method | Description | Parameters | Return Value |
| --- | --- | --- | --- |
| `set_total(value)` | Set the total number of data items | `value`: Total number of items | None |
| `set_page_config(data_list)` | Set page size options | `data_list`: List of page size options | None |
| `field(name)` | Get field value | `name`: Field name | Field value |
| `set_field(name, value)` | Set field value | `name`: Field name<br>`value`: Field value | None |

### Signals

| Signal | Description | Parameters |
| --- | --- | --- |
| `sig_page_changed` | Triggered when page changes | `page_size`: Items per page<br>`current_page`: Current page number |

### Fields

MPage uses MFieldMixin to manage internal state. Here are the main fields:

| Field | Description | Type | Default Value |
| --- | --- | --- | --- |
| `page_size_selected` | Currently selected page size | `int` | `25` |
| `page_size_list` | List of page size options | `list` | Preset options list |
| `total` | Total number of data items | `int` | `0` |
| `current_page` | Current page number | `int` | `0` |
| `total_page` | Total number of pages | `int` | Calculated |
| `display_text` | Display text | `str` | Calculated |

## Frequently Asked Questions

### How to get the current page number and page size?

You can get the current page number and page size through the `field` method:

```python
page = MPage()
page.set_total(255)

# Get current page number
current_page = page.field("current_page")

# Get page size
page_size = page.field("page_size_selected")
```

### How to manually set the current page number?

You can set the current page number through the `set_field` method:

```python
page = MPage()
page.set_total(255)

# Set current page number to 3
page.set_field("current_page", 3)
```

### How to calculate the total number of pages?

The total number of pages is automatically calculated based on the total number of data items and the page size. You can get it through the `field` method:

```python
page = MPage()
page.set_total(255)

# Get total number of pages
total_page = page.field("total_page")
```

### How to customize the display text for page size options?

You can set the `label` and `value` for each option in the `set_page_config` method:

```python
page = MPage()
page.set_page_config([
    {"label": "10 - Fastest", "value": 10},
    {"label": "20 - Fast", "value": 20},
    {"label": "50 - Medium", "value": 50},
    {"label": "100 - Slow", "value": 100}
])
```
