class Caballo:
    def __init__(self, tamaño):
        self.tablero = [[-1 for _ in range(tamaño)] for _ in range(tamaño)]
        self.tamaño = tamaño
        self.movimientos_posibles = [
            (-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, 2), (-2, 1)
        ]
        self.movimientos = 0

    def es_valido(self, x, y):
        return 0 <= x < self.tamaño and 0 <= y < self.tamaño and self.tablero[x][y] == -1

    def resolver(self, x, y, movimiento_numero=1):
        self.tablero[x][y] = movimiento_numero

        if movimiento_numero == self.tamaño * self.tamaño:
            return True  # Recorrido completo

        for dx, dy in self.movimientos_posibles:
            nuevo_x, nuevo_y = x + dx, y + dy
            if self.es_valido(nuevo_x, nuevo_y):
                if self.resolver(nuevo_x, nuevo_y, movimiento_numero + 1):
                    return True
                self.tablero[nuevo_x][nuevo_y] = -1  # Backtrack

        return False

    def obtener_estado(self):
        return {
            "tablero": self.tablero,
            "movimientos": self.movimientos,
            "resuelto": self.tablero[self.tamaño - 1][self.tamaño - 1] != -1  # Ver si se completó el recorrido
        }

    def resolver_completo(self):
        if self.resolver(0, 0):
            return self.obtener_estado()
        return {"resuelto": False, "movimientos": 0, "tablero": None}
