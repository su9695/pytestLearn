import pytest
class TestClass(object):
     @pytest.mark.xfail  # test_one 会执行失败，但会执行完整的用例
     def test_one(self):
          print('--start test one---')
         # pytest.xfail(reason='功能未完成') # test_one 方法后续的功能不会继续执行
          print("test_one方法执行")
          assert 1==1
     @pytest.mark.luke  #  配合 - m=luke使用，只会执行mark标记的用例
     def test_two(self):
          print('---start test two：方法二开始执行----')
          assert 'o' in 'love'
     def test_three(self):
         print('---start test three: 方法三开始执行----')
if __name__ == "__main__":
   # pytest.main(['-s','-r','pytestStudy/test_sample.py','-m=luke'])
   #  pytest.main(['-s', '-r', 'pytestStudy/test_sample.py', '-m= not luke'])  # 此处是不执行mark标记的内容
   # pytest.main(['-s','pytestStudy/test_sample.py::TestClass::test_three'])  #只执行 test_three 这个方法
    pytest.main(['-s','-k','not test_two and not test_three']) # 不执行 test_two和test_three
