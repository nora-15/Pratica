from pymongo import MongoClient
from clases.localizador import Localizador
class basedatos: 
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.dbname = "localizaciones"
        self.collectionname = "info"
        print("base de datos creada")

    def insert(self,localizacion):
        self.client[self.dbname][ self.collectionname ].insert_one(localizacion) # con esto, lo que hace es insertar la tabla en el database del mongo

# ahora vamos a crear otra de las funciones que hay  que es la de que nos muestre una lista con las ubicaciones que hay
    def printinfo(self):
        print(self.client.list_database_names) # con esto nos saldrá una lista con lo que hay en la bd

    def printbd(self):
       bd = self.client[self.dbname][ self.collectionname ].find({})
       for localizacion in bd:
            print("latitud: ",localizacion["latitud"])
            print("longitud: ",localizacion["longitud"])
            print("direccion: ",localizacion["direccion"])
            print("ciudad: ",localizacion["ciudad"])
            print("barrio: ",localizacion["barrio"])
            print("provincia: ",localizacion["provincia"])
            print("estado: ",localizacion["estado"])
            print("pais: ",localizacion["pais"])
            print("codigo postal: ",localizacion["codigo_postal"])
            print("temperatura: ",localizacion["clima"]["temperatura"])
            print("velocidad del viento: ",localizacion["clima"]["velocidad_viento"])
            print("")
    
    
    def pedirdatos(self):
        info = self.client[self.dbname][self.collectionname].find({}) #con esto lo que hacemos es encontrar la informacion que ya está en la database y almacenarla en una variable

#queremos devolver una lista  con esa informacion, solo queremos que devuelva la latitud y longitud para que no haya mucha info, y como ya hay otra funcion que al "mencionar" la lat y long, nos darán los demás datos
        listaubicaciones = [] 
        for localizacion in info: 
            latitud = localizacion["latitud"]
            longitud = localizacion["longitud"]

            loc = Localizador(latitud,longitud)
            listaubicaciones.append(loc)
        #print("localizaciones iniciales",listaubicaciones)
        return listaubicaciones
    
    #con esta funcion lo que hacemos es eliminar todo lo que hay en localizaciones-info
    def vaciarcoleccion(self):
        bd = self.client[self.dbname][self.collectionname]
        bd.delete_many({})