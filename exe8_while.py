def main():

    altura = int(input("Dê-me a altura da escada:"))

    while altura < 0:
        altura = int(input("Dê-me a altura da escada(Maior que 0!):"))

    i = 0

    while i < altura:
        print(" " * i, "*")
        i += 1


if __name__ == "__main__":
    main()
