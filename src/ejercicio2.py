from validaciones import es_divisible, ingresar_entero


def factorizar_numero(numero: int) -> tuple:
    factor = 2
    numero = abs(numero)
    while factor <= numero:
        while es_divisible(numero, factor):
            yield factor
            numero = numero // factor
        factor += 1


def imprimir_factores(numero: int) -> None:
    if abs(numero) <= 1:
        print(f"El número {numero} no tiene factores primos.")
    else:
        print(f"Los factores primos del número {numero} son:")
        for factor in factorizar_numero(numero):
            print(factor)


def main():
    numero = ingresar_entero()
    imprimir_factores(numero)


if __name__ == "__main__":
    main()
