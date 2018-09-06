## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
from math import *
def main():
    print("questao 2")

TC = int(input("Qual a temperatura local?(Em Celsios)"))

TF = int(((TC/5) * 9)+32)

print("Temperatura em Celsius: " + str(TC))
print("Temperatura em Fahrenheit: " + str(TF))

if __name__ == '__main__':
    main()
