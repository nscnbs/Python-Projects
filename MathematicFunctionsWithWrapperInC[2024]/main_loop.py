# main_loop.py

from library_loop import diofantic, nwd, factorial

if __name__ == "__main__":
    # Factorial
    n = 5
    print(f"{n}! = {factorial(n)}")

    # NWD
    num1, num2 = 36, 48
    print(f"NWD: {num1} i {num2} = {nwd(num1, num2)}")

    # Diofantic
    a, b, c = 120, 144, 72  # x = -3, y = 3
    # a, b, c = 18, 24, 30  # x = -5, y = 5
    # a, b, c = 120, 144, 71  # brak
    result = diofantic(a, b, c)
    if result.x != -1 and result.y != -1:
        print(f"Rozwiazanie rownania {a}x + {b}y = {c} to x = {result.x}, y = {result.y}")
    else:
        print(f"Brak rozwiazania dla rownania {a}x + {b}y = {c}")
