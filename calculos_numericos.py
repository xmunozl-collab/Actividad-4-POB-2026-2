import math


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        # si el valor no es positivo se lanza una excepcion aritmetica
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular el logaritmo")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser un número positivo para calcular la raíz cuadrada")
        return math.sqrt(valor)
