#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.MTag import MTag, MCheckableTag, MAddTag
from dayu_widgets.MFlowLayout import MFlowLayout
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MLabel import MLabel
from dayu_widgets.qt import *
from dayu_widgets import dayu_theme
from dayu_widgets.MMessage import MMessage

import functools


class MTagTest(QWidget):
    def __init__(self, parent=None):
        super(MTagTest, self).__init__(parent)
        self.default_lay = MFlowLayout()
        for t in ['Tag 1', 'Tag 2', 'Tag 3']:
            self.default_lay.addWidget(MTag(text=t))
        add_tag = MAddTag('Add Tag')
        add_tag.sig_add_tag.connect(self.slot_add_tag)
        self.default_lay.addWidget(add_tag)

        color_lay = MFlowLayout()
        for t, c in [
            ('magenta', dayu_theme.magenta),
            ('red', dayu_theme.red),
            ('volcano', dayu_theme.volcano),
            ('orange', dayu_theme.orange),
            ('gold', dayu_theme.gold),
            ('lime', dayu_theme.lime),
            ('green', dayu_theme.green),
            ('cyan', dayu_theme.cyan),
            ('blue', dayu_theme.blue),
            ('geekblue', dayu_theme.geekblue),
            ('purple', dayu_theme.purple),
        ]:
            tag = MTag(text=t, color=c, closable=True)
            tag.sig_closed.connect(functools.partial(MMessage.success, 'Delete "{}" tag success.'.format(t), self))
            color_lay.addWidget(tag)

        no_border_lay = MFlowLayout()
        for t, c in [('red', dayu_theme.red),
                     ('green', dayu_theme.green),
                     ('blue', dayu_theme.blue),
                     ('geekblue', dayu_theme.geekblue),
                     ('volcano', dayu_theme.volcano),
                     ('orange', dayu_theme.orange),
                     ('purple', dayu_theme.purple),
                     ('lime', dayu_theme.lime),
                     ]:
            tag = MTag(text=t, color=c, border=False)
            tag.sig_clicked.connect(functools.partial(MMessage.success, 'You clicked "{}" tag.'.format(t), self))
            no_border_lay.addWidget(tag)

        label = MLabel('Categories:')
        topic_lay = QHBoxLayout()
        topic_lay.addWidget(label)
        for i in ['Movies', 'Books', 'Music', 'Sports']:
            topic_lay.addWidget(MCheckableTag(text=i))
        topic_lay.addStretch()
        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('Normal'))
        main_lay.addLayout(self.default_lay)
        main_lay.addWidget(MDivider('Colorful'))
        main_lay.addLayout(color_lay)
        main_lay.addWidget(MDivider('No Border'))
        main_lay.addLayout(no_border_lay)
        main_lay.addWidget(MDivider('Checkable'))
        main_lay.addLayout(topic_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_add_tag(self, text):
        tag = MTag(text=text, closable=True)
        self.default_lay.insertWidget(self.default_lay.count() - 1, tag)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MTagTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
