"""
Lo importante de este ejercicio es entender que el enésimo número es:
    f(n) = f(n - 1) + f(n - 2)
Por lo que va a ser conveniente guardarnos en cada iteración los valores
anteriores n - 1 y n - 2.
Eso es lo que hace el ciclo for: calcula el valor enésimo (actual) y luego
actualiza los valores n - 1 y n - 2 para la próxima iteración.
Es importante destacar que se utiliza un ciclo for porque se sabe la
cantidad de iteraciones.

En una de las próximas clases vamos a ver otra posible solución para este problema,
usando recursividad...
"""

from validaciones import ingresar_natural


def imprimir_serie_fibonacci(n: int) -> None:
    """
    Este código se puede escribir de una forma mas concisa,
    pero lo dejo así intencionalmente para la clase de recursividad.
    """
    print(f"La serie de Fibonacci hasta el n = {n} es:")
    n_menos2 = 0
    n_menos1 = 1
    # El rango es de 0 a n + 1 porque queremos incluir el valor enésimo.
    for i in range(n + 1):
        if i == 0:
            # f(0)
            print(f"{i} - {n_menos2}")
        elif i == 1:
            # f(1)
            print(f"{i} - {n_menos1}")
        else:
            # f(n), en general.
            print(f"{i} - {n_menos1 + n_menos2}")
            n_menos2, n_menos1 = n_menos1, n_menos1 + n_menos2


def main():
    n = ingresar_natural()
    imprimir_serie_fibonacci(n)


if __name__ == "__main__":
    main()
