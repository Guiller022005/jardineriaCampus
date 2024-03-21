import os
import requests
import json
from datetime import datetime


def getAllgama():
    #json-server storage/empleado.json -b 50003
    peticion = requests.get("http://172.16.100.111:50007/gama")
    data = peticion,json()
    return data

def getAllNombre():
    gamaNombre = []
    for val in getAllgama():
        gamaNombre.append(val.get("gama"))
    return gamaNombre