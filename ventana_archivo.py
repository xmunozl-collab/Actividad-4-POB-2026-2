import os
import tkinter as tk
from tkinter import filedialog, messagebox
from leer_archivo import LeerArchivo


class VentanaArchivo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Leer archivo")
        self.resizable(False, False)

        tk.Label(self, text="Archivo:", anchor="w").place(x=20, y=20, width=60, height=23)
        self.campo_ruta = tk.Entry(self)
        self.campo_ruta.place(x=85, y=20, width=290, height=23)
        # por defecto se lee el prueba.txt
        self.campo_ruta.insert(0, "prueba.txt")

        self.boton_examinar = tk.Button(self, text="Examinar...", command=self.examinar)
        self.boton_examinar.place(x=385, y=19, width=90, height=25)
        self.boton_leer = tk.Button(self, text="Leer archivo", command=self.leer)
        self.boton_leer.place(x=20, y=55, width=120, height=25)

        # cuadro de texto con barra para mostrar el contenido
        self.texto = tk.Text(self, state="disabled")
        self.texto.place(x=20, y=95, width=435, height=190)
        barra = tk.Scrollbar(self, command=self.texto.yview)
        barra.place(x=455, y=95, width=20, height=190)
        self.texto.config(yscrollcommand=barra.set)

        # ventana centrada en la pantalla
        x = (self.winfo_screenwidth() - 495) // 2
        y = (self.winfo_screenheight() - 305) // 2
        self.geometry(f"495x305+{x}+{y}")

    # evento del boton Examinar
    def examinar(self):
        ruta = filedialog.askopenfilename(title="Seleccione un archivo de texto",
                                          filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if ruta != "":
            self.campo_ruta.delete(0, tk.END)
            self.campo_ruta.insert(0, ruta)

    # evento del boton Leer archivo
    def leer(self):
        ruta = self.campo_ruta.get().strip()
        # si no se da la ruta completa se busca en la carpeta del programa
        if not os.path.isabs(ruta):
            ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), ruta)

        try:
            lineas = LeerArchivo.leer(ruta)
        except (OSError, UnicodeDecodeError):
            messagebox.showerror("Error", "No se pudo leer el archivo.")
            return

        self.texto.config(state="normal")
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, "\n".join(lineas))
        self.texto.config(state="disabled")
