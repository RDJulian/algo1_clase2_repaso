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
def calcularEnesimoNumeroSerieFibonacci(n: int) -> int:
    """
    NOTA: Aunque parece similar, este algoritmo no tiene nada que ver con el Bubblesort.
    El rango es de 2 a n porque queremos obtener los resultados anteriores hasta el n deseado.
    Comienza en 2 porque los resultados 0 y 1 ya son conocidos.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        nMenosDos = 0
        nMenosUno = 1
        for i in range(2, n):
            auxiliar = nMenosUno
            nMenosUno = nMenosUno + nMenosDos
            nMenosDos = auxiliar
        return nMenosUno + nMenosDos


def imprimirSerieFibonacci(n: int) -> None:
    """Se imprime en el rango 0, n + 1 porque queremos imprimir el enesimo. Esto es equivalente a hacer 0, 1, ..., n."""
    for i in range(n + 1):
        print(f"{i} - {calcularEnesimoNumeroSerieFibonacci(i)}")


def main() -> None:
    n = ingresarNumeroValido()
    imprimirSerieFibonacci(n)


main()
