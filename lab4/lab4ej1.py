import tkinter as tk
from tkinter import messagebox

class Boleto:
    def __init__(self, tipo, dias_antes):
        self.tipo = tipo
        self.dias_antes = dias_antes
        self.precio = self.calcular_precio()

    def calcular_precio(self):
        precios = {
            "Palco": 100.0,
            "Platea": 50.0 if self.dias_antes >= 10 else 60.0,
            "Galería": 25.0 if self.dias_antes >= 10 else 30.0
        }
        return precios.get(self.tipo, 0)

    def obtener_info(self):
        return f"Boleto: {self.tipo}, Precio: ${self.precio:.2f}"

def comprar_boleto():
    tipo = tipo_var.get()
    dias_antes = int(dias_var.get())
    boleto = Boleto(tipo, dias_antes)
    messagebox.showinfo("Confirmación", boleto.obtener_info())

# Crear ventana
ventana = tk.Tk()
ventana.title("Compra de Boletos")

tk.Label(ventana, text="Seleccione el tipo de boleto:").pack()
tipo_var = tk.StringVar(value="Palco")
tk.OptionMenu(ventana, tipo_var, "Palco", "Platea", "Galería").pack()

tk.Label(ventana, text="Días antes de la función:").pack()
dias_var = tk.Entry(ventana)
dias_var.pack()

tk.Button(ventana, text="Comprar", command=comprar_boleto).pack()

ventana.mainloop()
