from base_de_datos import base_de_datos
from mensajes_consola import *

def crear_vivienda(correo=None):
    if correo==None:
        correo = input("Ingrese correo electrónico: ").strip().lower()
        id_usuario = None

    for u in base_de_datos['usuarios']:
        if u["correo"].lower() == correo:
            id_usuario = u["id"]
            break

    if id_usuario is None:
        print("Usuario no encontrado. Verifique el correo.")
        return

    direccion = input("Ingrese dirección: ").strip().lower()
    codigo_postal = input("Ingrese el código postal: ").strip().lower()
    nueva_vivienda = {
        "id": len(base_de_datos['viviendas']) + 1,
        "direccion": direccion,
        "codigo_postal": codigo_postal,
        "id_usuario": id_usuario
    }

    base_de_datos['viviendas'].append(nueva_vivienda)
    formatear_mensaje_consola("Vivienda agregada con exito.")

def mostrar_viviendas():
    for v in base_de_datos['viviendas']:
        print(v)

def buscar_viviendas_por_usuario(correo=None):
    if correo == None:
         correo = input("Ingrese correo de usuario: ").strip().lower()
    else:
        correo = correo
    id_usuario = None
    
    for u in base_de_datos['usuarios']: # Buscar ID del usuario por correo
        if u['correo'].lower() == correo:
            id_usuario = u['id']
            break

    if id_usuario is None: 
        print("Usuario no encontrado.")
        return 
    
    viviendas_encontradas = [ # Buscar viviendas asociadas al ID del usuario
        v for v in base_de_datos['viviendas'] if v['id_usuario'] == id_usuario
    ]

    if viviendas_encontradas: # Imprimir resultados
        formatear_mensaje_consola(f" Viviendas del usuario con correo '{correo}':")
        for v in viviendas_encontradas:
            formatear_mensaje_consola(f" - ID: {v['id']}, Dirección: {v['direccion']}, Código Postal: {v['codigo_postal']}")
    else:
        print("Este usuario no tiene viviendas registradas.")
    
    return viviendas_encontradas