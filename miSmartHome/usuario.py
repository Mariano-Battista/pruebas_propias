from base_de_datos import base_de_datos
from auth import * 
from states import states

def crear_usuario():
    nombre = input("Ingrese Nombre de usuario: ").strip().lower()
    contraseña = input("Ingrese una contraseña: ").strip().lower()
    correo = input("Ingrese correo electronico: ").strip().lower()
    rol = input("Ingrese rol del usuario (admin/estandar): ").strip().lower()
    nuevo_usuario = {
        "id": len(base_de_datos['usuarios']) + 1,
        "nombre": nombre,
        "contraseña": contraseña,
        "correo": correo,
        "Role": rol
    }
    base_de_datos['usuarios'].append(nuevo_usuario)
    formatear_mensaje_consola("Se agrego usuario con exito.")

def eliminar_usuario():
    nombre = input("Ingrese el nombre del usuario a eliminar: ").strip().lower()
    
    for u in base_de_datos['usuarios']:
        if u["nombre"] == nombre:
            if u["Role"] != "admin":
                if(verify_admin()==False):
                    formatear_mensaje_consola("Contraseña de admin incorrecta. No tiene permisos para realizar esta acción")
                    return
                base_de_datos['usuarios'].remove(u)
                print(f"Usuario eliminado: {u}")
                return
            else:
                formatear_mensaje_consola("No puede eliminar un usuario con perfil de admin")
                return
    formatear_mensaje_consola("Usuario no encontrado.")

def listar_usuarios():                          
    for u in base_de_datos['usuarios']:
        print(u)

def cambiar_rol():
    if(verify_admin()==False):
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        return
    nombre=input("ingrese nombre de usuario: ").strip().lower()
    if(nombre=="admin"):
        formatear_mensaje_consola("No se puede cambiar el rol de admin")
        return
    if(nombre==states['nombre']):
        formatear_mensaje_consola("No se puede cambiar el rol de usted mismo")
        return
    for usuario in base_de_datos['usuarios']:
        if (usuario['nombre']==nombre and usuario["Role"]=='estandar') :
            usuario['Role']='admin'
            formatear_mensaje_consola(f"se cambia el rol de {usuario['nombre']} a admin")
            return
        elif (usuario['nombre']==nombre and usuario["Role"]=='admin'):
            usuario['Role']='estandar'
            formatear_mensaje_consola(f"se cambia el rol de {usuario['nombre']} a estandar")
            return
    else:
        formatear_mensaje_consola("Usuario no encontrado")