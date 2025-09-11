import pyodbc
from ubicacion import Ubicacion

class Dispositivo:
    def __init__(self, id_dispositivo, nombre, estado, ubicacion):
        self.id = id_dispositivo
        self.nombre = nombre
        self.estado = estado
        self.ubicacion = ubicacion  # objeto Ubicacion

    def encender_apagar(self):
        self.estado = "apagado" if self.estado == "encendido" else "encendido"

# Conexión a SQL Server
def conectar_bd():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=smarthome;'
        'Trusted_Connection=yes;'
    )

# Cargar dispositivos de una vivienda
def cargar_dispositivos(vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = """
        SELECT d.id_dispositivo, d.nombre, d.estado, u.id_ubicacion, u.nombre
        FROM dispositivos d
        JOIN ubicacion u ON d.ubicacion_id = u.id_ubicacion
        WHERE u.vivienda_id = ?
    """
    cursor.execute(query, (vivienda.id,))
    resultados = cursor.fetchall()
    conn.close()

    ubicaciones_dict = {}

    for id_dispositivo, nombre, estado, id_ubicacion, nombre_ubicacion in resultados:
        if id_ubicacion not in ubicaciones_dict:
            ubicacion = Ubicacion(id_ubicacion, nombre_ubicacion)
            ubicaciones_dict[id_ubicacion] = ubicacion
            vivienda.agregar_ubicacion(ubicacion)
        else:
            ubicacion = ubicaciones_dict[id_ubicacion]

        dispositivo = Dispositivo(id_dispositivo, nombre, estado, ubicacion)
        ubicacion.agregar_dispositivo(dispositivo)

# Crear un nuevo dispositivo
def crear_dispositivo(nombre, estado, id_ubicacion):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "INSERT INTO dispositivos (nombre, estado, ubicacion_id) VALUES (?, ?, ?)"
    cursor.execute(query, (nombre, estado, id_ubicacion))
    conn.commit()
    conn.close()

# Mostrar todos los dispositivos
def mostrar_dispositivos():
    conn = conectar_bd()
    cursor = conn.cursor()

    query = """
        SELECT d.id_dispositivo, d.nombre, d.estado, u.nombre
        FROM dispositivos d
        JOIN ubicacion u ON d.ubicacion_id = u.id_ubicacion
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()

    dispositivos = []
    for id_dispositivo, nombre, estado, nombre_ubicacion in resultados:
        ubicacion = Ubicacion(None, nombre_ubicacion)
        dispositivo = Dispositivo(id_dispositivo, nombre, estado, ubicacion)
        dispositivos.append(dispositivo)

    return dispositivos
