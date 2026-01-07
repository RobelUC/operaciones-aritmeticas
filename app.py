from operaciones_aritmeticas import OperacionesAritmeticas

if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    operaciones = OperacionesAritmeticas(numero1, numero2)
    print("La suma de", numero1, "y", numero2, "es:", operaciones.suma_dos_numeros())
