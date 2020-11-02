def main():
    int_list = []
    count = 0

    limite_inferior = int(input("Dê-me o limite inferior do intrevalo:"))

    limite_superior = int(input("Dê-me o limite inferior do intrevalo:"))

    while limite_superior < limite_inferior:
        limite_superior = int(input("Dê-me o limite inferior do intrevalo(tem de ser maior que o inferior!):"))

    count = limite_inferior

    while count <= limite_superior:
        if not(count % 2):
            int_list.append(count)
            count += 1
        else:
            count += 1

    print(int_list)

    sum = 0

    for i in range(len(int_list)):
       sum += int_list[i]

    print("A soma é:", sum)

if __name__ == "__main__":
    main()
