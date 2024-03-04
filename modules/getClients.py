import storage.cliente as cli

def getAllClientesName():
    clienteName = []
    for val in cli.clientes:
        clienteName.append({
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
        })
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return {
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
        }
    
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(val)
    return clienteCredic

"""def getAllClientPaisRegionCiudad(pais,region=None,ciudad=None):
    clientZone = list()
    for val in cli.clientes:
        if(
            val.get('pais') == pais and
            (val.get('region') == region and val.get('region') == None) or
            (val.get('ciudad') == ciudad or val.get('ciudad') == None)
        ):

            clientZone.append(val)
    return clientZone
"""
def getAllClientsDirreccion2(direccion2):
    ClientDireccion = []
    for val in cli.clientes:
        ClientDireccion.append({
            "nombre_cliente": val.get('nombre_cliente'),
            "linea_direccion2": val.get('linea_direccion2'),
        })
    return ClientDireccion

#def getAllContarUsuarios(UsuarioXCiudad):
    NumeroClient = 0
    for val in cli.clientes:
        if val.get("codigo_cliente"):
            NumeroClient += 1
    return NumeroClient

def getAllClientsFax(Fax):
    ClientFax = []
    for val in cli.clientes:
        ClientFax.append({
            "fax": val.get('fax'),
            "nombre_cliente": val.get('nombre_cliente'),
        })
    return ClientFax

def getAllClientsCodigoEmpleado(CodigoEmpleado):
    CodigoEmpleado = []
    for val in cli.clientes:
        CodigoEmpleado.append({
            "codigo_empleado_rep_ventas": val.get('codigo_empleado_rep_ventas')
        })
    return CodigoEmpleado

def getAllClientsCodigoPostal(Postal):
    ClientPostal = []
    for val in cli.clientes:
        ClientPostal.append({
            "codigo_postal": val.get('codigo_postal')
        })
    return ClientPostal