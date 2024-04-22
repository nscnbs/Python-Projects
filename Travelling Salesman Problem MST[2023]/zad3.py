import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import math


dane = open("D:\\Studia\\V sem\\AlgoMeta\\Lista0\\bcl380.txt", "r").readlines()

# Podziel dane na współrzędne
wspolrzedne = {}
for edge in dane:
    x, y = map(int, edge.split()[1:])
    wspolrzedne[int(edge.split()[0])] = (x, y)

# Stwórz graf
G = nx.Graph()

# Dodaj współrzędne jako węzły do grafu
for i, (x, y) in wspolrzedne.items():
    G.add_node(i, coordinates=(x, y))

# Dodaj krawędzie do grafu z zaokrąglonymi wagami określonymi w pliku z danymi
for i in range(1, len(wspolrzedne) + 1):
    for j in range(i + 1, len(wspolrzedne) + 1):
        x1, y1 = wspolrzedne[i]
        x2, y2 = wspolrzedne[j]
        odleglosc = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
        G.add_edge(i, j, weight=odleglosc)

class StatystykiGrafu:
    """
    Klasa do generowania statystyk
    """

    def __init__(self, graf):
        self.graf = graf

    def losowa_dlugosc_cyklu(self):
        """
        Generuje losową długość cyklu w grafie.

        Returns: Długość losowego cyklu.
        """
        random.seed()
        cykl = list(range(1, self.graf.number_of_nodes() + 1))
        random.shuffle(cykl)

        waga = 0
        for i in range(1, self.graf.number_of_nodes()):
            waga += self.graf[cykl[i - 1]][cykl[i]]['weight']
        waga += self.graf[cykl[-1]][cykl[0]]['weight']

        return waga

    def generuj_statystyki(self, liczba_powtorzen):
        """
        Generuje statystyki na podstawie losowych długości cykli w grafie.

        Returns: Statystyki zawierające minimalne wartości
        """
        suma_grupy_10 = 0
        suma_grupy_50 = 0
        min10 = float('inf')
        min50 = float('inf')
        min_global = float('inf')

        statystyki = {'a': [], 'b': [], 'c': []}

        for i in range(1, liczba_powtorzen + 1):
            waga = self.losowa_dlugosc_cyklu()

            if min10 > waga:
                min10 = waga
            if min50 > waga:
                min50 = waga
            if min_global > waga:
                min_global = waga

            if i % 10 == 0:
                suma_grupy_10 += min10
                min10 = float('inf')
                srednia_min_a = suma_grupy_10 / (i // 10)
                statystyki['a'].append(srednia_min_a)

            if i % 50 == 0:
                suma_grupy_50 += min50
                min50 = float('inf')
                srednia_min_b = suma_grupy_50 / (i // 50)
                statystyki['b'].append(srednia_min_b)

        statystyki['c'] = min_global

        return statystyki

def show_stat(statystyki):
    fig, ax = plt.subplots()
    ax.scatter(range(1, len(statystyki['a']) * 10 + 1, 10), statystyki['a'], label='100 grup po 10 losowan')
    ax.scatter(range(50, len(statystyki['b']) * 50 + 1, 50), statystyki['b'], label='20 grup po 50 losowan', marker='x')
    ax.axhline(y=statystyki['c'], color='r', linestyle='--', label='Minimalna wartosc dla tych 1000 losowan')

    ax.set_xlabel('Powtorzenia')
    ax.set_ylabel('Minimalna Dlugosc Trasy')
    ax.legend()
    plt.show()


stat_grafu = StatystykiGrafu(G)
wyniki_stat = stat_grafu.generuj_statystyki(1000)

print(r"Minimalne wartosci:")
print("(a)", wyniki_stat['a'][-1])
print("(b)", min(wyniki_stat['b']))
print("(c)", wyniki_stat['c'])

show_stat(wyniki_stat)
