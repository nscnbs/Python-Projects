import numpy as np
from scipy.stats import binom
from sympy import nsimplify

def nierownosc_markowa(n, p, prog, gorna_granica):
    srednia = n * p
    prawdopodobienstwo = 1 - prog / srednia if gorna_granica else prog / srednia
    return max(0, min(1, prawdopodobienstwo))

def nierownosc_czebyszewa(n, p, prog, gorna_granica):
    wariancja = n * p * (1 - p)
    odchylenie_standardowe = np.sqrt(wariancja)

    granica = odchylenie_standardowe / prog
    prawdopodobienstwo = 1 - 1 / (granica**2) if gorna_granica else 1 / (1 + granica**2)
    return max(0, min(1, prawdopodobienstwo))

wartosci_n = [100, 1000, 10000]

for n in wartosci_n:
    print(f"n = {n}")
    p = 0.5

    rozklad_dwumianowy = binom(n, p)

    prog_a = 6.0 / 5.0
    dokladne_prawdopodobienstwo_a = nsimplify(1 - rozklad_dwumianowy.cdf(n * p * prog_a - 1)).evalf()
    markov_gorna_granica_a = nierownosc_markowa(n, p, prog_a, True)
    markov_dolna_granica_a = nierownosc_markowa(n, p, prog_a, False)
    czebyszew_gorna_granica_a = nierownosc_czebyszewa(n, p, prog_a, True)
    czebyszew_dolna_granica_a = nierownosc_czebyszewa(n, p, prog_a, False)
    
    print("a) P(X >= 1.2 * E(X)):")
    print(f"   Dokladne Prawdopodobienstwo: {dokladne_prawdopodobienstwo_a}")
    print(f"   Nierownosc Markowa Gorna Granica: {markov_gorna_granica_a}")
    print(f"   Nierownosc Markowa Dolna Granica: {markov_dolna_granica_a}")
    print(f"   Nierownosc Czebyszewa Gorna Granica: {czebyszew_gorna_granica_a}")
    print(f"   Nierownosc Czebyszewa Dolna Granica: {czebyszew_dolna_granica_a}")

    prog_b = 1.0 / 10.0
    dokladne_prawdopodobienstwo_b = nsimplify(1 - rozklad_dwumianowy.cdf(n * p * prog_b - 1)).evalf()
    markov_gorna_granica_b = nierownosc_markowa(n, p, prog_b, True)
    markov_dolna_granica_b = nierownosc_markowa(n, p, prog_b, False)
    czebyszew_gorna_granica_b = nierownosc_czebyszewa(n, p, prog_b, True)
    czebyszew_dolna_granica_b = nierownosc_czebyszewa(n, p, prog_b, False)
    
    print("b) P(|X - E(X)| >= 0.1 * E(X)):")
    print(f"   Dokladne Prawdopodobienstwo: {dokladne_prawdopodobienstwo_b}")
    print(f"   Nierownosc Markowa Gorna Granica: {markov_gorna_granica_b}")
    print(f"   Nierownosc Markowa Dolna Granica: {markov_dolna_granica_b}")
    print(f"   Nierownosc Czebyszewa Gorna Granica: {czebyszew_gorna_granica_b}")
    print(f"   Nierownosc Czebyszewa Dolna Granica: {czebyszew_dolna_granica_b}")

    print()
