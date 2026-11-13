import tkinter as tk
from tkinter import messagebox
from vendedor import Vendedor


class VentanaVendedor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vendedor")
        self.resizable(False, False)

        tk.Label(self, text="Nombre:", anchor="w").place(x=20, y=20, width=80, height=23)
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=105, y=20, width=190, height=23)

        tk.Label(self, text="Apellidos:", anchor="w").place(x=20, y=50, width=80, height=23)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=105, y=50, width=190, height=23)

        tk.Label(self, text="Edad:", anchor="w").place(x=20, y=80, width=80, height=23)
        self.campo_edad = tk.Entry(self)
        self.campo_edad.place(x=105, y=80, width=190, height=23)

        self.boton_crear = tk.Button(self, text="Crear vendedor", command=self.crear_vendedor)
        self.boton_crear.place(x=105, y=115, width=120, height=25)

        # etiqueta donde se muestran los datos del vendedor
        self.resultado = tk.Label(self, text="", anchor="nw", justify="left")
        self.resultado.place(x=20, y=160, width=290, height=70)

        # ventana centrada en la pantalla
        x = (self.winfo_screenwidth() - 330) // 2
        y = (self.winfo_screenheight() - 250) // 2
        self.geometry(f"330x250+{x}+{y}")

    # evento del boton Crear vendedor
    def crear_vendedor(self):
        nombre = self.campo_nombre.get().strip()
        apellidos = self.campo_apellidos.get().strip()

        if nombre == "" or apellidos == "":
            messagebox.showwarning("Alerta", "Debe ingresar el nombre y los apellidos.")
            return

        try:
            edad = int(self.campo_edad.get())
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        vendedor = Vendedor(nombre, apellidos)
        try:
            vendedor.verificar_edad(edad)
        except ValueError as e:
            # si la edad no sirve se muestra la excepcion
            self.resultado.config(text="")
            messagebox.showerror("Excepción", str(e))
            return

        self.resultado.config(text=vendedor.imprimir())
