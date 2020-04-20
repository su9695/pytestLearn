import allure
import pytest
import  os
@allure.feature('test_module_01')
@allure.story('test_story_01')
@allure.severity('normal')
@allure.title('登录的测试用例无效类')
def test_case_001():
    """
    用例描述：test case 001
    """
    assert 0
    allure.attach.file(r'C:\Users\Luke\Desktop\PythonLearn\testpic.jpg',
                       '我是附件截图的名字', attachment_type=allure.attachment_type.JPG)

@allure.story('test_story_02')
@allure.severity('bloker')
@allure.title('登录的测试用例')
def test_case_002():
    """
    用例描述：test case 002
    """
    assert 1
@allure.feature('test_moudle_02')
@allure.severity('critical')
@allure.title('登录测试有效类')
def test_case_003():
    """
    用例描述： test case 003
    """
    assert 0==0
if __name__ == "__main__":
    pytest.main(['-s', '-q', '--alluredir', './oPytestStudy/reports'])
    split = 'allure ' + 'generate ' + './oPytestStudy/reports ' + \
        '-o ' + './oPytestStudy/reports/allure-report/ ' + '--clean'
    os.system('cd C:/Users/Luke/Desktop/PythonLearn/StayAtHome/oPytestStudy')
    os.system(split)
    print(split)

