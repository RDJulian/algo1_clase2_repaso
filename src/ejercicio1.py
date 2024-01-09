from validaciones import ingresar_float


def contar_digitos_enteros(numero: float) -> int:
    contador = 0
    while not abs(numero) < 1:
        numero = numero / 10
        contador += 1
    return contador


def main():
    numero = ingresar_float()
    print(f"El número ingresado tiene {contar_digitos_enteros(numero)} dígitos enteros.")


if __name__ == "__main__":
    main()
