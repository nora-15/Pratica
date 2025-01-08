import socket
import threading
from clases import Plato,Pedido,Restaurante,Cliente

HOST = "127.0.0.1"
PORT = 65432
clientes =[]
restaurante = Restaurante()
menu = [["Hamburguesa", 8.50, "Comida"],["Refresco", 2.00, "Bebida"],["Pizza", 12.00, "Comida"]]
for elemento in menu:
    restaurante.agregar_plato_al_menu(Plato(elemento[0],elemento[1],elemento[2]))

def manejar_cliente(conn,addr):
    print("Conexión establecida")
    while True:
        try:
            mensaje = conn.recv(1024).decode("utf-8")
            if not mensaje:
                break
            separacion = mensaje.split("_")
            print(mensaje)
            respuesta = ""
            if separacion[0] == "hacer pedido":
                cliente = Cliente(separacion[1]) #creado un objeto de la clase cliente con el nombre psado en terminal
                pedido = Pedido(cliente) #creado un objeto de la clase pedido con el objeto cliente creado anteriormente
                listapedido = separacion[2].split(", ")
                existe = False
                for elemento in listapedido:
                    for item in menu:
                        if item[0] == elemento:
                            existe = True           
                            pedido.agregar_plato(Plato(item[0],item[1],item[2]))

                if existe == False:
                    respuesta = "El plato no está en el menú."
                else: 
                    cliente.hacer_pedido(pedido)
                    restaurante.registrar_pedido(pedido)
                    respuesta = "Pedido realizado" 

            if separacion[0] == "ver pedido":
                existe = False
                for pedido in restaurante.pedidos:
                    if pedido.cliente.nombre == separacion[1]:
                        respuesta = f"Pedido de {pedido.cliente.nombre} - Estado {pedido.estado}" 
                        
                        existe = True
                if existe == False:
                    respuesta = "El cliente no ha hecho ningún pedido."


            if separacion[0] == "ver menú":
                respuesta = restaurante.ver_menu()

            if separacion[0] == "ver total":
                existe = False
                for pedido in restaurante.pedidos:
                    if pedido.cliente.nombre == separacion[1]:
                        respuesta = pedido.calcular_total()
                        existe = True
                if existe == False:
                    respuesta = "El cliente no ha hecho ningún pedido."
            if separacion[0] == "salir":
                clientes.remove(conn)
            conn.sendall(respuesta.encode("utf-8"))
            print ("enviado")
        except Exception as e:
            print(f"[DESCONECTADO] {addr} desconectado")
            break
    conn.close()
    
def iniciarservidor():
    with    socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server: 
        server.bind((HOST,PORT))
        server.listen()
        print("Servidor escuchando")
        while True:
            conn,addr = server.accept()
            clientes.append(conn)
            thread = threading.Thread(target=manejar_cliente,args=(conn,addr))
            thread.start()
            thread.join()

if __name__ == "__main__":
    iniciarservidor()
