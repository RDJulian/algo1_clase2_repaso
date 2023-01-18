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


def calcularMaximoComunDivisor(unNumero: int, otroNumero: int) -> int:
    mcd = 1
    while not unNumero == 1:
        unNumero, factorPrimo = factorizarNumero(unNumero)
        if esDivisible(otroNumero, factorPrimo):
            mcd = mcd * factorPrimo
            otroNumero = int(otroNumero / factorPrimo)
    return mcd


def calcularMinimoComunMultiplo(unNumero: int, otroNumero: int, mcd: int) -> int:
    return int(unNumero * otroNumero / mcd)


def main() -> None:
    unNumero = ingresarNumeroValido()
    otroNumero = ingresarNumeroValido()
    mcd = calcularMaximoComunDivisor(unNumero, otroNumero)
    mcm = calcularMinimoComunMultiplo(unNumero, otroNumero, mcd)
    print(f"El MCD de los numeros {unNumero} y {otroNumero} es {mcd} y el MCM es {mcm}")


main()
