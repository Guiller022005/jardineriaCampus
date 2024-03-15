# import storage.pago as pagos
from tabulate import tabulate
from datetime import datetime
import requests
import json

def getAllPagos():
     #json-server storage/gama_producto.json -b 50005 
    peticion = requests.get("http://172.16.100.111:50005")
    data = peticion.json()
    return data












# Devuelve un listado con el codigo de cliente de aquellos clientes q realizaron algun pago en 2008. Tenga en cuenta q debera eliminar aquellos codigos de cliente q aparezcan repetidos.
def getAllCodigoClienteFecha():
    CodigoFecha = []
    codigos_vistos = set()  # Usamos un conjunto para evitar duplicados
    for val in getAllPagos():
        if("2008") in val.get("fecha_pago"):
            Codigo_cliente = val.get("codigo_cliente")
            if Codigo_cliente not in codigos_vistos:
                CodigoFecha.append({
                    "codigo_cliente": val.get("codigo_cliente"),
                    "fecha": val.get("fecha_pago"),
                    "total": val.get("total")
                })
                codigos_vistos.add(Codigo_cliente)
    return CodigoFecha

# Devuelve un listado con todos los pagos q se realizaron en en el año 2008 mediante paypal, ordena el resultado de mayor a menor
def getAllPagosFecha():
    pagosFecha = []
    for val in getAllPagos():
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") is ("PayPal"):
            pagosFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"], reverse=True)
    return pagosFecha

# Devuelve un listado con todas las formas de pago q aparecen en la tabla pago. Tenga en cuenta q no deben aparecer formas de pago repetidas
def getAllFormasDePago():
    tipoPago = set()
    for val in getAllPagos():
        formaPago = val.get("forma_pago")
        if formaPago not in tipoPago:
            tipoPago.add(formaPago)
    return tipoPago

# Devuelve un listado con todos los productos q pertenecen a la gama Ornamentales y q tienen mas de 100 unidades en shok.
# El listado debera estar ordenado por su precio de venta, mostrarlo en primer lugar los de mayor precio

def menu():
   while True:
    print("""
                
       ____                        __                   __                                    
      / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  ____ _____ _____  _____
     / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ __ `/ __ `/ __ \/ ___/
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  ) 
   /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/\__,_/\__, /\____/____/  
   ___       /_/___            __                            /_/          /____/   
                            0. Salir
                            1. Obtener todos codigos de clientes q realizaron algun pago en 2008. 
                            2. Obtener los pagos q se realizaron en en el año 2008 mediante paypal
                            3. Obtener todas las formas de pago 
        """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllCodigoClienteFecha(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 2):
        print(tabulate(getAllPagosFecha(), headers="keys", tablefmt="github"))
    elif(opcion == 3):
        print(tabulate(getAllFormasDePago(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 0):
        break
    try:
        entrada = input("Ingresa Ctrl + c para ir a menu: ")
        print("Entrada recibida: ", entrada)
    except KeyboardInterrupt:
       menu()