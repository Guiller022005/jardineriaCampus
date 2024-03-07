import storage.pedido as pe
from datetime import datetime
# Devuleve un listado con los distintos estados por los q puede pasar un pedido
"""def getAllEstadosPedido():
    estados = set()
    for val in pedido.pedido:
        estado = val.get("estado")
        if estado not in estados:
            estados.add(estado)
    return estados
"""
# Devuelve un listado con el codigo de pedido,
# codigo de cliente, fecha esperada y
# fecha de entrega de los pedidos q no
# han sido entregados a tiempo

def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
           val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if(diff.days < 0):
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregado

# Devuelve un listado con el codigo de pedido, codigo de cliente, fecha esperada y fecha de entrega de los pedidos cuya fecha de entrega de
# los pedidos cuya fecha de entrega ha sido al menos dos dias antes de la fecha esperada
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for val in pe.pedido:
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
           val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if (diff.days >= 2):
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_de_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega")
                })
    return pedidosEntregado


#Devuelve el listado de todos los pedidos q fueron rechazados en 2009 
def getAllPedidosRechazados():
    pedidosRechazados = []
    for val in pe.pedido:
        if("2009") in val.get("fecha_pedido") and val.get("estado") is ("Rechazado"):
            pedidosRechazados.append({
                    "codigo_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pedido": val.get("fecha_pedido"),
                    "estado_pedido": val.get("estado")
                })
    return pedidosRechazados