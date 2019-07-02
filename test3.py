import pytest
class TestClass(object):
    def test_01(self):
        x = 'this'
        assert  'h' in x
    def test_02(self):
        x = 5
        assert  x ==6
if __name__=="__main__":
    pytest.main("-q test3.py")