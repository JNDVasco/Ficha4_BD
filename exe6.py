def main():
    string_numero = input("Dê-me um número:")

    sum_numero = 0

    for i in range(0, len(string_numero)):
        sum_numero += int(string_numero[i])

    print("A soma de %s é: %d" % (string_numero, sum_numero))


if __name__ == "__main__":
    main()
