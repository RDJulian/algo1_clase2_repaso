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


def calcularMaximoComunDivisor(unNumero: int, otroNumero: int) -> int:
    """
    Para encontrar el MCD, se busca la interseccion entre los factores primos de ambos numeros.
    La solucion planteada factoriza a uno de los numeros e intenta dividir al otro por el factor encontrado.
    Si es divisor, entonces lo multiplica por el MCD actual.
    """
    mcd = 1
    for factor in factorizarNumero(unNumero):
        if esDivisible(otroNumero, factor):
            mcd = mcd * factor
            otroNumero = otroNumero // factor
    return mcd


def calcularMinimoComunMultiplo(unNumero: int, otroNumero: int, mcd: int) -> int:
    """El MCM se deriva del MCD de esta forma."""
    return modulo(unNumero * otroNumero // mcd)


def main() -> None:
    unNumero = ingresarNumeroValido()
    otroNumero = ingresarNumeroValido()
    mcd = calcularMaximoComunDivisor(unNumero, otroNumero)
    mcm = calcularMinimoComunMultiplo(unNumero, otroNumero, mcd)
    print(f"El MCD de los numeros {unNumero} y {otroNumero} es {mcd} y el MCM es {mcm}.")


main()
