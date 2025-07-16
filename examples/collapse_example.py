#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.3
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.collapse import MCollapse
from dayu_widgets3.label import MLabel


class CollapseExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CollapseExample, self).__init__(parent)
        self.setWindowTitle("Examples for MCollapse")
        self._init_ui()

    def _init_ui(self):
        label_1 = MLabel(
            "史蒂夫·乔布斯（Steve Jobs），1955年2月24日生于美国加利福尼亚州旧金山，美国发明家、企业家、美国苹果公司联合创办人。"
        )
        label_2 = MLabel(
            "斯蒂夫·盖瑞·沃兹尼亚克（Stephen Gary Wozniak），美国电脑工程师，曾与史蒂夫·乔布斯合伙创立苹果电脑（今之苹果公司）。斯蒂夫·盖瑞·沃兹尼亚克曾就读于美国科罗拉多大学，后转学入美国著名高等学府加州大学伯克利分校（UC Berkeley）并获得电机工程及计算机（EECS）本科学位（1987年）。"
        )
        label_3 = MLabel(
            "乔纳森·伊夫是一位工业设计师，现任Apple公司设计师兼资深副总裁，英国爵士。他曾参与设计了iPod，iMac，iPhone，iPad等众多苹果产品。除了乔布斯，他是对苹果那些著名的产品最有影响力的人。"
        )
        label_1.setWordWrap(True)
        label_2.setWordWrap(True)
        label_3.setWordWrap(True)
        section_list = [
            {"title": "史蒂夫乔布斯", "expand": True, "widget": label_1},
            {
                "title": "可关闭的",
                "expand": True,
                "widget": MLabel("This is a closable collapse item"),
                "closable": True,
            },
            {"title": "斯蒂夫·盖瑞·沃兹尼亚克", "expand": True, "widget": label_2},
        ]

        section_group = MCollapse()
        section_group.add_section_list(section_list)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(section_group)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = CollapseExample()
        dayu_theme.apply(test)
        test.show()
