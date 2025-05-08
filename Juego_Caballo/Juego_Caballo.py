class Caballo:
    def __init__(self, tamaño):
        self.tablero = [[-1 for _ in range(tamaño)] for _ in range(tamaño)]
        self.tamaño = tamaño
        self.movimientos_posibles = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        self.movimientos = 0  # Inicializamos el contador de movimientos

    def es_valido(self, x, y):
        """Verifica si la posición es válida (dentro del tablero y no visitada previamente)"""
        return 0 <= x < self.tamaño and 0 <= y < self.tamaño and self.tablero[x][y] == -1

    def resolver(self, x, y, movimiento_numero=1):
        """Resuelve el recorrido del caballo utilizando backtracking"""
        self.tablero[x][y] = movimiento_numero
        self.movimientos = movimiento_numero  # Actualiza el número de movimientos

        if movimiento_numero == self.tamaño * self.tamaño:
            return True  # Si se recorren todas las casillas, el recorrido está completo

        # Intentamos mover el caballo a cada una de las posibles posiciones
        for dx, dy in self.movimientos_posibles:
            nuevo_x, nuevo_y = x + dx, y + dy
            if self.es_valido(nuevo_x, nuevo_y):
                if self.resolver(nuevo_x, nuevo_y, movimiento_numero + 1):
                    return True
                self.tablero[nuevo_x][nuevo_y] = -1  # Backtrack si el movimiento no es válido

        return False  # Si no encontramos una solución

    def obtener_estado(self):
        """Devuelve el estado del juego: el tablero, los movimientos y si se completó el recorrido"""
        return {
            "tablero": self.tablero,
            "movimientos": self.movimientos,
            "resuelto": self.tablero[self.tamaño - 1][self.tamaño - 1] != -1  # Verifica si se completó el recorrido
        }

    def resolver_completo(self):
        """Inicia la resolución del recorrido desde la casilla (0,0)"""
        if self.resolver(0, 0):
            return self.obtener_estado()
        return {"resuelto": False, "movimientos": 0, "tablero": None}
