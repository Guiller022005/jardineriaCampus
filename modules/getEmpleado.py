import storage.empleado as em
from datetime import datetime
from tabulate import tabulate
#Devuelve un listado con el nombre, apellidos y email
#de los empleados cuyo jefe tiene de jefe igual a 7


def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []
    for val in em.empleados:
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
    for val in em.empleados:
        if(val.get("codigo_jefe") == None):
            puestoNombreApellidoEmail.append(
                {
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "puesto": val.get("puesto")
            }
        )
    return puestoNombreApellidoEmail










# Devuelve un listado con el nombre, apellidos y puesto de aquellos empleados q no sean representantes de ventas
def getAllPuestoRepresentanteDeVentas():
    puestoRepresentanteVentas = []
    for vente in em.empleados:
        if vente.get("puesto") != "Representante Ventas":
            puestoRepresentanteVentas.append(
                {
                "nombre": vente.get("nombre"),
                "apellidos": f"{vente.get('apellido1')}{vente.get('apellido2')}",
                "email": vente.get("email"),
                "puesto": vente.get("puesto")
        })
    return puestoRepresentanteVentas
    












def menu():
    print("""
                
       ____                        __                   __                             __               __          
      / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ___  ____ ___  ____  / /__  ____ _____/ /___  _____
     / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
   /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
   ___       /_/___            __                                           /_/                                     
  <  /    _____/ (_)__  ____  / /____                                                                                                      

                            1. Obtener informacion de nombre, email del jefe
                            2. Obtener informacion de jefe de la empresa
                            3. Obtener un listado con el nombre, apellidos y puesto de aquellos empleados q no sean representantes de ventas
    """)


    opcion = int(input("\nSeleccione una de las opciones: "))
    
    if(opcion == 1):
        codigoJefe = int(input("Ingresa el codigo del jefe"))
        print(tabulate(getAllNombreApellidoEmailJefe(codigoJefe), headers="keys", tablefmt="fancy_grid"))
    
    elif(opcion == 2):
        print(tabulate(getAllPuestoNombreApellidosEmailJefe(), headers="keys", tablefmt="github"))
    
    elif(opcion == 3):
        print(tabulate(getAllPuestoRepresentanteDeVentas(), headers="keys", tablefmt="grid"))