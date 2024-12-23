

# Clase GestorDeDatosClimaticos para manejar el flujo de datos y presentación

import json
from clases.localizador import Localizador
from base_de_datos import base_de_datos

class GestorDeDatosClimaticos:

    ubicaciones = []


    def __init__(self):
        self.bd = base_de_datos.basedatos() #crear un tipo de variable de la clase base de datos que es la que está creada en bd.py
       # self.bd.vaciarcoleccion() #(esta funcion sirve para depurar)
        print("Iniciando gestor de datos climaticos")
        self.ubicaciones = self.bd.pedirdatos() #pedir los datos del mongo
        print(f"Numero de ubicaciones actuales: {self.get_numero_ubicaciones()}")
    def get_numero_ubicaciones(self):
        return len(self.ubicaciones)

    def mostrar_codigos_postales_y_provincias_almacenadas(self):
        provincias_codigos_postales = {}
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia in provincias_codigos_postales:
                provincias_codigos_postales[ubicacion.provincia].append(ubicacion.codigo_postal)
            else:
                provincias_codigos_postales[ubicacion.provincia] = [ubicacion.codigo_postal]

        if provincias_codigos_postales:
            print(json.dumps(provincias_codigos_postales, indent=2, ensure_ascii=False))
        else:
            print("No hay ubicaciones almacenadas")

    # metodos necesarios
    def insertar_nueva_ubicacion(self,latitud, longitud):
        ubicacion_encontrada = False
        for ubicacion in self.ubicaciones:
            if ubicacion.check_lat_lng(latitud, longitud):
                ubicacion_encontrada = True
                print("================================================")
                print("Ubicación ya existe")
                print(ubicacion.mostrar_informacion())
                print("================================================")
                break
        
        if not ubicacion_encontrada:
            p=Localizador(latitud, longitud) # con esto obtenemos la ciudad, cp, barrio; a través de la clase localizador dandoles solo la lat y long
            self.ubicaciones.append(p) # añadir lo uqe esta alamacenado en p a la lista de ubicaciones
            tabla = p.to_dict() #con esto creamos una variable que la convertimos a tabla hash para despues insertarla en la bd
            self.bd.insert(tabla)
            self.bd.printbd()
            # almacenar en base de datos la tabla has de la clase p
            print("Ubicación agregada correctamente")
        else:
            print("Ubicación ya existe")
        return ubicacion_encontrada

    def buscar_por_codigo_postal(self,codigo_postal):
        ubicacion_encontrada = None
        for ubicacion in self.ubicaciones:
            if ubicacion.codigo_postal == codigo_postal:
                ubicacion_encontrada = ubicacion
                break
        return ubicacion_encontrada
    
    def buscar_por_provincia(self,provincia):
        lista_ubicaciones = []
        for ubicacion in self.ubicaciones:
            if ubicacion.provincia == provincia:
                lista_ubicaciones.append(ubicacion)
        return lista_ubicaciones