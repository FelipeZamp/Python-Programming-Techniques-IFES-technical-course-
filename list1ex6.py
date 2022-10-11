# Escreva uma função que recebe um número como parâmetro e para cada número menor que o parâmetro, 
# a função imprime "Fizz" se o número for múltiplo de três, imprime "Buzz" se o número for múltiplo de cinco, 
# e imprime "FizzBuzz" se o número for múltiplo de três e cinco. 
# Caso o número não seja múltiplo nem de três nem de cinco, ele deve ser impresso. 
# Note que, ao contrário das funções anteriores, sua função não deve retornar nada. 
# Ela precisa simplesmente imprimir o que foi pedido.

def verificarMultiplo(n):
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else: print(i)


num = int(input("Digite um número qualquer: "))


verificarMultiplo(num)