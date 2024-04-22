# library_rec.py

class DiofanticResult:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


def diofantic(a, b, c):
    result = DiofanticResult(0, 0)

    if a == 0 and b == 0:
        result.x = -1
        result.y = -1
        return result

    if a == 0:
        if c % b == 0:
            result.x = 0
            result.y = c // b
        else:
            result.x = -1
            result.y = -1
        return result

    if b == 0:
        if c % a == 0:
            result.x = c // a
            result.y = 0
        else:
            result.x = -1
            result.y = -1
        return result

    gcd = nwd(a, b)
    if c % gcd != 0:
        result.x = -1
        result.y = -1
        return result

    tempResult = diofantic(b, a % b, c)
    if tempResult.x == -1 and tempResult.y == -1:
        result.x = -1
        result.y = -1
        return result

    result.x = tempResult.y
    result.y = tempResult.x - (a // b) * tempResult.y

    return result
