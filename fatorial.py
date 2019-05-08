# Esse programa calcula o fatorial de um número

def main():
    numero = int(input("Qual o número que cê quer fatoriar? "))
    fatorial = 1
    
    for fator in range(1 ,numero+1):
        fatorial *= fator

    print(fatorial)

main()
