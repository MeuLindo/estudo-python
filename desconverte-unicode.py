def main():
    print("Esse programa converte código Unicode para caracteres")

    unicode = input("\nEntre a mensagem em unicode\n")

    mensagem = ""

    for codigo in unicode.split():
        numCodigo = int(codigo)
        mensagem += chr(numCodigo)

    print("A mensagem decodificada é: ", mensagem)

main()
