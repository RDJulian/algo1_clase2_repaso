from validaciones import ingresar_natural


def serie_fibonacci(n: int) -> tuple:
    """
    El rango es de 0 a n + 1 porque queremos incluir el valor enésimo.
    """
    n_menos2 = 0
    n_menos1 = 1
    for i in range(n + 1):
        if i == 0:
            yield i, 0
        elif i == 1:
            yield i, 1
        else:
            enesimo = n_menos1 + n_menos2
            n_menos2 = n_menos1
            n_menos1 = enesimo
            yield i, enesimo


def main():
    n = ingresar_natural()
    print(f"La serie de Fibonacci hasta el n = {n} es:")
    for n, enesimo in serie_fibonacci(n):
        print(f"{n} - {enesimo}")


if __name__ == "__main__":
    main()
