import importlib
import os

from dayu_widgets.qt import QMainWindow, QTextEdit, QStackedWidget, Qt
from dayu_widgets import dayu_theme
from dayu_widgets.dock_widget import MDockWidget
from dayu_widgets.item_view_set import MItemViewSet


def get_test_widget():
    result = []
    for index, i in enumerate(os.listdir('.')):
        if i.startswith('__') or (not i.endswith('.py')) or i == 'demo.py':
            continue
        name = i.split('.')[0]
        module_name = 'examples.{component}'.format(component=name)
        class_name = ''.join(map(lambda x: x.title(), name.split('_')))
        module = importlib.import_module(module_name, class_name)
        if hasattr(module, class_name):
            with open('./{}.py'.format(name)) as f:
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
    test = MDemo()
    test.show()
    sys.exit(app.exec_())
