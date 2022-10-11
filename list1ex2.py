# Escreva uma função que recebe um número n como parâmetro e imprime se n é positivo ou negativo.

def verificarPositivo(n):
    if n > 0:
         print(f"{n} é positivo")
    elif n < 0:
         print(f"{n} é negativo")
    else:
         print(f"Zero")

num = float(input("Digite um número qualquer: "))

verificarPositivo(num)