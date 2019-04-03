import importlib

from dayu_widgets.MButtonGroup import MToolButtonGroup
from dayu_widgets.MDockWidget import MDockWidget
from dayu_widgets import dayu_theme
from dayu_widgets.MToolButton import MToolButton
from dayu_widgets.qt import *


def get_test_widget():
    result = []
    for index, i in enumerate(os.listdir('.')):
        if i.startswith('__') or (not i.endswith('.py')) or i == 'demo.py':
            continue
        name = i.split('.')[0]
        module_name = 'dayu_widgets.examples.{component}'.format(component=name)
        module = importlib.import_module(module_name, name)
        if hasattr(module, name):
            with open('./{}.py'.format(name)) as f:
                result.append((name, getattr(module, name), f.readlines()))
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

        list_widget = MToolButtonGroup(orientation=Qt.Vertical,
                                       size=dayu_theme.small,
                                       type=MToolButton.TaoBaoType,
                                       exclusive=True,
                                       parent=self)
        list_widget.sig_checked_changed.connect(self.slot_change_widget)
        data_list = []
        for index, (name, cls, code) in enumerate(get_test_widget()):
            data_list.append({'text': name[:-4], 'data': code, 'checkable': True})
            widget = cls()
            widget.setProperty('code', code)
            self.stacked_widget.addWidget(widget)
        list_widget.set_button_list(data_list)
        list_widget.set_checked(0)

        left_widget = QWidget()
        left_lay = QVBoxLayout()
        left_widget.setLayout(left_lay)
        left_lay.addWidget(list_widget)
        scroll_area = QScrollArea()
        scroll_area.setWidget(left_widget)

        test_widget = MDockWidget('Example List')
        test_widget.setWidget(left_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, test_widget)

        code_widget = MDockWidget('Example Code')
        code_widget.setWidget(self.text_edit)
        self.addDockWidget(Qt.RightDockWidgetArea, code_widget)
        self.setCentralWidget(self.stacked_widget)

    def slot_change_widget(self, index):
        self.stacked_widget.setCurrentIndex(index)
        widget = self.stacked_widget.widget(index)
        self.text_edit.setPlainText(''.join(widget.property('code')))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MDemo()
    test.show()
    sys.exit(app.exec_())
