import os
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG
import modules.getProducto as gP
import modules.validaciones as vali





BASE_URL = "http://154.38.171.54:5008/productos"

def getAllDataProducto():
    #json-server storage/producto.json -b 5501
    peticion = requests.get("http://154.38.171.54:5008/productos")
    data = peticion.json()
    return data 

def getProductoCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{codigo}")
    return [peticion.json()] if peticion.ok else []

def getCodi(codigo):
    codigoProd = list()
    for val in getAllDataProducto():
        if val.get("codigo_producto") == codigo:
            codigoProd.append(val)
    return codigoProd

def nuevoCodigoProducto():
    codigodelProducto = list()
    for val in getAllDataProducto():
        codigodelProducto.append(val.get("codigo_producto"))
    if codigodelProducto:
        return max(codigodelProducto) + 1
    else:
        return 1

def postProducto():
    
    producto = dict()
    while True: 
        try:
            codigo = nuevoCodigoProducto()
            nombre["codigo_producto"] = codigo
            
            if(not producto.get("codigo_producto")):
                codigo = input("Ingrese el codigo del producto (Ej: OR-251): ")
                if(vali.validacionCodigo(codigo) is not None):
                    data = getCodi(codigo)
                    if(data):
                        print(tabulate(data, headers="keys", tablefmt="github"))
                        raise Exception("El codigo producto ya existe")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception("El codigo producto no cumple con el estandar establecido")
                
            elif (not producto.get("nombre")):
                nombre = input("Ingrese el nombre del producto: ")
                if(vali.validacionNombre(nombre) is not None):
                    producto["nombre"] = nombre
                else:
                    raise Exception("El nombre del producto no cumple con lo establecido")
                
            elif(not producto.get("gama")):
                opcion = input("Seleccione la gama (0-4):\n "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
                if vali.validacionOpciones(opcion):
                    gama = gG.getAllNombre()[int(opcion)]
                    producto["gama"] = gama
                else:
                    raise Exception("La opcion de la gama no cumple con lo establecido")
                
            elif(not producto.get("dimensiones")):
                dimensiones = input("Ingrese las dimensiones del producto (Ej: 240-26): ")
                if(vali.validacionDimension(dimensiones) is not None):
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("La dimension del producto no cumple con lo establecido")
                
            elif(not producto.get("proveedor")):
                proveedor = input("Ingrese el proveedor del producto: ")
                if(vali.validacionNombre(proveedor) is not None):
                    producto["proveedor"] = proveedor
                else:
                    raise Exception("El nombre del proveedor del producto no cumple con lo establecido")
            
            elif(not producto.get("descripcion")):
                descripcion = input("Ingrese una descripcion del producto: ")
                producto["descripcion"] = descripcion

            elif(not producto.get("cantidad_en_stock")):
                cantidadDeStock = input("Ingrese la cantidad de sotck (Ej: 100):  ")
                if(vali.validacionNumerica(cantidadDeStock) is not None):
                    cantidadDeStock = int(cantidadDeStock)
                    producto["cantidad_en_stock"] = cantidadDeStock
                else:
                    raise Exception("El numero de stock del producto no cumple con lo establecido")
                
            elif(not producto.get("precio_venta")):
                precioVenta = input("Ingrese el precio de venta (Ej: 14):  ")
                if(vali.validacionNumerica(precioVenta) is not None):
                    precioVenta = int(precioVenta)
                    producto["precio_venta"] = precioVenta
                else:
                    raise Exception("El numero del precio de venta no cumple con lo establecido")
                
            elif(not producto.get("precio_proveedor")):
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
    peticion = requests.post("http://154.38.171.54:50productos", headers=headers, data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    res["descripcion"] = f'{res.get("descripcion")[:20]}...' if res.get("descripcion") else None
    return [res]



def deleteProducto(id):
    data = getProductoCodigo(id)
    if(len(data)):
        print("Informacion del producto encontrado: ")
        if data.get("descripcion"):
            descripcion = data.get("descripcion")
            data["descripcion"] = f'{descripcion[:8]}...' if len(descripcion) > 20 else descripcion
        print(tabulate([data], headers="keys", tablefmt="github"))
        while True:
            try:
                confirmacion = input("Deseas eliminar este producto?(s/n): ")
                if vali.validacionSiNo(confirmacion):
                    if confirmacion == "s":
                        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
                        if(peticion.ok):
                            return[["messege", "Producto eliminado correctamente"]]
                        break
                    else:
                        return [
                        ["messege", "La eliminacion del producto fue cancelada"],
                        ["status", 200]
                    ]
                else:
                    raise Exception("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)
    else:
        return [["Producto no encontrado", id], 
                ["status", 400 ]
            ]


def updateProductoNombre(id):
    data = gP.getProductCodigo(id)
    if(len(data)):        
        if data.get("descripcion"):
            descripcion = data.get("descripcion")
            data["descripcion"] = f'{descripcion[:8]}...' if len(descripcion) > 20 else descripcion
        print("Producto Encontrado")
        print(tabulate([data], headers="keys", tablefmt="github"))
        continuarActualizar = True
        while continuarActualizar:
            try:

                print("""
                        ¿Que dato deseas cambiar?
                        
                    1. Codigo del producto
                    2. Nombre 
                    3. Gama 
                    4. Dimensiones
                    5. Proveedor
                    6. Descripcion 
                    7. Cantidad en Stock
                    8. Precio Venta
                    9. Precio Proveedor
                    
                """)
                opcion = input("\nSeleccione una de las opciones: ")
                if(vali.validacionOpciones(opcion) is not None):
                    opcion = int(opcion)
                    if(opcion >= 0 and opcion <= 9):
                        if(opcion == 1):
                            while True:
                                try:
                                    codigo = input("Ingrese el codigo del producto: ")
                                    if(vali.validacionCodigo(codigo) is not None):
                                        data2 = getCodi(codigo)
                                        if(data2):
                                            print(tabulate(data2, headers="keys", tablefmt="github"))
                                            raise Exception("El codigo producto ya existe")
                                        else:
                                            data["codigo_producto"] = codigo
                                            break
                                    else:
                                        raise Exception("El codigo producto no cumple con el estandar establecido")
                                except Exception as error:
                                    print(error)
                        
                        if(opcion == 2):
                            while True:
                                try:
                                    nombre = input("Ingrese el nombre del producto: ")
                                    if(vali.validacionNombre(nombre) is not None):
                                        data["nombre"] = nombre
                                        break
                                    else:
                                        raise Exception("El nombre del producto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 3):
                            while True:
                                try:
                                    opcion = input("Seleccione la gama (0-4):\n "+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())]))
                                    if vali.validacionOpciones(opcion):
                                        gama = gG.getAllNombre()[int(opcion)]
                                        data["gama"] = gama
                                        break
                                    else:
                                        raise Exception("La opcion de la gama no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 4):
                            while True:
                                try:
                                    dimensiones = input("Ingrese las dimensiones del producto (Ej: 240-26): ")
                                    if(vali.validacionDimension(dimensiones) is not None):
                                        data["dimensiones"] = dimensiones
                                        break
                                    else:
                                        raise Exception("La dimension del producto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 5):
                            while True:
                                try:
                                    proveedor = input("Ingrese el proveedor del producto: ")
                                    if(vali.validacionNombre(proveedor) is not None):
                                        data["proveedor"] = proveedor
                                        break
                                    else:
                                        raise Exception("El nombre del proveedor del producto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 6):
                            while True:
                                try:
                                    descripcion = input("Ingrese una descripcion del producto: ")
                                    if descripcion:
                                        data["descripcion"] = descripcion
                                        break
                                except Exception as error:
                                    print(error)
                        if(opcion == 7):
                            while True:
                                try:
                                    cantidadDeStock = input("Ingrese la cantidad de sotck (Ej: 100):  ")
                                    if(vali.validacionNumerica(cantidadDeStock) is not None):
                                        cantidadDeStock = int(cantidadDeStock)
                                        data["cantidadEnStock"] = cantidadDeStock
                                        break
                                    else:
                                        raise Exception("El numero de stock del producto no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 8):
                            while True:
                                try:
                                    precioVenta = input("Ingrese el precio de venta (Ej: 14):  ")
                                    if(vali.validacionNumerica(precioVenta) is not None):
                                        precioVenta = int(precioVenta)
                                        data["precio_venta"] = precioVenta
                                        break
                                    else:
                                        raise Exception("El numero del precio de venta no cumple con lo establecido")
                                except Exception as error:
                                    print(error)
                        if(opcion == 9):
                            while True:
                                try:
                                    precioProveedor = input("Ingrese el precio del proveedor (Ej: 11):  ")
                                    if(vali.validacionNumerica(precioProveedor) is not None):
                                        precioProveedor = int(precioProveedor)
                                        data["precio_proveedor"] = precioProveedor
                                        break
                                    else:
                                        raise Exception("El numero del precio del proveedor no cumple con lo establecido")
                                except Exception as error:
                                    print(error)

                        confirmacion = ""            
                        while (confirmacion !=  "s" and confirmacion != "n"):
                            confirmacion = input("Deseas cambiar mas datos?(s/n): ")
                            if vali.validacionSiNo(confirmacion):
                                if confirmacion == "n":
                                    continuarActualizar = False
                                    break
                                else:
                                    confirmacion == "s"
                                    break
                            else:
                                print("La confirmacion no cumple con lo establecido por favor solo s/n")
            except Exception as error:
                print(error)


                
        headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}
        peticion = requests.put(f"http://154.38.171.54:5008/productos/{id}", headers=headers, data=json.dumps(data))
        res = peticion.json()
        res["Mensaje"] = "Producto Actualizado"
        res["descripcion"] = f'{res.get("descripcion")[:8]}...' if res.get("descripcion") else None
        return [res]

    else:
        return [{
                    "message": "Producto no encontrado",
                    "id": id
            }]   


# def postProducto():
#     # json-server storage/producto.json -b 50001
#     producto = dict()
#     while True:
#         try:
#             # expresion regular q valide de una cadena Numeros y Letras en mayusculas pero la cadena es de 6 caracteres los primeros
#             if(not producto.get("codigo_producto")):
#                 codigo = input("Ingrese el codigo del producto")
#                 if(re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo) is not None):
#                     data = gP.getProductCodigo(codigo)
#                     if(data):
#                         print(tabulate(data, headers="keys", tablefmt="github"))
#                         raise Exception("El codigo producto ya existe")
#                     else:
#                         producto["codigo_producto"] = codigo
#                 else:
#                     raise Exception("El codigo no cumple con el estandar establecido")
                
#             #expresion regular q valida de una cadena solo letras pero q las primeras de cada palabra sea en mayusculas
#             if(not producto.get("nombre")):
#                 nombre = input("Ingrese el nombre del producto")
#                 if(re.match(r'^([A-Z][a-z]*\s*)+$', nombre) is not None):
#                     producto["nombre"] = nombre
#                     break
#                 else:
#                     raise Exception("El nombre del producto no cumple con el estandar establecido")


#         except Exception as error:
#             print(error)    


# def ActualizarProducto(id):
#     data = gP.getAllProducto(id)
#     if data is None:
#         print(f"El producto con ID {id} no existe")
#         return    
    
#     while True:
#         print(tabulate(data, headers="keys", tablefmt="pretty"))
#         modificacion = input("Ingrese el campo que desea modificar (Escriba listo para finalizar): ")
#         if modificacion.lower() == "listo":
#             break
#         nuevo_valor = input(f"Ingrese el nuevo valor para {modificacion}: ")
#         if modificacion in data[0]:
#             data[0][modificacion] = nuevo_valor
#         else:
#             print(f"El campo {modificacion} no existe")

#     peticion = requests.put(f"{BASE_URL}/productos/{id}", data=json.dumps(data[0]))
#     return peticion.json()





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
            3. Actualizar el nombre de un producto
            0. Atras
            
        """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 3):
                if(opcion == 1):
                    print(tabulate(postProducto(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 2):
                    idProducto = input("Ingrese el id del producto q desea eliminar: ")
                    print(tabulate(deleteProducto(idProducto), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    
                if(opcion == 3):
                    idProducto = input("Ingrese el id del producto q desea Actualizar: ")
                    
                    print(tabulate(updateProductoNombre(idProducto), headers="keys", tablefmt="pretty"))


                elif(opcion == 0):
                    break 
        input("Presione una tecla para continuar.......")