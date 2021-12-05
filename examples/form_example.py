#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.4
# Email : muyanru345@163.com
###################################################################

# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from Qt import QtWidgets
from dayu_widgets.form import MForm


# from schematics.models import Model
# from schematics.types import StringType
#
# class LoginForm(Model):
#     user_name = StringType(min_length=5, max_length=15)
#     password = StringType(min_length=5, max_length=15)
#
#     class Options()
#


class MFormTest(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MFormTest, self).__init__(parent)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    # Import third-party modules
    from dayu_widgets import dayu_theme

    app = QtWidgets.QApplication(sys.argv)
    test = MFormTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
