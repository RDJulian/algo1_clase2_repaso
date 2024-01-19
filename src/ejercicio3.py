"""
Este ejercicio se puede resolver buscando primero el MCD, principalmente de dos formas:
1. Una forma es buscando la intersección de los factores primos de ambos números.
En base a lo desarrollado en el ejercicio 2, acá se hace lo mismo, pero con los dos números.
Lo importante es ir preguntando, para cada factor de uno de los dos números, si además es
factor del otro. En esos casos, se multiplica el factor encontrado por el MCD.

2. Otra solución, mucho mas directa pero mágica (en el sentido que puede ser dificil
de entender el por qué funciona) es usar el Algoritmo de Euclides:
    https://es.wikipedia.org/wiki/Algoritmo_de_Euclides

Luego, con el MCD, se puede calcular el MCM de la siguiente forma:
    numero1 * numero2 / mcd(numero1, numero2)

De todas formas, tanto el MCD como el MCM ya están implementados en el módulo math:
    gcd() y lcm()
"""

from validaciones import es_divisible, ingresar_entero


def calcular_mcd(numero1: int, numero2: int) -> int:
    """
    Esta función muy probablemente se pueda optimizar, pero lo dejo así
    para que se entienda lo que está pasando (muy similar al ejercicio 2).
    """
    mcd = 1
    factor = 2
    while abs(numero1) != 1:
        if es_divisible(numero1, factor):
            numero1 = numero1 // factor
            # Acá es donde se revisa si el factor también divide al segundo número.
            if es_divisible(numero2, factor):
                mcd *= factor
                numero2 = numero2 // factor
        else:
            factor += 1
    return mcd


def calcular_mcm(numero1: int, numero2: int) -> int:
    # El MCM se deriva del MCD de esta forma.
    return abs(numero1 * numero2 // calcular_mcd(numero1, numero2))


def main():
    numero1 = ingresar_entero()
    numero2 = ingresar_entero()
    mcd = calcular_mcd(numero1, numero2)
    mcm = calcular_mcm(numero1, numero2)
    print(f"El MCD de los números {numero1} y {numero2} es {mcd} y el MCM es {mcm}.")


if __name__ == "__main__":
    main()
