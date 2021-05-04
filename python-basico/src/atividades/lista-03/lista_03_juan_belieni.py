def conta_frutas(s, t, a, b, macas, laranjas):
    n_macas, n_laranjas = 0, 0

    for maca in macas:
        pos = a + maca
        if s <= pos <= b:
            n_macas += 1

    for laranja in laranjas:
        pos = b + laranja
        if s <= pos <= t:
            n_laranjas += 1

    return n_macas, n_laranjas


# print(conta_frutas(4, 8, 1, 12, [-3, 1, 4], [-2, -5, -6]))


def recordes(recorde, *pontos):
    recorde_max = recorde
    recorde_min = recorde

    n_recordes_max = 0
    n_recordes_min = 0

    for pontuacao in pontos:
        if pontuacao > recorde_max:
            recorde_max = pontuacao
            n_recordes_max += 1
        if pontuacao < recorde_min:
            recorde_min = pontuacao
            n_recordes_min += 1

    return n_recordes_max, n_recordes_min


# print(recordes(10, 12, 24, 11))


def kahoot(*alunos):
    nome_melhor = ""
    media_melhor = 0

    for (nome, media) in alunos:
        if media > media_melhor:
            media_melhor = media
            nome_melhor = nome

    return nome_melhor


# print(kahoot(("Maisa", 90), ("João", 100), ("Welly", 98), ("Igor", 89)))


def dist(*pontos):
    dists = [abs(pontos[i] - pontos[i - 1]) for i in range(1, len(pontos))]
    return min(dists)


# print(dist(-4, 2, 4, 7, 14, 15))


def maximo_elemento(elementos):
    quantidade_aparicoes = {}

    for elemento in elementos:
        if elemento not in quantidade_aparicoes:
            quantidade_aparicoes[elemento] = 1
        else:
            quantidade_aparicoes[elemento] += 1

    maior_qtd_aparicoes = max(quantidade_aparicoes.values())
    elementos_mais_aparicoes = [elemento for elemento in quantidade_aparicoes if
                                quantidade_aparicoes[elemento] == maior_qtd_aparicoes]

    if len(elementos_mais_aparicoes) == 1:
        return elementos_mais_aparicoes[0]

    return min(elementos)


# print(maximo_elemento([1, 7, 7, 4, 2]))

def calcular_distancia(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


# print(calcular_distancia((0, 0), (1, 1)))
