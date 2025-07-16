# Import future modules
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Import third-party modules
from dayu_widgets3.progress_bar import MProgressBar


def test_progress_bar_init(qtbot):
    bar = MProgressBar()
    bar.setRange(0, 10)
    bar.setValue(5)
    assert bar.text() == "50%"
