from geopy.geocoders import Nominatim

from clases.clima import Clima



# Clase para obtener la dirección a partir de la latitud y longitud usando Nominatim
class Localizador:

    latitud = None
    longitud = None
    direccion =None
    ciudad=None
    barrio=None
    provincia=None
    estado=None
    pais=None
    codigo_postal=None
    clima=None

    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.__obtener_direccion()
        self.clima = Clima(self.latitud, self.longitud)

    def to_dict(self):
        return{
            "latitud":self.latitud,
            "longitud":self.longitud,
            "direccion":self.direccion,
            "ciudad":self.ciudad,
            "barrio":self.barrio,
            "provincia":self.provincia,
            "estado":self.estado,
            "pais":self.provincia,
            "codigo_postal":self.codigo_postal,
            "clima":self.clima.to_dict()
        }

    def __obtener_direccion(self):
        try:
            geolocator = Nominatim(user_agent="test")
            location = geolocator.reverse(f"{self.latitud}, {self.longitud}")
            # rellenamos los datos normales
            self.direccion = location.address if location else "Dirección no encontrada"
            # rellenamos los datos extra
            try:
                self.barrio = location.raw['address']['suburb'] if 'suburb' in location.raw['address'] else None
                self.ciudad = location.raw['address']['city'] if 'city' in location.raw['address'] else None
                self.provincia = location.raw['address']['province'] if 'province' in location.raw['address'] else None
                self.estado = location.raw['address']['state'] if 'state' in location.raw['address'] else None
                self.pais = location.raw['address']['country'] if 'country' in location.raw['address'] else None
                self.codigo_postal = location.raw['address']['postcode'] if 'postcode' in location.raw['address'] else None
            except:
                pass
        except Exception as e:
            print(f"Error al obtener la dirección: {e}")
            self.direccion = "Error al obtener la dirección"
        
    def check_lat_lng(self, latitud, longitud):
        if self.latitud == latitud:
            if self.longitud == longitud:
                return True
            else:
                return False
        else:
            return False

    def mostrar_informacion(self):
        info_localizador = (
            f"Localizador:\n"
            f"  Latitud: {self.latitud}\n"
            f"  Longitud: {self.longitud}\n"
            f"  Dirección: {self.direccion}\n"
            f"  Ciudad: {self.ciudad}\n"
            f"  Barrio: {self.barrio}\n"
            f"  Provincia: {self.provincia}\n"
            f"  Estado: {self.estado}\n"
            f"  País: {self.pais}\n"
            f"  Código postal: {self.codigo_postal}"
        )
        
        # Mostrar información del Localizador y del Clima
        print(info_localizador)
        print(self.clima)

# a = Localizador("42.86","-2.64")
# print(f"Direccion: {a.direccion}")
# print(f"Temperatura: {a.clima.temperatura}")
# print(f"Velocidad del viento: {a.clima.velocidad_viento}")