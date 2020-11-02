def main():
    int_list = []
    count = 0

    while count < 3:
        number = int(input("Dá-me um número:"))
        int_list.append(number)
        count += 1

    val = max(int_list)
    print("O valor máximo é:", val)


if __name__ == "__main__":
    main()
