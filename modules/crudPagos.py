import os
from tabulate import tabulate
import json
import requests
import modules.crudPagos as pstPagos
import modules.validaciones as vali
def postPagos():
    cliente = {
            "codigo_cliente": input("Ingrese el codigo del cliente: "),
            "forma_pago": input("Ingrese la fecha del pedido: "),
            "id_transaccion": input("Ingrese la fecha esperada"),
            "fecha_pago": input("Ingrese la fecha de entrega: "),
            "total": input("Ingrese el estado del pedido: "),
    }
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.120:50005",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]
def getAllDataPagos():
    #json-server storage/pago.json -b 5504
    peticion = requests.get("http://localhost:5504/pagos")
    data = peticion.json()
    return data 

def postPagos():
    pago = dict()
    while True:
        try:
            if(not pago.get("codigo_cliente")):
                codigocliente = input("Ingrese el codigo del cliente: ")
                if(vali.validacionNumerica(codigocliente) is not None):
                    codigocliente = int(codigocliente)
                    pago["codigo_cliente"] = codigocliente
                else:
                    raise Exception("El codigo del cliente no cumple con lo establecido")  

            if(not pago.get("forma_pago")):
                formaPago = input("Ingrese la forma de pago: ")
                if(vali.validacionNombre(formaPago) is not None):
                    pago["forma_pagoado"] = formaPago
                else:
                    raise Exception("La forma de pago no cumple con lo establecido")  
                
            if(not pago.get("id_transaccion")):
                idTransaccion = input("Ingrese la id de la transaccion: ")
                if(vali.validaiconTransccion(idTransaccion) is not None):
                    pago["id_transaccion"] = idTransaccion
                else:
                    raise Exception("La id de la transaccion no cumple con lo establecido")
                
            if(not pago.get("fecha_pago")):
                fechaPago = input("Ingrese la fecha de pago: ")
                if(vali.validacionFecha(fechaPago) is not None):
                    pago["fecha_pago"] = fechaPago
                else:
                    raise Exception("La fehca no cumple con lo establecido") 

            if(not pago.get("total")):
                total = input("Ingrese el total del pago: ")
                if(vali.validacionNumerica(total) is not None):
                    total = int(total)
                    pago["total"] = total
                    break
                else:
                    raise Exception("El pago no cumple con lo establecido")   
                
        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5504/pagos", headers=headers, data=json.dumps(pago))
    res = peticion.json()
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