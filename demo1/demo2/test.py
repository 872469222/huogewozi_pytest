def doubule(a):
    return a * 2
# w wwwww 我要把你提交上去333312312312312

def test_doubule_int():
    assert 2 == doubule(1)


def test_doubule1_minus():
    assert -20  == doubule(-1)

def test_doubule_float():
    assert 0.2 == doubule(0.1)


def test_doubule2_minus():
    assert -0.2 == doubule(-0.1)


def test_double_0():
    assert 0 == doubule(0)


def test_double_bignum():
    assert 20 == doubule(100)


def test_double_str():
    assert 'aa' == doubule('a')


def test_double_str1():
    assert 'a$a$' == doubule('a$')