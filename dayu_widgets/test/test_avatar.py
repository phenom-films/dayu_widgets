# Import third-party modules
from examples.avatar_example import AvatarExample
import pytest

# Import local modules
from dayu_widgets import dayu_theme
from dayu_widgets.avatar import MAvatar
from dayu_widgets.qt import MPixmap


class TestAlertExample(object):
    @pytest.fixture(autouse=True)
    def set_up(self, qtbot):
        """Set up to test the view."""
        # We need to initialize this here because pytest won't let us use an
        # __init__ constructor. If we did, the tests won't run.
        self.view = (
            AvatarExample()
        )  # noqa: E501 pylint: disable=attribute-defined-outside-init, line-too-long
        qtbot.addWidget(self.view)
        dayu_theme.apply(self.view)
        self.avatar = self.view.avatar

    def test_set_image_field(self):
        image = self.view.pix_map_list[1]
        self.view.set_field("image", image)
        assert self.view.field("image") == image

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
    def test_mavatar_init(self, qtbot, size, result, image):
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
    def test_avatar_class_method(self, qtbot, cls, result, image):
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
    def test_mavatar_with_wrong_image(self, qtbot, input_file, error_type):
        """Make sure when user give a wrong type arg, raise TypeError"""
        with pytest.raises(TypeError) as exc_info:
            widget = MAvatar()
            widget.set_dayu_image(input_file)
            qtbot.addWidget(widget)

        exception_msg = exc_info.value.args[0]
        assert (
            exception_msg == "Input argument 'value' should be QPixmap or None,"
            " but get {}".format(error_type)
        )
