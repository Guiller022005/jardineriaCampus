import os
import re
from tabulate import tabulate
import json
import requests
import modules.getOficina as pstOficina
import modules.validaciones as vali
# def postOficina():
#     oficina = {
#             "codigo_oficina": input("Ingrese el codigo del empleado: "),
#             "ciudad": input("Ingrese el nombre del empleado: "),
#             "pais": input("Ingrese el puesto"),
#             "region": input("Ingrese el primer apellido: "),
#             "codigo_postal": input("Ingrese el segundo apellido: "),
#             "telefono": input("Ingrese la extension del empleado: "),
#             "linea_direccion1": int(input("Ingrese el codigo de oficina: ")),
#             "linea_direccion2": int(input("Ingrese el codigo del jefe del empleado: "))
#     }
#     headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
#     peticion = requests.post("http://172.16.100.111:50002/oficina",headers=headers, data=json.dumps(oficina, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Producto Guardado"
#     return [res]

def getAllDataOficina():
    #json-server storage/oficina.json -b 5505
    peticion = requests.get("http://172.16.100.111:50002/oficina")
    data = peticion.json()
    return data 

def getAllCodigoOficina():
    oficinaNombre = list()
    for val in getAllDataOficina():
        oficinaNombre.append(val.get("codigo_oficina"))
    return oficinaNombre


def getOficinaCodigo(codigo):
    for val in getAllDataOficina():
        if(val.get("codigo_oficina") == codigo):
             return [val]

def getCodigo(codigo):
    for val in getAllDataOficina():
        if(val.get("codigo_oficina") == codigo):
             return [val]

def deleteOficina(id):

    data = pstOficina.getAllCodeByCode(id)

    if(len(data)):
        peticion = requests.delete(f"http://172.16.100.111:50002/oficina/{id}")
        if(peticion.status_code == 204):
            data.append({"mensage": "oficina eliminado correctamente"})
            return {
            "body": data,
            "status": peticion.status_code,
            }
    else:
        return {
            "body": [{
                "mensage": "oficina no encontrado",
                "id": id
            }],
            "status": 400,
        }


def updateOficina(id):
    data = getOficinaCodigo(id)
    if (len(data)):
        print("Oficina Encontrada")
        print(tabulate([data], headers="keys", tablefmt="github"))
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Codigo oficina 
                    2. Ciudad
                    3. Pais
                    4. Region
                    5. Codigo postal
                    6. Telefono
                    7. Linea direccion 1
                    8. Linea direccion 2
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 8):
                        if(opcion == 1):
                            while True:
                                try:
                                    codigo = input("Ingrese el codigo de la oficina (Ej: BCN-ES): ")
                                    if(vali.validacionCoidgoOficina(codigo) is not None):
                                        data2 = getCodigo(codigo)
                                        if(data2):
                                            print(tabulate(data2, headers="keys", tablefmt="github"))
                                            raise Exception("El codigo oficina ya existe")
                                        else:
                                            data["codigo_oficina"] = codigo
                                            break
                                    else:
                                        raise Exception("El codigo oficina no cumple con el estandar establecido")
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
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
                        if(opcion == 3):
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
                        if(opcion == 4):
                            while True:
                                try:
                                    region = input("Ingrese la region: ")
                                    if(vali.validacionNombre(region) is not None):
                                        data["region"] = region
                                        break
                                    else:
                                        raise Exception("El nombre de la region no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 5):
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
                        if(opcion == 6):
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
                        if(opcion == 7):
                            while True:
                                try:
                                    direccion1 = input("Ingrese una linea de direccion: ")
                                    data["linea_direccion1"] = direccion1
                                    break
                                except Exception as error:
                                    print(error)
                        if(opcion == 8):
                            while True:
                                try:
                                    direccion2 = input("Ingrese otra linea de direccion: ")
                                    data["linea_direccion2"] = direccion2
                                    break
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
        peticion = requests.put(f"http://172.16.100.111:50002/oficina/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        res["Mensaje"] = "Oficina Actualizada"
        return [res]
    
    else:
        return [{
                    "message": "Oficina no encontrada",
                    "id": id
            }]   
        
def postOficina():

    oficina = dict()
    while True:
        try:
            if(not oficina.get("codigo_oficina")):
                codigo = input("Ingrese el codigo de la oficina (Ej: BCN-ES): ")
                if(vali.validacionCoidgoOficina(codigo) is not None):
                    data = getOficinaCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo oficina ya existe")
                    else:
                        oficina["codigo_oficina"] = codigo
                else:
                    raise Exception("El codigo oficina no cumple con el estandar establecido")
                
            if(not oficina.get("ciudad")):
                ciudad = input("Ingrese la ciudad: ")
                if(vali.validacionNombre(ciudad) is not None):
                    oficina["ciudad"] = ciudad
                else:
                    raise Exception("El nombre de la ciudad no cumple con lo establecido")
                
            if(not oficina.get("pais")):
                pais = input("Ingrese el pais: ")
                if(vali.validacionNombre(pais) is not None):
                    oficina["pais"] = pais
                else:
                    raise Exception("El nombre del pais no cumple con lo establecido")
                
            if(not oficina.get("region")):
                region = input("Ingrese la region: ")
                if(vali.validacionNombre(region) is not None):
                    oficina["region"] = region
                else:
                    raise Exception("El nombre de la region no cumple con lo establecido")
                
            if(not oficina.get("codigo_postal")):
                codigoPostal = input("Ingrese el codigo postal: ")
                if(vali.validacionNumerica(codigoPostal) is not None):
                    oficina["codigo_postal"] = codigoPostal
                else:
                    raise Exception("El codigo postal no cumple con lo establecido")
                
            if(not oficina.get("telefono")):
                telefono = input("Ingrese el numero de telefono: ")
                if(vali.validacionNumero(telefono) is not None):
                    oficina["telefono"] = telefono
                else:
                    raise Exception("El telefono ingresado no cumple con lo establecido")
                
            if(not oficina.get("linea_direccion1")):
                direccion1 = input("Ingrese una linea de direccion: ")
                oficina["linea_direccion1"] = direccion1
                 
            if not oficina.get("linea_direccion2"):  
                direccion2 = input("Ingrese otra linea de direccion(opcional): ")
                if direccion2:
                    oficina["linea_direccion2"] = direccion2
                else:
                    break

        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.100.111:50002/oficina", headers=headers, data=json.dumps(oficina))
    res = peticion.json()
    res["Mensaje"] = "Oficina Guardada"
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
                                                                                         
                                                                                                                                                    
            1. Guardar una oficina nueva
            2. Eliminar una oficina
            3. Actualizar una oficina
            0. Atras
            
        """)
        opcion =(input("\nSeleccione una de las opciones: "))
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 3):
                if(opcion == 1):
                    
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                            idOficina = input("Ingrese el id del oficina q desea eliminar: ")
                            print(tabulate(deleteOficina(idOficina)), headers="keys", tablefmt="github")
                            input("Presione una tecla para continuar......")
                
                if(opcion == 3):
                    idProducto = input("Ingrese el id de la oficina q desea Actualizar: ")
                    
                    print(tabulate(updateOficina(idProducto)["body"], headers="keys", tablefmt="pretty"))
                    input("Presione una tecla para continuar......")
                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar")