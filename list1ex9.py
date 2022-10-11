# Escreva uma função que recebe como entrada uma lista ordenada de números 
# e retorna o índice do primeiro elemento maior que um elemento limite. 
# Se nenhum elemento da lista for maior que o limite desejado, retorne o valor -1


def retornarIndice(lista: list, limite: float):
    lista.sort()
    for posicao , elemento in enumerate(lista):
        if elemento > limite:
            return posicao
    return -1



lista = [2,5,1,3,4,10,7,9,6,8]

n = int(input("Digite um número: "))

print(f"Posição do número: {retornarIndice(lista, n)}")