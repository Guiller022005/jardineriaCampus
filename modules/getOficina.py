import storage.oficina as of
from datetime import datetime
from tabulate import tabulate
#Devuelve un listado con el codigo de
#oficina y la ciudad donde hat oficinas

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad"),
        })
    return codigoCiudad

#Devuelve un listado con la ciudad y el telefono
#de las oficinas de españa
def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais")== pais):
            ciudadTelefono.append({
            "pais": val.get("pais"),
            "ciudad": val.get("ciudad"),
            "telefono": val.get("telefono"),
            "oficinas": val.get("codigo_oficina"),
            
        })
    return ciudadTelefono
# Cuenta cuantas oficinas hay por pais
def getAllContarOficinas(pais):
    contador = 0
    for val in of.oficina:
        if val.get('pais') == pais:
            contador = contador + 1
    return contador
# Filtrar por ciudad y direccion
def getAllCiudadDireccion():
    DireccionesOficina = []
    for val in of.oficina:
        DireccionesOficina.append({
            "ciudad": val.get("ciudad"),
            "direcciones": f"{val.get('linea_direccion1')}{'linea_direccion2'}",
        })
    return DireccionesOficina
# Filtrar por codigo_postal:
def getAllCodigoPostal():
    DireccionesOficina = []
    for val in of.oficina:
        DireccionesOficina.append({
            "codigo_postal": val.get("codigo_postal"),
            "codigo_oficina": val.get("codigo_oficina")
        })
    return DireccionesOficina


def menu():
   while True:
    print("""

                
       ____                        __                   __        ____  _____      _                
      / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \/ __(_)____(_)___  ____ _    
     / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/    
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ /     
   /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/      
   ___       /_/___            __                                                                                   

                            0. Salir
                            1. Obtener un listado con el codigo de oficina y la ciudad donde hay oficinas
                            2. Obtener un listado con la ciudad y el telefono de las oficinas de un pais
                            3. Obtener cuantas oficinas hay por pais
                            4. Obtener direcciones de oficinas en distintas ciudades
                            5. Obtener codigo postal y codigo de oficina
        """)
    opcion = int(input("\nSeleccione una de las opciones: "))

    if(opcion == 1):
        print(tabulate(getAllCodigoCiudad(), headers="keys", tablefmt="fancy_grid"))
    
    elif(opcion == 2):
        pais = str(input("Ingresa el pais"))
        print(tabulate(getAllCiudadTelefono(pais), headers="keys", tablefmt="github"))
    
    elif(opcion == 3):
        pais = str(input("Ingresa el pais"))
        num_oficinas = getAllContarOficinas(pais)
        print(tabulate([[num_oficinas]], headers=["Número de Oficinas"], tablefmt="grid"))
    elif(opcion == 4):
        print(tabulate(getAllCiudadDireccion(), headers="keys", tablefmt="grid"))
    elif(opcion == 5):
        print(tabulate(getAllCodigoPostal(), headers="keys", tablefmt="grid"))
    elif(opcion == 0):
            break