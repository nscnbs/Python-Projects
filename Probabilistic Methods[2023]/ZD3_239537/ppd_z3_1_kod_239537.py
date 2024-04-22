import random
import matplotlib.pyplot as plt
import numpy as np

class Symulacja:
    def __init__(self):
        self.secure_random = random.SystemRandom()
        self.n = 0
        self.flag_Bn = False
        self.Bn = 0
        self.Un = 0
        self.count_empty = 0
        self.count_fill = 0
        self.Cn = 0
        self.Dn = 0
        self.DnCn = 0
        self.p = 0
        self.test = 0
        self.urny = []

    def dodanie_kul(self):
        Ln1_values = []  # Lista przechowująca wyniki eksperymentu dla d = 1
        Ln2_values = []  # Lista przechowująca wyniki eksperymentu dla d = 2

        m = 1000
        for self.n in range(1000, 100001, 1000):
            print(f"Obliczenia dla n = {self.n}...")
            Ln1 = self.max_load_experiment(1)
            Ln2 = self.max_load_experiment(2)
            Ln1_values.append(np.mean(Ln1))
            Ln2_values.append(np.mean(Ln2))

            try:
                with open("results.txt", "a") as n_file:
                    n_file.write(
                        f"{m}\t{self.Bn}\t{self.Un}\t{self.Cn}\t{self.Dn}\t{self.DnCn}\n"
                    )
            except IOError as e:
                print(f"Error: {e}")

            m = m + 1000


    def count_empty_urns(self, urny, length):
        count = 0
        for p in range(length):
            if urny[p] == 0:
                count += 1
        return count

    def max_load_experiment(self, d):
        loads = []
        for _ in range(50):
            max_load = 0
            urny = [0] * self.n
            for _ in range(self.n):
                if d == 1:
                    p = self.secure_random.randint(0, self.n - 1)
                elif d == 2:
                    chosen = [self.secure_random.randint(0, self.n - 1) for _ in range(2)]
                    p = min(chosen, key=lambda x: urny[x])
                else:
                    raise ValueError("Invalid value of d")

                urny[p] += 1
                max_load = max(max_load, urny[p])

            loads.append(max_load)

        return loads

def main():
    symulator = Symulacja()
    symulator.dodanie_kul()

if __name__ == '__main__':
    main()
