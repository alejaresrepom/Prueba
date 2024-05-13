import json
import mysql.connector

# Paso 1: Conectar con la base de datos MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Registros2021*',
        database='db_libreria'
    )
    print("Conexión establecida con éxito")
except mysql.connector.Error as err:
    print(f"Error al conectar a MySQL: {err}")
    exit(1)

# Paso 2: Cargar datos desde el archivo JSON
try:
    with open('archivo.json') as f:
        data = json.load(f)
    print("Datos cargados exitosamente desde el archivo JSON")
except FileNotFoundError:
    print("El archivo JSON no se encontró")
    exit(1)
except json.JSONDecodeError:
    print("Error al decodificar el archivo JSON")
    exit(1)

# Paso 3: Insertar datos en la base de datPos
try:
    cursor = conn.cursor()
    for item in data['tabla']:
        query = """INSERT INTO tabla (
            id, titulo, autor_nombre, autor_nacionalidad, autor_fecha_nacimiento,
            autor_genero, nombre_editorial, ubicacion_editorial, isbn, precio,
            cantidad_stock, coordenadas_editorial
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, POINT(%s, %s))""" # Usamos POINT() para construir un objeto de geometría
        values = (
            item['id'], item['titulo'], item['autor_nombre'], item['autor_nacionalidad'],
            item['autor_fecha_nacimiento'], item['autor_genero'], item['nombre_editorial'],
            item['ubicacion_editorial'], item['isbn'], item['precio'], item['cantidad_stock'],
            item['coordenadas_editorial']['latitud'], item['coordenadas_editorial']['longitud']  # Extraemos latitud y longitud

        )
        cursor.execute(query, values)
    conn.commit()
    print("Datos insertados en la base de datos correctamente")
except mysql.connector.Error as err:
    print(f"Error al insertar datos en MySQL: {err}")
    conn.rollback()

# Paso 4: Cerrar la conexión con la base de datos
conn.close()