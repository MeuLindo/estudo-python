# chaos.py
# https://upload.wikimedia.org/wikipedia/commons/1/1f/Logistic_map_animation.gif
def main():
    print('Esse programa ilustra uma função caótica')
    x = eval(input("Entre um número entre 0 e 1: "))
    y = eval(input("Entre um outro número entre 0 e 1: "))
    for i in range(100):
        x = 3.56996 * x * (1 - x)
        y = 3.56995 * y * (1 - y)
        print(x,y)


    input('Digite <Enter> para sair.')
    
main()
