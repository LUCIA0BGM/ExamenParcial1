import tkinter as tk
from tkinter import messagebox
from Juego_TorresHanoi import TorresHanoi
from comunicacion.cliente import enviar_resultado

class JuegoHanoiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de las Torres de Hanói")
        self.root.geometry("500x500")

        self.label = tk.Label(root, text="Introduce el número de discos (n >= 1):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button_resolver = tk.Button(root, text="Resolver", command=self.resolver)
        self.button_resolver.pack(pady=20)

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack(pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

    def resolver(self):
        # Obtener el valor de N
        try:
            n = int(self.entry.get())
            if n < 1:
                messagebox.showerror("Error", "El número de discos debe ser mayor o igual a 1.")
                return
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número válido.")
            return

        # Crear la instancia del juego
        juego = TorresHanoi(n)
        
        print("\nResolviendo el juego...")
        juego.resolver(n, 0, 1, 2)  # Resolvemos el juego

        # Obtener los resultados y mostrar el tablero
        resultados = juego.obtener_estado()

        if not resultados["resuelto"]:
            messagebox.showinfo("Resultado", "No se pudo resolver el juego.")
        else:
            self.dibujar_tablero(juego.torres)  # Dibujamos las torres con los discos

            self.result_label.config(text=f"Movimientos: {resultados['movimientos']}")

            # Enviar el resultado al servidor
            datos = {
                "discos": n,  # Número de discos
                "movimientos": resultados['movimientos'],
                "resuelto": resultados['resuelto']
            }
            enviar_resultado("hanoi", datos, callback=lambda r: print("[Servidor]:", r))

    def dibujar_tablero(self, torres):
        self.canvas.delete("all")
        cell_width = 100
        cell_height = 200
        space = 20  # Espacio entre las torres

        # Dibujar las torres
        for i in range(3):
            self.canvas.create_rectangle(i * (cell_width + space), cell_height, (i + 1) * (cell_width + space), cell_height + 150, fill="brown")

        # Dibujar los discos
        for i, torre in enumerate(torres):
            for j, disco in enumerate(torre):
                self.canvas.create_oval(i * (cell_width + space) + 10, cell_height + 150 - (j + 1) * 30,
                                        (i + 1) * (cell_width + space) - 10, cell_height + 150 - j * 30,
                                        fill="red")
                self.canvas.create_text(i * (cell_width + space) + cell_width / 2, cell_height + 150 - (j + 1) * 30 + 15, text=str(disco), font=("Arial", 8))

if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoHanoiApp(root)
    root.mainloop()
