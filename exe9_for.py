def main():

    altura = int(input("Dê-me a altura da escada:"))

    while altura < 0:
        altura = int(input("Dê-me a altura da escada(Maior que 0!):"))

    for i in range(0, altura):
        print(" " * (altura-i), "*")


if __name__ == "__main__":
    main()
