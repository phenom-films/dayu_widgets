# Import local modules
from dayu_widgets.progress_bar import MProgressBar


def test_progress_bar_init(qtbot):
    bar = MProgressBar()
    bar.setRange(0, 10)
    bar.setValue(5)
    assert bar.text() == "50%"
