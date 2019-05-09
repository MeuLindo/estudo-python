# Texto para Unicode

def main():

    print("Esse programa converte texto em seu correspondente em Unicode\n")

    # Coleta mensagem

    mensagem = input("Entre a mensagem a ser transformada: ")

    print("\n Segue os Unicódicos: ")

    for letra in mensagem:
        print(ord(letra), end=" ")

    print()

main()
