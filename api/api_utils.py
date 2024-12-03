import requests


ABUSEIPDB_API_KEY = '0676c04dabf7b8641a7760b132d39bf3a4813a2ca49cd215d7accc8813ea9cf1a4e5f39c88d65839'
IPSTACK_API_KEY = '8eb1aab27b0ab5a04703673adf5013f7'

def obtener_datos_abuseipdb(ip):
    url = 'https://api.abuseipdb.com/api/v2/check'
    params = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    headers = {
        'Key': ABUSEIPDB_API_KEY,
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def obtener_datos_ipstack(ip):
    url = f'http://api.ipstack.com/{ip}'
    params = {
        'access_key': IPSTACK_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()