import datetime
from utils import buscar_automatizacion_por_id,esta_en_rango_horario
from base_de_datos import base_de_datos
from mensajes_consola import formatear_mensaje_consola
from auth import * 
from dispositivos import buscar_dispositivo

def crear_automatizacion():
    formatear_mensaje_consola("--- Registro de Automatizacion ---")
    nombre = input("Ingrese Nombre de la automatizacion: ").strip().lower()
    id_vivienda = int(input("Ingrese el id de la vivienda")) #Hacer validaciones!!
    hora_inicio = input("Ingrese el horario de inicio (HH:MM): ").strip().lower()#Hacer validaciones!!
    hora_fin = input("Ingrese el horario de finalizacion (HH:MM): ").strip().lower()#Hacer validaciones!!
    id_dispositivo = int(input("Ingrese el id del dispositivo que desea automatizar: "))    
    
    nueva_automatizacion = {
    "id":len(base_de_datos["automatizaciones"])+1,
    "nombre": nombre,
    "id_vivienda": id_vivienda,
    "hora_inicio":hora_inicio,
    "hora_fin":hora_fin,
    "id_dispositivo":id_dispositivo,
    "estado":"activo"
    }
    base_de_datos["automatizaciones"].append(nueva_automatizacion)
    formatear_mensaje_consola(f"Automatizacion {nombre} registrada con éxito.")

def eliminar_automatizacion():
        formatear_mensaje_consola("--- Eliminar Automatizacion ---")
        id_automatizacion = int(input("Ingrese el id de la automatizacion que desea eliminar: "))
        for automatizacion in base_de_datos["automatizaciones"]:
            if automatizacion["id"] == id_automatizacion:
                base_de_datos["automatizaciones"].remove(automatizacion)
                formatear_mensaje_consola(f"Automatizacion {id_automatizacion} eliminada con éxito.")

def listar_automatizaciones(id_vivienda=None):  #revisar
    formatear_mensaje_consola("--- Lista de Automatizaciones ---")

    automatizaciones = base_de_datos.get("automatizaciones", [])

    # Filtrar si se proporciona id_vivienda
    if id_vivienda is not None:
        automatizaciones = [a for a in automatizaciones if a.get("id_vivienda") == id_vivienda]

    # Verificar si hay automatizaciones para mostrar
    if not automatizaciones:
        formatear_mensaje_consola("No hay automatizaciones registradas" if id_vivienda is None 
                                  else f"No hay automatizaciones registradas para la vivienda con ID {id_vivienda}")
        return

    # Mostrar todos las automatizaciones de la base de datos
    for automatizacion in automatizaciones:
        formatear_mensaje_consola(
            f"id de automatizacion: {automatizacion['id']} - id de vivienda: {automatizacion['id_vivienda']},\n"
            f"Nombre: {automatizacion['nombre']}\n"
            f"Hora de inicio: {automatizacion['hora_inicio']}\n"
            f"Hora de finalizacion: {automatizacion['hora_fin']}\n"
            f"ID Dispositivo: {automatizacion['id_dispositivo']}\n" 
            f"Estado: {automatizacion['estado']}\n"
        )

def editar_automatizacion():
    formatear_mensaje_consola("--- Edición de Automatización ---")
    
    try:
        id_automatizacion = int(input("Ingrese el ID de la automatización a editar: "))
    except ValueError:
        formatear_mensaje_consola("ID inválido. Debe ser un número.")
        return

    # Buscar la automatización por ID
    automatizacion = next((a for a in base_de_datos["automatizaciones"] if a["id"] == id_automatizacion), None)

    if not automatizacion:
        formatear_mensaje_consola(f"No se encontró una automatización con ID {id_automatizacion}")
        return

    formatear_mensaje_consola(f"Editando automatización: {automatizacion["nombre"]}")

    # Pedir nuevos datos (si el usuario no escribe nada, se mantiene el valor actual)
    nombre = input(f"Nombre [{automatizacion["nombre"]}]: Ingrese un nuevo nombre o nada para conservar el actual").strip().lower()
    if nombre:
        automatizacion["nombre"] = nombre

    hora_inicio = input(f"Hora de inicio (HH:MM) [{automatizacion["hora_inicio"]}]: ").strip()
    if hora_inicio:
        automatizacion["hora_inicio"] = hora_inicio  # validar el formato HH:MM

    hora_fin = input(f"Hora de fin (HH:MM) [{automatizacion["hora_fin"]}]: ").strip()
    if hora_fin:
        automatizacion["hora_fin"] = hora_fin  # validar el formato HH:MM

    try:
        id_dispositivo = input(f"ID del dispositivo [{automatizacion["id_dispositivo"]}]: Ingrese el ID del dispositivo a cambiar o nada para conservar el actual ").strip()
        if id_dispositivo:
            automatizacion["id_dispositivo"] = int(id_dispositivo)
    except ValueError:
        formatear_mensaje_consola("ID de dispositivo inválido. No se actualizó.")

    # Permitir cambiar el estado (opcional)
    estado = input(f"Estado (activo/inactivo) [{automatizacion["estado"]}]: ").strip().lower()
    if estado in ["activo", "inactivo"]:
        automatizacion["estado"] = estado
    elif estado:
        formatear_mensaje_consola("Estado inválido. Debe ser 'activo' o 'inactivo'. No se actualizó.")

    formatear_mensaje_consola("Automatización actualizada con éxito.")

def activar_desactivar_automatizacion(id_vivienda=None):
    try:
        id = int(input("Ingrese el ID de la automatización que desea activar o desactivar: "))
    except ValueError:
        formatear_mensaje_consola("ID inválido. Debe ser un número.")
        return

    automatizacion = buscar_automatizacion_por_id(id)

    if automatizacion is None:
        formatear_mensaje_consola(f"No se encontró una automatización con ID {id}.")
        return

    if automatizacion["estado"] == "activo":
        automatizacion["estado"] = "inactivo"
        formatear_mensaje_consola(f"La automatización '{automatizacion['nombre']}' está ahora inactiva.")
    else:
        automatizacion["estado"] = "activo"
        formatear_mensaje_consola(f"La automatización '{automatizacion['nombre']}' está ahora activa.")

        # Ejecutar automatización solo si se proporcionó id_vivienda
        if id_vivienda is not None:
            iniciar_automatizaciones_activas(id_vivienda)
def iniciar_automatizaciones_activas(id_vivienda):
    automatizaciones = [
        a for a in base_de_datos.get("automatizaciones", [])
        if a["id_vivienda"] == id_vivienda and a["estado"] == "activo"
    ]

    if not automatizaciones:
        formatear_mensaje_consola("No hay automatizaciones activas en esta vivienda.")
        return

    for automatizacion in automatizaciones:
        en_horario = esta_en_rango_horario(automatizacion["hora_inicio"], automatizacion["hora_fin"])

        dispositivo = next(
            (d for d in base_de_datos["dispositivos"] if d["id"] == automatizacion["id_dispositivo"]),
            None
        )

        if dispositivo is None:
            formatear_mensaje_consola(f"Dispositivo con ID {automatizacion["id_dispositivo"]} no encontrado.")
            continue

        # Cambiar estado del dispositivo según el horario
        dispositivo["estado"] = en_horario

        estado_str = "encendido" if en_horario else "apagado"
        formatear_mensaje_consola(
            f"{'✔' if en_horario else '✖'} Automatización '{automatizacion["nombre"]}': "
            f"Dispositivo '{dispositivo["nombre"]}' ({dispositivo["ubicacion"]}) ahora está {estado_str}."
        )




