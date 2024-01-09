from ejercicio2 import factorizar_numero
from validaciones import es_divisible, ingresar_entero


def calcular_mcd(numero1: int, numero2: int) -> int:
    """
    Para encontrar el MCD, se puede buscar la intersección entre los factores primos de ambos números.
    La solución planteada factoriza a uno de los números e intenta dividir al otro por el factor encontrado.
    Si es divisor, entonces lo multiplica por el MCD actual.
    """
    mcd = 1
    for factor in factorizar_numero(numero1):
        if es_divisible(numero2, factor):
            mcd = mcd * factor
            numero2 = numero2 // factor
    return mcd


def calcular_mcm(numero1: int, numero2: int) -> int:
    """El MCM se deriva del MCD de esta forma."""
    return abs(numero1 * numero2 // calcular_mcd(numero1, numero2))


def main():
    numero1 = ingresar_entero()
    numero2 = ingresar_entero()
    mcd = calcular_mcd(numero1, numero2)
    mcm = calcular_mcm(numero1, numero2)
    print(f"El MCD de los números {numero1} y {numero2} es {mcd} y el MCM es {mcm}.")


if __name__ == "__main__":
    main()
