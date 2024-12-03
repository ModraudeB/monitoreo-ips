from flask import Flask, render_template, request
from database.db_utils import obtener_conexion

app = Flask(__name__)

@app.route('/')
def index():
    estado = request.args.get('estado', 'Todos')
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    if estado == 'Todos':
        cursor.execute("SELECT * FROM ip_analysis")
    else:
        cursor.execute("SELECT * FROM ip_analysis WHERE classification = %s", (estado,))

    datos_ip = cursor.fetchall()
    cursor.close()
    conexion.close()
    return render_template('index.html', datos_ip=datos_ip, estado=estado)

if __name__ == '__main__':
    app.run(debug=True)
