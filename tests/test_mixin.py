from dayu_widgets.qt import *
from dayu_widgets import mixin
import pytest


def test_property_mixin(qtbot):
    @mixin.property_mixin
    class MTestClass(QWidget):
        def __init__(self, parent=None):
            super(MTestClass, self).__init__(parent)
            self._test_attr = None
            self.set_my_property('first_value')

        def set_my_property(self, value):
            self.setProperty('my_property', value)

        def _set_my_property(self, value):
            self._test_attr = value

    test_widget = MTestClass()
    assert test_widget._test_attr == 'first_value'
    qtbot.addWidget(test_widget)
    test_widget.set_my_property('test_string')
    assert test_widget._test_attr == 'test_string'


def test_cursor_mixin(qtbot):
    @mixin.cursor_mixin
    class MTestClass(QPushButton):
        def __init__(self, parent=None):
            super(MTestClass, self).__init__(parent)
            geo = QApplication.desktop().screenGeometry()
            self.setGeometry(geo.width() / 4, geo.height() / 4, geo.width() / 2, geo.height() / 2)

    main_widget = QWidget()
    button_test = MTestClass()
    button_normal = QPushButton()
    test_lay = QVBoxLayout()
    test_lay.addWidget(button_test)
    test_lay.addWidget(button_normal)
    main_widget.setLayout(test_lay)

    qtbot.addWidget(main_widget)
    main_widget.show()
    button_test.setEnabled(False)
    assert QApplication.overrideCursor() is None  # Not override cursor

    qtbot.mouseMove(button_test)  # mouse enter

    def check_cursor():
        assert QApplication.overrideCursor().shape() == Qt.ForbiddenCursor

    qtbot.waitUntil(check_cursor)

    qtbot.mouseMove(button_normal)  # mouse leave

    def check_cursor():
        assert QApplication.overrideCursor() is None  # Restore override cursor

    qtbot.waitUntil(check_cursor)

    button_test.setEnabled(True)
    qtbot.mouseMove(button_test)  # mouse enter

    def check_cursor():
        assert QApplication.overrideCursor().shape() == Qt.PointingHandCursor

    qtbot.waitUntil(check_cursor)

    qtbot.mouseMove(button_normal)  # mouse leave

    def check_cursor():
        assert QApplication.overrideCursor() is None  # Restore override cursor

    qtbot.waitUntil(check_cursor)


def test_focus_shadow_mixin(qtbot):
    @mixin.focus_shadow_mixin
    class MTestClass(QPushButton):
        def __init__(self, parent=None):
            super(MTestClass, self).__init__(parent)
            geo = QApplication.desktop().screenGeometry()
            self.setGeometry(geo.width() / 4, geo.height() / 4, geo.width() / 2, geo.height() / 2)

    main_widget = QWidget()
    button_test = MTestClass()

    button_normal = QPushButton()
    test_lay = QVBoxLayout()
    test_lay.addWidget(button_test)
    test_lay.addWidget(button_normal)
    main_widget.setLayout(test_lay)

    qtbot.addWidget(main_widget)

    assert button_test.graphicsEffect() is None

    main_widget.show()
    # focus in

    graphics_effect = button_test.graphicsEffect()
    assert graphics_effect is not None
    assert graphics_effect.isEnabled()
    assert isinstance(graphics_effect, QGraphicsDropShadowEffect)

    qtbot.mouseClick(button_normal, Qt.LeftButton)  # focus out

    def check_effect():
        assert button_test.graphicsEffect() is not None
        assert not button_test.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_effect)

    qtbot.mouseClick(button_test, Qt.LeftButton)  # focus in

    def check_effect():
        assert button_test.graphicsEffect() is not None
        assert button_test.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_effect)


def test_hover_shadow_mixin(qtbot):
    @mixin.hover_shadow_mixin
    class MTestClass(QPushButton):
        def __init__(self, parent=None):
            super(MTestClass, self).__init__(parent)
            geo = QApplication.desktop().screenGeometry()
            self.setGeometry(geo.width() / 4, geo.height() / 4, geo.width() / 2, geo.height() / 2)

    main_widget = QWidget()
    button_test = MTestClass()
    button_normal = QPushButton()
    test_lay = QVBoxLayout()
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
        assert isinstance(graphics_effect, QGraphicsDropShadowEffect)

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


@pytest.mark.parametrize('input_widget, result', (
        (QLabel, False),
        (QWidget, False),
        (QStackedWidget, True),
        (QStackedLayout, False),
        (QTabWidget, True),
        (QTabBar, False),
))
def test_stackable(input_widget, result):
    assert mixin._stackable(input_widget) == result


def test_stacked_animation_mixin_normal(qtbot):
    @mixin.stacked_animation_mixin
    class MTestClass(QStackedWidget):
        def __init__(self, parent=None):
            super(MTestClass, self).__init__(parent)

    main_widget = MTestClass()
    qtbot.addWidget(main_widget)
    assert hasattr(main_widget, '_to_show_pos_ani')
    assert isinstance(main_widget._to_show_pos_ani, QPropertyAnimation)
    assert hasattr(main_widget, '_to_hide_pos_ani')
    assert isinstance(main_widget._to_hide_pos_ani, QPropertyAnimation)
    assert hasattr(main_widget, '_opacity_eff')
    assert isinstance(main_widget._opacity_eff, QGraphicsOpacityEffect)
    assert hasattr(main_widget, '_opacity_ani')
    assert isinstance(main_widget._opacity_ani, QPropertyAnimation)
    assert hasattr(main_widget, '_play_anim')
    assert hasattr(main_widget, '_disable_opacity')

    assert main_widget._previous_index == 0
    label_1 = QLabel('test')
    index_1 = main_widget.addWidget(label_1)

    def check_index():
        assert main_widget._previous_index == index_1
        assert not label_1.graphicsEffect().isEnabled()

    qtbot.waitUntil(check_index)

    label_2 = QLabel('test2')
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
    class MTestClass(QPushButton):
        def __init__(self, parent=None):
            super(MTestClass, self).__init__(parent)

    main_widget = MTestClass()
    qtbot.addWidget(main_widget)
    assert not hasattr(main_widget, '_to_show_pos_ani')
    assert not hasattr(main_widget, '_to_hide_pos_ani')
    assert not hasattr(main_widget, '_opacity_eff')
    assert not hasattr(main_widget, '_opacity_ani')
    assert not hasattr(main_widget, '_play_anim')
    assert not hasattr(main_widget, '_disable_opacity')
