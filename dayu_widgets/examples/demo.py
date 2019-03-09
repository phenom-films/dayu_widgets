import importlib
import os

from dayu_widgets import MRadioGroup
from dayu_widgets.qt import *
from dayu_widgets import STATIC_FOLDERS
from dayu_widgets.MTheme import global_theme


qss = '''

QSplitter::handle {{
    background-color: {border};
    image: url(splitter.svg);
}}

QSplitter::handle:horizontal {{
    width: 2px;
}}

QSplitter::handle:vertical {{
    height: 2px;
}}

'''.format(**global_theme)
qss = qss.replace('url(', 'url({}/'.format(STATIC_FOLDERS[0].replace('\\', '/')))


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


class MDemo(QDialog):
    def __init__(self, parent=None):
        super(MDemo, self).__init__(parent)
        self.setWindowTitle('Dayu Widgets Demo')
        self._init_ui()

    def _init_ui(self):
        list_widget = MRadioGroup(type='button', orientation=Qt.Vertical)
        list_widget.sig_checked_changed.connect(self.slot_change_widget)
        self.stacked_widget = QStackedWidget()
        self.text_edit = QTextEdit()
        data_list = []
        for name, cls, code in get_test_widget():
            data_list.append({'text': name, 'date': code})
            widget = cls()
            widget.setProperty('code', code)
            self.stacked_widget.addWidget(widget)
        list_widget.set_radio_list(data_list)
        list_widget.set_checked(0)

        left_widget = QWidget()
        left_lay = QVBoxLayout()
        left_widget.setLayout(left_lay)
        left_lay.addWidget(list_widget)
        left_lay.addStretch()

        splitter = QSplitter()
        splitter.setStyleSheet(qss)
        splitter.addWidget(left_widget)
        splitter.addWidget(self.stacked_widget)
        splitter.addWidget(self.text_edit)
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 30)
        splitter.setStretchFactor(2, 70)
        main_lay = QVBoxLayout()
        main_lay.addWidget(splitter)
        self.setLayout(main_lay)

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
