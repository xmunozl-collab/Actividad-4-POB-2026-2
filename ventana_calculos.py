import tkinter as tk
from tkinter import messagebox
from calculos_numericos import CalculosNumericos


class VentanaCalculos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cálculos numéricos")
        self.resizable(False, False)

        tk.Label(self, text="Valor numérico:", anchor="w").place(x=20, y=20, width=100, height=23)
        self.campo_valor = tk.Entry(self)
        self.campo_valor.place(x=125, y=20, width=150, height=23)

        self.boton_logaritmo = tk.Button(self, text="Logaritmo neperiano", command=self.logaritmo)
        self.boton_logaritmo.place(x=20, y=60, width=140, height=25)
        self.boton_raiz = tk.Button(self, text="Raíz cuadrada", command=self.raiz)
        self.boton_raiz.place(x=170, y=60, width=105, height=25)

        self.resultado = tk.Label(self, text="Resultado = ", anchor="w")
        self.resultado.place(x=20, y=105, width=260, height=23)

        # ventana centrada en la pantalla
        x = (self.winfo_screenwidth() - 300) // 2
        y = (self.winfo_screenheight() - 150) // 2
        self.geometry(f"300x150+{x}+{y}")

    # eventos de los botones
    def logaritmo(self):
        self.calcular(CalculosNumericos.calcular_logaritmo_neperiano)

    def raiz(self):
        self.calcular(CalculosNumericos.calcular_raiz_cuadrada)

    def calcular(self, operacion):
        self.resultado.config(text="Resultado = ")

        try:
            valor = float(self.campo_valor.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Error", "El valor debe ser numérico para realizar el cálculo")
            return

        try:
            resultado = operacion(valor)
            self.resultado.config(text=f"Resultado = {resultado:.4f}")
        except ArithmeticError as e:
            messagebox.showerror("Excepción aritmética", str(e))
