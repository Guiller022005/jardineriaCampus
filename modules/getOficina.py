import storage.oficina as of
#Devuelve un listado con el codigo de
#oficina y la ciudad donde hat oficinas

def getAllCodigoCiudad():
    codigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            "codigo": val.get("codigo_oficina"),
            "ciudad": val.get("ciudad")
        })
    return codigoCiudad

#Devuelve un listado con la ciudad y el telefono
#de las oficinas de españa
def getAllCiudadTelefono(pais):
    ciudadTelefono = []
    for val in of.oficina:
        if(val.get("pais")== pais):
            ciudadTelefono.append({
            "ciudad": val.get("ciudad"),
            "telefono": val.get("telefono"),
            "oficinas": val.get("codigo_oficina"),
            "pais": val.get("pais")
        })
    return ciudadTelefono

def menu():
    print("""
                
                                                   ____                        __                   __        ____  _____      _                
      / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / __ \/ __(_)____(_)___  ____ _    
     / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / / / /_/ / ___/ / __ \/ __ `/    
    / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / __/ / /__/ / / / / /_/ /     
   /_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/   \____/_/ /_/\___/_/_/ /_/\__,_/      
   ___       /_/___            __                                                                                   

                            1. Obtener todos los clientes (codigo y nombre)
                            2. Obtenerun cliente por su codigo (codigo y nombre)
                            3. Obtener toda la informacion de un cliente segun su limite de credito y ciudad que pertenece (ejem: 3000.0, San Francisco)
    """)