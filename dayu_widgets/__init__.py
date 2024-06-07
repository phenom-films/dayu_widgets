# -*- coding: utf-8 -*-
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import os
import sys


DEFAULT_STATIC_FOLDER = os.path.join(sys.modules[__name__].__path__[0], "static")
CUSTOM_STATIC_FOLDERS = []
# Import local modules
from dayu_widgets.theme import MTheme


dayu_theme = MTheme("dark", primary_color=MTheme.orange)
# dayu_theme.default_size = dayu_theme.small
# dayu_theme = MTheme('light')

# Import local modules
from dayu_widgets.alert import MAlert
from dayu_widgets.avatar import MAvatar
from dayu_widgets.badge import MBadge
from dayu_widgets.breadcrumb import MBreadcrumb
from dayu_widgets.browser import MClickBrowserFilePushButton
from dayu_widgets.browser import MClickBrowserFileToolButton
from dayu_widgets.browser import MClickBrowserFolderPushButton
from dayu_widgets.browser import MClickBrowserFolderToolButton
from dayu_widgets.browser import MDragFileButton
from dayu_widgets.browser import MDragFolderButton
from dayu_widgets.button_group import MCheckBoxGroup
from dayu_widgets.button_group import MPushButtonGroup
from dayu_widgets.button_group import MRadioButtonGroup
from dayu_widgets.button_group import MToolButtonGroup
from dayu_widgets.card import MCard
from dayu_widgets.card import MMeta
from dayu_widgets.carousel import MCarousel
from dayu_widgets.check_box import MCheckBox
from dayu_widgets.collapse import MCollapse
from dayu_widgets.combo_box import MComboBox
from dayu_widgets.divider import MDivider
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets.flow_layout import MFlowLayout
from dayu_widgets.item_model import MSortFilterModel
from dayu_widgets.item_model import MTableModel
from dayu_widgets.item_view import MBigView
from dayu_widgets.item_view import MListView
from dayu_widgets.item_view import MTableView
from dayu_widgets.item_view import MTreeView
from dayu_widgets.item_view_full_set import MItemViewFullSet
from dayu_widgets.item_view_set import MItemViewSet
from dayu_widgets.label import MLabel
from dayu_widgets.line_edit import MLineEdit
from dayu_widgets.line_tab_widget import MLineTabWidget
from dayu_widgets.loading import MLoading
from dayu_widgets.loading import MLoadingWrapper
from dayu_widgets.menu import MMenu
from dayu_widgets.menu_tab_widget import MMenuTabWidget
from dayu_widgets.message import MMessage
from dayu_widgets.page import MPage
from dayu_widgets.progress_bar import MProgressBar
from dayu_widgets.progress_circle import MProgressCircle
from dayu_widgets.push_button import MPushButton
from dayu_widgets.radio_button import MRadioButton
from dayu_widgets.sequence_file import MSequenceFile
from dayu_widgets.slider import MSlider
from dayu_widgets.spin_box import MDateEdit
from dayu_widgets.spin_box import MDateTimeEdit
from dayu_widgets.spin_box import MDoubleSpinBox
from dayu_widgets.spin_box import MSpinBox
from dayu_widgets.spin_box import MTimeEdit
from dayu_widgets.switch import MSwitch
from dayu_widgets.tab_widget import MTabWidget
from dayu_widgets.text_edit import MTextEdit
from dayu_widgets.toast import MToast
from dayu_widgets.tool_button import MToolButton


__all__ = [
    "MAlert",
    "MAvatar",
    "MBadge",
    "MBreadcrumb",
    "MClickBrowserFilePushButton",
    "MClickBrowserFileToolButton",
    "MClickBrowserFolderPushButton",
    "MClickBrowserFolderToolButton",
    "MDragFileButton",
    "MDragFolderButton",
    "MCheckBoxGroup",
    "MPushButtonGroup",
    "MRadioButtonGroup",
    "MToolButtonGroup",
    "MCard",
    "MMeta",
    "MCarousel",
    "MCheckBox",
    "MCollapse",
    "MComboBox",
    "MDivider",
    "MFieldMixin",
    "MFlowLayout",
    "MSortFilterModel",
    "MTableModel",
    "MBigView",
    "MListView",
    "MTableView",
    "MTreeView",
    "MItemViewFullSet",
    "MItemViewSet",
    "MLabel",
    "MLineEdit",
    "MLineTabWidget",
    "MLoading",
    "MLoadingWrapper",
    "MMenu",
    "MMenuTabWidget",
    "MMessage",
    "MPage",
    "MProgressBar",
    "MProgressCircle",
    "MPushButton",
    "MRadioButton",
    "MSequenceFile",
    "MSlider",
    "MDateEdit",
    "MDateTimeEdit",
    "MDoubleSpinBox",
    "MSpinBox",
    "MTimeEdit",
    "MSwitch",
    "MTabWidget",
    "MTextEdit",
    "MToast",
    "MToolButton",
]
