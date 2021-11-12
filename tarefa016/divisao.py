import traceback


def divide(dividendo, divisor):
    return dividendo / divisor


def main():
    dividendo = int(input("Insira o valor do dividendo: "))
    divisor = int(input("Insira o valor do divisor: "))

    try:
        print(divide(dividendo, divisor))
    except ZeroDivisionError:
        print("\033[91m" + traceback.format_exc())


if __name__ == "__main__":
    main()
