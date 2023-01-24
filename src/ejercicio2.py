# Validaciones
def esEntero(numero: str):
    """
    Esta funcion utiliza un try except para probar si un número es casteable a int, devolviendo True.
    Caso contrario, devuelve False.
    """
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
    while not esNatural(numero) or int(numero) == 0:
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return int(numero)


# Solucion al problema
def siguienteNumeroSucesionCollatz(numero: int) -> int:
    if numero % 2 == 0:
        return numero // 2
    else:
        return numero * 3 + 1


def sucesionCollatz(numero: int) -> tuple:
    """
    La condicion de corte tiene que ser igual a 1 porque si no, por la definicion de la sucesion, se entraria en un
    bucle.
    """
    paso = 0
    while not numero == 1:
        yield paso, numero
        numero = siguienteNumeroSucesionCollatz(numero)
        paso += 1
    yield paso, numero


def imprimirSucesionCollatz(numero: int) -> None:
    print(f"La sucesion de Collatz comenzando desde el numero {numero} es:")
    for paso, resultado in sucesionCollatz(numero):
        print(f"{paso} - {resultado}")


def main() -> None:
    numero = ingresarNumeroValido()
    imprimirSucesionCollatz(numero)


main()
