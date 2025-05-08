import socket
import threading
import json
from modelos import Base, engine, Session, ResultadoNReinas, ResultadoCaballo, ResultadoHanoi

# Crear las tablas automáticamente si no existen
Base.metadata.create_all(bind=engine)

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

def manejar_cliente(conn, addr):
    print(f"[+] Conexión aceptada de {addr}")
    session = Session()

    try:
        with conn:
            while True:
                data = conn.recv(4096)
                if not data:
                    break

                # Imprimir los datos recibidos
                print(f"[Servidor] Datos recibidos: {data.decode()}")
                
                mensaje = json.loads(data.decode())

                juego = mensaje.get("juego")
                datos = mensaje.get("datos")

                print(f"[{addr}] Datos recibidos para juego: {juego} -> {datos}")

                # Manejo de los diferentes juegos
                if juego == "nreinas":
                    resultado = ResultadoNReinas(**datos)
                    session.add(resultado)
                elif juego == "caballo":
                    resultado = ResultadoCaballo(**datos)
                    session.add(resultado)
                elif juego == "hanoi":
                    # Ajusta los datos según los campos de ResultadoHanoi
                    resultado = ResultadoHanoi(discos=datos["discos"], movimientos=datos["movimientos"], resuelto=datos["resuelto"])
                    session.add(resultado)
                else:
                    print(f"[!] Juego desconocido: {juego}")
                    continue

                session.commit()  # Guardar en la base de datos
                conn.sendall(b"Resultado guardado correctamente")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        session.close()
        print(f"[-] Conexión cerrada con {addr}")

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[+] Servidor escuchando en {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
            hilo.start()

if __name__ == "__main__":
    iniciar_servidor()
