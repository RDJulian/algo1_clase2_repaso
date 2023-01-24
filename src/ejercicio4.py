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


def factorizarNumero(numero: int) -> tuple:
    """
    Esta funcion recibe un número y lo devuelve factorizado, junto con el divisor.
    Si el número es primo, no es necesario ejecutar nada más, simplemente se devuelve 1 y sí mismo.
    """
    factor = 2
    numero = modulo(numero)
    while factor <= numero:
        while esDivisible(numero, factor):
            yield factor
            numero = numero // factor
        factor += 1


def imprimirFactoresPrimos(numero: int) -> None:
    if -1 <= numero <= 1:
        print(f"El numero {numero} no tiene factores primos.")
    else:
        print(f"Los factores primos del numero {numero} son:")
        for factor in factorizarNumero(numero):
            print(factor)


def main() -> None:
    numero = ingresarNumeroValido()
    imprimirFactoresPrimos(numero)


main()
