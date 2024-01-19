"""
Un ejemplo de como modularizar el código y hacer módulos permite la reutilización.
Estas funciones las necesite en todos los ejercicios de este repo, por lo que fue
conveniente moverlas a este archivo, para luego poder importarlas en las soluciones.

Se pueden importar funciones de otro archivo de dos formas:
    1. import modulo
Esto va a importar TODAS las funciones de ese módulo. Si se importa de esta forma,
luego se deben llamar a las funciones de la forma:
    modulo.funcion()

Por ejemplo:
    import validaciones
    validaciones.es_float()

    2. from modulo import funcion1, funcion2, ...
Esto va a importar solamente las funciones especificadas del módulo. De esta forma,
se llaman directamente:
    funcion()

Por ejemplo:
    from validaciones import es_float, es_entero
    es_float()

Ante la duda, releer el capítulo VI del apunte.
"""


def es_float(string: str) -> bool:
    """
    Esta función utiliza un try except para probar si un string es casteable a float,
    devolviendo True. Caso contrario, devuelve False.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def es_entero(string: str) -> bool:
    """
    Esta función utiliza un try except para probar si un string es casteable a entero,
    devolviendo True. Caso contrario, devuelve False.
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def es_natural(string: str) -> bool:
    """
    Un número es natural si es entero y positivo (incluyendo al 0).
    """
    return es_entero(string) and int(string) >= 0


def ingresar_float() -> float:
    """
    Función para validar que lo que se ingresa es un float.
    La condición de corte del while es que el número sea un float. Caso contrario,
    se sigue ejecutando.
    """
    numero = input("Ingrese un número float: ")
    while not es_float(numero):
        numero = input("La entrada no es un float. Ingrese nuevamente: ")
    return float(numero)


def ingresar_entero() -> int:
    """
    Función para validar que lo que se ingresa es un entero.
    La condición de corte del while es que el número sea un entero. Caso contrario,
    se sigue ejecutando.
    """
    numero = input("Ingrese un número entero: ")
    while not es_entero(numero):
        numero = input("La entrada no es un entero. Ingrese nuevamente: ")
    return int(numero)


def ingresar_natural() -> int:
    """
    Función para validar que lo que se ingresa es un natural.
    La condición de corte del while es que el número sea un natural. Caso contrario,
    se sigue ejecutando.
    """
    numero = input("Ingrese un número natural: ")
    while not es_natural(numero):
        numero = input("La entrada no es un natural. Ingrese nuevamente: ")
    return int(numero)


def es_divisible(dividendo: int, divisor: int) -> bool:
    return dividendo % divisor == 0
