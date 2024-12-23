from pymongo import MongoClient
from clases.localizador import Localizador

# lo que hacemos en la base de datos es definir cada una de las funciones
# hay que crear una clase que encapsula las operaciones relacionadas con la bd
class basedatos: 
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/') # con esot iniciamos la bd
        self.dbname = "localizaciones" # con esto asignamos un nombre a la bd
        self.collectionname = "info"
        print("base de datos creada")

    
    def numerolocalizaciones(self):
        bd = self.client[self.dbname][self.collectionname] #accedemos a las localizaaciones y lo alacenamos en la bd
        numerototal = bd.count_documents({}) # estamos contando el numero de locaclizaciones y lo estamos almacenando en una variable
        return numerototal # devuelve esa variable con la información
    
    #es una funcion que lo que hace es insertar la ubicacion
    def insertarubicacion(self,localizacion):
        self.client[self.dbname][self.collectionname].insert_one(localizacion)

    
    # definir la funcion de buscar por latitud y longitud 
    def buscarporlatlong(self,latitud,longitud):
        resultado = self.client[self.dbname][self.collectionname].find_one({"latitud":latitud,"longitud":longitud}) #que busque en la base de datos si ya está una localcizacion con esa lati y long
        if (resultado!=None): # si no está en la bd, que se almacene en la bd y si ya existe, que devuelva None
            localizacion = Localizador(resultado["latitud"],resultado["longitud"])
            return localizacion
        else: 
            return None
    
    #funcion buscar por codigo postal
    def buscarporcp(self,codigopostal):
        resultado = self.client[self.dbname][self.collectionname].find({"codigo_postal":codigopostal})
        if(resultado!=None):
            localizaciones = [] #hemos creado una lista que almacenará todas las ubicaciones que comparten provincia
            # creamos un bucle for para que recorra la lista 
            for ubicacion in resultado:
                localizacion = Localizador(ubicacion["latitud"],ubicacion["longitud"])
                localizaciones.append(localizacion) # con el comando append lo que hacemos es añadir los elementos a la lista
            return localizaciones
        else:
            return None
        
    #funcion buscar por provincia
    def buscarporprov(self,provincia):
        resultado = self.client[self.dbname][self.collectionname].find({"provincia":provincia})
        if(resultado!=None):
            localizaciones = [] #hemos creado una lista que almacenará todas las ubicaciones que comparten provincia
            for ubicacion in resultado:
                localizacion = Localizador(ubicacion["latitud"],ubicacion["longitud"])
                localizaciones.append(localizacion)
            return localizaciones
        else:
            return None
    

    #función obtener localizaciones
    def obtenerlocalizaciones(self):
        localizaciones = self.client[self.dbname][self.collectionname].find({})
        localizaciones_lista = list(localizaciones) # convertimos localizaciones_lista a una lista
        return localizaciones_lista
    
     #con esta funcion lo que hacemos es eliminar todo lo que hay en localizaciones-info
    def vaciarcoleccion(self):
        bd = self.client[self.dbname][self.collectionname]
        bd.delete_many({})

