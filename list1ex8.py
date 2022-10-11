# Escreva uma função que recebe como entrada uma lista de números 
# e retorna True se um número passado como parâmetro está presente na lista.

def verificarLista(lista, n):
    
    for i in range(len(lista)):
        if lista[i] == n:
            return True
        else:
            return False
        

lista = [1,2,3,4,5,6,7,8,9,10]

x = int(input("Digite um número: "))

print(f"O número está na lista? : {verificarLista(lista, x)}")
