import os
from tabulate import tabulate
import json
import requests
import modules.postOficina as pstOficina

def postOficina():
    oficina = {
            "codigo_oficina": input("Ingrese el codigo del empleado: "),
            "ciudad": input("Ingrese el nombre del empleado: "),
            "pais": input("Ingrese el puesto"),
            "region": input("Ingrese el primer apellido: "),
            "codigo_postal": input("Ingrese el segundo apellido: "),
            "telefono": input("Ingrese la extension del empleado: "),
            "linea_direccion1": int(input("Ingrese el codigo de oficina: ")),
            "linea_direccion2": int(input("Ingrese el codigo del jefe del empleado: "))
    }
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.104.17:50002",headers=headers, data=json.dumps(oficina, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]


def menu():
    while True:
        os.system("clear")
        print("""  
    ___       __          _       _      __                         __      __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/_/_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/  
      ____/ /__     ____  / __(_)____(_)___  ____ _                                       
     / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/                                       
    / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ /                                        
    \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/                                         
                                                                                         
                                                                                                                                                    
            1. Guardar un producto nuevo
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            
            print(tabulate(postOficina(), headers="keys", tablefmt="github"))
            input("Presione una tecla para continuar......")
            break
        elif(opcion == 0):
            break 