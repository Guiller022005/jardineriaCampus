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
# Filtro para limite de credito ciudad
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append(val)
    return clienteCredic

# Filtro para limite de credito por region
def getAllClientCreditoPais(limiteCredit, pais):
    clienteCredit = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('pais') == pais):
            clienteCredit.append(val)
    return clienteCredit

# Filtro por pais, ciudad y region
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
# Filtro q permita buscar nombres q coincidad parcialmente con los de los clientes
def getAllClientsCoincide(nombre_busqueda):
    clients_info = []
    for cliente in cli.clientes:
        nombre_cliente = cliente.get("nombre_contacto")
        codigo_cliente = cliente.get("codigo_cliente")
        if nombre_busqueda.lower() in nombre_cliente.lower():  # Verifica si el término de búsqueda está contenido en el nombre del cliente
            info = {
                "nombre_contacto": nombre_cliente,
                "codigo_cliente": codigo_cliente
            }
            clients_info.append(info)
    return clients_info
# Filtro para buscar Direccion2 de todos los clientes
def getAllClientsDirreccion2(direccion2):
    ClientDireccion = []
    for val in cli.clientes:
        ClientDireccion.append({
            "nombre_cliente": val.get('nombre_cliente'),
            "linea_direccion2": val.get('linea_direccion2'),
        })
    return ClientDireccion

# Filtro para contar la cantidad de clientes en una determinada ciudad
def getAllContarClientes(ciudad):
    contador = 0
    for val in cli.clientes:
        if val.get('ciudad') == ciudad:
            contador = contador + 1
    return contador

# Filtro para contar la cantidad de clientes en un determinado pais
def getAllContarCliPais(pais):
    contador = 0
    for val in cli.clientes:
        if val.get("pais") == pais:
            contador = contador + 1
    return contador



# Filtro para Fax de clientes
def getAllClientsFax(Fax):
    ClientFax = []
    for val in cli.clientes:
        ClientFax.append({
            "fax": val.get('fax'),
            "nombre_cliente": val.get('nombre_cliente'),
        })
    return ClientFax

# Filtro para codigo de empleado
def getAllClientsCodigoEmpleado(CodigoEmp):
    CodigoEmpleado = []
    for val in cli.clientes:
        CodigoEmpleado.append({
            "nombre_cliente": val.get('nombre_cliente'),
             "codigo_empleado_rep_ventas": val.get('codigo_empleado_rep_ventas')
        })
    return CodigoEmpleado
    
# Filtro para codigo postal
def getAllClientsCodigoPostal(Postal):
    ClientPostal = []
    for val in cli.clientes:
        ClientPostal.append({
            "nombre_cliente": val.get('nombre_cliente'),
            "codigo_postal": val.get('codigo_postal')
        })
    return ClientPostal

# Filtro para telefono clientes
def getAllClientsTelefono(Telefono):
    TelefonoEmpleado = []
    for val in cli.clientes:
        TelefonoEmpleado.append({
            "nombre_cliente": val.get('nombre_cliente'),
            "telefono": val.get('telefono')
        })
    return TelefonoEmpleado

#