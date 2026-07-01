"""
Solución del candidato.
El reto: 'implementá una función procesar(texto) que devuelva el texto
en mayúsculas y sin espacios al inicio/final, y una clase Contador
que cuente cuántas veces se llamó a incrementar()'.

Contrato del reto: tu solución va en solucion.py en la raíz del repo.
"""


def procesar(texto):
    return texto.strip().upper()


class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor += 2
        return self.valor
