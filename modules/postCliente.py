import os
from tabulate import tabulate
import json
import requests
import modules.postCliente as pstClient

def postCliente():
    cliente = {
            "codigo_cliente": input("Ingrese el codigo del cliente: "),
            "nombre": input("Ingrese el nombre del cliente: "),
            "nombre_contacto": input("Ingrese el nombre de contacto"),
            "apellido_contacto": input("Ingrese el apellido de contacto: "),
            "telefono": input("Ingrese el numero de telefono: "),
            "fax": input("Ingrese el numero de fax: "),
            "linea_direccion1": int(input("Ingresa la linea de direccion 1: ")),
            "linea_direccion2": int(input("Ingresa la linea de direccion 2: ")),
            "ciudad": int(input("Ingrese la ciudad: ")),
            "region": int(input("Ingrese la region: ")),
            "pais": int(input("Ingrese el pais: ")),
            "codigo_postal": int(input("Ingrese el codigo postal: ")),
            "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del empleado de ventas: ")),
            "limite_credito": int(input("Ingrese el limite de credito: "))
    }
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.111:50001",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
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
      ____/ /__     _____/ (_)__  ____  / /____  _____                                    
     / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \/ ___/                                    
    / /_/ /  __/  / /__/ / /  __/ / / / /_/  __(__  )                                     
    \__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/____/                                      
                                                                                                                                                                                      
            1. Guardar un producto nuevo
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            
            print(tabulate(postCliente(), headers="keys", tablefmt="github"))
            input("Presione una tecla para continuar......")
            break
        elif(opcion == 0):
            break 