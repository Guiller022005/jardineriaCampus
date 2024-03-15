import os
from tabulate import tabulate
import json
import requests
import modules.postEmpleado as pstEmpleado

def postEmpleado():
    empleado = {
            "codigo_empleado": input("Ingrese el codigo del empleado: "),
            "nombre": input("Ingrese el nombre del empleado: "),
            "Cargo": input("Ingrese el puesto"),
            "apellido1": input("Ingrese el primer apellido: "),
            "apellido2": input("Ingrese el segundo apellido: "),
            "extension": input("Ingrese la extension del empleado: "),
            "email": int(input("Ingrese el email del empleado: ")),
            "codigo_oficina": int(input("Ingrese el codigo de oficina: ")),
            "codigo_jefe": int(input("Ingrese el codigo del jefe del empleado: "))
    }
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.111:50003",headers=headers, data=json.dumps(empleado, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""  
    ___       __          _       _      __                         __      __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/_  \__,_/_/     _\__,_/\__,_/\__/\____/____/  
      ____/ /__     / ____/___ ___  ____  / /__  ____ _____/ /___  _____                  
     / __  / _ \   / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/                  
    / /_/ /  __/  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  )                   
    \__,_/\___/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/                    
                                /_/                                                       
                                                                                                                                                    
            1. Guardar un producto nuevo
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            
            print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
            input("Presione una tecla para continuar......")
            break
        elif(opcion == 0):
            break 