import socket

HOST = "127.0.0.1"
PORT = 65432

def iniciarcliente():
    with    socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client: 
        client.connect((HOST,PORT))
        print("Conexión establecida")
        while True:
            numero= int(input("Selecciona una opción:\n1. Hacer un pedido\n2. Ver el estado de mi pedido\n3. Ver menú\n4. Ver el precio de mi pedido\n5. Salir\n\n"))
            if numero == 1:
                nombre = input("Indique su nombre: ")
                elementopedido = input("Indique que quiere en su pedido separado por comas: ")
                client.sendall(f"hacer pedido_{nombre}_{elementopedido}".encode("utf-8"))
                respuesta = client.recv(1024).decode("utf-8")
                print("\n"+respuesta+"\n")
            
            elif numero == 2:
                nombre = input("Introduce el nombre al que está hecho el pedido: ")
                client.sendall(f"ver pedido_{nombre}".encode("utf-8"))
                respuesta = client.recv(1024).decode("utf-8")
                print("\n"+respuesta+"\n")
            
            elif numero == 3:
                client.sendall("ver menú".encode("utf-8"))
                menu = client.recv(1024).decode("utf-8")
                print ("\n"+ menu+"\n")
            
            elif numero == 4:
                nombre = input("Introduce el nombre al que está hecho el pedido: ")
                client.sendall(f"ver total_{nombre}".encode("utf-8"))
                respuesta = client.recv(1024).decode("utf-8")
                print("\n"+respuesta+"\n")

            elif numero == 5:
                client.sendall("salir".encode("utf-8"))
                print("cerrando conexión")
                client.close()
                break
            else: 
                print("Opción no válida")
            client.sendall("Hola".encode("utf-8"))

if __name__ == "__main__":
    iniciarcliente()