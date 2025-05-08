class TorresHanoi:
    def __init__(self, discos):
        self.discos = discos
        self.torres = [
            list(range(discos, 0, -1)),  # Torre de origen con los discos ordenados
            [],  # Torre auxiliar vacía
            []   # Torre de destino vacía
        ]
        self.movimientos = 0

    def mover(self, origen, destino):
        if not self.torres[origen]:
            return False  # No hay discos en la torre origen
        if self.torres[destino] and self.torres[origen][-1] > self.torres[destino][-1]:
            return False  # No se puede poner un disco grande sobre uno pequeño

        # Realizar el movimiento
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)
        self.movimientos += 1
        return True

    def es_resuelto(self):
        return len(self.torres[2]) == self.discos

    def obtener_estado(self):
        return {
            "torres": self.torres,
            "movimientos": self.movimientos,
            "resuelto": self.es_resuelto()
        }

    def resolver(self, n, origen, auxiliar, destino):
        if n == 1:
            self.mover(origen, destino)
            return
        self.resolver(n - 1, origen, destino, auxiliar)
        self.mover(origen, destino)
        self.resolver(n - 1, auxiliar, origen, destino)
