# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles são iguais.

def menorNumero(n1, n2):
    if n1<n2:
        print(n1)
    elif n1 == n2:
        print("Os números são iguais")
    else:
        print(n2)


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

menorNumero(num1,num2)