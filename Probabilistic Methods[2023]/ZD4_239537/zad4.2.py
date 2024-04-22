import random
from datetime import datetime

file_path = "random_Mersenne_Twister.txt"

seed_value = int((datetime.now() - datetime(1970, 1, 1)).total_seconds())
random.seed(seed_value)

with open(file_path, 'w') as file:
    for i in range(1000000):
        a = random.randint(0, 1)
        file.write(str(a))

print("Zapisano do pliku:", file_path)
