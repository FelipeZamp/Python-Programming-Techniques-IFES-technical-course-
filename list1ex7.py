# Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F).

def calcularConceito(nota):
    if nota >= 90:
        conceito = "A"
    elif nota >= 83 :
        conceito = "B"
    elif nota >= 70 :
        conceito = "C"
    elif nota >= 67:
        conceito = "D"
    elif nota >= 60:
        conceito = "E"
    else:
        conceito = "F"
    return conceito



nota = float(input("Digite a nota do aluno: "))

print(f"O conceito da nota é: {calcularConceito}")