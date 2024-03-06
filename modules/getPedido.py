import storage.pedido as pedido

# Devuleve un listado con los distintos estados por los q puede pasar un pedido
def getAllEstadosPedido():
    pedidoEstado = []
    for val in pedido.pedido:
        pedidoEstado.append({
            "codigo_pedido": val.get('codigo_pedido'),
            "estado": val.get('estado')
        })
    return pedidoEstado