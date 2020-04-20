from selenium import webdriver
import pytest
# open_url yield 之前代码 – 用例代码 – open_url yield 之后代码 --》 refresh_page yield 之后代码+》driver.qiut
@pytest.fixture(scope='class')
def open_url():
    driver=webdriver.Chrome()
    driver.get('http://omp.888ly.cn')
    yield driver
    driver.quit()
@pytest.fixture(scope='class')
def refresh_page(open_url):
    yield
    print('start to refresh')
    open_url.refresh()
@pytest.mark.usefixtures('open_url')
@pytest.mark.usefixtures('refresh_page')
class TestLogin(object):
    def test_login(self):
        print('开始了')
        assert 1==1
        print('结束了')
if __name__ == "__main__":
    pytest.main(['-s','-k','test_fixture'])

