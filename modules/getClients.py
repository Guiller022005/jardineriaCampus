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

def getAllClientPaisRegionCiudad(pais,region=None,ciudad=None):
    clientZone = list()
    for val in cli.clientes:

        if(val.get('pais') == pais):
            if (val.get('region') == region) or region == None:
                if (val.get('ciudad') == ciudad) or ciudad == None:
                    userInZone = dict({
                    "pais":{val.get('pais')},
                    "ciudad":{val.get('ciudad')},
                    "region":{val.get('region')}
                    })
                    clientZone.append(userInZone)
    return clientZone

def getAllClientsDirreccion2(direccion2):
    ClientDireccion = []
    for val in cli.clientes:
        ClientDireccion.append({
            "nombre_cliente": val.get('nombre_cliente'),
            "linea_direccion2": val.get('linea_direccion2'),
        })
    return ClientDireccion

def getAllContarUsuarios(ciudad):
    contador = 0
    for val in cli.clientes:
        if val.get('ciudad') == ciudad:
            contador = contador + 1
    return contador
"""def getAllContarUsuarios(ciudad):
    NumeroClientes = 0  # Inicializamos el contador fuera del bucle
    for val in cli.clientes:
        if val.get('ciudad') == ciudad:  # Verificamos si el cliente tiene la ciudad especificada
            NumeroClientes += 1  # Incrementamos el contador si el cliente tiene la ciudad especificada
    return NumeroClientes"""

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

def getAllClientsTelefono(Telefono):
    TelefonoEmpleado = []
    for val in cli.clientes:
        TelefonoEmpleado.append({
            "telefono": val.get('telefono')
        })
    return TelefonoEmpleado