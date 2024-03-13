from datetime import datetime
from tabulate import tabulate
import json
import requests
import modules.postProducto as pstProducto
import modules.getGamas as gG
#Devuelve un listado con todas los productos q pertenecen a la gama ornamentales
#y q tienen mas de 100 unidades en stock. El listado debera estar ordenado por su precio de venta,
# mostrando en primer lugar los de mayor precio
def getAllData():
    #json-server storage/producto.json -b 50001 
    peticion = requests.get("http://172.16.100.123:50001")
    data = peticion.json()
    return data

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):
            condiciones.append(val)

    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
            condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else val.get("descripcion"),
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor"),

            }
    return condiciones
     
# Obtener la gama, nombre, codigo producto, precio de venta
def getAllGamaCodigoNombre():
    producto =[]
    for val in getAllData():
        
            producto.append({
                "gama": val.get('gama'),
                "nombre": val.get('nombre'),
                "codigo_producto": val.get('codigo_producto'),
                "base": val.get('precio_venta'),
            })
    return producto
# Obtener el nombre del producto y la descripcion de este
def getAllNombreDescripcion():
    descripcion = []
    for val in getAllData():
        descripcion.append({
            "nombre": val.get('nombre'),
            "descripcion": val.get('descripcion'),
            "codigo_producto": val.get('codigo_producto'),
        })
    return descripcion
# Obtener el proveedor del producto y precio
def getAllProveedorPrecio():
    proveedor = []
    for val in getAllData():
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
    for val in getAllData():
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
                            0.  Regresar al menu principal :
                            1. Obtener todos los productos q pertenecen a la gama (ejem Ornamentales) y su cantidad (ejem 100 en stock) :
                            2. Obtener la gama, el nombre del cliente y el codigo de cliente :
                            3. Obtener el nombre del producto y la descripcion de este :
                            4. Obtener el proveedor del producto y precio base :
                            5. Obtener el precio por fabrica y el precio neto individual :
                            6. Crear y guardar
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
    elif(opcion == 6):
        producto = {
            "codigo_producto": input("Ingrese el codigo del producto: "),
            "nombre": input("Ingrese el nombre del producto: "),
            "gama": gG.getAllNombre()[int(input("Seleccione la gama:\n"+"".join([f"\t{i}.{val}\n" for i, val in enumerate(gG.getAllNombre())])))],
            "dimensiones": input("Ingrese las dimensiones del producto: "),
            "proveedor": input("Ingrese el proveedor del producto: "),
            "descripcion": input("Ingrese la descripcion del producto: "),
            "cantidad_en_stock": int(input("Ingrese la cantidad en stock: ")),
            "precio_venta": int(input("Ingrese el precio de ventas: ")),
            "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
        }
        pstProducto.postProducto(producto)
        print("Producto guardado")     
    elif(opcion == 0):
        break
    try:
        entrada = input("Ingresa Ctrl + c para ir a menu: ")
        print("Entrada recibida: ", entrada)
    except KeyboardInterrupt:
       menu()
