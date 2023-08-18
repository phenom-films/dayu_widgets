# Import built-in modules
import os


DEFAULT_STATIC_FOLDER = os.path.join(__path__[0], "static")
CUSTOM_STATIC_FOLDERS = []
# Import local modules
from dayu_widgets3.theme import MTheme


dayu_theme = MTheme("dark", primary_color=MTheme.orange)
# dayu_theme.default_size = dayu_theme.small
# dayu_theme = MTheme('light')

# Import local modules
from dayu_widgets3.alert import MAlert
from dayu_widgets3.avatar import MAvatar
from dayu_widgets3.badge import MBadge
from dayu_widgets3.breadcrumb import MBreadcrumb
from dayu_widgets3.browser import MClickBrowserFilePushButton
from dayu_widgets3.browser import MClickBrowserFileToolButton
from dayu_widgets3.browser import MClickBrowserFolderPushButton
from dayu_widgets3.browser import MClickBrowserFolderToolButton
from dayu_widgets3.browser import MDragFileButton
from dayu_widgets3.browser import MDragFolderButton
from dayu_widgets3.button_group import MCheckBoxGroup
from dayu_widgets3.button_group import MPushButtonGroup
from dayu_widgets3.button_group import MRadioButtonGroup
from dayu_widgets3.button_group import MToolButtonGroup
from dayu_widgets3.card import MCard
from dayu_widgets3.card import MMeta
from dayu_widgets3.carousel import MCarousel
from dayu_widgets3.check_box import MCheckBox
from dayu_widgets3.collapse import MCollapse
from dayu_widgets3.combo_box import MComboBox
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.flow_layout import MFlowLayout
from dayu_widgets3.item_model import MSortFilterModel
from dayu_widgets3.item_model import MTableModel
from dayu_widgets3.item_view import MBigView
from dayu_widgets3.item_view import MListView
from dayu_widgets3.item_view import MTableView
from dayu_widgets3.item_view import MTreeView
from dayu_widgets3.item_view_full_set import MItemViewFullSet
from dayu_widgets3.item_view_set import MItemViewSet
from dayu_widgets3.label import MLabel
from dayu_widgets3.line_edit import MLineEdit
from dayu_widgets3.line_tab_widget import MLineTabWidget
from dayu_widgets3.loading import MLoading
from dayu_widgets3.loading import MLoadingWrapper
from dayu_widgets3.menu import MMenu
from dayu_widgets3.menu_tab_widget import MMenuTabWidget
from dayu_widgets3.message import MMessage
from dayu_widgets3.page import MPage
from dayu_widgets3.progress_bar import MProgressBar
from dayu_widgets3.progress_circle import MProgressCircle
from dayu_widgets3.push_button import MPushButton
from dayu_widgets3.radio_button import MRadioButton
from dayu_widgets3.slider import MSlider
from dayu_widgets3.spin_box import MDateEdit
from dayu_widgets3.spin_box import MDateTimeEdit
from dayu_widgets3.spin_box import MDoubleSpinBox
from dayu_widgets3.spin_box import MSpinBox
from dayu_widgets3.spin_box import MTimeEdit
from dayu_widgets3.switch import MSwitch
from dayu_widgets3.tab_widget import MTabWidget
from dayu_widgets3.text_edit import MTextEdit
from dayu_widgets3.toast import MToast
from dayu_widgets3.tool_button import MToolButton


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
