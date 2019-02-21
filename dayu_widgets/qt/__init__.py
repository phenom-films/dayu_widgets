try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
except:
    from PySide.QtCore import *
    from PySide.QtGui import *
    from PySide.QtWebKit import *


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


class MCacheDict(object):
    def __init__(self, cls):
        super(MCacheDict, self).__init__()
        self.cls = cls
        self._cache_pix_dict = {}

    def __call__(self, path):
        assert isinstance(path, basestring)
        import os
        from dayu_widgets import STATIC_FOLDERS
        path = next((os.path.join(prefix, path) for prefix in [''] + STATIC_FOLDERS if
                     os.path.isfile(os.path.join(prefix, path))), path)
        lower_path = unicode(path.lower())
        pix_map = self._cache_pix_dict.get(lower_path, None)
        if pix_map is None:
            pix_map = self.cls(lower_path)
            self._cache_pix_dict.update({lower_path: pix_map})
        return pix_map


MPixmap = MCacheDict(QPixmap)
MIcon = MCacheDict(QIcon)
