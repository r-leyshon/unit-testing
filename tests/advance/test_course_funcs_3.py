from unittest.mock import call

import pytest

from src.advance.course_funcs_3 import (goodie, cap_abc, fruity_bars)


class TestGoodie(object):
    @pytest.fixture
    def super_file(self, tmpdir):
        # setup
        contents = """name,polarity,\nspiderman,good,\nvenom,bad"""
        # append the filepth with the tempdir ref
        pth = tmpdir.join("superheroes.csv")
        with open(pth, "w") as f:
            f.write(contents)
            f.close()
        # pytest no longer supports use of yield as shown in course
        yield pth
        # tmpdir will handle the teardown phase, removing the csv from disk
    

    def test_goodie(self, super_file):
        expected = ['spiderman']
        found = goodie(super_file)
        assert found == expected


class TestCapAbc(object):
    # uses the pytest mocker fixture
    def test_cap_abc(self, mocker):
        # don't forget to give the full relative pth to the dep being mocked
        cap_a_mock = mocker.patch(
            "src.advance.course_funcs_3.cap_a",
            return_value="Abc, it's eAsy As one, two, three."
            )
        # now use the code that would call the mock target
        result = cap_abc()
        # now go on to test as usual
        assert result == "ABC, it's eAsy As one, two, three.",\
        f"Expected A,B & C to be capitalised.\nInstead got {result}"


class TestFruityBars(object):
    @pytest.mark.mpl_image_compare # This will handle the image baseline and comparison
    def test_fruity_bars(self):
        return fruity_bars()
