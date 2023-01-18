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
    while not esNatural(numero):
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return int(numero)


def calcularEnesimoNumeroSerieFibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        primero = 0
        segundo = 1
        enesimo = None
        for i in range(n - 1):
            enesimo = primero + segundo
            primero = segundo
            segundo = enesimo
        return enesimo


def imprimirSerieFibonacci(n: int) -> None:
    for i in range(n + 1):
        print(f"{i} - {calcularEnesimoNumeroSerieFibonacci(i)}")


def main() -> None:
    n = ingresarNumeroValido()
    imprimirSerieFibonacci(n)


main()
