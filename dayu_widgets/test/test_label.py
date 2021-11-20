#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test class MLabel.
"""
# Import third-party modules
import pytest

# Import local modules
from dayu_widgets.label import MLabel
from dayu_widgets.qt import QVBoxLayout
from dayu_widgets.qt import QWidget
from dayu_widgets.qt import Qt


@pytest.mark.parametrize(
    "func,text,attr",
    (("h1", "any", 1), ("h2", "", 2), ("h3", "test", 3), ("h4", "doesn't matter", 4)),
)
def test_label_dayu_level(qtbot, func, text, attr):
    """Test MLabel with different level"""
    label = MLabel(text)
    getattr(label, func)()
    qtbot.addWidget(label)

    assert label.get_dayu_level() == attr
    assert label.text() == text


@pytest.mark.parametrize(
    "func,text,attr",
    (
        (None, "any", ""),
        ("secondary", "Secondary", "secondary"),
        ("warning", "Warning", "warning"),
        ("danger", "Danger", "danger"),
    ),
)
def test_label_dayu_type(qtbot, func, text, attr):
    """Test MLabel with different type"""
    label = MLabel(text)
    if func:
        getattr(label, func)()
    qtbot.addWidget(label)

    assert label.get_dayu_type() == attr
    assert label.text() == text


@pytest.mark.parametrize(
    "text, func, attr",
    (
        ("Mark", "mark", "dayu_mark"),
        ("Code", "code", "dayu_code"),
        ("Underline", "underline", "dayu_underline"),
        ("Delete", "delete", "dayu_delete"),
        ("Strong", "strong", "dayu_strong"),
    ),
)
def test_label_dayu_style(qtbot, func, text, attr):
    """Test MLabel with different style"""
    label = MLabel(text)
    getattr(label, func)()
    qtbot.addWidget(label)

    assert label.property(attr)
    assert label.text() == text


@pytest.mark.parametrize("text, elide", (("test" * 30, True), ("test", False)))
def test_label_elide_mode(qtbot, text, elide):
    """Test MLabel elide mode"""
    main_widget = QWidget()
    main_widget.setGeometry(0, 0, 30, 200)
    main_lay = QVBoxLayout()
    main_widget.setLayout(main_lay)

    label_left = MLabel()
    label_left.set_elide_mode(Qt.ElideLeft)
    label_left.setText(text)
    label_right = MLabel()
    label_right.set_elide_mode(Qt.ElideRight)
    label_right.setText(text)
    label_center = MLabel(text)
    label_center.set_elide_mode(Qt.ElideMiddle)
    label_center.setText(text)

    main_lay.addWidget(label_left)
    main_lay.addWidget(label_right)
    main_lay.addWidget(label_center)

    qtbot.addWidget(main_widget)

    main_widget.show()
    ellipsis = "…"
    if elide:
        assert label_left.property("text").startswith(ellipsis)
        assert label_right.property("text").endswith(ellipsis)
        center_text = label_center.property("text")
        assert center_text.count(ellipsis) and not center_text.endswith(ellipsis)
    else:
        assert label_left.property("text") == label_left.text()
        assert label_right.property("text") == label_right.text()
        assert label_center.property("text") == label_center.text()
    assert label_left.get_elide_mode() == Qt.ElideLeft
    assert label_right.get_elide_mode() == Qt.ElideRight
    assert label_center.get_elide_mode() == Qt.ElideMiddle
