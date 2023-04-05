import pytest
import sys

from src.prac.course_funcs_2 import (fizz, buzz)

class TestFizz(object):
    def test_fizz_fizzes(self):
        results = list()
        ints = [3, 30, 300]
        for i in ints:
            results.append(fizz(i))
        assert all([f == "fizz" for f in results])


class TestBuzz(object):
    def test_buzz_buzzes(self):
        results = list()
        ints = [5, 50, 500]
        for i in ints:
            results.append(buzz(i))
        assert all([f == "buzz" for f in results])


####Marking a known fail####
# dont forget to run pytest with the -rx flag to get the reason for the xfail
@pytest.mark.xfail(reason="Not yet implemented")
class TestFizzbuzz(object):
    def test_fizzbuzz_fizzbuzzes(self):
        res = fizzbuzz(15)
        assert res == "fizzbuzz",\
        "Not yet implemented fizzbuzz"


####Marking a skip under conditions - not working####
# a test that uses deprecated print statement
# @pytest.mark.skipif(sys.version_info >= (3, 0), reason="Only works with python 2")
# class TestUsesPython2Print(object):
#     def test_uses_python2_print():
#         print "Old python syntax"
#         pass
