# Escreva uma função que recebe dois números (a e b) como parâmetro 
# e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def somaLimite(n1,n2,limite):
    if n1+n2>limite:
        print(True)
    else:
        print(False)


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
lim = float(input("Digite o limite: "))

somaLimite(num1,num2,lim)