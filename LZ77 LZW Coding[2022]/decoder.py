import sys


def elias_omega(code):
    codes = []
    i = 0
    n = 1
    while i < len(code):
        if code[i] == "0":
            codes.append(n)
            n = 1
            i += 1
        elif code[i] == "1":
            s = code[i : i + n + 1]
            i += n + 1
            n = int(s, base=2)
    return codes


def decode(input_file, output_file, func=elias_omega):
    with open(input_file, "rb") as inp, open(output_file, "wb") as output:
        dictionary = []
        for i in range(256):
            dictionary.append(bytes([i]))

        hexstring = inp.read().hex()
        bitstring = "".join(
            [
                "{0:08b}".format(int(hexstring[x : x + 2], base=16))
                for x in range(0, len(hexstring), 2)
            ]
        )

        num = bitstring[:3]
        bitstring = bitstring[3:len(bitstring)-(int(num, base=2))]

        codes = list(map(lambda x : x -1, func(bitstring)))

        idx = 0
        OLD = codes[idx]
        S = dictionary[OLD]
        C = dictionary[OLD][:1]
        result = S
        idx += 1
        while idx < len(codes):
            NEW = codes[idx]
            if NEW >= len(dictionary):
                S = dictionary[OLD]
                S = S + C
            else:
                S = dictionary[NEW]
            result += S
            C = S[:1]
            dictionary.append(dictionary[OLD] + C)
            OLD = NEW
            idx += 1

        # print(result)
        output.write(result)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        decode(sys.argv[1], sys.argv[2])
    else:
        print(
            "decoder input_file output_file"
        )
