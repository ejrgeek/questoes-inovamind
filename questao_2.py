def popula_dicionario(matriz: list) -> dict:
    anos_dict = {}
    for inicio, fim in matriz:
        anos_dict[inicio] = 0
        anos_dict[fim] = 0

    return anos_dict


def ano_mais_pessoas_trabalhando(matriz: list):

    anos_dict = popula_dicionario(matriz)

    for inicio, fim in matriz:
        anos_dict[inicio] += 1
        anos_dict[fim] += 1

    anos = [ano for ano, quantidade in anos_dict.items() if quantidade == max(anos_dict.values())]

    return anos


mock = [
    [1960, 2005], [1945, 2008], [1938, 2005], [1960, 2005], [1960, 2005]
]


resultado = ano_mais_pessoas_trabalhando(mock)
print(resultado)
