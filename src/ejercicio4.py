# Validaciones
def esEntero(numero: str):
    try:
        int(numero)
        return True
    except ValueError:
        return False


def ingresarNumeroValido() -> int:
    """Ver comentario del ejercicio 1."""
    numero = input("Ingrese un numero: ")
    while not esEntero(numero):
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return int(numero)


# Solucion al problema
def modulo(numero: int) -> int:
    """
    Devuelve el valor verdadero. También se puede directamente filtrar los numeros negativos en ingresarNumeroValido().
    """
    if numero < 0:
        return numero * (-1)
    else:
        return numero


def esDivisible(dividendo: int, divisor: int) -> bool:
    return dividendo % divisor == 0


def esNumeroPrimo(numero: int) -> bool:
    """
    Se asume que un número es primo hasta que se encuentra un divisor entre 1 y sí mismo.
    En ese caso, se devuelve False.
    Si no se encuentra ningun divisor, devuelve True.
    """
    if numero == 0 or numero == 1:
        return False
    else:
        divisor = 2
        esPrimo = True
        while esPrimo and divisor < numero:
            esPrimo = not esDivisible(numero, divisor)
            divisor += 1
        return esPrimo


def buscarFactorPrimo(numero: int) -> int:
    """
    Esta funcion solo busca el primer divisor primo del número ingresado y lo devuelve.
    Se sabe de antemano que el número ingresado no es primo.
    """
    factorPrimo = 2
    encontrado = False
    while not encontrado:
        if esDivisible(numero, factorPrimo) and esNumeroPrimo(factorPrimo):
            encontrado = True
        else:
            factorPrimo += 1
    return factorPrimo


def factorizarNumero(numero: int) -> tuple:
    """
    Esta funcion recibe un número y lo devuelve factorizado, junto con el divisor.
    Si el número es primo, no es necesario ejecutar nada más, simplemente se devuelve 1 y sí mismo.
    """
    if esNumeroPrimo(numero):
        return 1, numero
    else:
        factorPrimo = buscarFactorPrimo(numero)
        return numero // factorPrimo, factorPrimo


def imprimirFactoresPrimos(numero: int) -> None:
    if -1 <= numero <= 1:
        print(f"El numero {numero} no tiene factores primos.")
    else:
        numero = modulo(numero)
        while not numero == 1:
            numero, factorPrimo = factorizarNumero(numero)
            print(factorPrimo)


def main() -> None:
    numero = ingresarNumeroValido()
    imprimirFactoresPrimos(numero)


main()
