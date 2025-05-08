import tkinter as tk
from tkinter import messagebox
from Juego_Caballo import Caballo
from comunicacion.cliente import enviar_resultado

class JuegoCaballoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Caballo")
        self.root.geometry("500x500")

        self.label = tk.Label(root, text="Introduce el tamaño del tablero (n >= 5):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button_resolver = tk.Button(root, text="Resolver", command=self.resolver)
        self.button_resolver.pack(pady=20)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def resolver(self):
        # Obtener el valor de N
        try:
            n = int(self.entry.get())
            if n < 5:
                messagebox.showerror("Error", "El tamaño del tablero debe ser mayor o igual a 5.")
                return
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido.")
            return

        # Crear la instancia del juego
        juego = Caballo(n)
        
        print("\nResolviendo el juego...")
        resultados = juego.resolver_completo()  # Resolvemos el recorrido

        # Obtener los resultados y mostrar el tablero
        if not resultados["resuelto"]:
            messagebox.showinfo("Resultado", "No se pudo resolver el recorrido del caballo.")
        else:
            self.dibujar_tablero(juego.tablero)  # Dibujamos el tablero con el recorrido

            self.result_label.config(text=f"Movimientos: {resultados['movimientos']}")

            # Enviar el resultado al servidor
            datos = {
                "movimientos": resultados['movimientos'],
                "resuelto": resultados['resuelto']
            }
            enviar_resultado("caballo", datos, callback=lambda r: print("[Servidor]:", r))

    def dibujar_tablero(self, tablero):
        self.canvas.delete("all")
        cell_size = 400 // len(tablero)

        # Dibujar las casillas del tablero
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(i * cell_size, j * cell_size,
                                              (i + 1) * cell_size, (j + 1) * cell_size,
                                              fill=color)

        # Dibujar el recorrido del caballo
        for i in range(len(tablero)):
            for j in range(len(tablero)):
                if tablero[i][j] != -1:  # Si el caballo pasó por esta casilla
                    self.canvas.create_oval(i * cell_size + 10, j * cell_size + 10,
                                            (i + 1) * cell_size - 10, (j + 1) * cell_size - 10,
                                            fill="red")
                    self.canvas.create_text(i * cell_size + cell_size / 2, j * cell_size + cell_size / 2,
                                            text=str(tablero[i][j]), font=("Arial", 8))


if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoCaballoApp(root)
    root.mainloop()
