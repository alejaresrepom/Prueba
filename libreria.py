import json
import mysql.connector

# Paso 1: Conectar con la base de datos MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Registros2021*',
        database='db_libreria',
        charset='utf8mb4',  # Usar utf8mb4 en lugar de utf8
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

# Paso 3: Insertar datos en las tablas de la base de datos
try:
    cursor = conn.cursor()
    for item in data['tabla']:
        # Insertar datos en la tabla 'autor'
        autor_query = """INSERT INTO autor (
            autor_nombre, autor_nacionalidad, autor_fecha_nacimiento
        ) VALUES (%s, %s, %s)"""
        autor_values = (
            item['autor_nombre'], item['autor_nacionalidad'], item['autor_fecha_nacimiento']
        )
        cursor.execute(autor_query, autor_values)
        
        # Insertar datos en la tabla 'editorial'
        editorial_query = """INSERT INTO editorial (
            nombre_editorial, ubicacion_editorial, coordenadas_editorial
        ) VALUES (%s, %s, POINT(%s, %s))"""
        editorial_values = (
            item['nombre_editorial'], item['ubicacion_editorial'],
            item['coordenadas_editorial']['latitud'], item['coordenadas_editorial']['longitud']
        )
        cursor.execute(editorial_query, editorial_values)
        
        # Insertar datos en la tabla 'libro'
        libro_query = """INSERT INTO libro (
            id, isbn, titulo, autor_nombre, autor_genero, nombre_editorial, cantidad_stock
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        libro_values = (
            item['id'], item['isbn'], item['titulo'], item['autor_nombre'],
            item['autor_genero'], item['nombre_editorial'], item['cantidad_stock']
        )
        cursor.execute(libro_query, libro_values)
        
    conn.commit()
    print("Datos insertados en las tablas de la base de datos correctamente")
except mysql.connector.Error as err:
    print(f"Error al insertar datos en MySQL: {err}")
    conn.rollback()

# Paso 4: Cerrar la conexión con la base de datos
conn.close()
