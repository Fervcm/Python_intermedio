from codecs import ascii_encode
from time import process_time_ns
from xml.dom import ValidationErr


def divisors(num):
    
    assert num > -1, "No se pueden ingresar numeros negativos"
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Se deben ingresar numeros"
    print(divisors(int(num)))
    print("El programa termino")
    print("Debes ingresar un numero")

if __name__ == "__main__":
    run()