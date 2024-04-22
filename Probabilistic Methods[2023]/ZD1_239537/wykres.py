import numpy as np
import matplotlib.pyplot as plt
import random
import math

x = 0.0
y = 0.0
count = 0

# Funkcje sprawdzające warunek dla każdej funkcji
def check_function_1(x, y):
    return y <= x**(1/3)

def check_function_2(x, y):
    return y <= math.sin(x)

def check_function_3(x, y):
    return y <= 4 * x * (1 - x)**3

def check_function_4(x, y):
    return (x - 1)**2 + (y - 1)**2 <= 1

# Funkcja generująca wyniki
def generate_results(a, b, M, function):
    global count
    results = []
    count = 0
    for n in range(50, 5001, 50):
        for k in range(50):
            for i in range(n):
                x = random.uniform(a, b)
                y = random.uniform(0, M)
                if function(x, y):
                    count += 1
            result = count * (b - a) * M / float(n)
            results.append(result)
    return results

# Wybór funkcji przez użytkownika
print("Wybierz funkcję do wygenerowania wykresu:")
print("1. f(x) = x^(1/3)")
print("2. f(x) = sin(x)")
print("3. f(x) = 4 * x * (1 - x)^3")
print("4. Obszar ograniczony przez okrąg o promieniu 1 wokół punktu (1, 1)")

choice = int(input("Wybór (wpisz liczbę od 1 do 4): "))

if choice == 1:
    function = check_function_1
elif choice == 2:
    function = check_function_2
elif choice == 3:
    function = check_function_3
elif choice == 4:
    function = check_function_4
else:
    print("Nieprawidłowy wybór.")
    exit()

# Generowanie wyników dla wybranej funkcji
results = generate_results(0, 8, 2, function)  # Parametry dla przykładu, można zmienić odpowiednio dla innych funkcji

# Zapisywanie wyników do pliku
with open('data.txt', 'w') as file:
    file.write(';'.join(map(str, results)))

# Wczytywanie danych z pliku
with open('data.txt', 'r') as file:
    line = file.readline()
    data = [float(val) for val in line.strip().split(';') if val]

# Generowanie wykresu dla wybranej funkcji
x = np.arange(50, len(data) * 50 + 1, 50)
plt.plot(x, data, label=f'Funkcja {choice}')

# Dodanie opisów osi i tytułu
plt.xlabel('Iteracje')
plt.ylabel('Wartości')
plt.title(f'Wykres dla wybranej funkcji {choice}')
plt.legend()
plt.show()
