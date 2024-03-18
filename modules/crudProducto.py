import os
import re
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG
import modules.getProducto as gP
import modules.validaciones as vali
def postProducto():
    # json-server storage/producto.json -b 50001
    producto = dict()
    while True:
        try:
            # expresion regular q valide de una cadena Numeros y Letras en mayusculas pero la cadena es de 6 caracteres los primeros
            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto")
                if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
                    data = gP.getProductCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception("El codigo no cumple con el estandar establecido")
                
            #expresion regular q valida de una cadena solo letras pero q las primeras de cada palabra sea en mayusculas
            if(not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto")
                if(re.match(r'^([A-Z][a-z]*\s*)+$', nombre) is not None):
                    producto["nombre"] = nombre
                    break
                else:
                    raise Exception("El nombre del producto no cumple con el estandar establecido")


        except Exception as error:
            print(error)    
def deleteProducto(id):
    data = gP.getProductCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.100.120:50006/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"mensage": "producto eliminado correctamente"})
            return {
            "body": data,
            "status": peticion.status_code,
            }
    else:
        return {
            "body": [{
                "mensage": "producto no encontrado",
                "id": id
            }],
            "status": 400,
        }
def getAllData():
    #json-server storage/producto.json -b 5501
    peticion = requests.get("http://localhost:5501/productos")
    data = peticion.json()
    return data 

def getProductoCodigo(codigo):
    peticion = requests.get(f"http://localhost:5501/productos/{codigo}")
    return [peticion.json()] if peticion.ok else []

def postProducto():
    
    producto = dict()
    while True: 
        try:

            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto (Ej: OR-251): ")
                if(vali.validacionCodigo(codigo) is not None):
                    data = getProductoCodigo(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception("El codigo producto no cumple con el estandar establecido")
                
            if(not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto: ")
                if(vali.validacionNombre(nombre) is not None):
                    producto["nombre"] = nombre
                else:
                    raise Exception("El nombre del producto no cumple con lo establecido")
                
            if(not producto.get("gama")):
                opcion = input("Seleccione la gama (0-4):\n "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
                if vali.validacionOpciones(opcion):
                    gama = gG.getAllNombre()[int(opcion)]
                    producto["gama"] = gama
                else:
                    raise Exception("La opcion de la gama no cumple con lo establecido")
                
            if(not producto.get("dimensiones")):
                dimensiones = input("Ingrese las dimensiones del producto (Ej: 240-26): ")
                if(vali.validacionDimension(dimensiones) is not None):
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("La dimension del producto no cumple con lo establecido")
                
            if(not producto.get("proveedor")):
                proveedor = input("Ingrese el proveedor del producto: ")
                if(vali.validacionNombre(proveedor) is not None):
                    producto["proveedor"] = proveedor
                else:
                    raise Exception("El nombre del proveedor del producto no cumple con lo establecido")
            
            if(not producto.get("descripcion")):
                descripcion = input("Ingrese una descripcion del producto: ")
                producto["descripcion"] = descripcion

            if(not producto.get("cantidad_en_stock")):
                cantidadDeStock = input("Ingrese la cantidad de sotck (Ej: 100):  ")
                if(vali.validacionNumerica(cantidadDeStock) is not None):
                    cantidadDeStock = int(cantidadDeStock)
                    producto["cantidad_en_stock"] = cantidadDeStock
                else:
                    raise Exception("El numero de stock del producto no cumple con lo establecido")
                
            if(not producto.get("precio_venta")):
                precioVenta = input("Ingrese el precio de venta (Ej: 14):  ")
                if(vali.validacionNumerica(precioVenta) is not None):
                    precioVenta = int(precioVenta)
                    producto["precio_venta"] = precioVenta
                else:
                    raise Exception("El numero del precio de venta no cumple con lo establecido")
                
            if(not producto.get("precio_proveedor")):
                precioProveedor = input("Ingrese el precio del proveedor (Ej: 11):  ")
                if(vali.validacionNumerica(precioProveedor) is not None):
                    precioProveedor = int(precioProveedor)
                    producto["precio_proveedor"] = precioProveedor
                    break
                else:
                    raise Exception("El numero del precio del proveedor no cumple con lo establecido")


        except Exception as error:
            print(error)
            
    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
    peticion = requests.post("http://localhost:5501", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def deleteProducto(id):
    data = getProductoCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://localhost:5501/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code, 
            }
    else:
        return {
                "body":[{
                    "message": "Producto no encontrado",
                    "id" : id
                }],
                "status": 400,
            }   
def menu():
    while True:
        os.system("clear")
        print("""  
    ___       __          _       _      __                         __      __                    __        
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \     
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/      
    ____  ____  ____  ____  __  __________________  _____                                                   
   / __ \/ __ \/ __ \/ __ \/ / / / ____/_  __/ __ \/ ___/                                                   
  / /_/ / /_/ / / / / / / / / / / /     / / / / / /\__ \                                                    
 / ____/ _, _/ /_/ / /_/ / /_/ / /___  / / / /_/ /___/ /                                                    
/_/   /_/ |_|\____/_____/\____/\____/ /_/  \____//____/                                                     
                                                                                                                                                    
            1. Guardar un producto nuevo
            2. Eliminar un producto
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    print(tabulate(postProducto(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    break
                if(opcion == 2):
                    idProducto = input("Ingrese el id del producto q desea eliminar: ")
                    print(tabulate(deleteProducto(idProducto)), headers="keys", tablefmt="github")
                    input("Presione una tecla para continuar......")
                    break
                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar")