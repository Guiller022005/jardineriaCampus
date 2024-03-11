import storage.producto as pr
from datetime import datetime
from tabulate import tabulate
#Devuelve un listado con todas los productos q pertenecen a la gama ornamentales
#y q tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in pr.producto:
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price)
    return condiciones
# Obtener la gama, nombre, codigo producto, precio de venta
def getAllGamaCodigoNombre():
    producto =[]
    for val in pr.producto:
        
            producto.append({
                "gama": val.get('gama'),
                "nombre": val.get('nombre'),
                "codigo_producto": val.get('codigo_producto'),
                "precio_venta": val.get('precio_venta'),
            })
    return producto
# Obtener el nombre del producto y la descripcion de este
def getAllNombreDescripcion():
    descripcion = []
    for val in pr.producto:
        descripcion.append({
            "nombre": val.get('nombre'),
            "descripcion": val.get('descripcion'),
            "codigo_producto": val.get('codigo_producto'),
        })
    return descripcion
# Obtener el proveedor del producto y precio
def getAllProveedorPrecio():
    proveedor = []
    for val in pr.producto:
        proveedor.append({
            "codigo_producto": val.get('codigo_producto'),
            "nombre": val.get('nombre'),
            "proveedor": val.get('proveedor'),
            "precio_proveedor": val.get('precio_proveedor'),
        })
    return proveedor
# Obtener el precio por fabrica y el precio neto individual
def getAllPrecioNetoAVenta():
    Precios = []
    for val in pr.producto:
        Precios.append({
            "nombre": val.get('nombre'),
            "codigo_producto": val.get('codigo_producto'),
            "precio_proveedor": val.get('precio_proveedor'),
            "precio_venta": val.get('precio_venta'),

        })
    return Precios


def menu():
   while True:
    print("""
    ____                        __                   __        __                                   __           __            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ____  _________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                             /_/                                                 
                            0.  Regresar al menu principal
                            1. Obtener un listado con los productos q pertenecen a la gama ornamentales
                            2. Obtener la gama, el nombre del cliente y el codigo de cliente
                            3. Obtener el nombre del producto y la descripcion de este
                            4. Obtener el proveedor del producto y precio
                            5. Obtener el precio por fabrica y el precio neto individual
        """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        try:
            gama = str(input("Introduce una gama"))
            stock = int(input("Introduce las unidades en stock"))
            print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="grid"))
        except KeyboardInterrupt:
            return menu()    
    elif(opcion == 2):
        try:
            print(tabulate(getAllGamaCodigoNombre(), headers="keys", tablefmt="github"))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 3):
        try:
              print(tabulate(getAllNombreDescripcion(), headers="keys", tablefmt="github"))
        except KeyboardInterrupt:
            return menu()
    elif(opcion == 4):
        try:
              print(tabulate(getAllProveedorPrecio(), headers="keys", tablefmt="github"))
        except KeyboardInterrupt:
            return menu()    
    elif(opcion == 5):
        try:
              print(tabulate(getAllPrecioNetoAVenta(), headers="keys", tablefmt="github"))
        except KeyboardInterrupt:
            return menu()       
    elif(opcion == 0):
        break
    try:
        entrada = input("Ingresa Ctrl + l para ir a menu: ")
        print("Entrada recibida: ", entrada)
    except KeyboardInterrupt:
       menu()
