from random import SystemRandom

file_path = "random_SystemRandom.txt"

random_generator = SystemRandom()

with open(file_path, 'w') as file:
    for i in range(1000000):
        a = random_generator.randint(0, 1)
        file.write(str(a))

print("Zapisano do pliku:", file_path)
