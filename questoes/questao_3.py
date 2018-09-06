## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from math import *

def main():
    print("questao 3")
r = float(input("Qual o raio do Círculo? "))

diam = float(2*r)
area = float(pi * (r**2))
circ = float(2*pi*r)

print("Com um raido de " + str(r) + " Temos:")
print("Diâmetro " + str(diam))
print("Área " + str(area))
print("Comprimento: " + str(circ))

if __name__ == '__main__':
 main()
