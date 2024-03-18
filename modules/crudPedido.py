import os
import re
from tabulate import tabulate
from datetime import datetime
import json
import requests
import modules.getGamas as gG
import modules.getPedido as Pe
import modules.validaciones as vali
def postProducto():
     

    Pedido = {
            "codigo_pedido": input("Ingrese el codigo del pedido: "),
            "fecha_pedido": input("Ingrese el nombre del pedido: "),
            "fecha_esperada": input("Ingrese la fecha esperada"),
            "fecha_entrega": input("Ingrese la fecha de entrega "),
            "estado": input("Ingrese el estado del pedido: "),
            "comentario": input("Ingrese el comentario del pedido: "),
            "codigo_cliente": int(input("Ingrese la codigo del cliente: ")),
}
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.100.120:50004",headers=headers, data=json.dumps(Pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]
def getAllDataPedido():
    #json-server storage/pedido.json -b 5503
    peticion = requests.get("http://localhost:5503/pedidos")
    data = peticion.json()
    return data 

def nuevoCodigoPedido():
    codigodelCliente = list()
    for val in getAllDataPedido():
        codigodelCliente.append(val.get("codigo_pedido"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1

def postPedido():
    pedido = dict()
    while True:
        try:
            codigoPedido = nuevoCodigoPedido()
            pedido["codigo_pedido"] = codigoPedido

            if(not pedido.get("fecha_pedido")):
                fechaPeido = input("Ingrese la fecha del pedido: ")
                if(vali.validacionFecha(fechaPeido) is not None):
                    pedido["fecha_pedido"] = fechaPeido
                else:
                    raise Exception("La fehca no cumple con lo establecido")
                
            if(not pedido.get("fecha_esperada")):
                fechaEntrega = input("Ingrese la fecha de espera: ")
                if(vali.validacionFecha(fechaEntrega) is not None):
                    pedido["fecha_esperada"] = fechaEntrega
                else:
                    raise Exception("La fehca no cumple con lo establecido")
                
            fechaEntregada = input("Ingrese la fehca entregada: ")
            if(not pedido.get("fecha_entrega")):
                pedido["fecha_entrega"] = fechaEntregada

            if(not pedido.get("estado")):
                estado = input("Ingrese el estado del pedido: ")
                if(vali.validacionNombre(estado) is not None):
                    pedido["estado"] = estado
                else:
                    raise Exception("El estado del pedido no cumple con lo establecido")            

            comentario = input("Ingrese un comentario: ")
            if(not pedido.get("comentario")):
                pedido["comentario"] = comentario

            if(not pedido.get("codigo_cliente")):
                codigocliente = input("Ingrese el codigo del cliente: ")
                if(vali.validacionNumerica(codigocliente) is not None):
                    codigocliente = int(codigocliente)
                    pedido["codigo_cliente"] = codigocliente
                    break
                else:
                    raise Exception("El codigo del cliente no cumple con lo establecido")     

        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5503/pedidos", headers=headers, data=json.dumps(pedido))
    res = peticion.json()
    res["Mensaje"] = "Pedido Agregado"
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
  ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____                             
 / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                             
/ /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                              
\__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                               
            /_/                                                                                                                      
                                                                                                                                                    
            1. Guardar un pedido nuevo
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 1):
                if(opcion == 1):
                
                    print(tabulate(postProducto(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    break
                
                elif(opcion == 0):
                    break 