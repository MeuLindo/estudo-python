# Calcula x dada formúmula quadrática

import math

def main():
    a = float(input("Qual o coeficiente a: "))
    b = float(input("Qual o coeficiente b: "))
    c = float(input("Qual o coeficiente c: "))

    delta = math.sqrt(b * b - 4 * a * c)
    
    xlinha = (delta - b) / ( 2 * a )
    xlinhalinha = (-delta - b) / ( 2 * a )

    print("Os valores são x'= ", xlinha, "e x''= ", xlinhalinha)

main()
