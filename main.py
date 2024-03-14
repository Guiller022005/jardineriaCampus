import os
import requests
from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedidos
import modules.getPagos as pago
import modules.getProducto as Repproducto
import modules.postProducto as CRUDproducto

def menuProducto():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __                                 
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __    
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ /     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/ __\__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/      
  ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____                                
 / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/                                
/ /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  )                                 
\__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/                                  
            /_/                                                                                  
        
            1. Reportes de los productos
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal


            """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            Repproducto.menu()
        if(opcion == 2):
            CRUDproducto.menu()
        elif(opcion == 0):
            break

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
                        7. Salir
    """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            cliente.menu()
        elif(opcion == 2):
            oficina.menu()
        elif(opcion == 3):
            empleado.menu()
        elif(opcion == 4):
            pedidos.menu()
        elif(opcion == 5):
            pago.menu()
        elif(opcion == 6):
            menuProducto()
        elif(opcion == 0):
            break

