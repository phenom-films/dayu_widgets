#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from Qt import QtWidgets

# Import local modules
from dayu_widgets import utils
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.item_view_full_set import MItemViewFullSet
from dayu_widgets.push_button import MPushButton
import examples._mock_data as mock


@utils.add_settings("DaYu", "DaYuExample", event_name="hideEvent")
class ItemViewFullSetExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(ItemViewFullSetExample, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        item_view_set_table = MItemViewFullSet()
        item_view_set_table.set_header_list(mock.header_list)

        item_view_set_all = MItemViewFullSet(big_view=True)
        item_view_set_all.set_header_list(mock.header_list)

        refresh_button = MPushButton("Refresh Data")
        refresh_button.clicked.connect(self.slot_update_data)
        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("Only Table View"))
        main_lay.addWidget(refresh_button)
        main_lay.addWidget(item_view_set_table)
        main_lay.addWidget(MDivider("Table View and Big View"))
        main_lay.addWidget(item_view_set_all)
        self.setLayout(main_lay)

        self.view_list = [
            item_view_set_table,
            item_view_set_all,
        ]
        self.bind(
            "item_view_full_set_example_header_state",
            item_view_set_table.table_view.header_view,
            "state",
        )
        self.slot_update_data()

    def slot_update_data(self):
        for view in self.view_list:
            view.setup_data(mock.data_list)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets import dayu_theme
    from dayu_widgets.qt import application

    with application() as app:
        test = ItemViewFullSetExample()
        dayu_theme.apply(test)
        test.show()
