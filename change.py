# change.py
#   Um programa para calcular o total de moedas

def main():
    print("Contador de troco")
    print()
    print("Entre a quantidade de cada tipo de moeda.")

    um = eval(input("Quantas moedas de R$1.00 ?"))
    cinquenta = eval(input("Quantas moedas de R$0.50 ?"))
    vinteCinco = eval(input("Quantas moedas de R$0.25 ?"))
    dez = eval(input("Quantas moedas de R$0.10 ?"))
    cinco = eval(input("Quantas moedas de R$0.05 ?"))

    total = um * 1 + cinquenta * 0.5 + vinteCinco * 0.25 + dez * 0.1 + cinco * 0.05

    print()
    print("O valor total de moedas é R$", total)

main()
