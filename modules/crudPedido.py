import os
import re
from tabulate import tabulate
from datetime import datetime
import json
import requests
import modules.getGamas as gG
import modules.getPedido as Pe
import modules.validaciones as vali

def getAllDataPedido():
    #json-server storage/pedido.json -b 5503
    peticion = requests.get("http://172.16.100.111:50004/pedido")
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

def getCodigoPedido(codigo):
    peticion = requests.get(f"http://172.16.100.111:50004/pedido/{codigo}")
    return peticion.json() if peticion.ok else []

def updatePedido(id):
    data = getCodigoPedido(id)
    if(len(data)):
        print("Empleado Encontrado")
        print(tabulate([data], headers="keys", tablefmt="github"))
        data["codigo_pedido"] = data["codigo_pedido"]
        continuarActualizar = True     
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Fecha pedido 
                    2. Fecha espera
                    3. Fecha entrega
                    4. Estado
                    5. Comentario
                    6. Codigo del cliente
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 6):
                        if(opcion == 1):
                            while True:
                                try:
                                    fechaPedido = input("Ingrese la fecha del pedido: ")
                                    if(vali.validacionFecha(fechaPedido) is not None):
                                        data["fecha_pedido"] = fechaPedido
                                        break
                                    else:
                                        raise Exception("La fecha no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    fechaEspera = input("Ingrese la fecha de espera: ")
                                    if(vali.validacionFecha(fechaEspera) is not None):
                                        data["fecha_esperada"] = fechaEspera
                                        break
                                    else:
                                        raise Exception("La fecha no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    fechaEntregada = input("Ingrese la fehca entregada: ")
                                    if(vali.validacionFecha(fechaEntregada) is not None):
                                        data["fecha_entrega"] = fechaEntregada
                                        break
                                    else:
                                        raise Exception("La fecha no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    estado = input("Ingrese el estado del pedido: ")
                                    if(vali.validacionNombre(estado) is not None):
                                        data["estado"] = estado
                                        break
                                    else:
                                        raise Exception("El estado del pedido no cumple con lo establecido")            
                                except Exception as error:
                                    print(error)
                        if(opcion == 5):
                            while True:
                                try:
                                    comentario = input("Ingrese un comentario: ")
                                    data["comentario"] = comentario
                                    break
                                except Exception as error:
                                    print(error)
                        if(opcion == 6):
                            while True:
                                try:
                                    codigocliente = input("Ingrese el codigo del cliente: ")
                                    if(vali.validacionNumerica(codigocliente) is not None):
                                        codigocliente = int(codigocliente)
                                        data["codigo_cliente"] = codigocliente
                                        break
                                    else:
                                        raise Exception("El codigo del cliente no cumple con lo establecido")     
                                except Exception as error:
                                    print(error)
    
                        confirmacion = ""            
                        while (confirmacion !=  "s" and confirmacion != "n"):
                            confirmacion = input("Deseas cambiar mas datos?(s/n): ")
                            if vali.validacionSiNo(confirmacion):
                                if confirmacion == "n":
                                    continuarActualizar = False
                                    break
                                else:
                                    confirmacion == "s"
                                    break
                            else:
                                print("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)          
        
        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://172.16.100.111:50004/pedido/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        res["Mensaje"] = "Pedido Actualizado"
        return [res]
    else:
        return[{
            "messege": "Pedido no encontrado",
            "id": id
        }]


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
    peticion = requests.post("http://172.16.100.111:50004/pedido",headers=headers, data=json.dumps(Pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado"
    return [res]

def deletePedido(id):
    data = Pe.getPedidoCodigo(id)
    if(len(data)):
        peticion = requests.get(f"http://172.16.100.111:50004/pedido/{id}")
        if(peticion.status_code == 204):
            data.append({"mensage": "pedido eliminado correctamente"})
            return {
            "body": data,
            "status": peticion.status_code,
            }
    else:
        return {
            "body": [{
                "mensage": "pedido no encontrado",
                "id": id
            }],
            "status": 400,
        }
    


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
    peticion = requests.post("http://172.16.100.111:50004/pedido", headers=headers, data=json.dumps(pedido))
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
            2. Eliminar un pedido
            3. Actualizar un pago
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 3):
                if(opcion == 1):
                
                    print(tabulate(postProducto(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                    idPedido = input("Ingrese el id del producto q desea eliminar: ")
                    print(tabulate(deletePedido(idPedido)), headers="keys", tablefmt="github")
                    input("Presione una tecla para continuar......")

                if(opcion == 3):
                    idProducto = input("Ingrese el id del pedido q desea Actualizar: ")
                    
                    print(tabulate(updatePedido(idProducto)["body"], headers="keys", tablefmt="pretty"))
                    input("Presione una tecla para continuar......")
                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar")