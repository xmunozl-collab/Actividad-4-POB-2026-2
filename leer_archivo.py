class LeerArchivo:
    @staticmethod
    def leer(nombre_archivo):
        # se lee el archivo linea por linea
        lineas = []
        with open(nombre_archivo, encoding="utf-8") as archivo:
            linea = archivo.readline()
            while linea != "":
                lineas.append(linea.rstrip("\n"))
                linea = archivo.readline()
        return lineas
