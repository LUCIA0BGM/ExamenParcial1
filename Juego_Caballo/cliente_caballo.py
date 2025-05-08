from Juego_Caballo import Caballo
from comunicacion.cliente import enviar_resultado

def main():
    print("=== Juego del Caballo ===")

    while True:
        try:
            tamaño = int(input("Introduce el tamaño del tablero (n >= 5): "))
            if tamaño >= 5:
                break
            print("Por favor, introduce un tamaño mayor o igual a 5.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")

    juego = Caballo(tamaño)
    
    print("\nResolviendo el juego...")
    resultados = juego.resolver_completo()

    print("\nResultado:")
    if resultados["resuelto"]:
        print(f"Recorrido completado con éxito.")
    else:
        print("No se pudo completar el recorrido.")

    print(f"Movimientos: {resultados['movimientos']}")

    # Enviar al servidor
    print("\nEnviando resultado al servidor...")
    datos = {
        "movimientos": resultados['movimientos'],
        "resuelto": resultados["resuelto"]
    }
    enviar_resultado("caballo", datos, callback=lambda r: print("[Servidor]:", r))

if __name__ == "__main__":
    main()
