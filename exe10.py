def main():
    string = "João, Meio, Vasco"

    print("Alínea a)")
    print("Primeiro nome:", string[:4])

    print("\nAlínea b)")
    print("Primeiro nome:", string[-5:])

    print("\nAlínea c)")
    nome = string[-5:] + "," + string[:4]
    print("Ultímo nome, Primeiro nome:", nome)

    print("\nAlínea d)")
    print("Tamanho primeiro nome:", len(string[:4]))


if __name__ == "__main__":
    main()
