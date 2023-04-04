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
