#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################

import functools

from dayu_widgets import dayu_theme
from dayu_widgets.divider import MDivider
from dayu_widgets.flow_layout import MFlowLayout
from dayu_widgets.label import MLabel
from dayu_widgets.message import MMessage
from dayu_widgets.qt import QWidget, QHBoxLayout, QVBoxLayout
from dayu_widgets.tag import MTag, MCheckableTag, MNewTag


class MTagTest(QWidget):
    def __init__(self, parent=None):
        super(MTagTest, self).__init__(parent)
        self.setWindowTitle('Examples for MTag')
        self.default_lay = MFlowLayout()
        self.default_lay.addWidget(MTag(text='Tag 1'))
        self.default_lay.addWidget(MTag(text='Closeable Tag').closeable())
        add_tag = MNewTag('New Tag')
        add_tag.sig_add_tag.connect(self.slot_add_tag)
        self.default_lay.addWidget(add_tag)

        color_lay = MFlowLayout()
        for text, color in [
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
            tag = MTag(text=text).closeable()
            tag.set_dayu_color(color)
            tag.sig_closed.connect(
                functools.partial(MMessage.success, 'Delete "{}"'.format(text), self))
            color_lay.addWidget(tag)

        no_border_lay = MFlowLayout()
        for text, color in [('red', dayu_theme.red),
                            ('green', dayu_theme.green),
                            ('blue', dayu_theme.blue),
                            ('geekblue', dayu_theme.geekblue),
                            ('volcano', dayu_theme.volcano),
                            ('orange', dayu_theme.orange),
                            ('purple', dayu_theme.purple),
                            ('lime', dayu_theme.lime),
                            ]:
            tag = MTag(text=text).border(False).clickable()
            tag.set_dayu_color(color)
            tag.sig_clicked.connect(
                functools.partial(MMessage.success, 'Click "{}"'.format(text), self))
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
        main_lay.addWidget(MDivider('Border'))
        main_lay.addLayout(color_lay)
        main_lay.addWidget(MDivider('No Border & Click'))
        main_lay.addLayout(no_border_lay)
        main_lay.addWidget(MDivider('Checkable'))
        main_lay.addLayout(topic_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_add_tag(self, text):
        tag = MTag(text=text).closeable()
        self.default_lay.insertWidget(self.default_lay.count() - 1, tag)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    test = MTagTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
