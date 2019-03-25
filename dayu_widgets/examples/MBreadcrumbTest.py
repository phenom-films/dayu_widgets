#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets.MBreadcrumb import MBreadcrumb
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MMessage import MMessage
from dayu_widgets import dayu_theme
from dayu_widgets.qt import *


class MBreadcrumbTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MBreadcrumbTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        size_list = [('Huge', dayu_theme.size.huge),
                     ('Large', dayu_theme.size.large),
                     ('Medium', dayu_theme.size.medium),
                     ('Small', dayu_theme.size.small),
                     ('Tiny', dayu_theme.size.tiny)]
        entity_list = [
            {'text': 'Demo Project',
             'clicked': functools.partial(self.slot_show_message, MMessage.info, 'Go to "Demo Project"'),
             'icon': MIcon('cloud_line.svg')},
            {'text': 'pl',
             'clicked': functools.partial(self.slot_show_message, MMessage.info, 'Go to Sequence "pl"'),
             'icon': MIcon('female.svg')},
            {'text': 'pl_0010',
             'clicked': functools.partial(self.slot_show_message, MMessage.info, 'Go to Shot "pl_0010"'),
             'icon': MIcon('folder_line.svg')}
        ]
        no_icon_eg = MBreadcrumb()
        no_icon_eg.set_item_list([data_dict.get('text') for data_dict in entity_list])

        with_icon_eg = MBreadcrumb()
        with_icon_eg.set_item_list(entity_list)

        separator_eg = MBreadcrumb(separator='=>')
        separator_eg.set_item_list(entity_list)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('no icon'))
        main_lay.addWidget(no_icon_eg)
        main_lay.addWidget(MDivider('with icon'))
        main_lay.addWidget(with_icon_eg)
        main_lay.addWidget(MDivider('separator: =>'))
        main_lay.addWidget(separator_eg)

        for label, size in size_list:
            bread = MBreadcrumb(size=size)
            bread.set_item_list(entity_list)
            main_lay.addWidget(MDivider(label))
            main_lay.addWidget(bread)

        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_show_message(self, func, config):
        func(config, parent=self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MBreadcrumbTest()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
