import pytest

def fun(x):
    return x + 1

def test_A():
    print("test_fun1")
    assert fun(2) == 3  # 断言失败

def test_B():
    print("test_fun2")
    assert fun(2) == 3  # 断言失败

if __name__ == "__name__":
    pytest.main(["-s", "test_file.py"])