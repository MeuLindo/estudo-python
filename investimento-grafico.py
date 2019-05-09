# Calcula valor futuro e desenha gráfico

from graphics import *

def main():

    # Apresentação
    
    print("Esse programa mostra o crescimento de um investimento de 10 anos")

    # Coleta informaçöes

    principal = float(input("Qual o valor inicial do investimento? "))
    taxa = float(input("Qual a taxa de juros anual? "))

    # Cria janela com etiquetas no canto esquerdo

    win = GraphWin("Gráfico de crescimento de investimento", 320, 240)
    win.setBackground("white")
    Text(Point(20,230), '0.0K').draw(win)
    Text(Point(20,180), '2.5K').draw(win)
    Text(Point(20,130), '5.0K').draw(win)
    Text(Point(20,80), '7.5K').draw(win)
    Text(Point(20,30), '10.0K').draw(win)

    # Desenha a barra para o ivestimento inicial

    altura = principal * 0.02
    barra = Rectangle(Point(40, 230), Point(65, 230 - altura))
    barra.setFill("green")
    barra.setWidth(2)
    barra.draw(win)

    # Desenha as barras nos anos consecutivos

    for ano in range(1,11):
        # Calcula o valor para o próximo ano
        principal *= 1 + taxa/100

        # Desenha a barra para esse valor

        xll = ano * 25 + 40
        altura = principal * 0.02
        barra = Rectangle(Point(xll, 230), Point(xll+25, 230 - altura))
        barra.setFill("green")
        barra.setWidth(2)
        barra.draw(win)

    input("Aperte <ENTER> para sair.")
    win.close()
    
main()
