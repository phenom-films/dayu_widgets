#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.label import MLabel, MLabel
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, Qt, QLabel, QSizePolicy


class LabelExample(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(LabelExample, self).__init__(parent)
        self.setWindowTitle('Examples for MLabel')
        self._init_ui()

    def _init_ui(self):
        tilte_lay = QGridLayout()
        data_list = [
            (MLabel.h1, u'一级标题', 'h1 Level'),
            (MLabel.h2, u'二级标题', 'h2 Level'),
            (MLabel.h3, u'三级标题', 'h3 Level'),
            (MLabel.h4, u'四级标题', 'h4 Level'),
        ]
        for row, data in enumerate(data_list):
            cls, title1, title2 = data
            tilte_lay.addWidget(cls(text=title1), row, 0)
            tilte_lay.addWidget(cls(text=title2), row, 1)

        text_type_lay = QHBoxLayout()
        for text, cls in (('Normal', MLabel),
                          ('Secondary', MLabel.secondary),
                          ('Warning', MLabel.warning),
                          ('Danger', MLabel.danger)):
            ins = cls('MText: ' + text)
            text_type_lay.addWidget(ins)
        disable_text = MLabel(text='MText: Disabled')
        disable_text.setEnabled(False)
        text_type_lay.addWidget(disable_text)
        text_attr_lay = QHBoxLayout()
        for text, cls in (('Mark', MLabel.mark),
                          ('Code', MLabel.code),
                          ('Underline', MLabel.underline),
                          ('Delete', MLabel.delete),
                          ('Strong', MLabel.strong),
                           ):
            ins = cls('MText: ' + text)
            text_attr_lay.addWidget(ins)

        data_bind_lay = QHBoxLayout()
        data_bind_label = MLabel()
        button = MPushButton.primary(text='Random An Animal')
        button.clicked.connect(self.slot_change_text)
        data_bind_lay.addWidget(data_bind_label)
        data_bind_lay.addWidget(button)
        data_bind_lay.addStretch()
        self.register_field('show_text', 'Guess')
        self.bind('show_text', data_bind_label, 'text')

        lay_elide = QVBoxLayout()
        label_none = MLabel('This is a elide NONE mode label. '
                            'Ellipsis should NOT appear in the text.')
        label_left = MLabel(
            'This is a elide LEFT mode label. '
            'The ellipsis should appear at the beginning of the text. '
            'xiao mao xiao gou xiao ci wei')
        label_left.set_elide_mode(Qt.ElideLeft)
        label_middle = MLabel(
            'This is a elide MIDDLE mode label. '
            'The ellipsis should appear in the middle of the text. '
            'xiao mao xiao gou xiao ci wei')
        label_middle.set_elide_mode(Qt.ElideMiddle)
        label_right = MLabel()
        label_right.setText('This is a elide RIGHT mode label. '
            'The ellipsis should appear at the end of the text. '
            'Some text to fill the line bala bala bala.')
        label_right.set_elide_mode(Qt.ElideRight)
        lay_elide.addWidget(label_none)
        lay_elide.addWidget(label_left)
        lay_elide.addWidget(label_middle)
        lay_elide.addWidget(label_right)

        main_lay = QVBoxLayout()
        main_lay.addWidget(MDivider('different level'))
        main_lay.addLayout(tilte_lay)
        main_lay.addWidget(MDivider('different type'))
        main_lay.addLayout(text_type_lay)
        main_lay.addWidget(MDivider('different property'))
        main_lay.addLayout(text_attr_lay)
        # main_lay.addWidget(MDivider('data bind'))
        # main_lay.addLayout(data_bind_lay)
        main_lay.addWidget(MDivider('elide mode'))
        main_lay.addLayout(lay_elide)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_change_text(self):
        import random
        self.set_field('show_text', random.choice(['Dog', 'Cat', 'Rabbit', 'Cow']))

    def slot_link_text(self):
        self.set_field('is_link', not self.field('is_link'))


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    app = QApplication(sys.argv)
    test = LabelExample()
    from dayu_widgets import dayu_theme
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
