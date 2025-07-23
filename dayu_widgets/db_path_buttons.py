"""Path buttons widget."""

import os
import sys
from functools import partial
from itertools import zip_longest

from qtpy import QtCore
from qtpy import QtWidgets

from dayu_widgets import utils
from dayu_widgets.static import request_file


def parse_db_orm(orm):
    """
    Parse database ORM object into a dictionary format.
    
    Args:
        orm: Database ORM object that contains name, parent and tablename attributes
        
    Returns:
        dict: A dictionary containing:
            - name (str): Name of the orm object or 'ROOT' if it's root
            - icon: Icon for the orm object
            - get_children (callable): Function to get children of this orm
            - has_children (callable): Function to check if this orm has children
            - data: Original orm object
    """
    orm_map = {"view": "items", "search": "items", "folder": "children"}
    return {
        "name": "ROOT" if hasattr(orm, "parent") and orm.parent is None else orm.name,
        "icon": utils.icon_formatter(orm),
        "get_children": lambda x: [
            parse_db_orm(orm) for orm in getattr(x, orm_map.get(x.__tablename__, None)) if orm.active
        ],
        "has_children": lambda x: hasattr(x, orm_map.get(x.__tablename__, None)),
        "data": orm,
    }


def parse_path(path):
    """
    Parse file system path into a dictionary format.
    
    Args:
        path (str): File system path to parse
        
    Returns:
        dict: A dictionary containing:
            - name (str): Base name of the path or full path if base name is empty
            - icon: Icon for the path (folder icon)
            - get_children (callable): Function to get subdirectories of this path
            - has_children (callable): Function to check if this path has subdirectories
            - data: Original path string
    """
    return {
        "name": os.path.basename(path) or path,
        "icon": utils.icon_formatter(request_file("folder_line.svg")),
        "get_children": lambda x: [
            parse_path(os.path.join(path, i)) for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))
        ],
        "has_children": lambda x: next(
            (True for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))),
            False,
        ),
        "data": path,
    }


class MBaseButton(QtWidgets.QWidget):
    """
    Base button widget for path navigation.
    
    Signals:
        sig_name_button_clicked (int): Emitted when the name button is clicked
        sig_menu_action_clicked (int, dict): Emitted when a menu action is clicked
    """

    sig_name_button_clicked = QtCore.Signal(int)
    sig_menu_action_clicked = QtCore.Signal(int, dict)

    def __init__(self, data_dict, parent=None):
        """
        Initialize the base button.
        
        Args:
            data_dict (dict): Dictionary containing button data
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super(MBaseButton, self).__init__(parent)
        self.data_dict = data_dict
        name_button = QtWidgets.QToolButton(parent=self)
        name_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        name_button.setIcon(data_dict.get("icon"))
        name_button.clicked.connect(self.slot_button_clicked)
        name_button.setText(data_dict.get("name"))

        self.menu_button = QtWidgets.QToolButton(parent=self)
        self.menu_button.setAutoRaise(False)
        self.menu_button.setArrowType(QtCore.Qt.RightArrow)
        self.menu_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.menu_button.setIconSize(QtCore.QSize(10, 10))
        self.menu_button.clicked.connect(self.slot_show_menu)
        self.menu_button.setVisible(data_dict.get("has_children")(data_dict.get("data")))
        main_lay = QtWidgets.QHBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.setSpacing(0)
        main_lay.addWidget(name_button)
        main_lay.addWidget(self.menu_button)
        self.setLayout(main_lay)

    @QtCore.Slot()
    def slot_button_clicked(self):
        self.sig_name_button_clicked.emit(self.data_dict.get("index"))

    @QtCore.Slot()
    def slot_action_clicked(self, sub_obj):
        self.sig_menu_action_clicked.emit(self.data_dict.get("index"), sub_obj)

    @QtCore.Slot()
    def slot_show_menu(self):
        menu = QtWidgets.QMenu(self)
        data_list = self.data_dict.get("get_children")(self.data_dict.get("data"))
        for sub_obj in data_list:
            action = menu.addAction(sub_obj.get("icon"), sub_obj.get("name"))
            action.triggered.connect(partial(self.slot_action_clicked, sub_obj))
        self.menu_button.setMenu(menu)
        self.menu_button.showMenu()

    def enterEvent(self, *args, **kwargs):
        self.menu_button.setArrowType(QtCore.Qt.DownArrow)
        return super(MBaseButton, self).enterEvent(*args, **kwargs)

    def leaveEvent(self, *args, **kwargs):
        self.menu_button.setArrowType(QtCore.Qt.RightArrow)
        return super(MBaseButton, self).leaveEvent(*args, **kwargs)


class MDBPathButtons(QtWidgets.QFrame):
    """
    Path buttons widget for navigation.
    
    Signals:
        sig_current_changed: Emitted when the current path changes
    """

    sig_current_changed = QtCore.Signal()

    @utils.dayu_css()
    def __init__(self, parent=None):
        """
        Initialize the path buttons widget.
        
        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super(MDBPathButtons, self).__init__(parent)
        self.parse_function = None
        self.data_list = []

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        main_lay = QtWidgets.QHBoxLayout()
        main_lay.setContentsMargins(0, 0, 0, 0)
        main_lay.addLayout(self.layout)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def set_parse_function(self, func):
        """
        Set the parse function for the path buttons.
        
        Args:
            func (callable): Parse function to use
        """
        self.parse_function = func

    def setup_data(self, obj):
        """
        Setup the data for the path buttons.
        
        Args:
            obj: Object to parse and display
        """
        self.clear_downstream(0)
        if obj:
            self.add_level(self.parse_function(obj))
            self.sig_current_changed.emit()

    def add_level(self, data_dict):
        """
        Add a level to the path buttons.
        
        Args:
            data_dict (dict): Dictionary containing level data
        """
        index = len(self.data_list)
        data_dict.update({"index": index})
        button = MBaseButton(data_dict, parent=self)
        button.sig_name_button_clicked.connect(self.slot_button_clicked)
        button.sig_menu_action_clicked.connect(self.slot_menu_button_clicked)
        self.layout.addWidget(button)
        data_dict.update({"widget": button})
        self.data_list.append(data_dict)

    def clear_downstream(self, index):
        """
        Clear the downstream levels.
        
        Args:
            index (int): Index to clear from
        """
        for i, data_dict in enumerate(self.data_list):
            if i >= index:
                button = data_dict.get("widget")
                self.layout.removeWidget(button)
                button.setVisible(False)
        self.data_list = self.data_list[:index]

    @QtCore.Slot(QtCore.QObject, dict)
    def slot_show_menu(self, menu_button, data_dict):
        """
        Show the menu for a button.
        
        Args:
            menu_button (QtWidgets.QToolButton): Button to show menu for
            data_dict (dict): Dictionary containing button data
        """
        menu = QtWidgets.QMenu(self)
        data_list = data_dict.get("get_children")(data_dict.get("data"))
        index = data_dict.get("index")
        for sub_obj in data_list:
            action = menu.addAction(sub_obj.get("icon"), sub_obj.get("name"))
            action.triggered.connect(partial(self.slot_menu_button_clicked, index, sub_obj))
        menu_button.setMenu(menu)
        menu_button.showMenu()

    @QtCore.Slot(int)
    def slot_button_clicked(self, index):
        """
        Handle button click event.
        
        Args:
            index (int): Index of the button clicked
        """
        self.clear_downstream(index + 1)
        self.sig_current_changed.emit()

    @QtCore.Slot(int, dict)
    def slot_menu_button_clicked(self, index, data_dict):
        """
        Handle menu button click event.
        
        Args:
            index (int): Index of the button clicked
            data_dict (dict): Dictionary containing button data
        """
        self.clear_downstream(index + 1)
        self.add_level(data_dict)
        self.sig_current_changed.emit()

    @QtCore.Slot(list)
    def slot_go_to(self, obj_list):
        """
        Go to a specific path.
        
        Args:
            obj_list (list): List of objects to navigate to
        """
        for index, (his_obj, our_obj) in enumerate(zip_longest(obj_list, self.get_obj_list())):
            if his_obj is None:
                # 如果传来的 obj_list 最后一个是 None，则我方的 obj 多，直接清理掉多余的
                self.clear_downstream(index)
                return
            elif our_obj is None:
                # 我方的 obj 不够，则追加
                self.add_level(self.parse_function(his_obj))
            elif his_obj != our_obj:
                # 我方 跟 传来的 obj 不一样，清理掉后面的，并追加传来的orm
                self.clear_downstream(index)
                self.add_level(self.parse_function(his_obj))
            else:
                # 我方和传来的 obj 完全一样，不做处理
                continue

    def get_obj_list(self):
        """
        Get the list of objects.
        
        Returns:
            list: List of objects
        """
        return [i.get("data") for i in self.data_list]


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test = MDBPathButtons()
    test.set_parse_function(parse_path)
    test.setup_data("d:/")
    test.show()
    sys.exit(app.exec_())
