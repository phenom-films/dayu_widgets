"""
MAvatar.
"""

# Import third-party modules
from qtpy import QtCore
from qtpy import QtGui
from qtpy import QtWidgets

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.qt import MPixmap


class MAvatar(QtWidgets.QLabel):
    """
    Avatar component. It can be used to represent people or object.
    Property:
        image: avatar image, should be QPixmap.
        dayu_size: the size of image.
    """

    def __init__(self, parent=None, flags=QtCore.Qt.Widget):
        super(MAvatar, self).__init__(parent, flags)
        self._default_pix = MPixmap("user_fill.svg")
        self._pixmap = self._default_pix
        self._original_pixmap = self._default_pix
        self._dayu_size = 0
        self.set_dayu_size(dayu_theme.default_size)

    def set_dayu_size(self, value):
        """
        Set the avatar size.
        :param value: integer
        :return: None
        """
        self._dayu_size = value
        self._set_dayu_size()

    def _set_dayu_size(self):
        self.setFixedSize(QtCore.QSize(self._dayu_size, self._dayu_size))
        self._set_dayu_image()

    def _set_dayu_image(self):
        # Check if pixmap is null or has zero size
        if self._pixmap.isNull() or self._pixmap.size().isEmpty():
            # Reset to default pixmap
            self._pixmap = self._default_pix.copy()
            # Also update original pixmap reference to ensure consistency
            self._original_pixmap = self._default_pix

        # Scale the pixmap to the current size
        if self.height() > 0:
            scaled_pixmap = self._pixmap.scaledToWidth(self.height(), QtCore.Qt.SmoothTransformation)
            self.setPixmap(scaled_pixmap)

    def set_dayu_image(self, value):
        """
        Set avatar image.
        :param value: QPixmap or None.
        :return: None
        """

        if value is None:
            self._pixmap = self._default_pix
            self._original_pixmap = self._default_pix
        elif isinstance(value, QtGui.QPixmap):
            if value.isNull():
                self._pixmap = self._default_pix
                self._original_pixmap = self._default_pix
            else:
                self._pixmap = value
                self._original_pixmap = value
        else:
            msg = "Input argument 'value' should be QPixmap or None, but get {}"
            raise TypeError(msg.format(type(value)))
        self._set_dayu_image()

    def get_dayu_image(self):
        """
        Get the avatar image.
        :return: QPixmap
        """
        return self._original_pixmap

    def get_dayu_size(self):
        """
        Get the avatar size
        :return: integer
        """
        return self._dayu_size

    dayu_image = QtCore.Property(QtGui.QPixmap, get_dayu_image, set_dayu_image)
    dayu_size = QtCore.Property(int, get_dayu_size, set_dayu_size)

    @classmethod
    def huge(cls, image=None):
        """Create a MAvatar with huge size"""
        inst = cls()
        inst.set_dayu_size(dayu_theme.huge)
        inst.set_dayu_image(image)
        return inst

    @classmethod
    def large(cls, image=None):
        """Create a MAvatar with large size"""
        inst = cls()
        inst.set_dayu_size(dayu_theme.large)
        inst.set_dayu_image(image)
        return inst

    @classmethod
    def medium(cls, image=None):
        """Create a MAvatar with medium size"""
        inst = cls()
        inst.set_dayu_size(dayu_theme.medium)
        inst.set_dayu_image(image)
        return inst

    @classmethod
    def small(cls, image=None):
        """Create a MAvatar with small size"""
        inst = cls()
        inst.set_dayu_size(dayu_theme.small)
        inst.set_dayu_image(image)
        return inst

    @classmethod
    def tiny(cls, image=None):
        """Create a MAvatar with tiny size"""
        inst = cls()
        inst.set_dayu_size(dayu_theme.tiny)
        inst.set_dayu_image(image)
        return inst
