from Juego_NReinas import TableroReinas
from comunicacion.cliente import enviar_resultado

def main():
    print("=== Juego de las N Reinas ===")
    while True:
        try:
            n = int(input("Introduce el tamaño del tablero (N >= 4): "))
            if n >= 4:
                break
            print("Por favor, introduce un valor mayor o igual a 4.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    juego = TableroReinas(n)
    juego.resolver()

    resultados = juego.obtener_resultados()
    solucion = juego.obtener_tablero()

    print("\nResultado:")
    print("¿Resuelto?     :", resultados['resuelto'])
    print("Intentos       :", resultados['pasos'])
    print("Posiciones     :", solucion)

    # Enviar al servidor
    print("\nEnviando resultado al servidor...")
    enviar_resultado("nreinas", resultados, callback=lambda r: print("[Servidor]:", r))

if __name__ == "__main__":
    main()
