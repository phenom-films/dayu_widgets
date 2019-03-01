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


@Slot()
def _slot_browser_file(self):
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


@Slot()
def _slot_browser_folder(self):
    r_folder = QFileDialog.getExistingDirectory(self, 'Browser Folder', self.property('path'))
    if r_folder:
        if self.property('multiple'):
            self.sig_folders_changed.emit([r_folder])
        else:
            self.sig_folder_changed.emit(r_folder)
        self.set_path(r_folder)


@property_mixin
class MClickBrowserFileButton(MButton):
    sig_file_changed = Signal(str)
    sig_files_changed = Signal(list)
    slot_browser_file = _slot_browser_file

    def __init__(self, icon=None, text='', type=None, size=None, multiple=False, parent=None):
        super(MClickBrowserFileButton, self).__init__(icon=icon or MIcon('icon-upload.png'),
                                                      text=text, type=type, size=size, parent=parent)
        self.setProperty('multiple', multiple)
        self.setCursor(Qt.PointingHandCursor)
        self.clicked.connect(self.slot_browser_file)
        self.set_path('')

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)


@property_mixin
class MDragFileButton(QToolButton):
    sig_file_changed = Signal(str)
    sig_files_changed = Signal(list)
    slot_browser_file = _slot_browser_file

    def __init__(self, text='', icon=None, multiple=False, parent=None):
        super(MDragFileButton, self).__init__(parent=parent)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setProperty('multiple', multiple)
        self.setCursor(Qt.PointingHandCursor)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setText(text)
        self.setIcon(icon or MIcon('icon-upload.png'))
        self.setIconSize(QSize(50, 50))
        self.clicked.connect(self.slot_browser_file)
        self.setStyleSheet(qss)
        self.set_path('')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)

    def dragEnterEvent(self, event):
        print 'drag enter', event
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


@property_mixin
class MClickBrowserFolderButton(MButton):
    sig_folder_changed = Signal(str)
    sig_folders_changed = Signal(list)
    slot_browser_folder = _slot_browser_folder

    def __init__(self, icon=None, text='', type=None, size=None, multiple=False, parent=None):
        super(MClickBrowserFolderButton, self).__init__(icon=icon or MIcon('icon-upload.png'),
                                                        text=text, type=type, size=size, parent=parent)
        self.setProperty('multiple', multiple)
        self.setCursor(Qt.PointingHandCursor)
        self.clicked.connect(self.slot_browser_folder)
        self.set_path('')

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)


@property_mixin
class MDragFolderButton(QToolButton):
    sig_folder_changed = Signal(str)
    sig_folders_changed = Signal(list)
    slot_browser_folder = _slot_browser_folder

    def __init__(self, text='', icon=None, multiple=False, parent=None):
        super(MDragFolderButton, self).__init__(parent=parent)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.setProperty('multiple', multiple)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setText(text)
        self.setIcon(icon or MIcon('icon-browser.png'))
        self.setIconSize(QSize(50, 50))
        self.clicked.connect(self.slot_browser_folder)
        self.setStyleSheet(qss)
        self.set_path('')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/uri-list"):
            folder_list = [url.toLocalFile() for url in event.mimeData().urls() if os.path.isdir(url.toLocalFile())]
            count = len(folder_list)
            if count == 1 or (count > 1 and self.property('multiple')):
                event.acceptProposedAction()
                return

    def dropEvent(self, event):
        folder_list = [url.toLocalFile() for url in event.mimeData().urls() if os.path.isdir(url.toLocalFile())]
        if self.property('multiple'):
            self.sig_folders_changed.emit(folder_list)
        else:
            self.sig_folder_changed.emit(folder_list[0])
        self.set_path(folder_list[0])
