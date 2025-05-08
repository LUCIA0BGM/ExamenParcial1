from Juego_TorresHanoi import TorresHanoi
from comunicacion.cliente import enviar_resultado

def main():
    print("=== Juego de las Torres de Hanói ===")
    
    while True:
        try:
            discos = int(input("Introduce el número de discos (n >= 1): "))
            if discos >= 1:
                break
            print("Por favor, introduce un valor mayor o igual a 1.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    juego = TorresHanoi(discos)
    
    print("\nResolviendo el juego...")
    juego.resolver(discos, 0, 1, 2)  # Resolvemos el juego

    resultados = juego.obtener_estado()

    print("\nResultado:")
    print(f"¿Resuelto?     : {resultados['resuelto']}")
    print(f"Movimientos    : {resultados['movimientos']}")

    # Modificar los datos para enviar 'discos' en lugar de 'torres'
    datos = {
        "discos": discos,  # Enviamos el número de discos
        "movimientos": resultados['movimientos'],
        "resuelto": resultados['resuelto']
    }

    # Enviar al servidor
    print("\nEnviando resultado al servidor...")
    enviar_resultado("hanoi", datos, callback=lambda r: print("[Servidor]:", r))

if __name__ == "__main__":
    main()
