import states
from usuario import * 
from viviendas import * 
from automatizaciones import * 
from dispositivos import *


#-------------MENU PRINCIPAL-------------
def mostrar_opciones_principal_de_app():
    if(states['is_auth']==False):
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")


#------------MENU ADMIN------------------#
def menu_admin():
    formatear_mensaje_consola("MENU ADMIN")
    print("1. Usuarios")
    print("2. Viviendas")
    print("3. Dispositivos")
    print("4. Automatizaciones")
    print("5. Regresar al menu anterior")
    
    opcion_admin = input('Ingrese una opcion: ')
    if(opcion_admin == '1'):
        menu_usuario()
    elif(opcion_admin == '2'):
        menu_vivienda()
    elif(opcion_admin == '3'):
        menu_dispositivo()
    elif(opcion_admin=="4"):
        menu_automatizacion()
    elif(opcion_admin=="5"):
        logout()
#--------------MENU ESTANDAR--------------#
def menu_estandar():
    while True:
        formatear_mensaje_consola("Mis viviendas")
        viviendas_encontradas = buscar_viviendas_por_usuario(correo=states['correo'])
        if viviendas_encontradas == []:
            crear_vivienda(correo=states['correo'])
            viviendas_encontradas = buscar_viviendas_por_usuario(correo=states['correo'])
            
        opcion_admin = input('Ingrese el ID de la vivienda que quiere revisar : ')
        if(opcion_admin == '1'):
            menu_usuario()

#--------------MENU USUARIOS--------------#
def menu_usuario():
    while True:
        formatear_mensaje_consola("MENU USUARIOS")
        print("1. Crear nuevo usuario")
        print("2. Eliminar usuario existente")
        print("3. Mostrar todos los usuarios")
        print("4. Cambiar Rol a un usuario")
        print("5. Regresar al menu anterior")

        opcion_usuarios = input('Ingrese una opcion: ')
        if(opcion_usuarios == '1'):
            crear_usuario()
        elif(opcion_usuarios == '2'):
            eliminar_usuario()
        elif(opcion_usuarios == '3'):
            listar_usuarios()
        elif(opcion_usuarios=="4"):
            cambiar_rol()
        elif(opcion_usuarios=="5"):
            break

#--------------MENU VIVIENDAS--------------#
def menu_vivienda():
    while True:
        formatear_mensaje_consola("MENU VIVIENDAS")
        print("1. Crear Vivienda")
        print("2. Mostrar todas las viviendas")
        print("3. Mostrar viviendas de un usuario")
        print("4. Regresar al menu anterior")
    
        opcion_vivienda=input('Ingrese una opcion: ')
        if(opcion_vivienda == '1'):
            crear_vivienda()
        elif(opcion_vivienda == '2'):
            mostrar_viviendas()
        elif(opcion_vivienda == '3'):
            buscar_viviendas_por_usuario()
        elif(opcion_vivienda =="4"):
            break

#--------------MENU DISPOSITIVOS--------------#
def menu_dispositivo():
    while True:
        formatear_mensaje_consola("MENU DISPOSITIVOS")
        print("1. Crear Dispositivo")
        print("2. Eliminar Dispositivo")
        print("3. Mostrar todos los dispositivos")
        print("4. Buscar un dispositivo")
        print("5. Regresar al menu anterior")

        opcion_dispositivo=input('Ingrese una opcion: ')
        if(opcion_dispositivo == '1'):
            nuevo_dispositivo()
        elif(opcion_dispositivo == '2'):
            eliminar_dispositivo()
        elif(opcion_dispositivo == '3'):
            listar_dispositivos()
        elif(opcion_dispositivo=="4"):
            buscar_dispositivo()    
        elif(opcion_dispositivo =="5"):
            break   

#--------------MENU AUTOMATIZACIONES--------------#
def menu_automatizacion():
    while True:
        formatear_mensaje_consola("MENU AUTOMATIZACIONES")
        print("1. Crear nueva automatizacion")
        print("2. Eliminar automatizacion existente")
        print("3. Mostrar todos las automatizaciones")
        print("4. Modificar una automatizacion")
        print("5. Regresar al menu anterior")

        opcion_automatizacion = input('Ingrese una opcion: ')
        if(opcion_automatizacion == '1'):
            crear_usuario()
        elif(opcion_automatizacion == '2'):
            eliminar_usuario()
        elif(opcion_automatizacion == '3'):
            listar_usuarios()
        elif(opcion_automatizacion=="4"):
            cambiar_rol()
        elif(opcion_automatizacion=="5"):
            break

# # REDISEÑAR ESTO DE ABAJO OPCIONES ESTANDAR, CREAR MENUES
"""""

def mostrar_opciones_para_estandar():
    #Permitir consultar los datos personales.
    #Permitir activar/ejecutar/”configurar”(debería estar predefinida) la automatización.
    #Permitir consultar dispositivos.
    print("1. Listar dispositivos")
    print("2. Consultar Perfil")
    print("3. Consultar automatizaciones activas")
    print("4. Activar/desactivar automatizaciones")
    print("5. Cerrar sesión")

def llamar_opciones_para_estandar():
    opcion=input('Ingrese una opcion: ')
    if(opcion == '1'):
        listar_dispositivos()
    elif(opcion == '2'):
        consultar_perfil()
    elif(opcion == '3'):
        consultar_automatizaciones_activas()
    elif(opcion == '4'):
        menu_automatizaciones()
    elif(opcion == '5'):
        logout()
"""