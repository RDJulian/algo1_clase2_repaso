def esFloat(numero: str) -> bool:
    try:
        float(numero)
        return True
    except ValueError:
        return False


def ingresarNumero() -> float:
    numero = input("Ingrese un numero: ")
    while not esFloat(numero):
        numero = input("La entrada no es valida. Ingrese nuevamente: ")
    return float(numero)


def contarDigitosEnteros(numero: float) -> int:
    contador = 0
    while not (-1 < numero < 1):
        numero = numero / 10
        contador += 1
    return contador


def main() -> None:
    numero = ingresarNumero()
    print(f"El numero ingresado tiene {contarDigitosEnteros(numero)} digitos enteros.")


main()
