from programador import Programador


class EquipoMaraton:
    def __init__(self, nombre_equipo, universidad, lenguaje):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.programadores = []
        # el tamaño del equipo empieza en cero
        self.tamano_equipo = 0

    def esta_lleno(self):
        # maximo 3 programadores
        return self.tamano_equipo == 3

    def esta_completo(self):
        # minimo 2 programadores para poder competir
        return self.tamano_equipo >= 2

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo):
        if campo == "":
            raise ValueError("El campo no puede estar vacío.")
        for c in campo:
            if c.isdigit():
                raise ValueError("El nombre no puede tener dígitos.")
        if len(campo) >= 20:
            raise ValueError("La longitud debe ser inferior a 20 caracteres.")
