from flask import Flask, render_template, request, redirect, session, jsonify
import json

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Leer el archivo JSON
with open('archivo.json', 'r') as file:
    data = json.load(file)

# Ruta de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        # Verificar las credenciales
        if usuario == 'admin' and contrasena == 'admin':
            session['usuario'] = usuario
            return redirect('/principal')
        else:
            return render_template('login.html', mensaje='Credenciales incorrectas')
    return render_template('login.html')

# Ruta de la página principal
@app.route('/principal')
def principal():
    if 'usuario' in session:
        # Obtener los datos para la tabla
        datos_tabla = data['tabla']
        
        # Obtener los datos para el gráfico
        ubicaciones = {}
        for libro in datos_tabla:
            ubicacion = libro['ubicacion_editorial']
            if ubicacion in ubicaciones:
                ubicaciones[ubicacion] += 1
            else:
                ubicaciones[ubicacion] = 1

        # Preparar datos para el gráfico
        ubicaciones_data = [{'ubicacion': key, 'cantidad': value} for key, value in ubicaciones.items()]

        # Convertir los datos a una cadena JSON
        datos_json = json.dumps(ubicaciones_data)

        return render_template('principal.html', datos=datos_tabla, datos_json=datos_json)
    else:
        return redirect('/')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)