import pyodbc
from automatizacion import Automatizacion

def conectar_bd():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=smarthome;'
        'Trusted_Connection=yes;'
    )

# Cargar automatizaciones de una vivienda
def cargar_automatizaciones(vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = """
        SELECT id_automatizacion, nombre, hora_inicio, hora_fin, estado
        FROM automatizaciones
        WHERE id_vivienda = ?
    """
    cursor.execute(query, (vivienda.id,))
    resultados = cursor.fetchall()
    conn.close()

    for id_auto, nombre, hora_inicio, hora_fin, estado in resultados:
        auto = Automatizacion(id_auto, nombre, hora_inicio, hora_fin, estado)
        vivienda.automatizaciones.append(auto)

# Crear una nueva automatización
def crear_automatizacion(nombre, hora_inicio, hora_fin, estado, id_vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = """
        INSERT INTO automatizaciones (nombre, hora_inicio, hora_fin, estado, id_vivienda)
        VALUES (?, ?, ?, ?, ?)
    """
    cursor.execute(query, (nombre, hora_inicio, hora_fin, estado, id_vivienda))
    conn.commit()
    conn.close()

# Mostrar todas las automatizaciones
def mostrar_automatizaciones():
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "SELECT id_automatizacion, nombre, hora_inicio, hora_fin, estado FROM automatizaciones"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()

    automatizaciones = []
    for id_auto, nombre, hora_inicio, hora_fin, estado in resultados:
        auto = Automatizacion(id_auto, nombre, hora_inicio, hora_fin, estado)
        automatizaciones.append(auto)

    return automatizaciones

# Buscar automatizaciones por vivienda
def buscar_automatizaciones_por_vivienda(id_vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = """
        SELECT id_automatizacion, nombre, hora_inicio, hora_fin, estado
        FROM automatizaciones
        WHERE id_vivienda = ?
    """
    cursor.execute(query, (id_vivienda,))
    resultados = cursor.fetchall()
    conn.close()

    automatizaciones = []
    for id_auto, nombre, hora_inicio, hora_fin, estado in resultados:
        auto = Automatizacion(id_auto, nombre, hora_inicio, hora_fin, estado)
        automatizaciones.append(auto)

    return automatizaciones
