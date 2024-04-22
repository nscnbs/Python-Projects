import matplotlib.pyplot as plt
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

# Znajdź minimalne drzewo rozpinające
mst = nx.minimum_spanning_tree(G)

# Oblicz wagę minimalnego drzewa rozpinającego
waga_mst = sum([edge[2]['weight'] for edge in mst.edges(data=True)])

# Sprawdź, czy minimalne drzewo rozpinające jest drzewem
if nx.is_tree(mst):
    # Wyświetl wagę minimalnego drzewa rozpinającego
    print("Waga minimalnego drzewa rozpinajacego:", waga_mst)

# Wykonaj przeszukiwanie w głąb (DFS), aby uzyskać trasę TSP z MST
def dfs_tsp(graf, start):
    odwiedzone = set()
    trasa = []
    
    def dfs(wierzcholek):
        odwiedzone.add(wierzcholek)
        trasa.append(wierzcholek)
        for sasiad in graf.neighbors(wierzcholek):
            if sasiad not in odwiedzone:
                dfs(sasiad)
    
    dfs(start)
    trasa.append(start)
    
    return trasa

# Ustaw punkt początkowy dla TSP
start = 1    

# Znajdź trasę TSP na MST
trasa_tsp = dfs_tsp(mst, start)

# Oblicz wagę trasy TSP
waga_tsp = sum([G[trasa_tsp[i]][trasa_tsp[i + 1]]['weight'] for i in range(len(trasa_tsp) - 1)])

print("Waga TSP na MST:", waga_tsp)


fig = plt.figure()

# Narysuj minimalne drzewo rozpinające
pozycje = nx.get_node_attributes(G, "coordinates")
nx.draw(mst, pozycje, with_labels=True, node_color='orange', font_size=8, edge_color='green', width=2)

# Narysuj trasę TSP
krawedzie_tsp = [(trasa_tsp[i], trasa_tsp[i + 1]) for i in range(len(trasa_tsp) - 1)]
kolor_tsp = 'green'
nx.draw_networkx_edges(G, pozycje, edgelist=krawedzie_tsp, edge_color=kolor_tsp, width=2)

plt.show()
