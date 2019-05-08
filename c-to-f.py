# Celsius to Fahrenheit

def main():
    print('Esse programa converte temperatura em celsius para Fahrenheit')
    print()
    celsius = eval(input("Qual a temperatura em celsius? "))
    fahrenheit = 9/5 * celsius + 32
    print("A temperatura é", fahrenheit, "graus Fahrenheit.")

    input('Digite <Enter> para sair.')
main()
