# Archivo: app.py
import pyodbc
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# Configuración de la conexión a SQL Server
server = 'BRENDA\SQLEXPRESS'
database = 'Asistencia'
username = 'cristian'
password = '123456'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Pagina principal
@app.route('/')
def index():
    return render_template('index.html')

# Pagina para marcar asistencia
@app.route('/registrar_asistencia')
def registrar_asistencia():
    materia = request.args.get('materia')
    return render_template('asistencia.html', materia=materia)

# Funcion para guardar asistencia
@app.route('/guardar_asistencia', methods=['POST'])
def guardar_asistencia_endpoint():
    nombre = request.form.get('nombre')
    materia = request.form.get('materia')
    
    if guardar_asistencia(nombre, materia):
        return jsonify({'mensaje': 'Asistencia registrada exitosamente'}), 200
    else:
        return jsonify({'mensaje': 'Error al registrar la asistencia'}), 500

# Funcion que guarda los datos en la DB
def guardar_asistencia(nombre, materia):
    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO Asistencia (nombre, materia, fecha)
            VALUES (?, ?, ?)
        ''', (nombre, materia, datetime.now().date()))
        
        conn.commit()
        conn.close()
        return True
    except pyodbc.Error as e:
        print(f"Error al registrar la asistencia: {e}")
        return False

if __name__ == '__main__':
    app.run(debug=True)
