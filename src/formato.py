"""
Este archivo es un ejemplo de como usar strings con formato para imprimir mas facilmente.
Quedó del año pasado, esto ya lo estuvimos usando este año (2024), asi que pueden pasar de largo.
"""


def main():
    uno = 1
    dos = 2
    tres = 3
    print(f"Se puede dar formato de esta forma: {uno}, {dos}, {tres}")
    tres = "tres"
    print(f"Se imprime el nuevo valor de tres: {uno}, {dos}, {tres}")
    print(f"Tambien se puede imprimir todo junto: {uno}{dos}{tres}")
    print(f"Esto es util para dar el formato exacto mas facilmente.")


if __name__ == "__main__":
    main()
