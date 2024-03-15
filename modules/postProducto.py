import os
import re
from tabulate import tabulate
import json
import requests
import modules.getGamas as gG
import modules.getProducto as gP
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

#     producto = {
#             "codigo_producto": input("Ingrese el codigo del producto: "),
#             "nombre": input("Ingrese el nombre del producto: "),
#             "gama": gG.getAllNombre()[int(input("Seleccione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
#             "dimensiones": input("Ingrese las dimensiones del producto: "),
#             "proveedor": input("Ingrese el proveedor del producto: "),
#             "descripcion": input("Ingrese la descripcion del producto: "),
#             "cantidad_en_stock": int(input("Ingrese la cantidad en stock: ")),
#             "precio_venta": int(input("Ingrese el precio de ventas: ")),
#             "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
# }
    # headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    # peticion = requests.post("http://172.16.100.111:50006",headers=headers, data=json.dumps(producto, indent=4).encode("UTF-8"))
    # res = peticion.json()
    # res["Mensaje"] = "Producto Guardado"
    # return [res]

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
            0. Atras
            
        """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(re.match(r'[0-9]+$', opcion) is not None):
            opcion = int(opcion)
            if (opcion >= 0 and opcion <= 1):
                if(opcion == 1):
                
                    print(tabulate(postProducto(), headers="keys", tablefmt="github"))
                    input("Presione una tecla para continuar......")
                    break
                
                elif(opcion == 0):
                    break 