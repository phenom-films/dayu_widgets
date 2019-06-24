#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

from dayu_widgets.label import MLabel
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.avatar import MAvatar
from dayu_widgets.divider import MDivider
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import property_mixin, hover_shadow_mixin, cursor_mixin
from dayu_widgets.qt import *


@hover_shadow_mixin
@cursor_mixin
class MCard(QWidget):
    def __init__(self, title=None, image=None, size=None, extra=None, type=None, parent=None):
        super(MCard, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground)
        map_label = {
            dayu_theme.large: (MLabel.h2, 20),
            dayu_theme.medium: (MLabel.h3, 15),
            dayu_theme.small: (MLabel.h4, 10),
        }
        self._title_label = map_label.get(size or dayu_theme.default_size)[0](text=title)

        padding = map_label.get(size or dayu_theme.default_size)[-1]
        self._title_layout = QHBoxLayout()
        self._title_layout.setContentsMargins(padding, padding, padding, padding)
        if image:
            self._title_icon = MAvatar(image=image, size=size)
            self._title_layout.addWidget(self._title_icon)
        self._title_layout.addWidget(self._title_label)
        self._title_layout.addStretch()
        if extra:
            self._extra_button = MToolButton(type=MToolButton.IconOnlyType, icon=MIcon('more.svg'))
            self._title_layout.addWidget(self._extra_button)

        self._content_layout = QVBoxLayout()

        self._main_lay = QVBoxLayout()
        self._main_lay.setSpacing(0)
        self._main_lay.setContentsMargins(1, 1, 1, 1)
        if title:
            self._main_lay.addLayout(self._title_layout)
            self._main_lay.addWidget(MDivider())
        self._main_lay.addLayout(self._content_layout)
        self.setLayout(self._main_lay)

    def get_more_button(self):
        return self._extra_button

    def set_widget(self, widget):
        self._content_layout.addWidget(widget)


@hover_shadow_mixin
@cursor_mixin
class MMeta(QWidget):
    def __init__(self, cover=None, avatar=None, title=None, description=None, extra=False, parent=None):
        super(MMeta, self).__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground)
        # self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self._cover_label = QLabel()
        self._avatar = MAvatar()
        self._title_label = MLabel.h4()
        # self._title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self._description_label = MLabel.help()
        # self._description_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        self._description_label.setWordWrap(True)
        self._title_layout = QHBoxLayout()
        self._title_layout.addWidget(self._title_label)
        self._title_layout.addStretch()
        if extra:
            self._extra_button = MToolButton(type=MToolButton.IconOnlyType, icon=MIcon('more.svg'))
            self._title_layout.addWidget(self._extra_button)

        content_lay = QFormLayout()
        content_lay.setContentsMargins(5, 5, 5, 5)
        content_lay.addRow(self._avatar, self._title_layout)
        content_lay.addRow(self._description_label)

        self._button_layout = QHBoxLayout()

        main_lay = QVBoxLayout()
        main_lay.setSpacing(0)
        main_lay.setContentsMargins(1, 1, 1, 1)
        main_lay.addWidget(self._cover_label)
        main_lay.addLayout(content_lay)
        main_lay.addLayout(self._button_layout)
        main_lay.addStretch()
        self.setLayout(main_lay)
        self._cover_label.setFixedSize(QSize(200, 200))
        # self.setFixedWidth(200)

    def get_more_button(self):
        return self._extra_button

    def setup_data(self, data_dict):
        if data_dict.get('title'):
            self._title_label.setText(data_dict.get('title'))
            self._title_label.setVisible(True)
        else:
            self._title_label.setVisible(False)

        if data_dict.get('description'):
            self._description_label.setText(data_dict.get('description'))
            self._description_label.setVisible(True)
        else:
            self._description_label.setVisible(False)

        if data_dict.get('avatar'):
            self._avatar.set_dayu_image(data_dict.get('avatar'))
            self._avatar.setVisible(True)
        else:
            self._avatar.setVisible(False)

        if data_dict.get('cover'):
            fixed_height = self._cover_label.width()
            self._cover_label.setPixmap(data_dict.get('cover').scaledToWidth(fixed_height, Qt.SmoothTransformation))
            self._cover_label.setVisible(True)
        else:
            self._cover_label.setVisible(False)
