#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import os

from MButton import MButton
from MTheme import global_theme
from qt import *

qss = '''
QToolButton{{
    color: {content};
    background-color: {background};
    border: 2px dashed {border};
    border-radius: 10px;
    padding: 20px 40px;
    {text_font};
}}
QToolButton:hover{{
    color: #2d8cf0;
    border-color: #5cadff;
}}
QToolButton:pressed{{
    color: #2b85e4;
    border-color: #2b85e4;
}}
'''.format(**global_theme)


class MCanClickBrowserFileMixin(object):

    @Slot()
    def slot_browser_file(self):
        multi = self.property('multiple')
        filter_list = 'File(%s)' % (' '.join(['*' + e for e in self.property('format')])) \
            if self.property('format') else 'Any File(*)'
        if multi:
            r_files, _ = QFileDialog.getOpenFileNames(self, 'Browser File', self.property('path'), filter_list)
            if r_files:
                self.sig_files_changed.emit(r_files)
                self.set_path(r_files[0])
        else:
            r_file, _ = QFileDialog.getOpenFileName(self, 'Browser File', self.property('path'), filter_list)
            if r_file:
                self.sig_file_changed.emit(r_file)
                self.set_path(r_file)


class MCanDragFileMixin(object):

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/uri-list"):
            file_list = self._get_valid_file_list(event.mimeData().urls())
            count = len(file_list)
            if count == 1 or (count > 1 and self.property('multiple')):
                event.acceptProposedAction()
                return

    def dropEvent(self, event):
        file_list = self._get_valid_file_list(event.mimeData().urls())
        if self.property('multiple'):
            self.sig_files_changed.emit(file_list)
            self.set_path(file_list)
        else:
            self.sig_file_changed.emit(file_list[0])
            self.set_path(file_list[0])

    def _get_valid_file_list(self, url_list):
        import subprocess
        import sys
        file_list = []
        for url in url_list:
            file_name = url.toLocalFile()
            if sys.platform == 'darwin':
                p = subprocess.Popen(
                    'osascript -e \'get posix path of posix file \"file://{}\" -- kthxbai\''.format(file_name),
                    stdout=subprocess.PIPE,
                    shell=True)
                # print p.communicate()[0].strip()
                file_name = p.communicate()[0].strip()
                print file_name
                p.wait()

            if os.path.isfile(file_name):
                if self.property('format'):
                    if os.path.splitext(file_name)[-1] in self.property('format'):
                        file_list.append(file_name)
                else:
                    file_list.append(file_name)

        return file_list


class MCanClickBrowserFolderMixin(object):
    @Slot()
    def slot_browser_folder(self):
        r_folder = QFileDialog.getExistingDirectory(self, 'Browser Folder', self.property('path'))
        if r_folder:
            self.sig_folder_changed.emit(r_folder)
            self.set_path(r_folder)


class MCanDragFolderMixin(object):

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/uri-list"):
            folder_list = [url.toLocalFile() for url in event.mimeData().urls() if os.path.isdir(url.toLocalFile())]
            count = len(folder_list)
            if count == 1:
                event.acceptProposedAction()
                return

    def dropEvent(self, event):
        folder_list = [url.toLocalFile() for url in event.mimeData().urls() if os.path.isdir(url.toLocalFile())]
        self.sig_folder_changed.emit(folder_list[0])
        self.set_path(folder_list[0])


@property_mixin
class MBrowser(QWidget):
    clicked = Signal()

    def __init__(self, multiple=False, parent=None):
        super(MBrowser, self).__init__(parent=parent)
        self.setProperty('multiple', multiple)
        self._main_lay = QVBoxLayout()
        self._main_lay.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._main_lay)
        self.setCursor(Qt.PointingHandCursor)
        self.set_path('')

    def get_widget(self):
        return self._main_lay.itemAt(0).widget()

    def set_widget(self, widget):
        old_widget = self._main_lay.takeAt(0)
        if old_widget:
            old_widget.setVisible(False)
        self._main_lay.addWidget(widget)

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)


class MClickBrowserFileButton(MBrowser, MCanClickBrowserFileMixin):
    sig_file_changed = Signal(str)

    def __init__(self, text='', icon=None, size=None, multiple=False, parent=None):
        super(MClickBrowserFileButton, self).__init__(multiple=multiple, parent=parent)
        size = size or MView.LargeSize
        if text:
            button = MButton(text=text, icon=icon or MIcon('icon-upload.png'), size=size, type=MButton.PrimaryType)
        else:
            button = MButton(icon=icon or MIcon('icon-upload.png'), size=size, type=MButton.PrimaryType)
            self.setFixedWidth(global_theme.get(size + '_size'))
        button.clicked.connect(self.slot_browser_file)
        button.clicked.connect(self.clicked)

        self.set_widget(button)


class MDragFileButton(MBrowser, MCanClickBrowserFileMixin, MCanDragFileMixin):
    sig_file_changed = Signal(str)

    def __init__(self, text='', icon=None, multiple=False, parent=None):
        super(MDragFileButton, self).__init__(multiple=multiple, parent=parent)
        self.setAcceptDrops(True)
        button = QToolButton()
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setText(text)
        button.setIcon(icon or MIcon('icon-upload.png'))
        button.setIconSize(QSize(50, 50))
        button.clicked.connect(self.slot_browser_file)
        button.clicked.connect(self.clicked)
        button.setStyleSheet(qss)
        self.set_widget(button)


class MClickBrowserFolderButton(MBrowser, MCanClickBrowserFolderMixin):
    sig_folder_changed = Signal(str)

    def __init__(self, text='', icon=None, size=None, multiple=False, parent=None):
        super(MClickBrowserFolderButton, self).__init__(multiple=multiple, parent=parent)
        size = size or MView.LargeSize
        if text:
            button = MButton(text=text, icon=icon or MIcon('icon-browser.png'), size=size, type=MButton.PrimaryType)
        else:
            button = MButton(icon=icon or MIcon('icon-browser.png'), size=size, type=MButton.PrimaryType)
            self.setFixedWidth(global_theme.get(size + '_size'))
        button.clicked.connect(self.slot_browser_folder)
        button.clicked.connect(self.clicked)

        self.set_widget(button)


class MDragFolderButton(MBrowser, MCanClickBrowserFolderMixin, MCanDragFolderMixin):
    sig_folder_changed = Signal(str)

    def __init__(self, text='', icon=None, multiple=False, parent=None):
        super(MDragFolderButton, self).__init__(multiple=multiple, parent=parent)
        self.setAcceptDrops(True)
        button = QToolButton()
        button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button.setText(text)
        button.setIcon(icon or MIcon('icon-browser.png'))
        button.setIconSize(QSize(50, 50))
        button.clicked.connect(self.slot_browser_folder)
        button.clicked.connect(self.clicked)
        button.setStyleSheet(qss)
        self.set_widget(button)
