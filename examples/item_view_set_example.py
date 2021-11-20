#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
# Import built-in modules
import functools

# Import third-party modules
import examples._mock_data as mock

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.alert import MAlert
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_view_set import MItemViewSet
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget


class ItemViewSetExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ItemViewSetExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        item_view_set_table = MItemViewSet(view_type=MItemViewSet.TableViewType)
        item_view_set_table.set_header_list(mock.header_list)
        item_view_set_list = MItemViewSet(view_type=MItemViewSet.ListViewType)
        item_view_set_list.set_header_list(mock.header_list)
        item_view_set_tree = MItemViewSet(view_type=MItemViewSet.TreeViewType)
        item_view_set_tree.set_header_list(mock.header_list)
        item_view_set_thumbnail = MItemViewSet(view_type=MItemViewSet.BigViewType)
        item_view_set_thumbnail.set_header_list(mock.header_list)

        item_view_set_search = MItemViewSet(view_type=MItemViewSet.TreeViewType)
        item_view_set_search.set_header_list(mock.header_list)
        item_view_set_search.searchable()
        expand_button = MPushButton("Expand All")
        expand_button.clicked.connect(item_view_set_search.item_view.expandAll)
        coll_button = MPushButton("Collapse All")
        coll_button.clicked.connect(item_view_set_search.item_view.collapseAll)
        item_view_set_search.insert_widget(coll_button)
        item_view_set_search.insert_widget(expand_button)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider("Table View"))
        main_lay.addWidget(item_view_set_table)
        main_lay.addWidget(MDivider("List View"))
        main_lay.addWidget(item_view_set_list)
        main_lay.addWidget(MDivider("Tree View"))
        main_lay.addWidget(item_view_set_tree)
        main_lay.addWidget(MDivider("Big View"))
        main_lay.addWidget(item_view_set_thumbnail)
        main_lay.addWidget(MDivider("With Search line edit"))
        main_lay.addWidget(item_view_set_search)
        main_lay.addStretch()
        self.setLayout(main_lay)

        item_view_set_table.setup_data((mock.data_list))
        item_view_set_list.setup_data((mock.data_list))
        item_view_set_tree.setup_data((mock.tree_data_list))
        item_view_set_thumbnail.setup_data((mock.data_list))
        item_view_set_search.setup_data((mock.tree_data_list))


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import local modules
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = ItemViewSetExample()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
