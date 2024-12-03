import mysql.connector

def obtener_conexion():
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Eduardo178364162',
        database='db_ip'
    )
    return conexion
