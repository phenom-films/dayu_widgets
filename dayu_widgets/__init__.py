import os

STATIC_FOLDERS = [os.path.join(__path__[0], 'static')]
from MTheme import MTheme

# dayu_theme = MTheme('dark', primary_color=MTheme.orange)
dayu_theme = MTheme('light', primary_color='#722ed1')

from MAbstractSpinBox import MSpinBox, MDoubleSpinBox, MDateTimeEdit, MDateEdit, MTimeEdit
from MAlert import MAlert
from MAvatar import MAvatar
from MBadge import MBadge
from MBreadcrumb import MBreadcrumb
from MBrowser import MClickBrowserFilePushButton, MClickBrowserFileToolButton, \
    MClickBrowserFolderPushButton, MClickBrowserFolderToolButton, \
    MDragFileButton, MDragFolderButton
from MButtonGroup import MPushButtonGroup, MRadioButtonGroup, MCheckBoxGroup, MToolButtonGroup
from MCard import MCard, MMeta
from MCarousel import MCarousel
from MCheckBox import MCheckBox
from MCircle import MCircle
from MCollapse import MCollapse
from MComboBox import MComboBox
from MDivider import MDivider
from MFieldMixin import MFieldMixin
from MFlowLayout import MFlowLayout
from MItemModel import MTableModel, MSortFilterModel
from MItemView import MTableView, MTreeView, MBigView, MListView
from MItemViewFullSet import MItemViewFullSet
from MItemViewSet import MItemViewSet
from MLabel import MLabel
from MLineEdit import MLineEdit
from MLineTabWidget import MLineTabWidget
from MLoading import MLoading, MLoadingWrapper
from MMenu import MMenu
from MMenuTabWidget import MMenuTabWidget
from MMessage import MMessage
from MPage import MPage
from MProgressBar import MProgressBar
from MPushButton import MPushButton
from MRadioButton import MRadioButton
from MSequenceFile import MSequenceFile
from MSlider import MSlider
from MSwitch import MSwitch
from MTabWidget import MTabWidget
from MTag import MTag, MCheckableTag, MNewTag
from MToast import MToast
from MToolButton import MToolButton
