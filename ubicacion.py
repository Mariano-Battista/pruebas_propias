import pyodbc

class Ubicacion:
    def __init__(self, id_ubicacion, nombre):
        self.id = id_ubicacion
        self.nombre = nombre
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

# Conexión a SQL Server
def conectar_bd():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=smarthome;'
        'Trusted_Connection=yes;'
    )

# Crear una nueva ubicación
def crear_ubicacion(nombre, id_vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "INSERT INTO ubicacion (nombre, vivienda_id) VALUES (?, ?)"
    cursor.execute(query, (nombre, id_vivienda))
    conn.commit()
    conn.close()

# Mostrar todas las ubicaciones
def mostrar_ubicaciones():
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "SELECT id_ubicacion, nombre FROM ubicacion"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()

    ubicaciones = []
    for id_ubicacion, nombre in resultados:
        ubicaciones.append(Ubicacion(id_ubicacion, nombre))

    return ubicaciones

# Buscar ubicaciones por vivienda
def buscar_ubicaciones_por_vivienda(id_vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "SELECT id_ubicacion, nombre FROM ubicacion WHERE vivienda_id = ?"
    cursor.execute(query, (id_vivienda,))
    resultados = cursor.fetchall()
    conn.close()

    ubicaciones = []
    for id_ubicacion, nombre in resultados:
        ubicaciones.append(Ubicacion(id_ubicacion, nombre))

    return ubicaciones

