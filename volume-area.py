# Calcula o volume e a área de uma esfera

import math

def main():

    raio = float(input("Qual o raio da esfera? "))

    volume = 4/(3*math.pi*raio**3)
    area = 4*math.pi*raio**2

    print("O volume dessa esfera é de: ", volume, "L")
    print("A área dessa esfera é de: " , area )

main()
