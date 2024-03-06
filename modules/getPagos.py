import storage.pago as pagos
# Devuelve un listado con el codigo de cliente de aquellos clientes q realizaron algun pago en 2008. Tenga en cuenta q debera eliminar aquellos codigos de cliente q aparezcan repetidos.
"""def getAllCodigoClienteFecha():
     = []
    for val in pagos.pago:
        if(val.get("fecha_pago"))== "2008":
            CodigoFecha.append({
                "codigo_cliente": val.get("codigo_cliente")
            })"""
def getAllCodigoClienteFecha():
    CodigoFecha = set()  # Usamos un conjunto para evitar duplicados
    for val in pagos.pago:
        if (val.get("fecha_pago")) == "2008":
            CodigoFecha.add(val.get("codigo_cliente"))

    return list(CodigoFecha)