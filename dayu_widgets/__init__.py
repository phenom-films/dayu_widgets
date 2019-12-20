import os

DEFAULT_STATIC_FOLDER = os.path.join(__path__[0], 'static')
CUSTOM_STATIC_FOLDERS = []
from theme import MTheme

dayu_theme = MTheme('dark', primary_color=MTheme.orange)
# dayu_theme.default_size = dayu_theme.small
# dayu_theme = MTheme('light')

from spin_box import MSpinBox, MDoubleSpinBox, MDateTimeEdit, MDateEdit, MTimeEdit
from alert import MAlert
from avatar import MAvatar
from badge import MBadge
from breadcrumb import MBreadcrumb
from browser import MClickBrowserFilePushButton, MClickBrowserFileToolButton, \
    MClickBrowserFolderPushButton, MClickBrowserFolderToolButton, \
    MDragFileButton, MDragFolderButton
from button_group import MPushButtonGroup, MRadioButtonGroup, MCheckBoxGroup, MToolButtonGroup
from card import MCard, MMeta
from carousel import MCarousel
from check_box import MCheckBox
from progress_circle import MProgressCircle
from collapse import MCollapse
from combo_box import MComboBox
from divider import MDivider
from field_mixin import MFieldMixin
from flow_layout import MFlowLayout
from item_model import MTableModel, MSortFilterModel
from item_view import MTableView, MTreeView, MBigView, MListView
from item_view_full_set import MItemViewFullSet
from item_view_set import MItemViewSet
from label import MLabel
from line_edit import MLineEdit
from line_tab_widget import MLineTabWidget
from loading import MLoading, MLoadingWrapper
from menu import MMenu
from menu_tab_widget import MMenuTabWidget
from message import MMessage
from page import MPage
from progress_bar import MProgressBar
from push_button import MPushButton
from radio_button import MRadioButton
from sequence_file import MSequenceFile
from slider import MSlider
from switch import MSwitch
from tab_widget import MTabWidget
from toast import MToast
from tool_button import MToolButton
from text_edit import MTextEdit
