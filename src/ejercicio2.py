"""
Para entender la solución, recordemos que factorizar un número en sus factores
primos es, en esencia, ir dividiendo el número por divisores primos hasta que
todos los factores lo sean, por ejemplo:
    40 = 2 * 20 = 2 * 2 * 10 = 2 * 2 * 2 * 5 (* 1)
Por lo tanto, una forma de hacerlo en este caso es dividir el número por 2 todas
las veces que sea divisible, luego por 3, por 4 y finalmente por 5.
Cuando llega a 5, el número final es necesariamente 1.

El algoritmo planteado en esta solución hace eso:
    Mientras que el número sea distinto de 1,
        revisamos que sea divisible por el factor actual.
        Si es divisible,
            entonces es factor.
            Dividimos el número por el factor (ver arriba).
        Si no,
            avanzamos al siguiente factor.

Es importante destacar que este algoritmo NUNCA va a imprimir factores no primos.
Esto es así porque, por ejemplo, al dividir todas las veces posibles por 2, ningún
múltiplo de 2 va a poder ser un factor del número.

Para pensar: ¿Qué pasa si el factor lo inicializamos en 1, en vez de 2?
"""

from validaciones import es_divisible, ingresar_entero


def imprimir_factores_primos(numero: int) -> None:
    # Los números -1, 0 y 1 no tienen factores primos.
    if -1 <= numero <= 1:
        print(f"El número {numero} no tiene factores primos.")
    else:
        print(f"Los factores primos del número {numero} son:")
        factor = 2
        # Valor absoluto para contemplar números negativos.
        while abs(numero) != 1:
            if es_divisible(numero, factor):
                print(factor)
                numero = numero // factor
            else:
                factor += 1


def main():
    numero = ingresar_entero()
    imprimir_factores_primos(numero)


if __name__ == "__main__":
    main()
