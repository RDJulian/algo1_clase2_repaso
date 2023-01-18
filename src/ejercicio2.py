def esEntero(numero: str):
    try:
        int(numero)
        return True
    except ValueError:
        return False


def esPositivo(numero: str) -> bool:
    return int(numero) >= 0


def esNatural(numero: str) -> bool:
    return esEntero(numero) and esPositivo(numero)


def ingresarNumeroValido() -> int:
    numero = input("Ingrese un numero: ")
    while not esNatural(numero) or int(numero) == 0:
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return int(numero)


def siguienteNumeroSucesionCollatz(numero: int) -> int:
    if numero % 2 == 0:
        return int(numero / 2)
    else:
        return numero * 3 + 1


def imprimirSucesionCollatz(numero: int) -> None:
    paso = 0
    while not numero == 1:
        print(f"{paso} - {numero}")
        numero = siguienteNumeroSucesionCollatz(numero)
        paso += 1
    print(f"{paso} - {numero}")


def main() -> None:
    numero = ingresarNumeroValido()
    imprimirSucesionCollatz(numero)


main()
