## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from math import *

def main():
    print("questao 4")

x = float(input("Quantos quilômetros foram rodados com o carro? "))
y = float(input("Quantos dias o Carro foi utilizado? "))

km = float(0.15 * x)
dia = float(60 * y)
total = float(km + dia)

print("Total a pagar:" + str(total) + " reais")


if __name__ == '__main__':
   main()
