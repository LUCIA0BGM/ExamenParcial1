import tkinter as tk
from tkinter import messagebox
from Juego_NReinas import TableroReinas
from comunicacion.cliente import enviar_resultado

class JuegoNReinasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de las N Reinas")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text="Introduce el tamaño del tablero (N >= 4):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button_resolver = tk.Button(root, text="Resolver", command=self.resolver)
        self.button_resolver.pack(pady=20)

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack(pady=20)

    def resolver(self):
        # Obtener el valor de N
        try:
            n = int(self.entry.get())
            if n < 4:
                messagebox.showerror("Error", "El tamaño del tablero debe ser mayor o igual a 4.")
                return
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido.")
            return

        # Crear la instancia del juego
        juego = TableroReinas(n)
        juego.resolver()

        # Obtener los resultados y mostrar el tablero
        resultados = juego.obtener_resultados()
        if not resultados["resuelto"]:
            messagebox.showinfo("Resultado", "No se pudo resolver el juego.")
        else:
            self.dibujar_tablero(juego.obtener_tablero())  # Tomamos la solución

            # Enviar el resultado al servidor
            datos = {
                "tamanio": n,  # Número de reinas (tamaño del tablero)
                "pasos": resultados["pasos"],  # Número de pasos (movimientos)
                "resuelto": resultados["resuelto"]
            }
            enviar_resultado("nreinas", datos, callback=lambda r: print("[Servidor]:", r))

    def dibujar_tablero(self, solucion):
        self.canvas.delete("all")
        cell_size = 300 // len(solucion)

        # Dibujar las casillas del tablero
        for i in range(len(solucion)):
            for j in range(len(solucion)):
                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(i * cell_size, j * cell_size,
                                              (i + 1) * cell_size, (j + 1) * cell_size,
                                              fill=color)

        # Dibujar las reinas en el tablero
        for i, col in enumerate(solucion):
            self.canvas.create_oval(col * cell_size + 10, i * cell_size + 10,
                                    (col + 1) * cell_size - 10, (i + 1) * cell_size - 10,
                                    fill="red")


if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoNReinasApp(root)
    root.mainloop()
