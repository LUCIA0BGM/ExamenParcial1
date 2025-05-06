import socket
import json
import threading

# Dirección y puerto del servidor
HOST = '127.0.0.1'
PORT = 65432

def enviar_resultado(juego, datos, callback=None):
    """
    Envía los resultados al servidor en un hilo separado para no bloquear la interfaz.

    Args:
        juego (str): Nombre del juego (ej. "nreinas", "caballo", "hanoi").
        datos (dict): Diccionario con los datos de la partida.
        callback (func, opcional): Función a ejecutar cuando se reciba respuesta del servidor.
    """

    def tarea():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))

                mensaje = {
                    "juego": juego,
                    "datos": datos
                }

                s.sendall(json.dumps(mensaje).encode())

                respuesta = s.recv(1024).decode()
                print(f"[CLIENTE] Respuesta del servidor: {respuesta}")

                if callback:
                    callback(respuesta)
        except ConnectionRefusedError:
            print("[ERROR] No se pudo conectar al servidor.")
        except Exception as e:
            print(f"[ERROR] {e}")

    # Lanzar en hilo aparte
    hilo = threading.Thread(target=tarea, daemon=True)
    hilo.start()
