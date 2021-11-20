"""
Test get_obj_value set_obj_value has_obj_value
"""
import pytest
from dayu_widgets import utils


class _HasNameAgeObject(object):
    def __init__(self, name, age):
        super(_HasNameAgeObject, self).__init__()
        self.name = name
        self.age = age


@pytest.mark.parametrize(
    "obj", ({"name": "xiaoming", "age": 18}, _HasNameAgeObject("xiaoming", 18))
)
class TestObjValue(object):
    """Test get_obj_value has_obj_value set_obj_value collection."""

    @pytest.mark.parametrize(
        "attr, default, result",
        (("name", "hhh", "xiaoming"), ("age", 0, 18), ("score", 0, 0)),
    )
    def test_get_obj_value(self, obj, attr, default, result):
        """Test get_obj_value with dict/object as arg."""
        assert utils.get_obj_value(obj, attr, default) == result

    @pytest.mark.parametrize(
        "attr, result",
        (
            ("name", True),
            ("age", True),
            ("sex", False),
        ),
    )
    def test_has_obj_value(self, obj, attr, result):
        """Test has_obj_value with dict/object as arg."""
        assert utils.has_obj_value(obj, attr) == result

    @pytest.mark.parametrize(
        "attr, value",
        (
            ("name", "xiaohua"),
            ("age", 30),
            ("id", 80),
        ),
    )
    def test_set_obj_value(self, obj, attr, value):
        """Test set_obj_value with dict/object as arg."""
        utils.set_obj_value(obj, attr, value)
        assert utils.get_obj_value(obj, attr) == value
