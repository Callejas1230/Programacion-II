import tkinter as tk
from tkinter import messagebox

class Boleto:
    def __init__(self, numerodeboleto):
        self.numerodeboleto = numerodeboleto

    def mostrar_info(self):
        return f"Número: {self.numerodeboleto}, Precio: {self.precio:.1f}"

class Palco(Boleto):
    def __init__(self, numerodeboleto):
        super().__init__(numerodeboleto)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numerodeboleto, diasdeanticipacion):
        super().__init__(numerodeboleto)
        self.diasdeanticipacion = diasdeanticipacion
        self.precio = 50.0 if self.diasdeanticipacion >= 10 else 60.0

class Galeria(Boleto):
    def __init__(self, numerodeboleto, diasdeanticipacion):
        super().__init__(numerodeboleto)
        self.diasdeanticipacion = diasdeanticipacion
        self.precio = 25.0 if self.diasdeanticipacion >= 10 else 50.0

class TeatroMunicipalApp:
    def __init__(self, root):
        self.root = root
        root.title("Teatro Municipal")
        root.geometry("400x280")

        tk.Label(root, text="Teatro Municipal de Diego tu Papi", font=("Arial", 16)).pack(pady=5)

        self.tipo_boleto = tk.StringVar()
        frame_tipo = tk.Frame(root)
        frame_tipo.pack()
        tk.Label(frame_tipo, text="Tipo de Boleto:").grid(row=0, column=0, padx=5)
        tk.Radiobutton(frame_tipo, text="Palco", variable=self.tipo_boleto, value="palco", command=self.toggle_dias).grid(row=0, column=1)
        tk.Radiobutton(frame_tipo, text="Platea", variable=self.tipo_boleto, value="platea", command=self.toggle_dias).grid(row=0, column=2)
        tk.Radiobutton(frame_tipo, text="Galería", variable=self.tipo_boleto, value="galeria", command=self.toggle_dias).grid(row=0, column=3)

        frame_num = tk.Frame(root)
        frame_num.pack(pady=10)
        tk.Label(frame_num, text="Número:").grid(row=0, column=0, padx=5)
        self.entry_numero = tk.Entry(frame_num, width=10)
        self.entry_numero.grid(row=0, column=1)

        tk.Label(frame_num, text="Días para el Evento:").grid(row=1, column=0, padx=5)
        self.entry_dias = tk.Entry(frame_num, width=10, state=tk.DISABLED)
        self.entry_dias.grid(row=1, column=1)

        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)
        tk.Button(frame_btn, text="Vender", width=10, command=self.vender_boleto).grid(row=0, column=0, padx=10)
        tk.Button(frame_btn, text="Salir", width=10, command=root.quit).grid(row=0, column=1, padx=10)

        self.lbl_info = tk.Label(root, text="Información: ", fg="blue", font=("Arial", 11))
        self.lbl_info.pack(pady=10)

    def toggle_dias(self):
        self.entry_dias.config(state=tk.NORMAL if self.tipo_boleto.get() != "palco" else tk.DISABLED)

    def vender_boleto(self):
        tipo = self.tipo_boleto.get()
        try:
            numero = int(self.entry_numero.get())
            dias = int(self.entry_dias.get()) if tipo != "palco" else 0
        except ValueError:
            messagebox.showerror("Error", "Ingrese números válidos.")
            return

        boleto = Palco(numero) if tipo == "palco" else Platea(numero, dias) if tipo == "platea" else Galeria(numero, dias) if tipo == "galeria" else None
        
        if boleto:
            self.lbl_info.config(text="Información: " + boleto.mostrar_info())
        else:
            messagebox.showwarning("Advertencia", "Seleccione un tipo de boleto.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TeatroMunicipalApp(root)
    root.mainloop()
