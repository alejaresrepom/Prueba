import json

# Leer el archivo JSON
with open('archivo.json', 'r') as file:
    data = json.load(file)

# Agregar coordenadas a cada documento
for documento in data['tabla']:
    # Asignar las coordenadas según el nombre de la editorial
    if documento['nombre_editorial'] == 'Minotauro':
        documento['coordenadas_editorial'] = {'latitud': 40.4168, 'longitud': -3.7038}  # España
    elif documento['nombre_editorial'] == 'Diana':
        documento['coordenadas_editorial'] = {'latitud': 4.710989,'longitud': -74.072092}  # Colombia
    elif documento['nombre_editorial'] == 'Secker & Warburg':
        documento['coordenadas_editorial'] = {'latitud': 51.5074, 'longitud': -0.1278}  # Reino Unido
    elif documento['nombre_editorial'] == 'Harper & Brothers':
        documento['coordenadas_editorial'] = {'latitud': 40.7128, 'longitud': -74.006}  # Estados Unidos
    elif documento['nombre_editorial'] == 'Thomas Egerton':
        documento['coordenadas_editorial'] = {'latitud': 51.5074, 'longitud': -0.1278}  # Reino Unido
    elif documento['nombre_editorial'] == "Charles Scribner's Sons":
        documento['coordenadas_editorial'] = {'latitud': 40.7128, 'longitud': -74.006}  # Estados Unidos
    elif documento['nombre_editorial'] == 'Francisco de Robles':
        documento['coordenadas_editorial'] = {'latitud': 40.4168, 'longitud': -3.7038}  # España
    elif documento['nombre_editorial'] == 'J. B. Lippincott & Co.':
        documento['coordenadas_editorial'] = {'latitud': 40.7128, 'longitud': -74.006}  # Estados Unidos
    elif documento['nombre_editorial'] == 'The Russian Messenger':
        documento['coordenadas_editorial'] = {'latitud': 55.7558, 'longitud': 37.6176}  # Rusia
    else:
        # Manejar otros casos si es necesario
        pass

# Guardar los cambios en el archivo JSON original
with open('archivo.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Coordenadas agregadas exitosamente al archivo JSON.")
