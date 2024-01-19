"""
Este ejercicio se puede pensar de varias formas. Asumiendo base 10,
la idea planteada en esta solución es ir "corriendo la coma" hasta que no
queden dígitos enteros en el número. Cuando no haya mas dígitos, el número
necesariamente va a tener que ser (en módulo) menor que 1.
Por ejemplo:
    12345
    1234.5
    123.45
    12.345
    1.2345
    0.12345
Por lo tanto, vamos a dividir por diez mientras que el número no sea menor que 1.
La cantidad de iteraciones son la cantidad de dígitos. Se van contando con una variable.
"""

from validaciones import ingresar_float


def contar_digitos_enteros(numero: float) -> int:
    contador = 0
    # abs() es valor absoluto.
    while not abs(numero) < 1:
        numero = numero / 10
        contador += 1
    return contador


def main():
    numero = ingresar_float()
    print(f"El número ingresado tiene {contar_digitos_enteros(numero)} dígitos enteros.")


if __name__ == "__main__":
    main()
