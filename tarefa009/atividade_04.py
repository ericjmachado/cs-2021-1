

def main():
    ipi = float(input("Insira o valor do IPI: "))
    input("Insira o código da primeira peça: ")
    primeira_quantidade = int(input("Insira a quantidade da primeira peça: "))
    primeiro_valor = float(input("Insira o valor da primeira peça: "))

    input("Insira o código da segunda peça: ")
    segunda_quantidade = int(input("Insira a quantidade da segunda peça: "))
    segundo_valor = float(input("Insira o valor da segunda peça: "))

    resultado = (
        primeira_quantidade * primeiro_valor + segunda_quantidade * segundo_valor
    ) * (ipi / 100 + 1)

    print(f"O valor total a ser pago é R$ {resultado}")


if __name__ == "__main__":
    main()
