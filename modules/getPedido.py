# import storage.pedido as pe
from datetime import datetime
from tabulate import tabulate
import os
import requests
import json
def getAllPedidos():
    #json-server storage/empleado.json -b 50004
    peticion = requests.get("http://172.16.100.111:50004")
    data = peticion.json()
    return data

# Devuleve un listado con los distintos estados por los q puede pasar un pedido
def getAllEstadosPedido():
    estados = set()
    for val in getAllPedidos():
        estado = val.get("estado")
        if estado not in estados:
            estados.add(estado)
    return estados

# Devuelve un listado con el codigo de pedido,
# codigo de cliente, fecha esperada y
# fecha de entrega de los pedidos q no
# han sido entregados a tiempo

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosAtrasados = []
    for val in getAllPedidos():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
           val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                pedidosAtrasados.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosAtrasados

# Devuelve un listado con el codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos 
# cuya fecha de entrega ha sido al menos dos dias antes de la fecha esperada
def getAllPedidosEntregadosAntesDeTiempo():
    pedidosEntregados = []
    for val in getAllPedidos():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
           val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if (diff.days >= 2):
                pedidosEntregados.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregados


#Devuelve el listado de todos los pedidos q fueron rechazados en 2009 
def getAllPedidosRechazados():
    pedidosRechazados = []
    for val in getAllPedidos():
        if("2009") in val.get("fecha_pedido") and val.get("estado") == ("Rechazado"):
            pedidosRechazados.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pedido": val.get("fecha_pedido"),
                    "estado_pedido": val.get("estado")
                })
    return pedidosRechazados

# Devuelve un listado de todos los pedidos q han sido entregados en el mes de enero de cualquier año
def getAllPedidosEntregadosEnero():
    pedidosEntregadosMes = []
    for val in getAllPedidos():
        fecha_entrega = val.get("fecha_entrega")
        if fecha_entrega:
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            if start.month == 1 and val.get("estado") == "Entregado":
                pedidosEntregadosMes.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                    "estado_pedido": val.get("estado")
                })
    return pedidosEntregadosMes

# Devuelve el comentario del pedido con su codigo
def getAllcodigoPedidoComentario():
    pedidoComentario = []
    for val in getAllPedidos():
        pedidoComentario.append({
            "codigo_pedido": val.get("codigo_pedido"),
            "estado": val.get("estado"),
            "comentario": val.get("comentario"),
        })
    return pedidoComentario
def menu():
   while True:
    print("""
       ____                        __                   __                       ___     __          
      / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  ___  ____/ (_)___/ /___  _____
     / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ _ \/ __  / / __  / __ \/ ___/
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ /  __/ /_/ / / /_/ / /_/ (__  ) 
   /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/\___/\__,_/_/\__,_/\____/____/  
   ___       /_/___            __                            /_/                             
                            0. Salir
                            1. Obtener todos los pedidos atrasados de tiempo
                            2. Obtener todos los pedidos rechasados
                            3. getAllPedidosEntregadosAntesDeTiempo
                            4. Obtener los distintos estados por los que puede pasar un producto
                            5. Obtener los comentarios de los clientes con respecto a su pedido
        """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="fancy_grid"))
    elif(opcion == 2):
        print(tabulate(getAllPedidosRechazados(), headers="keys", tablefmt="github"))
    elif(opcion == 3):
        print(tabulate(getAllPedidosEntregadosAntesDeTiempo(), headers="keys", tablefmt="github"))
    elif(opcion == 4):
        print(tabulate(getAllPedidosEntregadosEnero(), headers="keys", tablefmt="github"))
    elif(opcion == 5):
        print(tabulate(getAllcodigoPedidoComentario(), headers="keys", tablefmt="github"))
    elif(opcion == 0):
        break
    try:
        entrada = input("Ingresa Ctrl + c para ir a menu: ")
        print("Entrada recibida: ", entrada)
    except KeyboardInterrupt:
       menu()