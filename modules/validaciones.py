import re

def validacionOpciones(opcion):
    val = re.match(r'[0-9]+$', opcion)
    return val

def validacionCodigo(codigo):
    val = re.match(r'^[A-Z]{2}-[0-9]{3}$', codigo)
    return val

def validacionCoidgoOficina(codigo):
    val = re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo)
    return val

def validacionNombre(nombre):
    val = re.match(r'^([A-ZÑ][a-zñ]*\s*)+$', nombre)
    return val

def validacionDimension(dimensiones):
    val = re.match(r'^\s*[0-9]+\s*-\s*[0-9]+\s*$', dimensiones)
    return val

def validacionNumerica(numero):
    val = re.match(r'^\s*\d+(\.\d+)?\s*$', numero)
    return val

def validacionNumero(numero):
    val = re.match(r'^\s*(\+\d{1,3}\s*)?\s*(\(\d+\))?\s*\d+(?:[\s-]?\d+)*\s*$', numero)
    return val

def validacionFecha(fecha):
    val = re.match(r'^\d{4}-\d{2}-\d{2}$', fecha)
    return val

def validaiconTransccion(transccion):
    val = re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', transccion)
    return val

def validacionSiNo(confirmacion):
    val = re.match(r'^[sn]$', confirmacion)
    return val