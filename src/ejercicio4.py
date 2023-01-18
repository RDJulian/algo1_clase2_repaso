def esEntero(numero: str):
    try:
        int(numero)
        return True
    except ValueError:
        return False


def esDivisible(dividendo: int, divisor: int) -> bool:
    return dividendo % divisor == 0


def esNumeroPrimo(numero: int) -> bool:
    if numero == 0 or numero == 1:
        return False
    else:
        divisor = 2
        esPrimo = True
        while esPrimo and divisor < numero:
            esPrimo = not esDivisible(numero, divisor)
            divisor += 1
        return esPrimo


def buscarPrimerFactorPrimo(numero: int) -> int:
    factorPrimo = 2
    encontrado = False
    while not encontrado:
        if esDivisible(numero, factorPrimo) and esNumeroPrimo(factorPrimo):
            encontrado = True
        else:
            factorPrimo += 1
    return factorPrimo


def factorizarNumero(numero: int) -> tuple:
    if esNumeroPrimo(numero):
        return 1, numero
    else:
        factorPrimo = buscarPrimerFactorPrimo(numero)
        return int(numero / factorPrimo), factorPrimo


def ingresarNumeroValido() -> int:
    numero = input("Ingrese un numero: ")
    while not esEntero(numero):
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return int(numero)


def modulo(numero: int) -> int:
    if numero < 0:
        return numero * (-1)
    else:
        return numero


def imprimirFactoresPrimos(numero: int) -> None:
    if numero == 0 or numero == 1 or numero == -1:
        print(f"El numero {numero} no tiene factores primos.")
    else:
        numero = modulo(numero)
        while not numero == 1:
            numero, factorPrimo = factorizarNumero(numero)
            print(f"{factorPrimo}")


def main() -> None:
    numero = ingresarNumeroValido()
    imprimirFactoresPrimos(numero)


main()
