

# Ejemplo de uso
from gestor_de_datos.gestordatosclimaticos import GestorDeDatosClimaticos

def insertar_ubicacion(gestor):
    print("Introduce la latitud y longitud de la ubicación: ")
    lat = input("Latitud: ")
    lng = input("Longitud: ")
    
    ubicacion_encontrada = gestor.insertar_nueva_ubicacion(lat, lng)
    if not ubicacion_encontrada:
        print(f"La ubicación '{lat}, {lng}' insertada correctamente.")
    else:
        print(f"La ubicación '{lat}, {lng}' ya existe.")
    print(f"Numero de ubicaciones actualmente: {gestor.get_numero_ubicaciones()}")

def buscar_ubicacion(gestor):
    codigo_postal = input("Introduce el codigo postal que deseas buscar: ")
    
    # Buscar la ubicación en el diccionario
    ubicacion = gestor.buscar_por_codigo_postal(codigo_postal)
    if ubicacion:
        print(f"Ubicación encontrada: {ubicacion.mostrar_informacion()}")
    else:
        print("Ubicación no encontrada.")

def buscar_ubicaciones_por_provincia(gestor):
    provincia = input("Introduce la provincia que deseas buscar: ")
    
    # Buscar todas las ubicaciones que pertenecen a la provincia
    resultados = gestor.buscar_por_provincia(provincia)
    
    if resultados:
        print(f"Numero de ubicaciones en '{provincia}': {len(resultados)}")
        for ubicacion in resultados:
            ubicacion.mostrar_informacion()
    else:
        print(f"No se encontraron ubicaciones en '{provincia}'.")

def mostrar_codigos_postales_y_provincias_almacenadas(gestor):
    print("================================================")
    gestor.mostrar_codigos_postales_y_provincias_almacenadas()
    print("================================================")

if __name__ == "__main__":
    # Crear el gestor de datos y obtener la información
    gestor = GestorDeDatosClimaticos()
    while True:
        print("================================================================")
        print("\nMenú Principal")
        print("1. Insertar una ubicación")
        print("2. Buscar una ubicación")
        print("3. Buscar ubicaciones por provincia")
        print("4. Mostrar provincias y CP almacenados")
        print("Escribe 'exit' para salir.")
        
        opcion = input("Selecciona una opción: ").strip().lower()

        if opcion == '1':
            insertar_ubicacion(gestor)
        elif opcion == '2':
            buscar_ubicacion(gestor)
        elif opcion == '3':
            buscar_ubicaciones_por_provincia(gestor)
        elif opcion == '4':
            mostrar_codigos_postales_y_provincias_almacenadas(gestor)
        elif opcion == 'exit':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    
    




    