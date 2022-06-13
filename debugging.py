from time import process_time_ns
from xml.dom import ValidationErr


def divisors(num):
    try:
        if num < 0:
            raise ValueError("No se pueden ingresar numeros negativos")
        divisors = []
        for i in range(1, num +1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)

def run():
    try:
        num = int(input("Ingresa un numero: "))
        print(divisors(num))
        print("El programa termino")
    except ValueError:
        print("Debes ingresar un numero")

if __name__ == "__main__":
    run()