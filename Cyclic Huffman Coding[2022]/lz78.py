def LZ78_encode(data):
    D = {}
    n = 1
    c = ''
    result = []

    for s in data:
        if c + s not in D:
            if c == '':
                # specjalny przypadek: symbol 's'
                # nie występuje jeszcze w słowniku
                result.append((0, int(s)))
                D[s] = n
            else:
                # ciąg 'c' jest w słowniku
                result.append((D[c], int(s)))
                D[c + s] = n
            n += 1
            c = ''
        else:
            c += s

    return result

if __name__ == '__main__':
    import sys
    from math import log, ceil

    if len(sys.argv) < 2:
        print("Podaj liczbę do zakodowania")
        sys.exit(1)

    data = sys.argv[1]
    comp = LZ78_encode(data)

    print("Kodowanie etap po etapie:")
    for i, (index, symbol) in enumerate(comp, start=1):
        print(f"Krok {i}: Dodaj do słownika wpis ({index}, {symbol})")

    print("\nWynik:")
    print(comp)
