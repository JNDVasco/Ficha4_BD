def main():
    string = "Monty Python"

    tamanho = len(string)

    while tamanho > 0:
        for i in range(0, tamanho):
            print(string[i], end='')
        print("")
        tamanho -=1


if __name__ == "__main__":
    main()