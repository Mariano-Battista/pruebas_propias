import pyodbc

class Vivienda:
    def __init__(self, id_vivienda, direccion):
        self.id = id_vivienda
        self.direccion = direccion
        self.ubicaciones = []
        self.automatizaciones = []

    def agregar_ubicacion(self, ubicacion):
        self.ubicaciones.append(ubicacion)

# Conexión a SQL Server
def conectar_bd():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=smarthome;'
        'Trusted_Connection=yes;'
    )


# Crear una nueva vivienda y asociarla a un usuario
def crear_vivienda(direccion, correo, rol):
    conn = conectar_bd()
    cursor = conn.cursor()

    # Insertar vivienda
    query_vivienda = "INSERT INTO viviendas (direccion) OUTPUT INSERTED.id_vivienda VALUES (?)"
    cursor.execute(query_vivienda, (direccion,))
    id_vivienda = cursor.fetchone()[0]

    # Asociar al usuario en la tabla intermedia
    query_relacion = "INSERT INTO usuario_vivienda (correo, vivienda_id, rol) VALUES (?, ?, ?)"
    cursor.execute(query_relacion, (correo, id_vivienda, rol))

    conn.commit()
    conn.close()

    return Vivienda(id_vivienda, direccion)

# Mostrar todas las viviendas
def mostrar_viviendas():
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "SELECT id_vivienda, direccion FROM viviendas"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conn.close()

    viviendas = []
    for id_vivienda, direccion in resultados:
        viviendas.append(Vivienda(id_vivienda, direccion))

    return viviendas
