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
from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets
from Qt.QtSvg import QSvgRenderer
import six


class MCacheDict(object):
    _render = QSvgRenderer()

    def __init__(self, cls):
        super(MCacheDict, self).__init__()
        self.cls = cls
        self._cache_pix_dict = {}

    def _render_svg(self, svg_path, replace_color=None):
        # Import local modules
        from dayu_widgets import dayu_theme

        replace_color = replace_color or dayu_theme.icon_color
        if (self.cls is QtGui.QIcon) and (replace_color is None):
            return QtGui.QIcon(svg_path)
        with open(svg_path, "r") as f:
            data_content = f.read()
            if replace_color is not None:
                data_content = data_content.replace("#555555", replace_color)
            self._render.load(QtCore.QByteArray(six.b(data_content)))
            pix = QtGui.QPixmap(128, 128)
            pix.fill(QtCore.Qt.transparent)
            painter = QtGui.QPainter(pix)
            self._render.render(painter)
            painter.end()
            if self.cls is QtGui.QPixmap:
                return pix
            else:
                return self.cls(pix)

    def __call__(self, path, color=None):
        # Import local modules
        from dayu_widgets import utils

        full_path = utils.get_static_file(path)
        if full_path is None:
            return self.cls()
        key = "{}{}".format(full_path.lower(), color or "")
        pix_map = self._cache_pix_dict.get(key, None)
        if pix_map is None:
            if full_path.endswith("svg"):
                pix_map = self._render_svg(full_path, color)
            else:
                pix_map = self.cls(full_path)
            self._cache_pix_dict.update({key: pix_map})
        return pix_map


def get_scale_factor():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication([])
    standard_dpi = 96.0
    scale_factor_x = QtWidgets.QApplication.desktop().logicalDpiX() / standard_dpi
    scale_factor_y = QtWidgets.QApplication.desktop().logicalDpiY() / standard_dpi
    return scale_factor_x, scale_factor_y


MPixmap = MCacheDict(QtGui.QPixmap)
MIcon = MCacheDict(QtGui.QIcon)
