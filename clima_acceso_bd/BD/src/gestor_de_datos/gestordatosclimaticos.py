from pymongo import MongoClient

# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación


import json
from clases.localizador import Localizador
from base_de_datos import base_de_datos

# hay que crear una clase, en este caso gestor de datos climaticos, para gestionar los datos climaticos
class GestorDeDatosClimaticos:


    def __init__(self):
        self.bd = base_de_datos.basedatos() #con esto estamos creando una variable que se llama bd inicializada con la clase de basededatos
        # self.bd.vaciarcoleccion()
        print("Iniciando gestor de datos climaticos")
        print(f"Numero de ubicaciones actuales: {self.get_numero_ubicaciones()}")


    def get_numero_ubicaciones(self):
        loc = self.bd.numerolocalizaciones()
        return(loc)

    # con esta funcion lo que hacemos es mostrar los cp y provincias que hay en la bd
    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        listalocalizaciones = self.bd.obtenerlocalizaciones()
        provincias_codigos_postales = {}
        for ubicacion in listalocalizaciones:
            provincia = ubicacion["provincia"]
            codigopostal = ubicacion["codigo_postal"]
            if provincia in provincias_codigos_postales: # si la provincia está en la bd, añadimos el cp a la lista
                provincias_codigos_postales[provincia].append(codigopostal)
            # sino, creamos una nueva entrada con la provincia y el cp
            else:
                provincias_codigos_postales[provincia] = [codigopostal]

        if provincias_codigos_postales:
            print(json.dumps(provincias_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    # metodos necesarios
    def insertar_nueva_ubicacion(self,latitud, longitud):
        self.bd.buscarporlatlong(latitud,longitud)
        ubicacion_encontrada = self.bd.buscarporlatlong(latitud,longitud)
        if ubicacion_encontrada!= None:

                print("================================================")
                print("Ubicación ya existe")
                print("latitud: ", ubicacion_encontrada.latitud," longitud: ",ubicacion_encontrada.longitud," ciudad: ",ubicacion_encontrada.ciudad)
                print("================================================")
        else: 
            nuevalocalizacion=Localizador(latitud,longitud)#con esto obtenemos ciudad, cp, barrio; a traves de la clase localizador dandoles solo la long y lat
            
            tabla=nuevalocalizacion.to_dict()# y con esto, convertimos a tabla hash
            self.bd.insertarubicacion(tabla)
            #almacenar en la base de datos la tabla hash de la clase nuevalocalizacion
            print("Ubicación agregada correctamente")
 
            
        return ubicacion_encontrada

    def buscar_por_codigo_postal(self,codigo_postal):
        lista_ubicaciones = self.bd.buscarporcp(codigo_postal)
        return lista_ubicaciones
    
    def buscar_por_provincia(self,provincia):
        lista_ubicaciones = self.bd.buscarporprov(provincia)

        return lista_ubicaciones
    
