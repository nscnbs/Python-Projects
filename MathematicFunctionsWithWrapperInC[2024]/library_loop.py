# library_loop.py

class DiofanticResult:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def diofantic(a, b, c):
    result = DiofanticResult(0, 0)
    nwd_ab = nwd(a, b)

    if c % nwd_ab == 0:
        result.x = 0
        result.y = 0

        a //= nwd_ab
        b //= nwd_ab
        c //= nwd_ab

        x0, y0, x1, y1 = 1, 0, 0, 1
        while b != 0:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1

        result.x = x0 * c
        result.y = y0 * c
    else:
        result.x = -1
        result.y = -1

    return result
