#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################

import os

from dayu_widgets.tool_button import MToolButton
from dayu_widgets.mixin import property_mixin, cursor_mixin
from dayu_widgets.push_button import MPushButton
from dayu_widgets.qt import QFileDialog, Slot, Signal, MIcon, Qt, QToolButton, QSize, QSizePolicy


@Slot()
def _slot_browser_file(self):
    multi = self.property('multiple')
    filter_list = 'File(%s)' % (' '.join(['*' + e for e in self.property('format')])) \
        if self.property('format') else 'Any File(*)'
    if multi:
        r_files, _ = QFileDialog.getOpenFileNames(self, 'Browser File', self.property('path'),
                                                  filter_list)
        if r_files:
            self.sig_files_changed.emit(r_files)
            self.set_path(r_files[0])
    else:
        r_file, _ = QFileDialog.getOpenFileName(self, 'Browser File', self.property('path'),
                                                filter_list)
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
@cursor_mixin
class MClickBrowserFilePushButton(MPushButton):
    sig_file_changed = Signal(str)
    sig_files_changed = Signal(list)
    slot_browser_file = _slot_browser_file

    def __init__(self, icon=None, text='', multiple=False, parent=None):
        super(MClickBrowserFilePushButton, self).__init__(
            icon=icon or MIcon('cloud_line.svg',
                               None if type is None or type == 'default' else '#fff'),
            text=text, parent=parent)
        self.setProperty('multiple', multiple)
        self.clicked.connect(self.slot_browser_file)
        self.setToolTip(self.tr('Click to browser file'))
        self.set_path('')

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)


@property_mixin
class MClickBrowserFileToolButton(MToolButton):
    sig_file_changed = Signal(str)
    sig_files_changed = Signal(list)
    slot_browser_file = _slot_browser_file

    def __init__(self, icon=None, size=None, multiple=False, parent=None):
        super(MClickBrowserFileToolButton, self).__init__(icon=icon or MIcon('cloud_line.svg'),
                                                          type=MToolButton.IconOnlyType,
                                                          size=size, parent=parent)
        self.setProperty('multiple', multiple)
        self.clicked.connect(self.slot_browser_file)
        self.set_path('')
        self.setToolTip(self.tr('Click to browser file'))

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)


@property_mixin
@cursor_mixin
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
        self.setIcon(icon or MIcon('cloud_line.svg'))
        self.setIconSize(QSize(80, 80))
        self.clicked.connect(self.slot_browser_file)
        self.set_path('')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setToolTip(self.tr('Click to browser file'))

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)

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
                    'osascript -e \'get posix path of posix file \"file://{}\" -- kthxbai\''.format(
                        file_name),
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
class MClickBrowserFolderPushButton(MPushButton):
    sig_folder_changed = Signal(str)
    sig_folders_changed = Signal(list)
    slot_browser_folder = _slot_browser_folder

    def __init__(self, icon=None, text='', multiple=False, parent=None):
        super(MClickBrowserFolderPushButton, self).__init__(
            icon=icon or MIcon('folder_line.svg',
                               None if type is None or type == MPushButton.DefaultType else '#fff'),
            text=text, parent=parent)
        self.setProperty('multiple', multiple)
        self.setCursor(Qt.PointingHandCursor)
        self.clicked.connect(self.slot_browser_folder)
        self.set_path('')
        self.setToolTip(self.tr('Click to browser folder'))

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)


@property_mixin
class MClickBrowserFolderToolButton(MToolButton):
    sig_folder_changed = Signal(str)
    sig_folders_changed = Signal(list)
    slot_browser_folder = _slot_browser_folder

    def __init__(self, multiple=False, icon=None, size=None, parent=None):
        super(MClickBrowserFolderToolButton, self).__init__(
            icon=icon or MIcon('folder_line.svg'), size=size,
            type=MToolButton.IconOnlyType, parent=parent)
        self.setProperty('multiple', multiple)
        self.setCursor(Qt.PointingHandCursor)
        self.clicked.connect(self.slot_browser_folder)
        self.set_path('')
        self.setToolTip(self.tr('Click to browser folder'))

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)


@property_mixin
@cursor_mixin
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
        self.setIcon(icon or MIcon('folder_line.svg'))
        self.setIconSize(QSize(80, 80))
        self.clicked.connect(self.slot_browser_folder)
        self.set_path('')
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setToolTip(self.tr('Click to browser folder'))

    def set_format(self, value):
        self.setProperty('format', value)

    def set_path(self, value):
        self.setProperty('path', value)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/uri-list"):
            folder_list = [url.toLocalFile() for url in event.mimeData().urls() if
                           os.path.isdir(url.toLocalFile())]
            count = len(folder_list)
            if count == 1 or (count > 1 and self.property('multiple')):
                event.acceptProposedAction()
                return

    def dropEvent(self, event):
        folder_list = [url.toLocalFile() for url in event.mimeData().urls() if
                       os.path.isdir(url.toLocalFile())]
        if self.property('multiple'):
            self.sig_folders_changed.emit(folder_list)
        else:
            self.sig_folder_changed.emit(folder_list[0])
        self.set_path(folder_list[0])
