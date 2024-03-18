import json
import requests

def getAllGama():
     #json-server storage/gama.json -b 50007 
    peticion = requests.get("http://172.16.103.34:50007/gama")
    data = peticion.json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllGama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre