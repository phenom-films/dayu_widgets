# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets.check_box import MCheckBox


def test_radio_button_init(qtbot):
    radio_1 = MCheckBox("test")
    radio_2 = MCheckBox("")
    qtbot.addWidget(radio_1)
    qtbot.addWidget(radio_2)

    assert radio_1.text() == "test"
    assert radio_2.text() == ""
