# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.browser import MClickBrowserFilePushButton
from dayu_widgets3.browser import MClickBrowserFileToolButton
from dayu_widgets3.browser import MClickBrowserFolderPushButton
from dayu_widgets3.browser import MClickBrowserFolderToolButton
from dayu_widgets3.browser import MDragFileButton
from dayu_widgets3.browser import MDragFolderButton
from dayu_widgets3.divider import MDivider
from dayu_widgets3.field_mixin import MFieldMixin
from dayu_widgets3.label import MLabel
from dayu_widgets3.qt import MIcon


class BrowserExample(QtWidgets.QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(BrowserExample, self).__init__(parent)
        self.setWindowTitle("Examples for MBrowser...")
        self._init_ui()

    def _init_ui(self):
        browser_1 = MClickBrowserFilePushButton(text="Browser File PushButton").primary()
        browser_2 = MClickBrowserFolderPushButton(text="Browser Folder PushButton")
        browser_2.setIcon(MIcon("upload_line.svg"))
        browser_3 = MClickBrowserFilePushButton(text="Browser Multi Files", multiple=True).primary()
        lay_1 = QtWidgets.QHBoxLayout()
        lay_1.addWidget(browser_1)
        lay_1.addWidget(browser_2)
        lay_1.addWidget(browser_3)

        browser_4 = MClickBrowserFileToolButton().huge()
        label_4 = MLabel()
        label_4.set_elide_mode(QtCore.Qt.ElideMiddle)
        browser_4.sig_file_changed.connect(label_4.setText)

        browser_5 = MClickBrowserFolderToolButton().huge()
        label_5 = MLabel()
        label_5.set_elide_mode(QtCore.Qt.ElideMiddle)
        browser_5.sig_folder_changed.connect(label_5.setText)

        lay_2 = QtWidgets.QHBoxLayout()
        lay_2.addWidget(label_4)
        lay_2.addWidget(browser_4)
        lay_2.addWidget(label_5)
        lay_2.addWidget(browser_5)

        browser_6 = MDragFileButton(text="Click or drag file here")
        browser_6.set_dayu_svg("attachment_line.svg")
        label_6 = MLabel()
        label_6.set_elide_mode(QtCore.Qt.ElideMiddle)
        browser_6.sig_file_changed.connect(label_6.setText)

        browser_7 = MDragFolderButton()
        label_7 = MLabel()
        label_7.set_elide_mode(QtCore.Qt.ElideRight)
        browser_7.sig_folder_changed.connect(label_7.setText)

        lay_3 = QtWidgets.QGridLayout()
        lay_3.addWidget(browser_6, 2, 0)
        lay_3.addWidget(browser_7, 2, 1)
        lay_3.addWidget(label_6, 3, 0)
        lay_3.addWidget(label_7, 3, 1)

        browser_8 = MDragFileButton(text="Click or drag media file here", multiple=False)
        browser_8.set_dayu_svg("media_line.svg")
        browser_8.set_dayu_filters([".mov", ".mp4"])
        browser_8_label = MLabel()
        browser_8_label.set_elide_mode(QtCore.Qt.ElideRight)
        self.register_field("current_file", "")
        self.bind("current_file", browser_8, "dayu_path", signal="sig_file_changed")
        self.bind("current_file", browser_8_label, "text")

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(MDivider("MClickBrowser*PushButton"))
        main_lay.addLayout(lay_1)
        main_lay.addWidget(MDivider("MClickBrowser*ToolButton"))
        main_lay.addLayout(lay_2)
        main_lay.addWidget(MDivider("MDragBrowser*ToolButton"))
        main_lay.addLayout(lay_3)
        main_lay.addWidget(MDivider("data bind"))
        main_lay.addWidget(browser_8)
        main_lay.addWidget(browser_8_label)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = BrowserExample()
        dayu_theme.apply(test)
        test.show()
