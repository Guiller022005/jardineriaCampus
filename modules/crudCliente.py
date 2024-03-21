import os
import re
from tabulate import tabulate
import json
import requests
import modules.crudCliente as pstClient
import modules.getClients as Cli
import modules.validaciones as vali


def getAllCliente():
    #json-server storage/cliente.json -b 5507
    peticion = requests.get("http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

def nuevoCodigoCliente():
    codigodelCliente = list()
    for val in getAllCliente():
        codigodelCliente.append(val.get("codigo_cliente"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1
    


def getClienteCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5001/cliente/{codigo}")
    return peticion.json() if peticion.ok else []

def getCodi(codigo):
    codigoCli =list()
    for val in getAllCliente():
        if val.get("codigo_cliente") == codigo:
            codigoCli.append(val)
    return codigoCli

def postClientes():

    cliente = dict()
    while True:
        try:
            codigoCliente = nuevoCodigoCliente()
            cliente["codigo_cliente"] = codigoCliente

            if(not cliente.get("nombre_cliente")):
                nombreCliente = input("Ingrese el nombre del cliente: ")
                if(vali.validacionNombre(nombreCliente) is not None):
                    cliente["nombre_cliente"] = nombreCliente
                else:
                    raise Exception("El nombre del cliente no cumple con lo establecido")
                
            if(not cliente.get("nombre_contacto")):
                nombreContacto = input("Ingrese el nombre del contacto: ")
                if(vali.validacionNombre(nombreContacto) is not None):
                    cliente["nombre_contacto"] = nombreContacto
                else:
                    raise Exception("El nombre del contacto no cumple con lo establecido")
                
            if(not cliente.get("apellido_contacto")):
                apellidoContacto = input("Ingrese el apellido de contacto: ")
                if(vali.validacionNombre(apellidoContacto) is not None):
                    cliente["apellido_contacto"] = apellidoContacto
                else:
                    raise Exception("El apellido del contacto no cumple con lo establecido")
                
            if(not cliente.get("telefono")):
                telefono = input("Ingrese el numero de telefono: ")
                if(vali.validacionNumero(telefono) is not None):
                    cliente["telefono"] = telefono
                else:
                    raise Exception("El telefono ingresado no cumple con lo establecido")
                
            if(not cliente.get("fax")):
                fax = input("Ingrese el fax: ")
                if(vali.validacionNumero(fax) is not None):
                    cliente["fax"] = fax
                else:
                    raise Exception("El fax ingresado no cumple con lo establecido")
                
            if(not cliente.get("linea_direccion1")):
                direccion1 = input("Ingrese una linea de direccion: ")
                cliente["linea_direccion1"] = direccion1
                 
            direccion2 = input("Ingrese otra linea de direccion(opcional): ")
            if direccion2:
                cliente["linea_direccion2"] = direccion2

            if(not cliente.get("ciudad")):
                ciudad = input("Ingrese la ciudad: ")
                if(vali.validacionNombre(ciudad) is not None):
                    cliente["ciudad"] = ciudad
                else:
                    raise Exception("El nombre de la ciudad no cumple con lo establecido")

            region = input("Ingrese la region (opcional): ")
            if region:
                if vali.validacionNombre(region) is not None:
                    cliente["region"] = region

            if(not cliente.get("pais")):
                pais = input("Ingrese el pais: ")
                if(vali.validacionNombre(pais) is not None):
                    cliente["pais"] = pais
                else:
                    raise Exception("El nombre del pais no cumple con lo establecido")
                
            if(not cliente.get("codigo_postal")):
                codigoPostal = input("Ingrese el codigo postal: ")
                if(vali.validacionNumerica(codigoPostal) is not None):
                    cliente["codigo_postal"] = codigoPostal
                else:
                    raise Exception("El codigo postal no cumple con lo establecido")
                
            if(not cliente.get("codigo_empleado_rep_ventas")):
                codigoEmpleado = input("Ingrese el codigo de empleado: ")
                if(vali.validacionNumerica(codigoEmpleado) is not None):
                    codigoEmpleado = int(codigoEmpleado)
                    cliente["codigo_empleado_rep_ventas"] = codigoEmpleado
                else:
                    raise Exception("El codigo de empleado no cumple con lo establecido")
                
            if(not cliente.get("limite_credito")):
                limiteCredito = input("Ingrese el limite de credito: ")
                if(vali.validacionNumerica(limiteCredito) is not None):
                    limiteCredito = float(limiteCredito)
                    cliente["limite_credito"] = limiteCredito
                    break
                else:
                    raise Exception("El codigo de empleado no cumple con lo establecido")
                
        except Exception as error:
            print(error)

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://154.38.171.54:5001/cliente", headers=headers, data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Cliente Agregado"
    return [res]

def deleteCliente(id):

    data = Cli.getAllCodeByCode(id)
    
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        if(peticion.status_code == 204):
            data.append({"message":"cliente eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "mensage":"cliente no encontrado",
                "id": id
            }],
            "status": 400,
        }

def updateCliente(id):
    data = getClienteCodigo(id)
    if(len(data)):
        print("Cliente Encontrado")
        print(tabulate([data], headers="keys", tablefmt="github"))
        data["codigo_cliente"] = data["codigo_cliente"]
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Nombre cliente
                    2. Nombre contacto
                    3. Apellido contacto 
                    4. Telefono
                    5. Fax
                    6. Linea dirrecion 1 
                    7. Linea dirrecion 2
                    8. Ciudad
                    9. Region
                   10. Pais
                   11. Codigo postal
                   12. Codigo empleado
                   13. Limite credito
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 13):
                        if(opcion == 1):
                            while True:
                                try:
                                    nombreCliente = input("Ingrese el nombre del cliente: ")
                                    if(vali.validacionNombre(nombreCliente) is not None):
                                        data["nombre_cliente"] = nombreCliente
                                        break
                                    else:
                                        raise Exception("El nombre del cliente no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    nombreContacto = input("Ingrese el nombre del contacto: ")
                                    if(vali.validacionNombre(nombreContacto) is not None):
                                        data["nombre_contacto"] = nombreContacto
                                        break
                                    else:
                                        raise Exception("El nombre del contacto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    apellidoContacto = input("Ingrese el apellido de contacto: ")
                                    if(vali.validacionNombre(apellidoContacto) is not None):
                                        data["apellido_contacto"] = apellidoContacto
                                        break
                                    else:
                                        raise Exception("El apellido del contacto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    telefono = input("Ingrese el numero de telefono: ")
                                    if(vali.validacionNumero(telefono) is not None):
                                        data["telefono"] = telefono
                                        break
                                    else:
                                        raise Exception("El telefono ingresado no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 5):
                            while True:
                                try:
                                    fax = input("Ingrese el fax: ")
                                    if(vali.validacionNumero(fax) is not None):
                                        data["fax"] = fax
                                        break
                                    else:
                                        raise Exception("El fax ingresado no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 6):
                            while True:
                                try:
                                    direccion1 = input("Ingrese una linea de direccion: ")
                                    if direccion1:
                                        data["linea_direccion1"] = direccion1
                                        break
                                except Exception as error:
                                    print(error)
                        if(opcion == 7):
                            while True:
                                try:
                                    direccion2 = input("Ingrese otra linea de direccion(opcional): ")
                                    if direccion2:
                                        data["linea_direccion2"] = direccion2
                                        break
                                except Exception as error:
                                    print(error)
                        if(opcion == 8):
                            while True:
                                try:
                                    ciudad = input("Ingrese la ciudad: ")
                                    if(vali.validacionNombre(ciudad) is not None):
                                        data["ciudad"] = ciudad
                                        break
                                    else:
                                        raise Exception("El nombre de la ciudad no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 9):
                            while True:
                                try:
                                    region = input("Ingrese la region (opcional): ")
                                    if vali.validacionNombre(region) is not None:
                                        data["region"] = region
                                        break
                                    else:
                                        raise Exception("El nombre de la region no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 10):
                            while True:
                                try:
                                    pais = input("Ingrese el pais: ")
                                    if(vali.validacionNombre(pais) is not None):
                                        data["pais"] = pais
                                        break
                                    else:
                                        raise Exception("El nombre del pais no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 11):
                            while True:
                                try:
                                    codigoPostal = input("Ingrese el codigo postal: ")
                                    if(vali.validacionNumerica(codigoPostal) is not None):
                                        data["codigo_postal"] = codigoPostal
                                        break
                                    else:
                                        raise Exception("El codigo postal no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 12):
                            while True:
                                try:
                                    codigoEmpleado = input("Ingrese el codigo de empleado: ")
                                    if(vali.validacionNumerica(codigoEmpleado) is not None):
                                        codigoEmpleado = int(codigoEmpleado)
                                        data["codigo_empleado_rep_ventas"] = codigoEmpleado
                                        break
                                    else:
                                        raise Exception("El codigo de empleado no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 13):
                            while True:
                                try:
                                    limiteCredito = input("Ingrese el limite de credito: ")
                                    if(vali.validacionNumerica(limiteCredito) is not None):
                                        limiteCredito = int(limiteCredito)
                                        data["limite_credito"] = limiteCredito
                                        break
                                    else:
                                        raise Exception("El limite de credito no cumple con lo establecido")
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
        peticion = requests.put(f"http://154.38.171.54:5001/cliente/{id}", headers=headers, data=json.dumps(data).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Cliente Actualizado"
        return [res]
    
    else:
        return[{
            "messege": "Producto no encontrado",
            "id": id
        }]

# def postCliente():
#     cliente = {
#             "codigo_cliente": input("Ingrese el codigo del cliente: "),
#             "nombre": input("Ingrese el nombre del cliente: "),
#             "nombre_contacto": input("Ingrese el nombre de contacto"),
#             "apellido_contacto": input("Ingrese el apellido de contacto: "),
#             "telefono": input("Ingrese el numero de telefono: "),
#             "fax": input("Ingrese el numero de fax: "),
#             "linea_direccion1": int(input("Ingresa la linea de direccion 1: ")),
#             "linea_direccion2": int(input("Ingresa la linea de direccion 2: ")),
#             "ciudad": int(input("Ingrese la ciudad: ")),
#             "region": int(input("Ingrese la region: ")),
#             "pais": int(input("Ingrese el pais: ")),
#             "codigo_postal": int(input("Ingrese el codigo postal: ")),
#             "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del empleado de ventas: ")),
#             "limite_credito": int(input("Ingrese el limite de credito: "))
#     }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://172.16.103.38:50001",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]







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
            2. Eliminar cliente
            3. Actualizar un empleado
            0. Atras
            
        """)
        opcion =(input("\nSeleccione una de las opciones: "))
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 3):
                if(opcion == 1):
                    
                    print(tabulate(postClientes(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                    idCliente = input("Ingrese el id del producto q desea eliminar: ")
                    print(tabulate(deleteCliente(idCliente)["body"],headers="keys",tablefmt="grid"))
                            
                if(opcion == 3):
                    idProducto = input("Ingrese el id del empleado q desea Actualizar: ")
                    
                    print(tabulate(updateCliente(idProducto), headers="keys", tablefmt="pretty"))
                    input("Presione una tecla para continuar......")


                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar")



