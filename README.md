# Monitoreo de Direcciones IP para Detección de Amenazas
Este proyecto permite monitorear direcciones IP sospechosas detectadas en logs de actividad para determinar patrones de comportamiento y posibles amenazas. La aplicación consume APIs externas para obtener información sobre las IPs, las clasifica según su reputación y muestra los datos en un dashboard interactivo.

Características
Conexión a las APIs de AbuseIPDB e ipstack.
Almacenamiento de datos en una base de datos MySQL.
Clasificación de IPs como "Confiables", "Sospechosas" o "Maliciosas".
Dashboard interactivo con mapa geográfico utilizando Leaflet.js.
Generación de alertas visuales y envío opcional de notificaciones por correo electrónico.

Tecnologías Utilizadas:
-Python 3
-Flask
-MySQL
-Leaflet.js
-APIs de AbuseIPDB e ipstack

Instalación
Requisitos previos:
-Python 3.8 o superior
-MySQL
-Claves API de AbuseIPDB e ipstack
-Git

Pasos de instalación:
1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/monitoreo-ips.git
2. Navega al directorio del proyecto:
    ```bash
    cd monitoreo-ips
3. Crea y activa un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
5. Configura las claves API:
 Crea un archivo api/api_keys.py (este archivo está en el .gitignore para no subirlo al repositorio).
 Añade tus claves API:
   ```bash
      # api/api_keys.py
      ABUSEIPDB_API_KEY = 'TU_ABUSEIPDB_API_KEY'
      IPSTACK_API_KEY = 'TU_IPSTACK_API_KEY'
6. Configura la base de datos:
 Crea la base de datos y la tabla ejecutando el script SQL proporcionado en database/db_schema.sql (crea este archivo con el 
 script SQL).
 Actualiza las credenciales de la base de datos en database/db_utils.py.
 7. Ejecuta el análisis de IPs:
    ```bash
    python main.py
8. Inicia la aplicación web:
    ```bash
   python app.py
9. Accede al dashboard en tu navegador:
    ```bash
    http://localhost:5000


MIT License
