# Calculadora de investimento

def main():

    print("Esse programa calcula o valor futuro")
    print("de um investimento.")
    print()
    
    principal = eval(input("Entre o valor principal (inicial): "))
    apr = eval(input("Entre a taxa de juros anual: "))
    anos = eval(input("Quantos anos de investimento? "))

    for i in range(anos):
        principal *= (1 + apr/100)

    print("O valor final após ", anos, " anos é de: R$", principal)

    input('Digite <Enter> para sair.')
    
main()
