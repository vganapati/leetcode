import functools

@functools.cache
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def test_0():
    assert fib(2) == 1

if __name__ == '__main__':
    test_0()