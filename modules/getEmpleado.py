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

# Devuelve un listado con el codigo de cliente de aquellos clientes q realizaron algun pago en 2008. Tenga en cuenta q debera eliminar aquellos codigos de cliente q aparezcan repetidos.