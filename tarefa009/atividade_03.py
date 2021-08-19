def main():
    valor = float(input("Insira o valor a ser reajustado: "))
    print(f"O valor: R$ {valor}, passou por um reajuste de 15% e seu novo valor é RS {valor + valor * 0.15}")


if __name__ == "__main__":
    main()
