# Escreva uma função que recebe dois números (a e b) como parâmetro 
# e retorna a quantidade (0, 1 ou 2) deles que é maior que um terceiro parâmetro, chamado limite.

def MaiorLimite(n1,n2,limite):
    list=[]
    if n1>limite:
        list.append(1)
    if n2>limite:
        list.append(2)
    print(f"Quantidade de números maiores que o limite: {len(list)}")
    


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
lim = float(input("Digite o limite: "))

MaiorLimite(num1,num2,lim)