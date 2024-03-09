import storage.pago as pagos

# Devuelve un listado con el codigo de cliente de aquellos clientes q realizaron algun pago en 2008. Tenga en cuenta q debera eliminar aquellos codigos de cliente q aparezcan repetidos.
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

# Devuelve un listado con todos los pagos q se realizaron en en el año 2008 mediante paypal, ordena el resultado de mayor a menor
def getAllPagosFecha():
    pagosFecha = []
    for val in pagos.pago:
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") is ("PayPal"):
            pagosFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagosFecha = sorted(pagosFecha, key=lambda x: x ["total"], reverse=True)
    return pagosFecha

# Devuelve un listadocon todas las formas de pago q aparecen en la tabla pago. Tenga en cuenta q no deben aparecer formas de pago repetidas
def getAllFormasDePago():
    tipoPago = set()
    for val in pagos.pago:
        formaPago = val.get("forma_pago")
        if formaPago not in tipoPago:
            tipoPago.add(formaPago)
    return tipoPago

# Devuelve un listado con todos los productos q pertenecen a la gama Ornamentales y q tienen mas de 100 unidades en shok.
# El listado debera estar ordenado por su precio de venta, mostrarlo en primer lugar los de mayor precio

def menu():
    print("""
                
       ____                        __                   __                                    
      / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  ____ _____ _____  _____
     / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ __ `/ __ `/ __ \/ ___/
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  ) 
   /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/\__,_/\__, /\____/____/  
   ___       /_/___            __                            /_/          /____/   
                            1. Obtener todos los clientes (codigo y nombre)
                            2. Obtenerun cliente por su codigo (codigo y nombre)
                            3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0, San Francisco)
    """)
    