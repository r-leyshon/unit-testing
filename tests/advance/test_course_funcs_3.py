import pytest

from src.advance.course_funcs_3 import (goodie)


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
