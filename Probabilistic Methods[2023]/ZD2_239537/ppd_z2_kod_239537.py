import random

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
        try:
            with open("results.txt", "w") as n_file:
                n_file.write("")
        except IOError as e:
            print(f"Error: {e}")

        m = 1000
        for self.n in range(1000, 100001, 1000):
            for k in range(1, 51):
                self.flag_Bn = False
                self.urny = [0] * self.n
                self.count_fill = self.n
                self.count_empty = self.n
                self.Cn = 0
                self.Dn = 0
                self.test = 0

                while self.count_fill > 0:
                    self.test += 1
                    self.p = self.secure_random.randint(0, self.n - 1)
                    self.urny[self.p] += 1

                    if self.urny[self.p] > 1 and not self.flag_Bn:
                        self.Bn = self.test
                        print(f"Bn: {self.test}")
                        self.flag_Bn = True

                    if self.test <= self.n:
                        if self.test == self.n:
                            self.Un = self.count_empty_urns(self.urny, self.n)
                            print(f"Un dla {self.n}: {self.Un}")

                    if self.urny[self.p] == 1:
                        self.count_empty -= 1
                        if self.count_empty == 0:
                            self.Cn = self.test

                    if self.urny[self.p] == 2:
                        self.count_fill -= 1
                        if self.count_fill == 0:
                            self.Dn = self.test

                self.DnCn = self.Dn - self.Cn
                print(f"Cn: {self.Cn}")
                print(f"Dn: {self.Dn}")
                print(f"Dn - Cn: {self.DnCn}\n")
                print("-----------------------------------\n")

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


def main():
    symulator = Symulacja()
    symulator.dodanie_kul()


if __name__ == '__main__':
    main()
