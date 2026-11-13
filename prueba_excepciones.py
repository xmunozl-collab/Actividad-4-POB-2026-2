class PruebaExcepciones:
    def __init__(self):
        # aqui se guardan los mensajes que se van mostrando
        self.mensajes = []

    def primer_bloque(self):
        try:
            self.mensajes.append("Ingresando al primer try")
            cociente = 10000 / 0  # se lanza una excepcion
            self.mensajes.append("Después de la división")  # nunca se ejecuta
        except ZeroDivisionError:
            self.mensajes.append("División por cero")
        finally:
            # el finally siempre se ejecuta
            self.mensajes.append("Ingresando al primer finally")

    def segundo_bloque(self):
        try:
            self.mensajes.append("Ingresando al segundo try")
            objeto = None
            objeto.toString()  # se lanza una excepcion
            self.mensajes.append("Imprimiendo objeto")  # nunca se ejecuta
        except ArithmeticError:
            # esta excepcion no es de este tipo, no entra aca
            self.mensajes.append("División por cero")
        except Exception:
            self.mensajes.append("Ocurrió una excepción")
        finally:
            self.mensajes.append("Ingresando al segundo finally")

    def ejecutar(self):
        self.mensajes = []
        self.primer_bloque()
        self.segundo_bloque()
        return self.mensajes
