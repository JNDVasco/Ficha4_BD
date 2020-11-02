def main():
    str1 = input("Dê-me a primeira string:")
    str2 = input("Dê-me a segunda string:")

    for i in range(0, len(str1)):
        if str1[i] in str2:
            final = str2.replace(str1[i], "")

    print(final)


if __name__ == "__main__":
    main()
