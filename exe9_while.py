def main():

    altura = int(input("Dê-me a altura da escada:"))

    while altura < 0:
        altura = int(input("Dê-me a altura da escada(Maior que 0!):"))

    i = altura

    while i > 0:
        print(" " * i, "*")
        i -= 1


if __name__ == "__main__":
    main()
