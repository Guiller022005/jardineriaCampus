import storage.pedido as pedido

# Devuleve un listado con los distintos estados por los q puede pasar un pedido
def getAllEstadosPedido():
    estados = set()
    for val in pedido.pedido:
        estado = val.get("estado")
        if estado not in estados:
            estados.add(estado)
    return estados