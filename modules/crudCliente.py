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
    peticion = requests.get("http://172.16.100.120:50001/cliente")
    data = peticion.json()
    return data




def deleteCliente(id):

    data = Cli.getAllCodeByCode(id)
    
    if(len(data)):
        peticion = requests.delete(f"http://172.16.100.120:50001/cliente/{id}")
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
    peticion = requests.post("http://172.16.100.120:50001",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]


def nuevoCodigoCliente():
    codigodelCliente = list()
    for val in getAllCliente():
        codigodelCliente.append(val.get("codigo_cliente"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1


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
    peticion = requests.post("http://172.16.100.120:50001/clientes", headers=headers, data=json.dumps(cliente))
    res = peticion.json()
    res["Mensaje"] = "Cliente Agregado"
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
            2. Eliminar cliente
            0. Atras
            
        """)
        opcion =input("\nSeleccione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    
                    print(tabulate(postCliente(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                    idCliente = input("Ingrese el id del producto q desea eliminar: ")
                    print(tabulate(deleteCliente(idCliente)["body"],headers="keys",tablefmt="grid"))
                            
                            
                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar")



