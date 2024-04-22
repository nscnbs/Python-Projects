import matplotlib.pyplot as plt
import networkx as nx
import math


dane = open("D:\\Studia\\V sem\\AlgoMeta\\Lista0\\xqf131.txt", "r").readlines()

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

# Znajdź minimalne drzewo rozpinające
mst = nx.minimum_spanning_tree(G)

# Oblicz wagę minimalnego drzewa rozpinającego
waga_mst = sum([edge[2]['weight'] for edge in mst.edges(data=True)])

# Sprawdź, czy minimalne drzewo rozpinające jest drzewem
if nx.is_tree(mst):
    # Wyświetl wagę minimalnego drzewa rozpinającego
    print("Waga minimalnego drzewa rozpinajacego:", waga_mst)


fig = plt.figure()

# Narysuj minimalne drzewo rozpinające
pozycje = nx.get_node_attributes(G, "coordinates")
nx.draw(mst, pozycje, with_labels=True, node_color='orange', edge_color='green', width=2, font_size=8)

plt.show()
