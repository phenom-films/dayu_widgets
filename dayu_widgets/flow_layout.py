# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################
"""MFlowLayout"""


from dayu_widgets.qt import QLayout, QWidgetItem, Qt, QRect, QSize, QSizePolicy, QPoint


class MFlowLayout(QLayout):
    """
    FlowLayout, the code is come from PySide/examples/layouts/flowlayout.py
    I change the code style and add insertWidget method.
    """
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(MFlowLayout, self).__init__(parent)

        if parent is not None:
            self.setMargin(margin)

        self.setSpacing(spacing)

        self.item_list = []

    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def insertWidget(self, index, widget):
        self.addChildWidget(widget)
        if index < 0:
            index = self.count()
        item = QWidgetItem(widget)
        self.item_list.insert(index, item)
        self.update()

    def addItem(self, item):
        self.item_list.append(item)

    def count(self):
        return len(self.item_list)

    def itemAt(self, index):
        if 0 <= index < len(self.item_list):
            return self.item_list[index]

        return None

    def takeAt(self, index):
        if 0 <= index < len(self.item_list):
            return self.item_list.pop(index)

        return None

    def expandingDirections(self):
        return Qt.Orientations(Qt.Orientation(0))

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.do_layout(QRect(0, 0, width, 0), True)
        return height

    def setGeometry(self, rect):
        super(MFlowLayout, self).setGeometry(rect)
        self.do_layout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()

        for item in self.item_list:
            size = size.expandedTo(item.minimumSize())

        size += QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size

    def do_layout(self, rect, test_only):
        x = rect.x()
        y = rect.y()
        line_height = 0

        for item in self.item_list:
            wid = item.widget()
            space_x = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                 QSizePolicy.PushButton,
                                                                 Qt.Horizontal)
            space_y = self.spacing() + wid.style().layoutSpacing(QSizePolicy.PushButton,
                                                                 QSizePolicy.PushButton,
                                                                 Qt.Vertical)
            next_x = x + item.sizeHint().width() + space_x
            if next_x - space_x > rect.right() and line_height > 0:
                x = rect.x()
                y = y + line_height + space_y
                next_x = x + item.sizeHint().width() + space_x
                line_height = 0

            if not test_only:
                item.setGeometry(QRect(QPoint(x, y), item.sizeHint()))

            x = next_x
            line_height = max(line_height, item.sizeHint().height())

        return y + line_height - rect.y()
