from base_de_datos import base_de_datos
from auth import * 
from states import states

def crear_usuario():
    nombre = input("Ingrese Nombre de usuario: ").strip().lower()
    contraseña = input("Ingrese una contraseña: ").strip().lower()
    correo = input("Ingrese correo electronico: ").strip().lower()
    rol = input("Ingrese rol del usuario (admin/estandar): ").strip().lower()
    nuevo_usuario = {
        "id": len(base_de_datos["usuarios"]) + 1,
        "nombre": nombre,
        "contraseña": contraseña,
        "correo": correo,
        "Role": rol
    }
    base_de_datos["usuarios"].append(nuevo_usuario)
    formatear_mensaje_consola("Se agrego usuario con exito.")

def eliminar_usuario():
    correo = input("Ingrese el correo del usuario a eliminar: ").strip().lower()
    
    for u in base_de_datos["usuarios"]:
        if u["correo"] == correo:
            if u["Role"] != "admin":
                if(verify_admin()==False):
                    formatear_mensaje_consola("Contraseña de admin incorrecta. No tiene permisos para realizar esta acción")
                    return
                base_de_datos["usuarios"].remove(u)
                print(f"Usuario eliminado: {u}")
                return
            else:
                formatear_mensaje_consola("No puede eliminar un usuario con perfil de admin")
                return
    formatear_mensaje_consola("Usuario no encontrado.")

def listar_usuarios():                          
    for u in base_de_datos["usuarios"]:
        print(u)

def mostrar_datos_usuario(correo=None):
    if correo is None:
        correo = input("Ingrese correo del usuario a verificar: ").strip().lower()
    
    # Buscar usuario por correo
    usuario = next((u for u in base_de_datos["usuarios"] if u["correo"] == correo), None)

    if usuario:
        formatear_mensaje_consola("--- Datos del Usuario ---")
        formatear_mensaje_consola(f"ID: {usuario['id']}")
        formatear_mensaje_consola(f"Nombre: {usuario['nombre']}")
        formatear_mensaje_consola(f"Correo: {usuario['correo']}")
        formatear_mensaje_consola(f"Rol: {usuario['Role']}")
    else:
        formatear_mensaje_consola("No se encontró un usuario con ese correo.")

def cambiar_rol():
    if verify_admin() == False:
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        return
    
    correo = input("ingrese el correo de usuario: ").strip().lower()
    
    if correo == "admin@mail.com":
        formatear_mensaje_consola("No se puede cambiar el rol del administrador del software")
        return
    
    if correo == states["correo"]:
        formatear_mensaje_consola("No se puede cambiar el rol de usted mismo")
        return

    encontrado = False  # bandera

    for usuario in base_de_datos["usuarios"]:
        if usuario["correo"] == correo:
            encontrado = True
            if usuario["Role"] == "estandar":
                usuario["Role"] = "admin"
                formatear_mensaje_consola(f"Se cambia el rol de {usuario['nombre']} a admin")
            else:
                usuario["Role"] = "estandar"
                formatear_mensaje_consola(f"Se cambia el rol de {usuario['nombre']} a estandar")
            break  
    
    if not encontrado:
        formatear_mensaje_consola("Usuario no encontrado")