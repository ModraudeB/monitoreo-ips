from api.api_utils import obtener_datos_abuseipdb, obtener_datos_ipstack
from database.db_utils import obtener_conexion
import smtplib
from email.mime.text import MIMEText

# Lista de direcciones IP a analizar
lista_ips = [
    '8.8.8.8',
    '1.1.1.1',
    '201.20.20.20',
    '192.168.1.1',
    '172.16.0.1',
    '203.0.113.5',
    '198.51.100.23',
    '123.45.67.89',
    '98.76.54.32',
    '156.78.90.12'
]

# Función para clasificar la IP según el puntaje de riesgo
def clasificar_ip(risk_score):
    if risk_score >= 75:
        return "Maliciosa"
    elif risk_score >= 25:
        return "Sospechosa"
    else:
        return "Confiable"

# Función para almacenar los datos en la base de datos
def almacenar_datos(ip_info):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
    INSERT INTO ip_analysis (ip_address, country, city, latitude, longitude, risk_score, classification)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        country = VALUES(country),
        city = VALUES(city),
        latitude = VALUES(latitude),
        longitude = VALUES(longitude),
        risk_score = VALUES(risk_score),
        classification = VALUES(classification)
    """
    valores = (
        ip_info['ip_address'],
        ip_info['country'],
        ip_info['city'],
        ip_info['latitude'],
        ip_info['longitude'],
        ip_info['risk_score'],
        ip_info['classification']
    )
    cursor.execute(sql, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

# Función opcional para enviar notificación por correo electrónico
def enviar_notificacion(ip):
    mensaje = MIMEText(f'Se ha detectado una IP maliciosa: {ip}')
    mensaje['Subject'] = 'Alerta de Seguridad - IP Maliciosa Detectada'
    mensaje['From'] = 'tucorreo@dominio.com'       # Reemplaza con tu correo
    mensaje['To'] = 'admin@dominio.com'            # Reemplaza con el correo del administrador

    try:
        servidor = smtplib.SMTP('smtp.dominio.com', 587)  # Configura tu servidor SMTP
        servidor.starttls()
        servidor.login('tucorreo@dominio.com', 'tu_contraseña')  # Credenciales de tu correo
        servidor.send_message(mensaje)
        servidor.quit()
        print(f'Notificación enviada para la IP maliciosa: {ip}')
    except Exception as e:
        print(f'Error al enviar notificación: {e}')

# Función principal para analizar las IPs
def analizar_ips():
    for ip in lista_ips:
        print(f'Analizando IP: {ip}')
        try:
            datos_abuseipdb = obtener_datos_abuseipdb(ip)
            datos_ipstack = obtener_datos_ipstack(ip)

            # Extraer el puntaje de riesgo de la respuesta de AbuseIPDB
            risk_score = datos_abuseipdb['data']['abuseConfidenceScore']
            classification = clasificar_ip(risk_score)

            # Extraer datos geográficos de ipstack
            ip_info = {
                'ip_address': ip,
                'country': datos_ipstack.get('country_name', 'Desconocido'),
                'city': datos_ipstack.get('city', 'Desconocido'),
                'latitude': datos_ipstack.get('latitude'),
                'longitude': datos_ipstack.get('longitude'),
                'risk_score': risk_score,
                'classification': classification
            }

            # Almacenar datos en la base de datos
            almacenar_datos(ip_info)
            print(f"IP {ip} clasificada como {classification}")

            # Enviar notificación si la IP es maliciosa
            if classification == 'Maliciosa':
                enviar_notificacion(ip)

        except Exception as e:
            print(f'Error al analizar la IP {ip}: {e}')

if __name__ == '__main__':
    analizar_ips()
