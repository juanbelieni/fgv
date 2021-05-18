def favoritos(lista: list, set_a: set, set_b: set):
    felicidade = 0
    for i in lista:
        if i in set_a:
            felicidade += 1
        if i in set_b:
            felicidade += -1

    return felicidade


# print(favoritos([1, 2, 3, 4, 5, 6, 7], {1, 3, 5, 7}, {1, 2, 4, 8}))


def GetInfo(a: set, b: set):
    return {
        "intersection": a.intersection(b),  # Set -> Interseção dos dois sets
        "union": a.union(b),  # Set -> União dos dois sets
        "JustA": a.difference(b),  # Set -> Elementos que estão em A e não estão em B
        "symetricDifference": a.symmetric_difference(b),
        # Set -> Diferênça simétrica de A e B, ou seja, elementos que pertencem a um deles, mas não à interseção.
        "a_sub_b": a.issubset(b),  # Booleano -> se A é subconjunto de B
        "LPinA": "LP" in a,  # Booleano -> se a string "LP" está em A
        "NoCommonElements": a.isdisjoint(b)  # Booleano -> Se A e B sãão conjuntos disjuntos
    }


# a = {1, 3, "Teste", "LP"}
# b = {2, 3, "LP"}
# print(GetInfo(a, b))

def int_to_Roman(inteiro: int):
    nums_romanos = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    romano = ''
    i = 0
    while inteiro > 0:
        k = list(nums_romanos.keys())[i]
        v = list(nums_romanos.values())[i]
        for _ in range(inteiro // k):
            romano += v
            inteiro -= k
        i += 1

    return romano


# print(int_to_Roman(1))
# print(int_to_Roman(3000))

def Roman_to_int(romano: str):
    nums_romanos = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    i = 0
    inteiro = 0
    while i < len(romano):
        if i + 1 < len(romano) and romano[i:i + 2] in nums_romanos:
            inteiro += nums_romanos[romano[i:i + 2]]
            i += 2
        else:
            inteiro += nums_romanos[romano[i]]
            i += 1

    return inteiro


# print(Roman_to_int("MMMCMLXXXVI"))
# print(Roman_to_int("C"))

def concatena(*dicts: dict):
    dict_desordenado = {}

    for dict in dicts:
        dict_desordenado.update(dict)

    dict_ordenado = {}

    for v in sorted(dict_desordenado.values()):
        i = list(dict_desordenado.values()).index(v)
        k = list(dict_desordenado.keys())[i]
        del dict_desordenado[k]
        dict_ordenado[k] = v

    return dict_ordenado


# print(concatena(
#     {"peixe": 1, "passaro": 10, "boi": 5, "porco": 8},
#     {"cavalo": 15, "gato": 2, "pinguim": -2}
# ))
# print(concatena({"a": 1, "b": 4, "c": 5}, {"d": 2, "e": 1, "f": 6}))


def concatena2(**dict_desordenado):
    dict_ordenado = {}

    for v in sorted(dict_desordenado.values()):
        i = list(dict_desordenado.values()).index(v)
        k = list(dict_desordenado.keys())[i]
        del dict_desordenado[k]
        dict_ordenado[k] = v

    return dict_ordenado


# print(concatena2(peixe=1, passaro=10, boi=5, porco=8, cavalo=15, gato=2, pinguim=-2))
# print(concatena2(a=1, b=4, c=5, d=2, e=1, f=6))


def partes(conjunto: frozenset):
    from itertools import combinations
    subconjuntos = {frozenset({}), conjunto.copy()}

    for r in range(1, len(conjunto)):
        for subconjunto in combinations(conjunto, r):
            subconjuntos.add(frozenset(subconjunto))

    return frozenset(subconjuntos);


# print(partes(frozenset({1, 2})))
# print(partes(frozenset({2, 4, 6, 8})))


def ler_texto():
    with open('alice.txt', 'r') as livro:
        palavras = livro.read().split()
        frequencia = {}

        for palavra in palavras:
            if palavra not in frequencia:
                frequencia[palavra] = 1
            else:
                frequencia[palavra] += 1

        return frequencia

# print(ler_texto())
