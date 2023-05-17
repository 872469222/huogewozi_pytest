import pytest
#aa

@pytest.mark.skip
def test_aaa():
    print("代码未开发完")
    assert True


@pytest.mark.skip(reason="代码没有实现")
def test_bbb():
    assert False


# 代码中添加 跳过代码块，pytest.skip(reason="")
def check_login():
    return False


def test_function():
    print("start")
    # 如果未登录，则跳过后续步骤
    if not check_login():
        pytest.skip("unsupported configuration")
    print("end")
