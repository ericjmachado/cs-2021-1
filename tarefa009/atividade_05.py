from math import floor


def main():
    salario_minimo = float(input("Insira o valor do salário mínimo: "))
    salario_colaborador = float(input("Insira o valor do salário do colaborador: "))
    print(
        f"O colaborador recebe o equivalente a {floor(salario_colaborador / salario_minimo)} salários minimos!"
    )


if __name__ == "__main__":
    main()
