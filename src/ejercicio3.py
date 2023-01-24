# Validaciones
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
    """Ver comentario del ejercicio 1."""
    numero = input("Ingrese un numero: ")
    while not esNatural(numero):
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return int(numero)


# Solucion al problema
def serieFibonacci(n: int) -> tuple:
    """
    NOTA: Aunque parece similar, este algoritmo no tiene nada que ver con el Bubblesort.
    El rango es de 2 a n porque queremos obtener los resultados anteriores hasta el n deseado.
    Comienza en 2 porque los resultados 0 y 1 ya son conocidos.
    """
    nMenosDos = 0
    nMenosUno = 1
    for n in range(n + 1):
        if n == 0:
            yield n, 0
        elif n == 1:
            yield n, 1
        else:
            enesimo = nMenosUno + nMenosDos
            nMenosDos = nMenosUno
            nMenosUno = enesimo
            yield n, enesimo


def imprimirSerieFibonacci(n: int) -> None:
    print(f"La serie de Fibonacci hasta el n = {n} es:")
    for n, enesimo in serieFibonacci(n):
        print(f"{n} - {enesimo}")


def main() -> None:
    n = ingresarNumeroValido()
    imprimirSerieFibonacci(n)


main()
