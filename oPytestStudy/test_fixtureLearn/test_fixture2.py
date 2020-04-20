import pytest
@pytest.fixture(scope='module',autouse='True')
def start(request):
    print('----------module-------')
    print('moudle: %s'%request.module.__name__)
    print('---------启动浏览器---------')
    yield 
    print('---------关闭浏览器----------')
@pytest.fixture(scope="function",autouse=True)
def open_home(request):
    print("function:%s \n--回到首页--"% request.function.__name__)

def test_case01():
    print('---用例01----')
def test_case01():
    print('----用例02----')
if __name__ == "__main__":
    pytest.main(['-sv','oPytestStudy/test_fixtureLearn/test_fixture2.py'])
