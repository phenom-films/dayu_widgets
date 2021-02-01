# -*- coding: utf-8 -*-
# ctrl + C stop QApplication
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
# Qt.py global variable for preferred Qt binding
os.environ["QT_PREFERRED_BINDING"] = "PyQt4;PyQt5;PySide;PySide2"
# For Houdini hython.exe
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"E:\Houdini18\bin\Qt_plugins\platforms"

import sys
MODULE = os.path.join(__file__,"..","..")
sys.path.insert(0,MODULE) if MODULE not in sys.path else None
import importlib

from dayu_widgets.qt import QMainWindow, QTextEdit, QStackedWidget, Qt
from dayu_widgets import dayu_theme
from dayu_widgets.dock_widget import MDockWidget
from dayu_widgets.item_view_set import MItemViewSet
import codecs

def get_test_widget():
    result = []
    DIR = os.path.dirname(__file__)
    for i in os.listdir(DIR):
        if i.startswith('__') or (not i.endswith('.py')) or i == 'demo.py':
            continue
        name = i.split('.')[0]
        module_name = 'examples.{component}'.format(component=name)
        class_name = ''.join(map(lambda x: x.title(), name.split('_')))
        module = importlib.import_module(module_name, class_name)
        if hasattr(module, class_name):
            with codecs.open(os.path.join(DIR,"%s.py" % name),encoding='utf-8') as f:
                result.append((name, getattr(module, class_name), f.readlines()))
    return result


@dayu_theme.deco
class MDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MDemo, self).__init__(parent)
        self.setWindowTitle('Dayu Widgets Demo')
        self._init_ui()

    def _init_ui(self):
        self.text_edit = QTextEdit()
        self.stacked_widget = QStackedWidget()

        list_widget = MItemViewSet(view_type=MItemViewSet.ListViewType)
        list_widget.set_header_list([{'key': 'name', 'label': 'Name', 'icon': 'list_view.svg'}])
        list_widget.sig_left_clicked.connect(self.slot_change_widget)
        data_list = []
        for index, (name, cls, code) in enumerate(get_test_widget()):
            data_list.append({'name': name[:-8], 'data': code})
            if not callable(cls):
                continue
            widget = cls()
            widget.setProperty('code', code)
            self.stacked_widget.addWidget(widget)
        list_widget.setup_data(data_list)

        test_widget = MDockWidget('Example List')
        test_widget.setWidget(list_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, test_widget)

        code_widget = MDockWidget('Example Code')
        code_widget.setWidget(self.text_edit)
        self.addDockWidget(Qt.RightDockWidgetArea, code_widget)
        self.setCentralWidget(self.stacked_widget)

    def slot_change_widget(self, index):
        self.stacked_widget.setCurrentIndex(index.row())
        widget = self.stacked_widget.widget(index.row())
        self.text_edit.setPlainText(''.join(widget.property('code')))


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication

    app = QApplication(sys.argv)
    
    try:
        test = MDemo()
        test.show()
    except:
        import traceback
        traceback.print_exc()

    sys.exit(app.exec_())
