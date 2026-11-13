import tkinter as tk
from tkinter import messagebox
from programador import Programador
from equipo_maraton import EquipoMaraton


class VentanaEquipo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Equipo maratón de programación")
        self.resizable(False, False)
        self.equipo = None

        # datos del equipo
        tk.Label(self, text="Datos del equipo", anchor="w", font=("Segoe UI", 9, "bold")).place(x=20, y=10, width=200, height=23)
        tk.Label(self, text="Nombre del equipo:", anchor="w").place(x=20, y=40, width=130, height=23)
        self.campo_equipo = tk.Entry(self)
        self.campo_equipo.place(x=155, y=40, width=190, height=23)
        tk.Label(self, text="Universidad:", anchor="w").place(x=20, y=70, width=130, height=23)
        self.campo_universidad = tk.Entry(self)
        self.campo_universidad.place(x=155, y=70, width=190, height=23)
        tk.Label(self, text="Lenguaje:", anchor="w").place(x=20, y=100, width=130, height=23)
        self.campo_lenguaje = tk.Entry(self)
        self.campo_lenguaje.place(x=155, y=100, width=190, height=23)
        self.boton_crear = tk.Button(self, text="Crear equipo", command=self.crear_equipo)
        self.boton_crear.place(x=155, y=135, width=120, height=25)

        # datos del programador
        tk.Label(self, text="Datos del programador", anchor="w", font=("Segoe UI", 9, "bold")).place(x=20, y=180, width=200, height=23)
        tk.Label(self, text="Nombre:", anchor="w").place(x=20, y=210, width=130, height=23)
        self.campo_nombre = tk.Entry(self)
        self.campo_nombre.place(x=155, y=210, width=190, height=23)
        tk.Label(self, text="Apellidos:", anchor="w").place(x=20, y=240, width=130, height=23)
        self.campo_apellidos = tk.Entry(self)
        self.campo_apellidos.place(x=155, y=240, width=190, height=23)
        self.boton_anadir = tk.Button(self, text="Añadir programador", command=self.anadir_programador)
        self.boton_anadir.place(x=155, y=275, width=140, height=25)

        # estado del equipo e integrantes
        self.estado = tk.Label(self, text="Integrantes: 0 de 3 (mínimo 2)", anchor="w")
        self.estado.place(x=20, y=320, width=340, height=23)
        self.texto = tk.Text(self, state="disabled")
        self.texto.place(x=20, y=350, width=340, height=90)

        # ventana centrada en la pantalla
        x = (self.winfo_screenwidth() - 380) // 2
        y = (self.winfo_screenheight() - 460) // 2
        self.geometry(f"380x460+{x}+{y}")

    # evento del boton Crear equipo
    def crear_equipo(self):
        nombre = self.campo_equipo.get().strip()
        universidad = self.campo_universidad.get().strip()
        lenguaje = self.campo_lenguaje.get().strip()

        if nombre == "" or universidad == "" or lenguaje == "":
            messagebox.showwarning("Alerta", "Debe ingresar el nombre, la universidad y el lenguaje.")
            return

        self.equipo = EquipoMaraton(nombre, universidad, lenguaje)
        self.actualizar()

    # evento del boton Añadir programador
    def anadir_programador(self):
        if self.equipo is None:
            messagebox.showwarning("Alerta", "Primero debe crear el equipo.")
            return

        nombre = self.campo_nombre.get().strip()
        apellidos = self.campo_apellidos.get().strip()

        try:
            # se validan el nombre y los apellidos
            EquipoMaraton.validar_campo(nombre)
            EquipoMaraton.validar_campo(apellidos)
            programador = Programador(nombre, apellidos)
            self.equipo.anadir(programador)
        except ValueError as e:
            messagebox.showerror("Excepción", str(e))
            return
        except Exception as e:
            messagebox.showerror("Excepción", str(e))
            return

        self.campo_nombre.delete(0, tk.END)
        self.campo_apellidos.delete(0, tk.END)
        self.actualizar()

    def actualizar(self):
        # muestra el estado del equipo y la lista de integrantes
        texto_estado = f"Integrantes: {self.equipo.tamano_equipo} de 3 (mínimo 2)"
        if self.equipo.esta_lleno():
            texto_estado += " - equipo lleno"
        elif self.equipo.esta_completo():
            texto_estado += " - equipo completo"
        self.estado.config(text=texto_estado)

        lineas = [f"Equipo: {self.equipo.nombre_equipo} ({self.equipo.universidad}) - {self.equipo.lenguaje}"]
        for i in range(self.equipo.tamano_equipo):
            p = self.equipo.programadores[i]
            lineas.append(f"{i + 1}. {p.nombre} {p.apellidos}")

        self.texto.config(state="normal")
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, "\n".join(lineas))
        self.texto.config(state="disabled")
