import os
import re
from tabulate import tabulate
import json
import requests
import modules.crudEmpleado as cem
import modules.getEmpleado as em
import modules.crudOficina as of
import modules.validaciones as vali
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
    peticion = requests.post("http://172.16.100.120:50003/empleado",headers=headers, data=json.dumps(empleado, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Empleado Guardado"
    return [res]

def deleteEmpleado(id):
    data = em.getAllCodeByCode(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.100.120:50003/empleado/{id}")
        if(peticion.status_code == 204):
            data.append({"mensage": "empleado eliminado correctamente"})
            return {
            "body": data,
            "status": peticion.status_code,
            }
    else:
        return {
            "body": [{
                "mensage": "empleado no encontrado",
                "id": id
            }],
            "status": 400,
        }
def getAllDataEmpleado():
    #json-server storage/empleado.json -b 50003
    peticion = requests.get("http://172.16.100.120:50003/empleado")
    data = peticion.json()
    return data 

def nuevoCodigoEmpleado():
    codigodelCliente = list()
    for val in getAllDataEmpleado():
        codigodelCliente.append(val.get("codigo_empleado"))
    if codigodelCliente:
        return max(codigodelCliente) + 1
    else:
        return 1

def postEmpleados():
    empleado = dict()
    while True:
        try:
            codigoEmpleado = nuevoCodigoEmpleado()
            empleado["codigo_empleado"] = codigoEmpleado

            if(not empleado.get("nombre")):
                nombreEmpleado = input("Ingrese el nombre del empleado: ")
                if(vali.validacionNombre(nombreEmpleado) is not None):
                    empleado["nombre"] = nombreEmpleado
                else:
                    raise Exception("El nombre del cliente no cumple con lo establecido")
                
            if(not empleado.get("apellido1")):
                apellido1 = input("Ingrese el apellido del empleado: ")
                if(vali.validacionNombre(apellido1) is not None):
                    empleado["apellido1"] = apellido1
                else:
                    raise Exception("El apellido del empleado no cumple con lo establecido") 

            apellido2 = input("Ingrese el otro apellido del empleado(opcional): ")
            if(vali.validacionNombre(apellido1) is not None):
                empleado["apellido2"] = apellido2   
            
            if(not empleado.get("extension")):
                extension = input("Ingrese la extension: ")
                if(vali.validacionNumerica(extension) is not None):
                    empleado["extension"] = extension
                else:
                    raise Exception("La extension ingresada no cumple con lo establecido")
                
            if(not empleado.get("email")):
                email = input("Ingrese el email del empleado: ")
                empleado["email"] = email

            if(not empleado.get("codigo_oficina")):
                opcion = input("Seleccione la oficina:\n "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(of.getAllCodigoOficina())]))
                if vali.validacionOpciones(opcion):
                    gama = of.getAllCodigoOficina()[int(opcion)]
                    empleado["codigo_oficina"] = gama
                else:
                    raise Exception("La opcion de la oficina no cumple con lo establecido")
                
            if(not empleado.get("codigo_jefe")):
                codigoJefe = input("Ingrese el codigo jefe: ")
                if(vali.validacionNumerica(codigoJefe) is not None):
                    codigoJefe = int(codigoJefe)
                    empleado["codigo_jefe"] = codigoJefe
                else:
                    raise Exception("El codigo jefe no cumple con lo establecido")            

            if(not empleado.get("puesto")):
                puesto = input("Ingrese el puesto del empleado: ")
                if(vali.validacionNombre(puesto) is not None):
                    empleado["puesto"] = puesto
                    break
                else:
                    raise Exception("El puesto del empleado no cumple con lo establecido")

        except Exception as error:
            print(error)
    
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://172.16.100.120:50003/empleado", headers=headers, data=json.dumps(empleado))
    res = peticion.json()
    res["Mensaje"] = "Empleado Agregado"
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
                                                                                                                                                    
            1. Guardar un empleado nuevo
            2. Eliminar un empleado
            0. Atras
            
        """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    
                    print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                            idEmpleado = input("Ingrese el id del empleado q desea eliminar: ")
                            print(tabulate(deleteEmpleado(idEmpleado)), headers="keys", tablefmt="github")
                            input("Presione una tecla para continuar......")
                            
                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar")