import random

file_path = "random_standart.txt"

with open(file_path, 'w') as file:
    for i in range(1000000):
        a = random.randint(0, 1)
        file.write(str(a))

print("Zapisano do pliku:", file_path)
