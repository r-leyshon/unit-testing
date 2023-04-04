import pytest

from src.interm.course_funcs_1 import (i_want_string, num_to_pH)
####Testing Exceptions####

class TestIWantString(object):
    # The well-trodden route:
    def test_str_exception_int(self):
        with pytest.raises(TypeError, match="That's not a string!"):
            i_want_string(1)


    # Alternatively
    def test_str_exception_bool(self):
        with pytest.raises(TypeError) as exc:
            i_want_string(False)
        assert exc.match("That's not a string!")


class TestNumToPH(object):
    # Test normal values, 2 - 3
    def test_normal_return_args(self):
        assert num_to_pH(1) == "acid"
        assert num_to_pH(14) == "alkali"


    def test_special_args(self):
        assert num_to_pH(7.0) == "neutral"


    def test_boundary_args(self):
        assert num_to_pH(-1) is None
        assert num_to_pH(14.1) is None
    