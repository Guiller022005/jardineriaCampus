import json
import requests

def getAllGama():
     #json-server storage/gama_producto.json -b 50002 
    peticion = requests.get("http://172.16.100.123:50002")
    data = peticion.json()
    return data

def getAllGama():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))