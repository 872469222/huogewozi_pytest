import pytest

# 1.40
def test_xfail():
    print("*****开始测试*****")
    pytest.xfail(reason="该功能尚未完成")
    print("测试过程")
    assert 1 == 1


@pytest.mark.xfail
def test_aaa():
    print("test_xfill 方法执行")
    assert 2 == 2


xfail = pytest.mark.xfail


@xfail(reason="bug 110")
def test_hello4():
    assert 0
