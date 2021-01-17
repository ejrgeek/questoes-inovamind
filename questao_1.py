def validador(sequencia: list) -> bool:

    abertura = ["[", "{", "("]
    fechamento = ["]", "}", ")"]

    pilha = []

    if len(sequencia) % 2 != 0 and len(sequencia) == 0:
        return False

    for i in sequencia:
        if i in abertura:
            pilha.append(i)
        elif i in fechamento:
            pos = fechamento.index(i)
            if len(pilha) > 0 and abertura[pos] == pilha[len(pilha)-1]:
                pilha.pop()
            else:
                return False
    if len(pilha) == 0:
        return True


mock_valido = [
    '[', '{', '(', ')', '}', ']'
]

mock_invalido = [
    '{', '[', '(', '(', ')', ']', '}'
]

resultado = validador(mock_invalido)
print(resultado)