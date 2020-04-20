from test_fixture_param1 import *
import pytest
excelData = getExcelData()
@pytest.mark.parametrize('omplogin', excelData, indirect=True)
def test_omplogin(omplogin):
    print(omplogin[0])
    print(omplogin[1])
    print(omplogin[2])
    assert omplogin[2] == 'luketest'

if __name__ == "__main__":
    pytest.main(['-s','oPytestStudy/test_fixtureLearn/test_fixture_param2.py'])
