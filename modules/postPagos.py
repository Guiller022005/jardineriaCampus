import os
from tabulate import tabulate
import json
import requests
import modules.postPagos as pstPagos

def postPagos():
    cliente = {
            "codigo_cliente": input("Ingrese el codigo del cliente: "),
            "forma_pago": input("Ingrese la fecha del pedido: "),
            "id_transaccion": input("Ingrese la fecha esperada"),
            "fecha_pago": input("Ingrese la fecha de entrega: "),
            "total": input("Ingrese el estado del pedido: "),
    }
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.111:50005",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]
def menu():
    while True:
        os.system("clear")
        print("""  
    ___       __          _       _      __                         __      __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/  
      ____/ /__     / /___  _____   ____  ____ _____ _____  _____                         
     / __  / _ \   / / __ \/ ___/  / __ \/ __ `/ __ `/ __ \/ ___/                         
    / /_/ /  __/  / / /_/ (__  )  / /_/ / /_/ / /_/ / /_/ (__  )                          
    \__,_/\___/  /_/\____/____/  / .___/\__,_/\__, /\____/____/                           
                                /_/          /____/                                                                                          
                                                                                                                                                                                      
            1. Guardar un producto nuevo
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            
            print(tabulate(postPagos(), headers="keys", tablefmt="github"))
            input("Presione una tecla para continuar......")
            break
        elif(opcion == 0):
            break 