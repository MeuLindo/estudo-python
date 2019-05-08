# Calcula a distancia entre dois pontos

import math

def main():

    x1, y1 = eval(input("Entre o primeiro ponto: x1,y1 "))
    x2, y2 = eval(input("Entre o primeiro ponto: x2,y2 "))

    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print("A distancia entre os pontos é de: ", distancia)

main()
