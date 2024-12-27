# Esquema con los elementos de cada clase:
# Hay 4 clases:
# Clase Plato, que contiene Nombre, Precio y Categoría
# Clase Pedido, que contiene Cliente, lista de platos y Estado (Pendiente, Preparando y Entregado)
# Clase Cliente, que contiene Nombre y Pedidos (lista de pedidos)
# Clase Restaurante, que contiene Menú (lista de platos) y Pedidos (lista de pedidos)



# Clase Plato
class Plato:

    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria  # 'Comida' o 'Bebida'

    def __str__(self):
        return f"{self.nombre} - {self.categoria} - ${self.precio}"


# Clase Pedido
class Pedido:

    def __init__(self, cliente):
        self.cliente = cliente
        self.lista_de_platos = []
        self.estado = "Pendiente"  # Estados: Pendiente, Preparando, Entregado

    def agregar_plato(self, plato):
        # TODO: Implementar la lógica para agregar un plato al pedido
        self.lista_de_platos.append(plato)
        print("agregar_plato")

    def cambiar_estado(self, nuevo_estado):
        # TODO: Implementar la lógica para cambiar el estado del pedido
        # Hay que tener en cuenta que el estado al que se cambie, sea uno de los tres que hay, para ello hay que hacer una condición
        lista_estado = ["Pendiente","Preparando","Entregado"]
        if nuevo_estado in lista_estado: 
            self.estado = nuevo_estado
            print("cambiar_estado")
        else:
            print("Los estados disponibles son Pendiente, Preparando o Entregado")

    def calcular_total(self):
        # TODO: Implementar la lógica para calcular el total del pedido
        # hay que inicializar una variable a cero, que alamcenará el resultado total 
        preciototal = 0
        for plato in self.lista_de_platos:
            preciototal = preciototal + plato.precio # con plato.precio,lo que hace es "ir directamente" al objeto tipo precio
        print(f"El precio total del pedido es {preciototal} euros")
        
        print("calcular_total")

    def __str__(self):
        return f"Pedido de {self.cliente.nombre} - Estado: {self.estado}"


# Clase Cliente
class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []

    def hacer_pedido(self, pedido):
        # TODO: Implementar la lógica para hacer un pedido
        self.pedidos.append(pedido)
        print("hacer_pedido")

    def ver_pedidos(self):
        # TODO: Implementar la lógica para ver los pedidos del cliente
        #puede ser que la lista esté vacía, por eso, hay que unsar un condicional.
        # la función len nos permite saber la longitud de la lista, y si es igual a 0; que imprima en consola "no tiene pedidos"
        if len(self.pedidos) == 0: 
            print(f"{self.nombre} no tiene pedidos")
        
        # por el contrario, hay que hacer un bucle para que recorra la lista "pedidos"; pero como self.pedido tiene la lista de platos,
        # hay que hacer otro bucle para que recorra esa lista con todos los platos. (dentro de la lista de platos, se ecuentra "plato")
        else:
            for pedido in self.pedidos:
                print(pedido)
                for plato in pedido.lista_de_platos:   
                    print(f"    {plato}")
        
        print("ver_pedidos")


# Clase Restaurante
class Restaurante:

    def __init__(self):
        self.menu = []
        self.pedidos = []

    def agregar_plato_al_menu(self, plato):
        # TODO: Implementar la lógica para agregar un plato al menú
        self.menu.append(plato)
        print("agregar_plato_al_menu")

    def registrar_pedido(self, pedido):
        # TODO: Implementar la lógica para registrar un pedido en el restaurante
        self.pedidos.append(pedido)
        print("registrar_pedido")

    def actualizar_estado_pedido(self, cliente, nuevo_estado):
        # TODO: Implementar la lógica para actualizar el estado del pedido de un cliente
        # lo primero, hay que centrarse en el cliente, para eso con el bucle "for" nos dirigimos al elemento de "pedidos"
        # ese elemento es una lista que contiene "pedido"
        for pedido in self.pedidos:
            if pedido.cliente == cliente: # si el cliente de la clase pedido es igual a clase cliente (que tiene como atributos nombre y pedidos)
                pedido.cambiar_estado(nuevo_estado) # la funcion cambiar_estado de la clase pedido; actualizarla a nuevo_estado
                print(f"Estado  del pedido de {cliente.nombre} actualizado a {nuevo_estado}")
        print("actualizar_estado_pedido")

    def ver_menu(self):
        # TODO: Implementar la lógica para ver el menú del restaurante
        print("     MENU    ")
        for plato in self.menu: # para cada plato del elemento "menu" (con lista_de_platos) de la clase restaurante, imprimir en consola plato
            print(plato)  
        print("ver_menu")


if __name__ == '__main__':
    # Ejemplo de uso del sistema
    # Crear el restaurante
    restaurante = Restaurante()
    
    # Crear platos
    plato1 = Plato("Hamburguesa", 8.50, "Comida")
    plato2 = Plato("Refresco", 2.00, "Bebida")
    plato3 = Plato("Pizza", 12.00, "Comida")
    
    # Agregar platos al menú
    restaurante.agregar_plato_al_menu(plato1)
    restaurante.agregar_plato_al_menu(plato2)
    restaurante.agregar_plato_al_menu(plato3)
    
    # Crear clientes
    cliente1 = Cliente("Carlos")
    cliente2 = Cliente("Lucía")
    
    # Crear pedidos
    pedido1 = Pedido(cliente1)
    pedido1.agregar_plato(plato1)
    pedido1.agregar_plato(plato2)
    cliente1.hacer_pedido(pedido1)
    pedido2 = Pedido(cliente2)
    pedido2.agregar_plato(plato3)
    
    # Registrar pedidos en el restaurante
    restaurante.registrar_pedido(pedido1)
    restaurante.registrar_pedido(pedido2)
    
    # Cambiar el estado del pedido de un cliente
    restaurante.actualizar_estado_pedido(cliente1, "Preparando")
    
    # Ver menú
    restaurante.ver_menu()
    
    # Cliente ve sus pedidos
    cliente1.ver_pedidos()
    cliente2.ver_pedidos()
