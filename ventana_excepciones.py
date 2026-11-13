import tkinter as tk
from prueba_excepciones import PruebaExcepciones


class VentanaExcepciones(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Excepciones")
        self.resizable(False, False)

        tk.Label(self, text="Resultado de la ejecución del programa:", anchor="w").place(x=20, y=15, width=300, height=23)

        # cuadro de texto donde se muestran los mensajes
        self.texto = tk.Text(self, state="disabled")
        self.texto.place(x=20, y=45, width=340, height=150)

        self.boton_ejecutar = tk.Button(self, text="Ejecutar", command=self.ejecutar)
        self.boton_ejecutar.place(x=20, y=210, width=100, height=25)
        self.boton_limpiar = tk.Button(self, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=130, y=210, width=100, height=25)

        # ventana centrada en la pantalla
        x = (self.winfo_screenwidth() - 380) // 2
        y = (self.winfo_screenheight() - 255) // 2
        self.geometry(f"380x255+{x}+{y}")

    # evento del boton Ejecutar
    def ejecutar(self):
        prueba = PruebaExcepciones()
        mensajes = prueba.ejecutar()
        self.texto.config(state="normal")
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, "\n".join(mensajes))
        self.texto.config(state="disabled")

    # evento del boton Limpiar
    def limpiar(self):
        self.texto.config(state="normal")
        self.texto.delete("1.0", tk.END)
        self.texto.config(state="disabled")
