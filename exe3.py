def main():
    desconto = 0.25

    preco_fruta = int(input("Diga-me o preço da fruta(euro/kg):"))
    quantidade = int(input("Diga-me a quantidade comprada(kg):"))
    quantidade_desconto = int(input("Diga-me a partir de que peso há desconto(kg):"))

    if quantidade > quantidade_desconto:
        quantidade_com_desconto = quantidade - quantidade_desconto
        total = quantidade_desconto * preco_fruta
        total += quantidade_com_desconto * (preco_fruta * desconto)
    else:
        total = quantidade * preco_fruta

    print("O preço total é:", total)


if __name__ == "__main__":
    main()
