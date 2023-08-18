# Import local modules
from dayu_widgets3.radio_button import MRadioButton


def test_radio_button_init(qtbot):
    radio_1 = MRadioButton("test")
    radio_2 = MRadioButton("")
    qtbot.addWidget(radio_1)
    qtbot.addWidget(radio_2)

    assert radio_1.text() == "test"
    assert radio_2.text() == ""
