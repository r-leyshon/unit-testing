import pytest

from src.interm.course_funcs_1 import (i_want_string)
####Testing Exceptions####


# The well-trodden route:
def test_str_exception_int():
    with pytest.raises(TypeError, match="That's not a string!"):
        i_want_string(1)


# Alternatively
def test_str_exception_bool():
    with pytest.raises(TypeError) as exc:
        i_want_string(False)
    assert exc.match("That's not a string!")
    