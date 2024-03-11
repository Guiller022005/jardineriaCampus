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

def getAllGamaCodigoNombre():
    producto =[]
    for val in pr.producto:
        
            producto.append({
                "codigo_cliente": val.get('codigo_cliente'),
                "nombre_cliente": val.get('nombre_cliente'),

            })
           



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
        """)
    opcion = int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        gama = str(input("Introduce una gama"))
        stock = int(input("Introduce las unidades en stock"))
        print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="grid"))
    
    elif(opcion == 0):
        break
    try:
        entrada = input("Ingresa Ctrl + l para ir a menu: ")
        print("Entrada recibida: ", entrada)
    except KeyboardInterrupt:
       menu()
