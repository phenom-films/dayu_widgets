# Import third-party modules
from qtpy import QtCore
from qtpy import QtWidgets


class MSizeGrip(QtWidgets.QSizeGrip):
    def __init__(self, parent=None):
        super(MSizeGrip, self).__init__(parent)


class MTextEdit(QtWidgets.QTextEdit):
    def __init__(self, parent=None):
        super(MTextEdit, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.SubWindow)
        self._size_grip = MSizeGrip(self)
        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self._size_grip, 0, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)
        self.setLayout(layout)
        self._size_grip.setVisible(False)

    def autosize(self):
        self.textChanged.connect(self._autosize_text_edit)
        return self

    def _autosize_text_edit(self):
        # w = self.width()
        doc = self.document()
        print(self.width(), doc.lineCount(), doc.idealWidth())

    def resizeable(self):
        """Show the size grip on bottom right. User can use it to resize MTextEdit"""
        self._size_grip.setVisible(True)
        return self
