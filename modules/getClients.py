import storage.cliente as cli
from datetime import datetime
from tabulate import tabulate
import storage.empleado as em
import storage.pago as pago

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
            return [{
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
        }]

# Filtro para limite de credito ciudad
def getAllClientCreditoCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append({
                "Codigo": val.get('codigo_cliente'),
                "Responsable": val.get('nombre_cliente'),
                "Director": val.get('nombre_contacto'),
                "Telefono": val.get('telefono'),
                "Fax": val.get('fax'),
                "Direcciones": f"{val.get('linea_direccion1')}{('linea_direccion')}",
                "Origen": f"{val.get('pais')}{val.get('region')}{val.get('ciudad')}{val.get('codigo_postal')}",
                "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                "Credito": val.get('limite_credito'),
            })
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
def getAllClientsCoincide(nombre):
    clients_info = []
    for cliente in cli.clientes:
        nombre_cliente = cliente.get("nombre_cliente")
        coincide = str(input("Ingresa un nombre"))
        if nombre.startswith(coincide) in nombre_cliente.lower():  # Verifica si el término de búsqueda está contenido en el nombre del cliente
            info = {
                "nombre_cliente": ("nombre_cliente"),
                "codigo_cliente": ("codigo_cliente")
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
def getAllClientsCodigoPostal():
    ClientPostal = []
    for val in cli.clientes:
        ClientPostal.append({
            "nombre_cliente": val.get('nombre_cliente'),
            "codigo_postal": val.get('codigo_postal')
        })
    return ClientPostal

# Filtro para telefono clientes
def getAllClientsTelefono():
    TelefonoEmpleado = []
    for val in cli.clientes:
        TelefonoEmpleado.append({
            "nombre_cliente": val.get('nombre_cliente'),
            "telefono": val.get('telefono')
        })
    return TelefonoEmpleado

# Devuelve un listado con el nombre de los todos los clientes españoles
def getAllClientsSpain(pais):
    clientSpain = []
    for val in cli.clientes:
        if(val.get("pais")) == "Spain":
            clientSpain.append({
                "nombre_cliente": val.get('nombre_cliente'),
            })
    return clientSpain
# Devuelve un listado con los clientes q sean de la ciudad madrid y cuyo codigo de representante de ventas sea 11 o 30
def getClientsMadridCodigo():
    clientMadrid = []
    for val in cli.clientes:
        
        if (val.get("ciudad") == "Madrid"):
            if(val.get("codigo_empleado_rep_ventas")== 11) or (val.get("codigo_empleado_rep_ventas") == 30):
        
                clientMadrid.append({
                "codigo_cliente":val.get("codigo_cliente"),
                "nombre_cliente":val.get("nombre_cliente"),
                "nombre_contacto":val.get("nombre_contacto"),
                "apellido_contacto":val.get("apellido_contacto"),
                "codigo_empleado_rep_ventas":val.get("codigo_empleado_rep_ventas"),
                "ciudad":val.get("ciudad"),
               
                })
    return clientMadrid

def getAllClientsYRepresentantes():
    ClientsRepreVent = list ()
    for val in cli.clientes:
        for i in em.empleados:
            if val.get("codigo_empleado_rep_ventas") == i.get("codigo_empleado"):
                ClientsRepreVent.append({
                    "Nombre Cliente": val.get("nombre_cliente"),
                    "Representante de ventas": f'{i.get("nombre")} {i.get("apellido1")}'
                })
    return ClientsRepreVent
def getAllPagos():
    ClientsPagos = list()
    for val in cli.clientes:
        for i in em.empleados:
            for d in pago.pago:
                if (d.get("codigo_cliente") == val.get("codigo_cliente")) and (val.get("codigo_empleado_rep_ventas") == i.get("codigo_empleado")):
                    if val.get("nombre_cliente") not in ClientsPagos:
                        if i.get('puesto') == 'Representante Ventas':
                            ClientsPagos.append({
                                'codigo': val.get('codigo_cliente'),
                                "Nombre Cliente": val.get("nombre_cliente"),
                                "id_transaccion": d.get("id_transaccion"),
                                "Representante de ventas": f'{i.get("nombre")} {i.get("apellido1")}'
                            })
    return ClientsPagos

def getAllNoPagos():
    ClientsNoPago = []
    for val in cli.clientes:
        pagos = False
        for d in pago.pago:
                if val.get('codigo_cliente')== d.get('codigo_cliente'):
                    pagos = True
                    break
        if not pagos:
            for d in em.empleados:
                if val.get('codigo_empleado_rep_ventas') == d.get('codigo_empleado'):
                    if d.get('puesto') == 'Representante Ventas':
                        ClientsNoPago.append({

                                'codigo': val.get('codigo_cliente'),
                                "Nombre Cliente": val.get("nombre_cliente"),
                                "puesto": d.get("puesto"),
                                "Representante de ventas": d.get('nombre')
                            })
    return ClientsNoPago


def menu():
   while True:
    print("""
    ____                        __                   __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                                   
                            0.  Regresar al menu principal
                            1. Obtener todos los clientes (codigo y nombre)
                            2. Obtener un cliente por su codigo (codigo y nombre)
                            3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0, San Francisco)
                            4. Obtener toda la informacion de un cliente segun su limite de credito y pais que pertenece (ejem: 3000.0, Spain)
                            5. Obtener informacion de cuantos clientes hay por ciudad
                            6. Obtener informacion por el numero de telefono   
                            7. Obtener Fax de clientes
                            8. Obtener informacion por pais, ciudad y region
                            9. Devuelve un listado con los clientes q sean de la ciudad madrid y cuyo codigo de representante de ventas sea 11 o 30
                            10. Obtener un listado con el nombre de cada cliente y el nombre y apellido de su representante de ventas.
                            11. Obtener a los clientes q hayan realizado pagos junto a su representante de ventas
                            12. 
        """)
    
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllClientesName(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 2):
        try:
            codigoCliente = int(input("Ingresa el codigo cliente: "))
            print(tabulate(getOneClientCodigo(codigoCliente), headers="keys", tablefmt="github"))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 3):
        try:
            limiteCredito = float(input("Ingresa el limite de credito"))
            ciudad = str(input("Ingresa la ciudad")) 
            print(tabulate(getAllClientCreditoCiudad(limiteCredito, ciudad), headers="keys", tablefmt="grid"))
        except KeyboardInterrupt:
            return menu()    
    elif(opcion == 4):
        try:
            limiteCredito = float(input("Ingresa el limite de credito"))
            pais = str(input("Ingresa el pais")) 
            print(tabulate(getAllClientCreditoPais(limiteCredito, pais),  headers='firstrow', 
               tablefmt='fancy_grid',
               stralign='center',
               floatfmt='.0f'))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 5):
        try:
            ContarXCiudad = str(input("Ingresa la ciudad"))
            print(getAllContarClientes(ContarXCiudad))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 6):
        print(tabulate(getAllClientsTelefono(), headers="keys", tablefmt="grid"))
    elif(opcion == 7):
        print(tabulate(getAllClientsCodigoPostal(), headers="keys", tablefmt="grid"))
    elif(opcion == 8):
        pais = input("Ingresa el pais")
        print(tabulate(getAllClientPaisRegionCiudad(pais), headers="keys", tablefmt="grid"))
    elif(opcion == 9):
        try:
            print(tabulate(getClientsMadridCodigo(), headers="keys", tablefmt="grid"))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 10):
        try:
            print(tabulate(getAllClientsYRepresentantes(), headers="keys", tablefmt="grid"))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 11):
        try:
            print(tabulate(getAllPagos(), headers="keys", tablefmt="grid"))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 12):
        try:
            print(tabulate(getAllNoPagos(), headers="keys", tablefmt="grid"))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 0):
        break
    
    try:
        entrada = input("Ingresa Ctrl + c para ir a menu: ")
        print("Entrada recibida: ", entrada)
    except KeyboardInterrupt:
       menu()
