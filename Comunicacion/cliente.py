import socket
import json
import threading

HOST = '127.0.0.1'
PORT = 65432

def enviar_resultado(juego, datos, callback=None):
    def tarea():
        try:
            print("[CLIENTE] Intentando conectar al servidor...")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print(f"[CLIENTE] Conexión establecida con {HOST}:{PORT}")

                mensaje = {
                    "juego": juego,
                    "datos": datos
                }

                # Enviar los datos como JSON
                s.sendall(json.dumps(mensaje).encode())
                print(f"[CLIENTE] Datos enviados: {mensaje}")

                # Recibir la respuesta del servidor
                respuesta = s.recv(1024).decode()
                print(f"[CLIENTE] Respuesta del servidor: {respuesta}")

                # Llamar al callback con la respuesta, si existe
                if callback:
                    callback(respuesta)

        except Exception as e:
            print(f"[ERROR] {e}")

    # Ejecutamos la tarea en un hilo separado
    hilo = threading.Thread(target=tarea, daemon=True)
    hilo.start()

    # Asegurarnos de que el hilo termine antes de cerrar el programa
    hilo.join()
