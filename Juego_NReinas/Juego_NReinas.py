class TableroReinas:
    def __init__(self, n):
        self.n = n
        self.tablero = [-1] * n  # tablero[i] = columna donde está la reina en la fila i
        self.solucion_encontrada = False
        self.intentos = 0

    def es_seguro(self, fila, col):
        for i in range(fila):
            if self.tablero[i] == col or \
               abs(self.tablero[i] - col) == abs(i - fila):
                return False
        return True

    def resolver(self, fila=0):
        if fila == self.n:
            self.solucion_encontrada = True
            return True

        for col in range(self.n):
            self.intentos += 1
            if self.es_seguro(fila, col):
                self.tablero[fila] = col
                if self.resolver(fila + 1):
                    return True
                self.tablero[fila] = -1  # backtrack

        return False

    def obtener_tablero(self):
        return self.tablero

    def obtener_resultados(self):
        return {
            "tamanio": self.n,
            "resuelto": self.solucion_encontrada,
            "pasos": self.intentos
        }

# Ejemplo de uso:
if __name__ == "__main__":
    n = 8
    juego = TableroReinas(n)
    juego.resolver()
    print("Resultado:", juego.obtener_resultados())
    print("Solución:", juego.obtener_tablero())
