import os
import re
import modules.validaciones as vali
import modules.getEmpleado as Reppempleado
import modules.crudEmpleado as CRUDempleado
import modules.getProducto as Repproducto
import modules.crudProducto as CRUDproducto
import modules.getOficina as Reppoficina
import modules.crudOficina as CRUDoficina
import modules.getClients as Reppcliente
import modules.crudCliente as CRUDcliente
import modules.getPedido as Reppedido
import modules.crudPedido as CRUDpedido
import modules.getPagos as Reppagos
import modules.crudPagos as CRUDpagos
import json
import os
import modules.validaciones as vali



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
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    Repproducto.menu()
                if(opcion == 2):
                    CRUDproducto.menu()
                elif(opcion == 0):
                    break

def menuEmpleado():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __                                
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /                                
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /                                 
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /                                  
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/_  \__,_/_/      __               __          
   /  |/  /__  ____  __  __   ____/ /__     / ____/___ ___  ____  / /__  ____ _____/ /___  _____
  / /|_/ / _ \/ __ \/ / / /  / __  / _ \   / __/ / __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / /  / /  __/ / / / /_/ /  / /_/ /  __/  / /___/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/  /_/\___/_/ /_/\__,_/   \__,_/\___/  /_____/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
                                                        /_/                                                                                                            
        
            1. Reportes de los empleados
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal


            """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    Reppempleado.menu()
                if(opcion == 2):
                    CRUDempleado.menu()
                elif(opcion == 0):
                    break

def menuOficina():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __                   
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /                   
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /                    
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /                     
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/                      
                                      __              _____      _                 
   ____ ___  ___  ____  __  __   ____/ /__     ____  / __(_)____(_)___  ____ ______
  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ /_/ / ___/ / __ \/ __ `/ ___/
 / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ (__  ) 
/_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/____/  
                                                                                  
            1. Reportes de las oficinas
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal


            """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    Reppoficina.menu()
                if(opcion == 2):
                    CRUDoficina.menu()
                elif(opcion == 0):
                    break

def menuCliente():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __                             
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  ____ ___  ___  ____  __  __
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / __ `__ \/ _ \/ __ \/ / / /
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / / / / / /  __/ / / / /_/ / 
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/ /_/ /_/\___/_/ /_/\__,_/  
           __             ___            __                                                  
      ____/ /__     _____/ (_)__  ____  / /____                                              
     / __  / _ \   / ___/ / / _ \/ __ \/ __/ _ \                                             
    / /_/ /  __/  / /__/ / /  __/ / / / /_/  __/                                             
    \__,_/\___/   \___/_/_/\___/_/ /_/\__/\___/                                              
                                                                                                                                                    
            1. Reportes de las oficinas
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal


            """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        # if(re.match(r'[0-9]+$', opcion) is not None):
        opcion = int(opcion)
        if(opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    Reppcliente.menu()
                if(opcion == 2):
                    CRUDcliente.menu()
                elif(opcion == 0):
                    break

def menuPedido():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __             
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /             
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /              
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /               
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  ___     __    
   ____ ___  ___  ____  __  __   ____/ /__     ____  ___  ____/ (_)___/ /___ 
  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ _ \/ __  / / __  / __ \/
 / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ /  __/ /_/ / / /_/ / /_/ /
/_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/\___/\__,_/_/\__,_/\____/ 
                                           /_/                                                                          
                                                                                                                                                    
            1. Reportes de las oficinas
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal


            """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    Reppedido.menu()
                if(opcion == 2):
                    CRUDpedido.menu()
                elif(opcion == 0):
                    break    
def menuPagos():
    while True:
        os.system("clear")
        print("""
    ____  _                            _     __               __            
   / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /            
  / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /             
 / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /              
/_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/               
   ____ ___  ___  ____  __  __   ____/ /__     ____  ____ _____ _____  _____
  / __ `__ \/ _ \/ __ \/ / / /  / __  / _ \   / __ \/ __ `/ __ `/ __ \/ ___/
 / / / / / /  __/ / / / /_/ /  / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ (__  ) 
/_/ /_/ /_/\___/_/ /_/\__,_/   \__,_/\___/  / .___/\__,_/\__, /\____/____/  
                                           /_/          /____/                                                                                     
                                                                                                                                                    
            1. Reportes de las oficinas
            2. Guardar, Actualizar y Eliminar productos
            0. Regresar al menu principal


            """)
        opcion = input("\nSeleccione una de las opciones: ")
        if(vali.validacionOpciones(opcion) is not None):
            opcion = int(opcion)
            if(opcion >= 0 and opcion <= 2):
                if(opcion == 1):
                    Reppagos.menu()
                if(opcion == 2):
                    CRUDpagos.menu()
                elif(opcion == 0):
                    break      