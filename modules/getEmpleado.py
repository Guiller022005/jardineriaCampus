import os
import requests
import json
from datetime import datetime
from tabulate import tabulate
import modules.crudEmpleado as pstEmpleado

#Devuelve un listado con el nombre, apellidos y email
#de los empleados cuyo jefe tiene de jefe igual a 7

def getAllEmpleado():
    #json-server storage/empleado.json -b 50003
    peticion = requests.get("http://172.16.103.34:50003")
    data = peticion,json()
    return data

def getAllData():
    empleadoPuesto = []
    for val in getAllEmpleado():
        empleadoPuesto.append(val.get("puesto"))
    return empleadoPuesto

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in getAllData():
        if(val.get("codigo_jefe") == codigo):
            nombreApellidoEmail.append(
            {
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "jefe": val.get("codigo_jefe")
            }
        )
    return nombreApellidoEmail

# Devuelve el nombre del puesto, nombre, apellidos y email del jefe de la empresa
def getAllPuestoNombreApellidosEmailJefe():
    puestoNombreApellidoEmail = []
    for val in getAllData():
        if(val.get("codigo_jefe") == None):
            puestoNombreApellidoEmail.append(
                {
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")}{val.get("apellido2")}',
                "email": val.get("email"),
                "puesto": val.get("puesto"),
                "extension": val.get("extension"),
                "codigo_oficina": val.get("codigo_oficina"),
                

            }
        )
    return puestoNombreApellidoEmail

#Devuelve un listado con el puesto, nombre y apellidos y codigo de oficina
def getAllPuestoNombreCodigoOficina():
    puestoNombreCodeOficina = []
    for val in getAllData():
            puestoNombreCodeOficina.append(
                {
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "codigo_oficina": val.get("codigo_oficina"),                

            }
        )
    return puestoNombreCodeOficina


# Devuelve un listado con el nombre, apellidos y puesto de aquellos empleados q no sean representantes de ventas
def getAllPuestoRepresentanteDeVentas():
    puestoRepresentanteVentas = []
    for vente in getAllData():
        if vente.get("puesto") != "Representante Ventas":
            puestoRepresentanteVentas.append(
                {
                "nombre": vente.get("nombre"),
                "apellidos": f"{vente.get('apellido1')}{vente.get('apellido2')}",
                "email": vente.get("email"),
                "puesto": vente.get("puesto")
        })
    return puestoRepresentanteVentas
    
# def getAllContarEmpleados(codigo_empleado):
#     contador = 0
#     for val in em.empleados:
#         if val.get('codigo_empleado') == codigo_empleado:
#             contador = contador + 1
#     return contador
def getAllContarEmpleados():
    contador = 0
    for val in getAllData():
        contador += 1
    return contador


def menu():
   while True:
    print("""
                
    ____                        __                   __                             __               __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
___       /_/___            __                                           /_/                                     
                                                                                                     

                            0. Salir
                            1. Obtener informacion de nombre, email del jefe
                            2. Obtener informacion de jefe de la empresa
                            3. Obtener un listado con el nombre, apellidos y puesto de aquellos empleados q no sean representantes de ventas
                            4. Obtener informacion con el puesto, nombre y apellidos y codigo de oficina
                            5. Obtener cuantos empleados hay en la empresa
        """)


    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        try:
            codigoJefe = int(input("Ingresa el codigo del jefe"))
            print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="fancy_grid"))
        except KeyboardInterrupt:
            return menu()    
    elif(opcion == 2):
        print(tabulate(getAllPuestoNombreApellidosEmailJefe(), headers="keys", tablefmt="github"))
    elif(opcion == 3):
        print(tabulate(getAllPuestoRepresentanteDeVentas(), headers="keys", tablefmt="grid"))
    elif(opcion == 4):
        print(tabulate(getAllPuestoNombreCodigoOficina(), headers="keys", tablefmt="grid"))
    elif(opcion == 5):
        print(f"Total Empleados: {getAllContarEmpleados()}")
    elif(opcion == 0):
        break
    try:
        entrada = input("Ingresa Ctrl + c para ir a menu: ")
        print("Entrada recibida: ", entrada)
    except KeyboardInterrupt:
       menu()
