import  pytest

def doubule(a):
    return a * 2


# 测试数据：整型
@pytest.mark.int
def  test_doubule_int():
    print("test double int")
    assert 2 == doubule(1)

# 测试数据：负数
@pytest.mark.minus
def test_doubule1_minus():
    print("test double minus")
    assert -2 == doubule(-1)

# 测试数据：浮点型
@pytest.mark.float
def test_doubule_float():
    assert 0.2 == doubule(0.1)


@pytest.mark.float
def test_doubule2_minus():
    assert -0.2 == doubule(-0.1)

@pytest.mark.zero
def test_doublle_0():
    assert 10 ==doubule(0)
@pytest.mark.bignum
def test_double_bignum():
    assert 200 == doubule(100)

@pytest.mark.str
def test_double_str():
    assert 'aa' == doubule('a')

@pytest.mark.str
def test_double_str1():
    assert 'a$a$' == doubule('a$')
