# Import third-party modules
import pytest
from qtpy import QtCore
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3 import mixin


def test_property_mixin(qtbot):
    @mixin.property_mixin
    class _TestClass(QtWidgets.QWidget):
        def __init__(self, parent=None):
            super(_TestClass, self).__init__(parent)
            self._test_attr = None
            self.set_my_property("first_value")

        def set_my_property(self, value):
            self.setProperty("my_property", value)

        def _set_my_property(self, value):
            self._test_attr = value

    test_widget = _TestClass()
    assert test_widget._test_attr == "first_value"
    qtbot.addWidget(test_widget)
    test_widget.set_my_property("test_string")
    assert test_widget._test_attr == "test_string"


def test_cursor_mixin(qtbot):
    @mixin.cursor_mixin
    class _TestClass(QtWidgets.QPushButton):
        def __init__(self, parent=None):
            super(_TestClass, self).__init__(parent)
            geo = QtWidgets.QApplication.desktop().screenGeometry()
            self.setGeometry(geo.width() / 4, geo.height() / 4, geo.width() / 2, geo.height() / 2)

    main_widget = QtWidgets.QWidget()
    button_test = _TestClass()
    button_normal = QtWidgets.QPushButton()
    test_lay = QtWidgets.QVBoxLayout()
    test_lay.addWidget(button_test)
    test_lay.addWidget(button_normal)
    main_widget.setLayout(test_lay)

    qtbot.addWidget(main_widget)
    main_widget.show()
    button_test.setEnabled(False)
    assert QtWidgets.QApplication.overrideCursor() is None  # Not override cursor

    qtbot.mouseMove(button_test)  # mouse enter

    def check_cursor():
        assert QtWidgets.QApplication.overrideCursor() is not None
        assert QtWidgets.QApplication.overrideCursor().shape() == QtCore.Qt.ForbiddenCursor

    qtbot.waitUntil(check_cursor)

    qtbot.mouseMove(button_normal)  # mouse leave

    def check_cursor():
        assert QtWidgets.QApplication.overrideCursor() is None  # Restore override cursor

    qtbot.waitUntil(check_cursor)

    button_test.setEnabled(True)
    qtbot.mouseMove(button_test)  # mouse enter

    def check_cursor():
        assert QtWidgets.QApplication.overrideCursor() is not None
        assert QtWidgets.QApplication.overrideCursor().shape() == QtCore.Qt.PointingHandCursor

    qtbot.waitUntil(check_cursor)

    qtbot.mouseMove(button_normal)  # mouse leave

    def check_cursor():
        assert QtWidgets.QApplication.overrideCursor() is None  # Restore override cursor

    qtbot.waitUntil(check_cursor)


def test_focus_shadow_mixin(qtbot):
    @mixin.focus_shadow_mixin
    class _TestClass(QtWidgets.QPushButton):
        def __init__(self, parent=None):
            super(_TestClass, self).__init__(parent)
            geo = QtWidgets.QApplication.desktop().screenGeometry()
            self.setGeometry(geo.width() / 4, geo.height() / 4, geo.width() / 2, geo.height() / 2)

    main_widget = QtWidgets.QWidget()
    button_test = _TestClass()

    button_normal = QtWidgets.QPushButton()
    test_lay = QtWidgets.QVBoxLayout()
    test_lay.addWidget(button_test)
    test_lay.addWidget(button_normal)
    main_widget.setLayout(test_lay)

    qtbot.addWidget(main_widget)

    assert button_test.graphicsEffect() is None

    main_widget.show()
    main_widget.setFocus()
    # focus in

    qtbot.mouseClick(button_test, QtCore.Qt.LeftButton)

    def check_focus_in():
        graphics_effect = button_test.graphicsEffect()
        assert graphics_effect is not None
        assert graphics_effect.isEnabled()
        assert isinstance(graphics_effect, QtWidgets.QGraphicsDropShadowEffect)

    qtbot.waitUntil(check_focus_in)

    qtbot.mouseClick(button_normal, QtCore.Qt.LeftButton)  # focus out

    def check_effect():
        assert button_test.graphicsEffect() is not None
        assert not button_test.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_effect)

    qtbot.mouseClick(button_test, QtCore.Qt.LeftButton)  # focus in

    def check_effect():
        assert button_test.graphicsEffect() is not None
        assert button_test.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_effect)


def test_hover_shadow_mixin(qtbot):
    @mixin.hover_shadow_mixin
    class _TestClass(QtWidgets.QPushButton):
        def __init__(self, parent=None):
            super(_TestClass, self).__init__(parent)
            geo = QtWidgets.QApplication.desktop().screenGeometry()
            self.setGeometry(geo.width() / 4, geo.height() / 4, geo.width() / 2, geo.height() / 2)

    main_widget = QtWidgets.QWidget()
    button_test = _TestClass()
    button_normal = QtWidgets.QPushButton()
    test_lay = QtWidgets.QVBoxLayout()
    test_lay.addWidget(button_test)
    test_lay.addWidget(button_normal)
    main_widget.setLayout(test_lay)

    qtbot.addWidget(main_widget)

    assert button_test.graphicsEffect() is None

    main_widget.show()

    qtbot.mouseMove(button_test)  # mouse in

    def check_effect():
        graphics_effect = button_test.graphicsEffect()
        assert graphics_effect is not None
        assert graphics_effect.isEnabled()
        assert isinstance(graphics_effect, QtWidgets.QGraphicsDropShadowEffect)

    qtbot.waitUntil(check_effect)

    qtbot.mouseMove(button_normal)  # mouse out

    def check_effect():
        assert button_test.graphicsEffect() is not None
        assert not button_test.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_effect)

    qtbot.mouseMove(button_test)  # mouse in

    def check_effect():
        assert button_test.graphicsEffect() is not None
        assert button_test.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_effect)


@pytest.mark.parametrize(
    "input_widget, result",
    (
        (QtWidgets.QLabel, False),
        (QtWidgets.QWidget, False),
        (QtWidgets.QStackedWidget, True),
        (QtWidgets.QStackedLayout, False),
        (QtWidgets.QTabWidget, True),
        (QtWidgets.QTabBar, False),
    ),
)
def test_stackable(input_widget, result):
    assert mixin._stackable(input_widget) == result


def test_stacked_animation_mixin_normal(qtbot):
    @mixin.stacked_animation_mixin
    class _TestClass(QtWidgets.QStackedWidget):
        def __init__(self, parent=None):
            super(_TestClass, self).__init__(parent)

    main_widget = _TestClass()
    qtbot.addWidget(main_widget)
    assert hasattr(main_widget, "_to_show_pos_ani")
    assert isinstance(main_widget._to_show_pos_ani, QtCore.QPropertyAnimation)
    assert hasattr(main_widget, "_to_hide_pos_ani")
    assert isinstance(main_widget._to_hide_pos_ani, QtCore.QPropertyAnimation)
    assert hasattr(main_widget, "_opacity_eff")
    assert isinstance(main_widget._opacity_eff, QtWidgets.QGraphicsOpacityEffect)
    assert hasattr(main_widget, "_opacity_ani")
    assert isinstance(main_widget._opacity_ani, QtCore.QPropertyAnimation)
    assert hasattr(main_widget, "_play_anim")
    assert hasattr(main_widget, "_disable_opacity")

    assert main_widget._previous_index == 0
    label_1 = QtWidgets.QLabel("test")
    index_1 = main_widget.addWidget(label_1)

    def check_index():
        assert main_widget._previous_index == index_1
        assert not label_1.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_index)

    label_2 = QtWidgets.QLabel("test2")
    index_2 = main_widget.addWidget(label_2)
    main_widget.setCurrentIndex(index_1)

    def check_index():
        assert main_widget._previous_index == index_1
        assert not label_1.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_index)
    main_widget.setCurrentIndex(index_2)

    def check_index():
        assert main_widget._previous_index == index_2
        assert not label_2.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_index)


def test_stacked_animation_mixin_error(qtbot):
    @mixin.stacked_animation_mixin
    class _TestClass(QtWidgets.QPushButton):
        def __init__(self, parent=None):
            super(_TestClass, self).__init__(parent)

    main_widget = _TestClass()
    qtbot.addWidget(main_widget)
    assert not hasattr(main_widget, "_to_show_pos_ani")
    assert not hasattr(main_widget, "_to_hide_pos_ani")
    assert not hasattr(main_widget, "_opacity_eff")
    assert not hasattr(main_widget, "_opacity_ani")
    assert not hasattr(main_widget, "_play_anim")
    assert not hasattr(main_widget, "_disable_opacity")
