"""
Test class MBadge.
"""
# Import third-party modules
import pytest

# Import local modules
from dayu_widgets.badge import MBadge
from dayu_widgets.qt import QLabel
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget


@pytest.mark.parametrize(
    "show, visible",
    (
        (True, True),
        (False, False),
    ),
)
def test_badge_dot(qtbot, show, visible):
    """Test MBadge init."""
    label = QLabel("test")
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
    assert badge_1.get_dayu_dot() == show
    assert badge_2.get_dayu_dot() == show
    assert badge_1.get_dayu_text() is None
    assert badge_2.get_dayu_text() is None
    assert badge_1.get_dayu_count() is None
    assert badge_2.get_dayu_count() is None


@pytest.mark.parametrize(
    "num, text, visible",
    (
        (1, "1", True),
        (100, "99+", True),
        (0, "0", False),
        (-1, "-1", False),
    ),
)
def test_badge_count(qtbot, num, text, visible):
    """Test MBadge init."""
    label = QLabel("test")
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
    assert badge_1.get_dayu_dot() is False
    assert badge_2.get_dayu_dot() is False
    assert badge_1.get_dayu_text() is None
    assert badge_2.get_dayu_text() is None
    assert badge_1.get_dayu_count() == num
    assert badge_2.get_dayu_count() == num
    assert badge_1.get_dayu_overflow() == 99
    assert badge_2.get_dayu_overflow() == 99


@pytest.mark.parametrize(
    "num, text, overflow",
    (
        (99, "99", 99),
        (100, "99+", 99),
        (20, "10+", 10),
        (9, "9", 10),
    ),
)
def test_badge_overflow(qtbot, num, text, overflow):
    """Test MBadge init."""
    badge = MBadge.count(num)
    badge.set_dayu_overflow(overflow)
    main_widget = QWidget()
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)
    main_lay.addWidget(badge)
    qtbot.addWidget(main_widget)
    main_widget.show()

    assert badge._badge_button.text() == text
    assert badge.get_dayu_dot() is False
    assert badge.get_dayu_text() is None
    assert badge.get_dayu_count() == num
    assert badge.get_dayu_overflow() == overflow


@pytest.mark.parametrize(
    "content,text,visible",
    (
        ("hot", "hot", True),
        ("", "", False),
    ),
)
def test_badge_text(qtbot, content, text, visible):
    """Test MBadge init."""
    label = QLabel("test")
    badge_1 = MBadge.text(text=content, widget=label)
    badge_2 = MBadge.text(text=content)
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
    assert badge_1.get_dayu_dot() is False
    assert badge_2.get_dayu_dot() is False
    assert badge_1.get_dayu_text() == text
    assert badge_2.get_dayu_text() == text
    assert badge_1.get_dayu_count() is None
    assert badge_2.get_dayu_count() is None
