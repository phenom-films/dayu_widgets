"""
Test class MBadge.
"""
import pytest

from dayu_widgets.badge import MBadge
from dayu_widgets.qt import QLabel, QWidget, QVBoxLayout


@pytest.mark.parametrize('show, visible', (
    (True, True),
    (False, False),
))
def test_badge_dot(qtbot, show, visible):
    """Test MAlert init."""
    label = QLabel('test')
    badge_1 = MBadge.dot(show=show, widget=label)
    badge_2 = MBadge.dot(show)
    main_widget = QWidget()
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)
    main_lay.addWidget(badge_1)
    main_lay.addWidget(badge_2)
    qtbot.addWidget(main_widget)
    main_widget.show()

    assert badge_1._badge_button.isVisible() == visible
    assert badge_2._badge_button.isVisible() == visible

@pytest.mark.parametrize('num, text, visible', (
    (1, '1', True),
    (100, '99+', True),
    (0, '0', False),
    (-1, '-1', False),
))
def test_badge_count(qtbot, num, text, visible):
    """Test MAlert init."""
    label = QLabel('test')
    badge_1 = MBadge.count(count=num, widget=label)
    badge_2 = MBadge.count(num)
    main_widget = QWidget()
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)
    main_lay.addWidget(badge_1)
    main_lay.addWidget(badge_2)
    qtbot.addWidget(main_widget)
    main_widget.show()

    assert badge_1._badge_button.text() == text
    assert badge_1._badge_button.isVisible() == visible
    assert badge_2._badge_button.text() == text
    assert badge_2._badge_button.isVisible() == visible

@pytest.mark.parametrize('content,text,visible', (
    ('hot', 'hot', True),
    ('', '', False),
))
def test_badge_text(qtbot, content, text, visible):
    """Test MAlert init."""
    label = QLabel('test')
    widget_1 = MBadge.text(text=content, widget=label)
    widget_2 = MBadge.text(text=content)
    main_widget = QWidget()
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)
    main_lay.addWidget(widget_1)
    main_lay.addWidget(widget_2)
    qtbot.addWidget(main_widget)
    main_widget.show()

    assert widget_1._badge_button.text() == text
    assert widget_1._badge_button.isVisible() == visible
    assert widget_2._badge_button.text() == text
    assert widget_2._badge_button.isVisible() == visible
