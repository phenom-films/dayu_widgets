"""
Test MAvatar class
"""

# Import third-party modules
import pytest
from qtpy import API
from qtpy import QtGui

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.avatar import MAvatar
from dayu_widgets.qt import MPixmap


def get_qt_binding():
    """Return current Qt binding being used"""
    return API


@pytest.mark.parametrize("image", ("check.svg", None))
@pytest.mark.parametrize(
    "size,result",
    (
        (None, dayu_theme.default_size),
        (dayu_theme.tiny, dayu_theme.tiny),
        (dayu_theme.small, dayu_theme.small),
        (dayu_theme.medium, dayu_theme.medium),
        (dayu_theme.large, dayu_theme.large),
        (dayu_theme.huge, dayu_theme.huge),
    ),
)
def test_mavatar_init(qtbot, size, result, image):
    """Test for MAvatar init with different args"""
    widget = MAvatar()
    if image:
        widget.set_dayu_image(MPixmap(image))
    if size:
        widget.set_dayu_size(size)

    qtbot.addWidget(widget)

    assert widget.height() == result
    assert widget.width() == result
    assert widget.get_dayu_size() == result
    pix = widget.pixmap()
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == result
    assert pix.width() == result

    orig = MPixmap("sphere.svg")
    widget.set_dayu_image(orig)
    pix = widget.pixmap()
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == result
    assert pix.width() == result
    assert orig is widget.get_dayu_image()


@pytest.mark.parametrize("image", ("check.svg", None))
@pytest.mark.parametrize(
    "cls, result",
    (
        (MAvatar.tiny, dayu_theme.tiny),
        (MAvatar.small, dayu_theme.small),
        (MAvatar.medium, dayu_theme.medium),
        (MAvatar.large, dayu_theme.large),
        (MAvatar.huge, dayu_theme.huge),
    ),
)
def test_avatar_class_method(qtbot, cls, result, image):
    """Test for MAvatar class methods"""
    if image:
        widget = cls(MPixmap(image))
    else:
        widget = cls()
    qtbot.addWidget(widget)

    assert widget.height() == result
    assert widget.width() == result
    pix = widget.pixmap()
    assert pix is not None
    assert not pix.isNull()
    assert pix.width() == result
    assert pix.width() == result


@pytest.mark.parametrize(
    "input_file, error_type",
    (
        ("3", str),
        (3, int),
        (set("google"), set),
        ({"name": "test"}, dict),
        (["g"], list),
        ((2,), tuple),
        (object(), object),
    ),
)
def test_mavatar_with_wrong_image(qtbot, input_file, error_type):
    """Make sure when user give a wrong type arg, raise TypeError"""
    with pytest.raises(TypeError) as exc_info:
        widget = MAvatar()
        widget.set_dayu_image(input_file)
        qtbot.addWidget(widget)

    exception_msg = exc_info.value.args[0]
    assert exception_msg == "Input argument 'value' should be QPixmap or None," " but get {}".format(error_type)


def test_mavatar_default_image(qtbot):
    """Test MAvatar default image behavior"""
    widget = MAvatar()
    qtbot.addWidget(widget)

    # Default image should be user_fill.svg
    default_pix = widget.pixmap()
    assert default_pix is not None
    assert not default_pix.isNull()

    # Store the default size before modifying the image
    default_size = default_pix.size()

    # Setting image to None should revert to default
    widget.set_dayu_image(None)
    # Check if the image is not null and has the same size
    assert not widget.pixmap().isNull()
    assert widget.pixmap().size() == default_size


def test_mavatar_null_image(qtbot):
    """Test MAvatar handling of null QPixmap"""
    widget = MAvatar()
    qtbot.addWidget(widget)

    # Create a null QPixmap
    null_pixmap = QtGui.QPixmap()
    assert null_pixmap.isNull()

    # Setting null pixmap should revert to default
    default_size = widget.pixmap().size()
    widget.set_dayu_image(null_pixmap)
    # Check if the image is not null and has the same size
    assert not widget.pixmap().isNull()
    assert widget.pixmap().size() == default_size


def test_mavatar_image_scaling(qtbot):
    """Test MAvatar image scaling behavior"""
    widget = MAvatar()
    qtbot.addWidget(widget)

    # Create a test image with different aspect ratio
    test_pixmap = QtGui.QPixmap(100, 200)  # 1:2 aspect ratio
    test_pixmap.fill(QtGui.QColor("red"))
    widget.set_dayu_image(test_pixmap)

    # Image should be scaled to widget size while maintaining aspect ratio
    scaled_pixmap = widget.pixmap()
    assert scaled_pixmap.width() == widget.width()
    assert not scaled_pixmap.isNull()


def test_mavatar_size_change(qtbot):
    """Test MAvatar behavior when size changes"""
    widget = MAvatar()
    qtbot.addWidget(widget)

    # Create a test image
    test_pixmap = QtGui.QPixmap(100, 100)
    test_pixmap.fill(QtGui.QColor("blue"))
    widget.set_dayu_image(test_pixmap)

    # Test different sizes
    sizes = [dayu_theme.tiny, dayu_theme.small, dayu_theme.medium, dayu_theme.large, dayu_theme.huge]

    for size in sizes:
        widget.set_dayu_size(size)
        # Widget should be square
        assert widget.width() == size
        assert widget.height() == size
        # Image should match widget size
        assert widget.pixmap().width() == size
        assert widget.pixmap().height() == size


def test_mavatar_qt_binding_compatibility(qtbot):
    """Test MAvatar compatibility with current Qt binding"""
    print(f"\nCurrent Qt binding: {get_qt_binding()}")

    widget = MAvatar()
    qtbot.addWidget(widget)

    # Basic functionality tests
    widget.set_dayu_size(dayu_theme.medium)
    assert widget.width() == dayu_theme.medium
    assert widget.height() == dayu_theme.medium

    # Test image setting
    test_pixmap = QtGui.QPixmap(100, 100)
    test_pixmap.fill(QtGui.QColor("blue"))
    widget.set_dayu_image(test_pixmap)
    assert not widget.pixmap().isNull()

    # Test property system
    assert isinstance(widget.property("dayu_size"), int)
    assert isinstance(widget.property("dayu_image"), QtGui.QPixmap)

    # Test signal connections
    widget.show()
    qtbot.wait(100)  # Small delay to ensure widget is shown
    assert widget.isVisible()
