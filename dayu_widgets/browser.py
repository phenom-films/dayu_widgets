#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
"""
MClickBrowserFilePushButton, MClickBrowserFileToolButton
MClickBrowserFolderPushButton, MClickBrowserFolderToolButton
Browser files or folders by selecting.

MDragFileButton, MDragFolderButton
Browser files or folders by dragging.
"""
# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import built-in modules
import os

# Import third-party modules
from Qt import QtCore
from Qt import QtWidgets
import six

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import cursor_mixin
from dayu_widgets.mixin import property_mixin
from dayu_widgets.push_button import MPushButton
from dayu_widgets.tool_button import MToolButton


# NOTE PySide2 Crash without QObject wrapper
# @Slot()
def _slot_browser_file(self):
    filter_list = (
        "File(%s)" % (" ".join(["*" + e for e in self.get_dayu_filters()]))
        if self.get_dayu_filters()
        else "Any File(*)"
    )
    if self.get_dayu_multiple():
        r_files, _ = QtWidgets.QFileDialog.getOpenFileNames(self, "Browser File", self.get_dayu_path(), filter_list)
        if r_files:
            self.sig_files_changed.emit(r_files)
            self.set_dayu_path(r_files[0])
    else:
        r_file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Browser File", self.get_dayu_path(), filter_list)
        if r_file:
            self.sig_file_changed.emit(r_file)
            self.set_dayu_path(r_file)


# @Slot()
def _slot_browser_folder(self):
    r_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Browser Folder", self.get_dayu_path())
    if r_folder:
        if self.get_dayu_multiple():
            self.sig_folders_changed.emit([r_folder])
        else:
            self.sig_folder_changed.emit(r_folder)
        self.set_dayu_path(r_folder)


# @Slot()
def _slot_save_file(self):
    filter_list = (
        "File(%s)" % (" ".join(["*" + e for e in self.get_dayu_filters()]))
        if self.get_dayu_filters()
        else "Any File(*)"
    )
    r_file, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", self.get_dayu_path(), filter_list)
    if r_file:
        self.sig_file_changed.emit(r_file)
        self.set_dayu_path(r_file)


class MClickBrowserFilePushButton(MPushButton):
    """A Clickable push button to browser files"""

    sig_file_changed = QtCore.Signal(str)
    sig_files_changed = QtCore.Signal(list)
    slot_browser_file = _slot_browser_file

    def __init__(self, text="Browser", multiple=False, parent=None):
        super(MClickBrowserFilePushButton, self).__init__(text=text, parent=parent)
        self.setProperty("multiple", multiple)
        self.clicked.connect(self.slot_browser_file)
        self.setToolTip(self.tr("Click to browser file"))

        self._path = None
        self._multiple = multiple
        self._filters = []

    def get_dayu_filters(self):
        """
        Get browser's format filters
        :return: list
        """
        return self._filters

    def set_dayu_filters(self, value):
        """
        Set browser file format filters
        :param value:
        :return: None
        """
        self._filters = value

    def get_dayu_path(self):
        """
        Get last browser file path
        :return: str
        """
        return self._path

    def set_dayu_path(self, value):
        """
        Set browser file start path
        :param value: str
        :return: None
        """
        self._path = value

    def get_dayu_multiple(self):
        """
        Get browser can select multiple file or not
        :return: bool
        """
        return self._multiple

    def set_dayu_multiple(self, value):
        """
        Set browser can select multiple file or not
        :param value: bool
        :return: None
        """
        self._multiple = value

    dayu_multiple = QtCore.Property(bool, get_dayu_multiple, set_dayu_multiple)
    dayu_path = QtCore.Property(six.string_types[0], get_dayu_path, set_dayu_path)
    dayu_filters = QtCore.Property(list, get_dayu_filters, set_dayu_filters)


class MClickBrowserFileToolButton(MToolButton):
    """A Clickable tool button to browser files"""

    sig_file_changed = QtCore.Signal(str)
    sig_files_changed = QtCore.Signal(list)
    slot_browser_file = _slot_browser_file

    def __init__(self, multiple=False, parent=None):
        super(MClickBrowserFileToolButton, self).__init__(parent=parent)
        self.set_dayu_svg("cloud_line.svg")
        self.icon_only()
        self.clicked.connect(self.slot_browser_file)
        self.setToolTip(self.tr("Click to browser file"))

        self._path = None
        self._multiple = multiple
        self._filters = []

    def get_dayu_filters(self):
        """
        Get browser's format filters
        :return: list
        """
        return self._filters

    def set_dayu_filters(self, value):
        """
        Set browser file format filters
        :param value:
        :return: None
        """
        self._filters = value

    def get_dayu_path(self):
        """
        Get last browser file path
        :return: str
        """
        return self._path

    def set_dayu_path(self, value):
        """
        Set browser file start path
        :param value: str
        :return: None
        """
        self._path = value

    def get_dayu_multiple(self):
        """
        Get browser can select multiple file or not
        :return: bool
        """
        return self._multiple

    def set_dayu_multiple(self, value):
        """
        Set browser can select multiple file or not
        :param value: bool
        :return: None
        """
        self._multiple = value

    dayu_multiple = QtCore.Property(bool, get_dayu_multiple, set_dayu_multiple)
    dayu_path = QtCore.Property(six.string_types[0], get_dayu_path, set_dayu_path)
    dayu_filters = QtCore.Property(list, get_dayu_filters, set_dayu_filters)


class MClickSaveFileToolButton(MToolButton):
    """A Clickable tool button to browser files"""

    sig_file_changed = QtCore.Signal(str)
    slot_browser_file = _slot_save_file

    def __init__(self, multiple=False, parent=None):
        super(MClickSaveFileToolButton, self).__init__(parent=parent)
        self.set_dayu_svg("save_line.svg")
        self.icon_only()
        self.clicked.connect(self.slot_browser_file)
        self.setToolTip(self.tr("Click to save file"))

        self._path = None
        self._multiple = multiple
        self._filters = []

    def get_dayu_filters(self):
        """
        Get browser's format filters
        :return: list
        """
        return self._filters

    def set_dayu_filters(self, value):
        """
        Set browser file format filters
        :param value:
        :return: None
        """
        self._filters = value

    def get_dayu_path(self):
        """
        Get last browser file path
        :return: str
        """
        return self._path

    def set_dayu_path(self, value):
        """
        Set browser file start path
        :param value: str
        :return: None
        """
        self._path = value

    dayu_path = QtCore.Property(six.string_types[0], get_dayu_path, set_dayu_path)
    dayu_filters = QtCore.Property(list, get_dayu_filters, set_dayu_filters)


class MDragFileButton(MToolButton):
    """A Clickable and draggable tool button to upload files"""

    sig_file_changed = QtCore.Signal(str)
    sig_files_changed = QtCore.Signal(list)
    slot_browser_file = _slot_browser_file

    def __init__(self, text="", multiple=False, parent=None):
        super(MDragFileButton, self).__init__(parent=parent)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.text_under_icon()
        self.setText(text)
        size = dayu_theme.drag_size
        self.set_dayu_size(size)
        self.setIconSize(QtCore.QSize(size, size))
        self.set_dayu_svg("cloud_line.svg")

        self.clicked.connect(self.slot_browser_file)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setToolTip(self.tr("Click to browser file"))

        self._path = None
        self._multiple = multiple
        self._filters = []

    def get_dayu_filters(self):
        """
        Get browser's format filters
        :return: list
        """
        return self._filters

    def set_dayu_filters(self, value):
        """
        Set browser file format filters
        :param value:
        :return: None
        """
        self._filters = value

    def get_dayu_path(self):
        """
        Get last browser file path
        :return: str
        """
        return self._path

    def set_dayu_path(self, value):
        """
        Set browser file start path
        :param value: str
        :return: None
        """
        self._path = value

    def get_dayu_multiple(self):
        """
        Get browser can select multiple file or not
        :return: bool
        """
        return self._multiple

    def set_dayu_multiple(self, value):
        """
        Set browser can select multiple file or not
        :param value: bool
        :return: None
        """
        self._multiple = value

    dayu_multiple = QtCore.Property(bool, get_dayu_multiple, set_dayu_multiple)
    dayu_path = QtCore.Property(six.string_types[0], get_dayu_path, set_dayu_path)
    dayu_filters = QtCore.Property(list, get_dayu_filters, set_dayu_filters)

    def dragEnterEvent(self, event):
        """Override dragEnterEvent. Validate dragged files"""
        if event.mimeData().hasFormat("text/uri-list"):
            file_list = self._get_valid_file_list(event.mimeData().urls())
            count = len(file_list)
            if count == 1 or (count > 1 and self.get_dayu_multiple()):
                event.acceptProposedAction()
                return

    def dropEvent(self, event):
        """Override dropEvent to accept the dropped files"""
        file_list = self._get_valid_file_list(event.mimeData().urls())
        if self.get_dayu_multiple():
            self.sig_files_changed.emit(file_list)
            self.set_dayu_path(file_list)
        else:
            self.sig_file_changed.emit(file_list[0])
            self.set_dayu_path(file_list[0])

    def _get_valid_file_list(self, url_list):
        # Import built-in modules
        import subprocess
        import sys

        file_list = []
        for url in url_list:
            file_name = url.toLocalFile()
            if sys.platform == "darwin":
                sub_process = subprocess.Popen(
                    "osascript -e 'get posix path of posix file \"file://{}\" -- kthxbai'".format(file_name),
                    stdout=subprocess.PIPE,
                    shell=True,
                )
                # print sub_process.communicate()[0].strip()
                file_name = sub_process.communicate()[0].strip()
                sub_process.wait()

            if os.path.isfile(file_name):
                if self.get_dayu_filters():
                    if os.path.splitext(file_name)[-1] in self.get_dayu_filters():
                        file_list.append(file_name)
                else:
                    file_list.append(file_name)

        return file_list


class MClickBrowserFolderPushButton(MPushButton):
    """A Clickable push button to browser folders"""

    sig_folder_changed = QtCore.Signal(str)
    sig_folders_changed = QtCore.Signal(list)
    slot_browser_folder = _slot_browser_folder

    def __init__(self, text="", multiple=False, parent=None):
        super(MClickBrowserFolderPushButton, self).__init__(text=text, parent=parent)
        self.setProperty("multiple", multiple)
        self.clicked.connect(self.slot_browser_folder)
        self.setToolTip(self.tr("Click to browser folder"))

        self._path = None
        self._multiple = multiple

    def get_dayu_path(self):
        """
        Get last browser file path
        :return: str
        """
        return self._path

    def set_dayu_path(self, value):
        """
        Set browser file start path
        :param value: str
        :return: None
        """
        self._path = value

    def get_dayu_multiple(self):
        """
        Get browser can select multiple file or not
        :return: bool
        """
        return self._multiple

    def set_dayu_multiple(self, value):
        """
        Set browser can select multiple file or not
        :param value: bool
        :return: None
        """
        self._multiple = value

    dayu_multiple = QtCore.Property(bool, get_dayu_multiple, set_dayu_multiple)
    dayu_path = QtCore.Property(six.string_types[0], get_dayu_path, set_dayu_path)


@property_mixin
class MClickBrowserFolderToolButton(MToolButton):
    """A Clickable tool button to browser folders"""

    sig_folder_changed = QtCore.Signal(str)
    sig_folders_changed = QtCore.Signal(list)
    slot_browser_folder = _slot_browser_folder

    def __init__(self, multiple=False, parent=None):
        super(MClickBrowserFolderToolButton, self).__init__(parent=parent)

        self.set_dayu_svg("folder_line.svg")
        self.icon_only()
        self.clicked.connect(self.slot_browser_folder)
        self.setToolTip(self.tr("Click to browser folder"))

        self._path = None
        self._multiple = multiple

    def get_dayu_path(self):
        """
        Get last browser file path
        :return: str
        """
        return self._path

    def set_dayu_path(self, value):
        """
        Set browser file start path
        :param value: str
        :return: None
        """
        self._path = value

    def get_dayu_multiple(self):
        """
        Get browser can select multiple file or not
        :return: bool
        """
        return self._multiple

    def set_dayu_multiple(self, value):
        """
        Set browser can select multiple file or not
        :param value: bool
        :return: None
        """
        self._multiple = value

    dayu_multiple = QtCore.Property(bool, get_dayu_multiple, set_dayu_multiple)
    dayu_path = QtCore.Property(six.string_types[0], get_dayu_path, set_dayu_path)


@property_mixin
@cursor_mixin
class MDragFolderButton(MToolButton):
    """A Clickable and draggable tool button to browser folders"""

    sig_folder_changed = QtCore.Signal(str)
    sig_folders_changed = QtCore.Signal(list)
    slot_browser_folder = _slot_browser_folder

    def __init__(self, multiple=False, parent=None):
        super(MDragFolderButton, self).__init__(parent=parent)
        self.setAcceptDrops(True)
        self.setMouseTracking(True)
        self.text_under_icon()
        self.set_dayu_svg("folder_line.svg")
        size = dayu_theme.drag_size
        self.set_dayu_size(size)
        self.setIconSize(QtCore.QSize(size, size))
        self.setText(self.tr("Click or drag folder here"))
        self.clicked.connect(self.slot_browser_folder)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setToolTip(self.tr("Click to browser folder or drag folder here"))

        self._path = None
        self._multiple = multiple

    def get_dayu_path(self):
        """
        Get last browser file path
        :return: str
        """
        return self._path

    def set_dayu_path(self, value):
        """
        Set browser file start path
        :param value: str
        :return: None
        """
        self._path = value

    def get_dayu_multiple(self):
        """
        Get browser can select multiple file or not
        :return: bool
        """
        return self._multiple

    def set_dayu_multiple(self, value):
        """
        Set browser can select multiple file or not
        :param value: bool
        :return: None
        """
        self._multiple = value

    dayu_multiple = QtCore.Property(bool, get_dayu_multiple, set_dayu_multiple)
    dayu_path = QtCore.Property(bool, get_dayu_path, set_dayu_path)

    def dragEnterEvent(self, event):
        """Override dragEnterEvent. Validate dragged folders"""
        if event.mimeData().hasFormat("text/uri-list"):
            folder_list = [url.toLocalFile() for url in event.mimeData().urls() if os.path.isdir(url.toLocalFile())]
            count = len(folder_list)
            if count == 1 or (count > 1 and self.get_dayu_multiple()):
                event.acceptProposedAction()
                return

    def dropEvent(self, event):
        """Override dropEvent to accept the dropped folders"""
        folder_list = [url.toLocalFile() for url in event.mimeData().urls() if os.path.isdir(url.toLocalFile())]
        if self.get_dayu_multiple():
            self.sig_folders_changed.emit(folder_list)
        else:
            self.sig_folder_changed.emit(folder_list[0])
        self.set_dayu_path(folder_list[0])
