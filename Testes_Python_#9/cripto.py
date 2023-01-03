def posicao(caractere):
    return ord(caractere) - ord("A")


def recupera(numero):
    return chr(numero + ord("A"))


def rot13(texto):
    resultado = ""
    for caractere in texto:
        resultado_caractere = recupera((posicao(caractere) + 13) % 26)
        resultado += resultado_caractere
        return resultado