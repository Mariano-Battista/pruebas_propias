
from auth import verify_admin
from base_de_datos import base_de_datos
from mensajes_consola import formatear_mensaje_consola



def nuevo_dispositivo():
    if(verify_admin()==False):
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        return
    else:    
        formatear_mensaje_consola("--- Registro de Dispositivo ---")
        nombre = input("Ingrese Nombre del dispositivo: ").strip().lower()
        tipo = input("Tipo de dispositivo: ").strip().lower()
        id_vivienda = int(input("Ingrese el id de la vivienda")) #Hacer validaciones!!
        ubicacion = input("Ubicación del dispositivo: ").strip().lower()
        
        nuevo_dispositivo = {
            "id":len(base_de_datos["dispositivos"])+1,
            "nombre": nombre,
            "tipo": tipo,
            "id_vivienda": id_vivienda,
            "ubicacion": ubicacion,
            "estado": False,
        }
        base_de_datos["dispositivos"].append(nuevo_dispositivo)
        formatear_mensaje_consola(f"Dispositivo {nombre} registrado con éxito.")



def listar_dispositivos(id_vivienda=None):
    formatear_mensaje_consola("--- Lista de Dispositivos ---")

    dispositivos = base_de_datos.get("dispositivos", [])

    # Filtrar si se proporciona id_vivienda
    if id_vivienda is not None:
        dispositivos = [d for d in dispositivos if d.get("id_vivienda") == id_vivienda]

    # Verificar si hay dispositivos para mostrar
    if not dispositivos:
        formatear_mensaje_consola("No hay dispositivos registrados" if id_vivienda is None 
                                  else f"No hay dispositivos registrados para la vivienda con ID {id_vivienda}")
        return

    # Mostrar todos los dispositivos de la base de datos
    for dispositivo in dispositivos:
        formatear_mensaje_consola(
            f"id: {dispositivo["id"]} ,Nombre: {dispositivo["nombre"]}, Tipo: {dispositivo["tipo"]}, "
            f"id_vivienda: {dispositivo["id_vivienda"]}, Ubicación: {dispositivo["ubicacion"]}, Estado: {dispositivo["estado"]}"
        )


def buscar_dispositivo(id=None):
    formatear_mensaje_consola("--- Buscar Dispositivo ---")
    if id == None:
       id = int(input("Ingrese id del dispositivo: "))

    encontrado = False  # bandera
    if id is not None:

        for dispositivo in base_de_datos["dispositivos"]:
            if id == dispositivo["id"]:
                formatear_mensaje_consola(f"id: {dispositivo["id"]} ,Nombre: {dispositivo["nombre"]}, Tipo: {dispositivo["tipo"]}, Ubicación: {dispositivo["ubicacion"]}, Estado: {dispositivo["estado"]}")
                encontrado = True
                break

    if not encontrado:
        formatear_mensaje_consola(f"Dispositivo {id} no encontrado.")

def eliminar_dispositivo():
    if(verify_admin()==False):
        formatear_mensaje_consola("No tiene permisos para realizar esta acción")
        
        return
    else:
        formatear_mensaje_consola("--- Eliminar Dispositivo ---")
        id = int(input("Ingrese ID del dispositivo: "))
        for dispositivo in base_de_datos["dispositivos"]:
            if dispositivo["id"] == id:
                base_de_datos["dispositivos"].remove(dispositivo)
                formatear_mensaje_consola(f"Dispositivo {dispositivo["nombre"]} eliminado con éxito.")
           
def activar_desactivar_dispositivo():
    try:
        id_dispositivo = int(input("Ingrese el ID del dispositivo que desea activar o desactivar: "))
    except ValueError:
        formatear_mensaje_consola("El ID ingresado no es válido.")
        return

    dispositivo = None
    for d in base_de_datos.get("dispositivos", []):
        if d["id"] == id_dispositivo:
            dispositivo = d
            break

    if not dispositivo:
        formatear_mensaje_consola(f"No se encontró un dispositivo con ID {id_dispositivo}.")
        return

    # Alternar el estado del dispositivo
    dispositivo["estado"] = not dispositivo["estado"]

    estado_str = "encendido" if dispositivo["estado"] else "apagado"
    formatear_mensaje_consola(f"El dispositivo '{dispositivo["nombre"]}' ahora está {estado_str}.")
