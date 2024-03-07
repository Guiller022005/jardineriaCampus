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
    CodigoFecha = []
    codigos_vistos = set()  # Usamos un conjunto para evitar duplicados
    for val in pagos.pago:
        if "2008" in val.get("fecha_pago"):
            Codigo_cliente = val.get("codigo_cliente")
    if ("codigo_cliente ")not in codigos_vistos:
        CodigoFecha.append(
            {
            "codigo_cliente": ("codigo_cliente"),
            "fecha": val.get("fecha_pago"),
            "total": val.get("tatal")
            }
        )
        codigos_vistos.add("codigo_cliente")
    return CodigoFecha