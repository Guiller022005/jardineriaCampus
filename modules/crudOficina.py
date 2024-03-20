import os
import re
from tabulate import tabulate
import json
import requests
import modules.getOficina as pstOficina
import modules.validaciones as vali
def postOficina():
    oficina = {
            "codigo_oficina": input("Ingrese el codigo del empleado: "),
            "ciudad": input("Ingrese el nombre del empleado: "),
            "pais": input("Ingrese el puesto"),
            "region": input("Ingrese el primer apellido: "),
            "codigo_postal": input("Ingrese el segundo apellido: "),
            "telefono": input("Ingrese la extension del empleado: "),
            "linea_direccion1": int(input("Ingrese el codigo de oficina: ")),
            "linea_direccion2": int(input("Ingrese el codigo del jefe del empleado: "))
    }
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://172.16.103.28:50002/oficina",headers=headers, data=json.dumps(oficina, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def deleteOficina(id):

    data = pstOficina.getAllCodeByCode(id)

    if(len(data)):
        peticion = requests.delete(f"http://172.16.103.28:50002/oficina/{id}")
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
def getAllDataOficina():
    #json-server storage/oficina.json -b 5505
    peticion = requests.get("http://172.16.103.28:50002/oficina")
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
    peticion = requests.post("http://172.16.103.28:50002/oficina", headers=headers, data=json.dumps(oficina))
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
            0. Atras
            
        """)
        opcion =(input("\nSeleccione una de las opciones: "))
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    
                    print(tabulate(postOficina(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                            idOficina = input("Ingrese el id del oficina q desea eliminar: ")
                            print(tabulate(deleteOficina(idOficina)), headers="keys", tablefmt="github")
                            input("Presione una tecla para continuar......")
                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar")