import requests

# Clase para obtener el clima (temperatura y velocidad del viento) de Open-Meteo
class Clima:

    latitud =None
    longitud =None
    temperatura =None
    velocidad_viento =None


    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
        self.__obtener_datos_climaticos()
        
    def to_dict(self):
        return{
            "latitud":self.latitud,
            "longitud":self.longitud,
            "temperatura":self.temperatura,
            "velocidad_viento":self.velocidad_viento,
        }

    def __str__(self):
        return (
            f"Clima:\n"
            f"  Latitud: {self.latitud}\n"
            f"  Longitud: {self.longitud}\n"
            f"  Temperatura: {self.temperatura}°C\n"
            f"  Velocidad del viento: {self.velocidad_viento} km/h")

    def __obtener_datos_climaticos(self):
        try:
            # URL de la API de Open-Meteo
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current_weather=true&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
            # Hacer la solicitud a la API
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200 and "current_weather" in data:
                current_weather = data["current_weather"]
                self.temperatura = current_weather["temperature"]
                self.velocidad_viento = current_weather["windspeed"]
            else:
                print("Error: No se pudieron obtener los datos climáticos.")
                self.temperatura, self.velocidad_viento = "Desconocido", "Desconocido"
        except Exception as e:
            print(f"Error al obtener los datos climáticos: {e}")
            self.temperatura, self.velocidad_viento = "Error", "Error"
        return self.temperatura, self.velocidad_viento


# a = Clima("42.86","-2.64")
# a.obtener_datos_climaticos()
