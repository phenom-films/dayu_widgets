# Import third-party modules
from qtpy import QtWidgets

# Import local modules
from dayu_widgets3.carousel import MCarousel
from dayu_widgets3.label import MLabel
from dayu_widgets3.qt import MPixmap
from dayu_widgets3.slider import MSlider
from dayu_widgets3.switch import MSwitch


class CarouselExample(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CarouselExample, self).__init__(parent)
        self.setWindowTitle("Examples for MCarousel")
        self._init_ui()

    def _init_ui(self):
        switch = MSwitch()
        switch.setChecked(True)
        slider = MSlider()
        slider.setRange(1, 10)
        switch_lay = QtWidgets.QFormLayout()
        switch_lay.addRow(MLabel("AutoPlay"), switch)
        switch_lay.addRow(MLabel("Interval"), slider)
        test = MCarousel(
            [MPixmap("app-{}.png".format(a)) for a in ["maya", "nuke", "houdini"]],
            width=300,
            height=300,
            autoplay=True,
        )
        switch.toggled.connect(test.set_autoplay)
        slider.valueChanged.connect(lambda x: test.set_interval(x * 1000))
        slider.setValue(3)

        main_lay = QtWidgets.QVBoxLayout()
        main_lay.addWidget(test)
        main_lay.addLayout(switch_lay)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import local modules
    from dayu_widgets3 import dayu_theme
    from dayu_widgets3.qt import application

    with application() as app:
        test = CarouselExample()
        dayu_theme.apply(test)
        test.show()
