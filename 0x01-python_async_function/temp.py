def test(a=1):
    yield a
    yield a*2
    yield a*3
    yield 0
    yield a*4
    return "yes"
