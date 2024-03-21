import os
from tabulate import tabulate
import json
import requests
import modules.crudPagos as pstPagos
import modules.validaciones as vali

def getAllDataPagos():
    #json-server storage/pago.json -b 50004
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json()
    return data 

def getPagoCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{codigo}")
    return peticion.json() if peticion.ok else []


# def postPagos():
#     cliente = {
#             "codigo_cliente": input("Ingrese el codigo del cliente: "),
#             "forma_pago": input("Ingrese la fecha del pedido: "),
#             "id_transaccion": input("Ingrese la fecha esperada"),
#             "fecha_pago": input("Ingrese la fecha de entrega: "),
#             "total": input("Ingrese el estado del pedido: "),
#     }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://154.38.171.54:5006/pagos",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Pedido Guardado"
#     return [res]

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
    peticion = requests.post("http://154.38.171.54:5006/pagos", headers=headers, data=json.dumps(pago))
    res = peticion.json()
    return [res]

def deletePagos(id):
    data = pstPagos.getPagosCodigo(id)
    if(len(data)):
        peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
        if(peticion.status_code == 204):
            data.append({"mensage": "pago eliminado correctamente"})
            return {
            "body": data,
            "status": peticion.status_code,
            }
    else:
        return {
            "body": [{
                "mensage": "pago no encontrado",
                "id": id
            }],
            "status": 400,
        }
    
def updatePago(id):
    data = getPagoCodigo(id)
    if(len(data)):
        print("Pago Encontrado")
        print(tabulate([data], headers="keys", tablefmt="github"))
        data["codigo_cliente"] = data["codigo_cliente"]
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Forma de pago 
                    2. Id transaccion
                    3. Fecha pago
                    4. Total
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 4):
                        if(opcion == 1):
                            while True:
                                try:
                                    formaPago = input("Ingrese la forma de pago: ")
                                    if(vali.validacionNombre(formaPago) is not None):
                                        data["forma_pago"] = formaPago
                                        break
                                    else:
                                        raise Exception("La forma de pago no cumple con lo establecido")  
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    idTransaccion = input("Ingrese la id de la transaccion: ")
                                    if(vali.validaiconTransccion(idTransaccion) is not None):
                                        data["id_transaccion"] = idTransaccion
                                        break
                                    else:
                                        raise Exception("La id de la transaccion no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    fechaPago = input("Ingrese la fecha de pago: ")
                                    if(vali.validacionFecha(fechaPago) is not None):
                                        data["fecha_pago"] = fechaPago
                                        break
                                    else:
                                        raise Exception("La fehca no cumple con lo establecido") 
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    total = input("Ingrese el total del pago: ")
                                    if(vali.validacionNumerica(total) is not None):
                                        total = int(total)
                                        data["total"] = total
                                        break
                                    else:
                                        raise Exception("El pago no cumple con lo establecido")   
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
        peticion = requests.put(f"http://154.38.171.54:5006/pagos/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        return [res]
    else:
        return[{
            "messege": "Pago no encontrado",
            "id": id
        }]


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
                                                                                                                                                                                      
            1. Guardar un pago nuevo
            2. Eliminar un pago
            3. Actualizar un pago
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 3):
                if(opcion == 1):
                    
                    print(tabulate(postPagos(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                            idPagos = input("Ingrese el id del pago q desea eliminar: ")
                            print(tabulate(deletePagos(idPagos)), headers="keys", tablefmt="github")
                            input("Presione una tecla para continuar......")

                if(opcion == 3):
                    idProducto = input("Ingrese el id del pago q desea Actualizar: ")
                    
                    print(tabulate(updatePago(idProducto)["body"], headers="keys", tablefmt="pretty"))
                    input("Presione una tecla para continuar......")

                elif(opcion == 0):
                    break 
                input("Presione una tecla para continuar")