import pytest



def fun(x):
    return x + 1


class TestMethod:
    def test_A(self):
        print("test_A 类内")
        assert fun(2) == 3
        # 断言失败

    def test_B(self):
        print("test_B 类内")
        assert fun(2) == 3  # 断言成功

    def setup(self):
        print("打印在（函数）执行之前 setup 类内")

    def teardown(self):
        print("打印在（函数）执行之后 teardow 类内")

    def setup_class(self):
        print("打印在（类）执行之前 setup_class 类内")

    def teardown_class(self):
        print("打印在（类）执行之后  setdown_class 类内")

if __name__ == "__name__":
    pytest.main(["-s", "test_file类内.py"])