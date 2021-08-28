def main():
    anos = int(input("Insira os anos: "))
    meses = int(input("Insira os meses: "))
    dias = int(input("Insira os dias: "))

    total_dias = (anos * 365) + (meses * 30) + dias

    print(f"{anos} anos, {meses} meses e {dias} dias = {total_dias} dias.")


if __name__ == "__main__":
    main()
