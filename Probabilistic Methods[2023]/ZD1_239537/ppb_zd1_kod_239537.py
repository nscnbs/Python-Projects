# Illia Azler 239537


import random
import math

x = 0.0
y = 0.0
count = 0


def check_int():
    while True:
        try:
            c = int(input(""))
            if c <= 0 or c > 4:
                print("Niepoprawna liczba\nPodaj ponownie: ")
                continue
            return c
        except ValueError:
            print("Niewlasciwe dane\nPodaj ponownie: ")


def main():
    global x, y, count
    print("Podaj numer funkcji:")
    f = check_int()
    if f == 1:
        a = 0
        b = 8
        M = 2
        for n in range(50, 5001, 50):
            for k in range(50):
                for i in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, M)
                    if y <= x ** (1 / 3):
                        count += 1
                wynik = count * (b - a) * M / float(n)
                print(f"{wynik};", end="")
                count = 0
            print()
    elif f == 2:
        a = 0
        b = 3.141592653589793
        M = 1
        for n in range(50, 5001, 50):
            for k in range(50):
                for i in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, M)
                    if y <= math.sin(x):
                        count += 1
                wynik = count * (b - a) * M / float(n)
                print(f"{wynik};", end="")
                count = 0
            print()
    elif f == 3:
        a = 0
        b = 1
        M = 8
        for n in range(50, 5001, 50):
            for k in range(50):
                for i in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, M)
                    if y <= 4 * x * (1 - x) ** 3:
                        count += 1
                wynik = count * (b - a) * M / float(n)
                print(f"{wynik};", end="")
                count = 0
            print()
    elif f == 4:
        a = 0
        b = 2
        M = 2
        for n in range(50, 5001, 50):
            for k in range(50):
                for i in range(n):
                    x = random.uniform(a, b)
                    y = random.uniform(0, M)
                    if (x - 1) ** 2 + (y - 1) ** 2 <= 1:
                        count += 1
                wynik = count * (b - a) * M / float(n)
                print(f"{wynik};", end="")
                count = 0
            print()


if __name__ == '__main__':
    main()
