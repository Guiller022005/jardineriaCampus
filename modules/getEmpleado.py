import storage.empleado as em
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
    for val in em.empleados:
        if(val.get("puesto")) != "Representante Ventas":
            puestoRepresentanteVentas.append(
                {
                "nombre": val.get("nombre"),
                "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                "email": val.get("email"),
                "puesto": val.get("puesto")
            }
        )
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

                            1. Obtener todos los clientes (codigo y nombre)
                            2. Obtenerun cliente por su codigo (codigo y nombre)
                            3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0, San Francisco)
    """)