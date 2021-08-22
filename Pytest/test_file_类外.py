import pytest

def fun(x):
    return x + 1

def test_A():
    print("test_A")
    assert fun(2) == 3
    # 断言失败

def test_B():
    print("test_B")
    assert fun(2) == 3  # 断言成功

def setup():
    print("打印在（函数）执行之前")

def teardown():
    print("打印在（函数）执行之后")

if __name__ == "__name__":
    pytest.main(["-s", "test_file类外.py"])