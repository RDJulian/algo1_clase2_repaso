# Validaciones
def esFloat(numero: str) -> bool:
    """
    Esta funcion utiliza un try except para probar si un número es casteable a float, devolviendo True.
    Caso contrario, devuelve False.
    """
    try:
        float(numero)
        return True
    except ValueError:
        return False


def ingresarNumero() -> float:
    """
    En todos estos ejercicios, se utiliza una funcion similar para ingresar los datos.
    La condicion de corte es si el número es válido para las otras funciones (y para el ejercicio en general).
    En este caso, mientras que no sea un float, se pide al usuario que ingrese nuevamente.
    """
    numero = input("Ingrese un numero: ")
    while not esFloat(numero):
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return float(numero)


# Solucion al problema
def contarDigitosEnteros(numero: float) -> int:
    contador = 0
    while not -1 < numero < 1:
        numero = numero / 10
        contador += 1
    return contador


def main() -> None:
    numero = ingresarNumero()
    print(f"El numero ingresado tiene {contarDigitosEnteros(numero)} digitos enteros.")


main()
