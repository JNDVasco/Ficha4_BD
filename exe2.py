def main():
    pontos_vantagem = int(input("Diga-me a vantagem em pontos da equipa:"))

    posse_de_bola = input("A equipa tem posse de bola?(s/n):")

    while not(posse_de_bola == 's' or posse_de_bola == 'n'):
        posse_de_bola = input("A equipa tem posse de bola?(Responda 's' ou 'n'):")

    tempo_restante = int(input("Diga-me o tempo restante em segundos:"))

    resultado = pontos_vantagem - 3

    if posse_de_bola == "s":
        resultado += 0.5
    elif posse_de_bola == "n":
        resultado -= 1
        if resultado < 0:
            resultado = 0
    else:
        print("Erro!")
        return 0

    resultado *= resultado

    print("Resultado:", resultado)
    print("Tempo restante:", tempo_restante)

    esta_seguro = (resultado > tempo_restante)

    print("O jogo ", "está seguro" if esta_seguro else "não está seguro")


if __name__ == "__main__":
    main()
