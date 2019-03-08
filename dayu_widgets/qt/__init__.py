try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
except:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtWebKit import *
    from PySide.QtSvg import *


def property_mixin(cls):
    def event(self, event):
        if event.type() == QEvent.DynamicPropertyChange:
            p = event.propertyName()
            if hasattr(self, '_set_{}'.format(p)):
                callback = getattr(self, '_set_{}'.format(p))
                callback(self.property(str(p)))
        return super(cls, self).event(event)

    setattr(cls, 'event', event)
    return cls


class MView(object):
    LargeSize = 'large'
    DefaultSize = 'default'
    SmallSize = 'small'
    TinySize = 'tiny'


class MCacheDict(object):
    _render = QSvgRenderer()

    def __init__(self, cls):
        super(MCacheDict, self).__init__()
        self.cls = cls
        self._cache_pix_dict = {}

    def __call__(self, path, color=None):
        assert isinstance(path, basestring)
        import os
        from dayu_widgets import STATIC_FOLDERS
        path = next((os.path.join(prefix, path) for prefix in [''] + STATIC_FOLDERS if
                     os.path.isfile(os.path.join(prefix, path))), path)
        key = unicode(path.lower())
        pix_map = self._cache_pix_dict.get(key, None)
        if pix_map is None:
            if path.endswith('svg') and isinstance(color, basestring):
                key += color
                with open(path, 'r+') as f:
                    self._render.load(QByteArray(f.read().replace('#555555', color)))
                    pix = QPixmap(128, 128)
                    pix.fill(Qt.transparent)
                    painter = QPainter(pix)
                    self._render.render(painter)
                    painter.end()
                    if self.cls is QIcon:
                        pix_map = QIcon(pix)
                    elif self.cls is QPixmap:
                        pix_map = pix
            else:
                pix_map = self.cls(path)
            self._cache_pix_dict.update({key: pix_map})
        return pix_map


MPixmap = MCacheDict(QPixmap)
MIcon = MCacheDict(QIcon)
