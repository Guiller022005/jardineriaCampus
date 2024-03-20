import os
import re
import requests
from tabulate import tabulate
import modules.menu as me
import modules.validaciones as vali
import json



if(__name__ == "__main__"):
    #https://patorjk.com/software/taag/#p=display&h=2&v=2&f=Slant&t=Men%C3%BA%20principal%0A1.%20cliente%0A2.%20oficina%0A3.%20empleado%0A4.%20pedidos%0A
    while True:
        os.system("clear")
        print("""
    __  ___             __                _            _             __
   /  |/  /__  ____  __/_/_   ____  _____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / __ \/ ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / /_/ / /  / / / / / /__/ / /_/ / /_/ / /  
/_/__/_/\___/_/ /_/\__,_/  / .___/_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
  <  /    _____/ (_)__  __/_/   / /____             /_/               
          

                        1. Cliente
                        2. Oficina
                        3. Empleado
                        4. Pedidos
                        5. Pagos
                        6. Productos
                        0. Salir
    """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 6):
                if (opcion == 1):  
                    me.menuCliente()
                elif(opcion == 2):
                    me.menuOficina()
                elif(opcion == 3):
                    me.menuEmpleado()
                elif(opcion == 4):
                    me.menuPedido()
                elif(opcion == 5):
                    me.menuPagos()
                elif(opcion == 6):
                    me.menuProducto()
                elif(opcion == 0):
                    break
        

# with open("storage/cliente.json", "r") as f:
#     fichero = f.read()
#     data = json.loads(fichero)
#     for i, val in enumerate(data):
#         data[i]["id"] = (i+1)
#     data = json.dumps(data, indent=4).encode("utf-8")
# with open("storage/cliente.json", "wb+") as f1:
#     f1.write(data)
#     f1.close()
    




#import sys 
#def menu():
#    contador = 1
#    print("Menu Principal")
#    for nombre, objeto in sys.modules.items():
#        if nombre.startswith("modules"):
#            modulo = getattr(objeto, "name", None)
#            if(modulo != "modules"):
#                contador += 1
#
#menu()