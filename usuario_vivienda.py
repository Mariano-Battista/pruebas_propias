import pyodbc
from vivienda import Vivienda

class UsuarioVivienda:
    def __init__(self, correo, vivienda_id, rol):
        self.correo = correo
        self.vivienda_id = vivienda_id
        self.rol = rol

# Conexión a SQL Server
def conectar_bd():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=smarthome;'
        'Trusted_Connection=yes;'
    )

# Obtener todas las viviendas asignadas a un usuario con su rol
def obtener_viviendas_con_rol(correo):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = """
        SELECT v.id_vivienda, v.direccion, uv.rol
        FROM viviendas v
        JOIN usuario_vivienda uv ON v.id_vivienda = uv.vivienda_id
        WHERE uv.correo = ?
    """
    cursor.execute(query, (correo,))
    resultados = cursor.fetchall()
    conn.close()

    viviendas = []
    for id_vivienda, direccion, rol in resultados:
        vivienda = Vivienda(id_vivienda, direccion)
        viviendas.append((vivienda, rol))  # Retorna tupla (vivienda, rol)

    return viviendas

# Obtener el rol del usuario en una vivienda específica
def obtener_rol_en_vivienda(correo, id_vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = """
        SELECT rol
        FROM usuario_vivienda
        WHERE correo = ? AND vivienda_id = ?
    """
    cursor.execute(query, (correo, id_vivienda))
    resultado = cursor.fetchone()
    conn.close()

    return resultado[0] if resultado else None
# Asociar un usuario a una vivienda con un rol
def asociar_usuario_a_vivienda(correo, id_vivienda, rol):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "INSERT INTO usuario_vivienda (correo, vivienda_id, rol) VALUES (?, ?, ?)"
    cursor.execute(query, (correo, id_vivienda, rol))
    conn.commit()
    conn.close()

# Eliminar la relación usuario-vivienda
def eliminar_usuario_de_vivienda(correo, id_vivienda):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "DELETE FROM usuario_vivienda WHERE correo = ? AND vivienda_id = ?"
    cursor.execute(query, (correo, id_vivienda))
    conn.commit()
    conn.close()
