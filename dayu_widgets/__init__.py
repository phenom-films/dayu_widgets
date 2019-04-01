import os

STATIC_FOLDERS = [os.path.join(__path__[0], 'static')]
from MTheme import MTheme

# dayu_theme = MTheme('dark')
dayu_theme = MTheme()

from MAbstractSpinBox import MSpinBox, MDoubleSpinBox, MDateTimeEdit, MDateEdit, MTimeEdit
from MAlert import MAlert
from MAvatar import MAvatar
from MBadge import MBadge
from MBreadcrumb import MBreadcrumb
from MBrowser import MClickBrowserFilePushButton, MClickBrowserFileToolButton, \
    MClickBrowserFolderPushButton, MClickBrowserFolderToolButton, \
    MDragFileButton, MDragFolderButton
from MButtonGroup import MPushButtonGroup, MRadioButtonGroup, MCheckBoxGroup, MToolButtonGroup
from MCheckBox import MCheckBox
from MCircle import MCircle
from MCollapse import MCollapse
from MComboBox import MComboBox
from MDivider import MDivider
from MFieldMixin import MFieldMixin
from MLabel import MLabel
from MLineEdit import MLineEdit
from MMenu import MMenu
from MMessage import MMessage
from MProgressBar import MProgressBar
from MPushButton import MPushButton
from MRadioButton import MRadioButton
from MSequenceFile import MSequenceFile
from MSlider import MSlider
from MSwitch import MSwitch
from MItemView import MTableView, MTreeView, MBigView, MListView
from MItemModel import MTableModel, MSortFilterModel
from MItemViewSet import MItemViewSet
from MItemViewFullSet import MItemViewFullSet
from MTabWidget import MTabWidget
from MMenuTabWidget import MMenuTabWidget
from MToolButton import MToolButton
from MLineTabWidget import MLineTabWidget
