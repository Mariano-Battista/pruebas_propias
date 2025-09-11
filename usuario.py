import pyodbc

class Usuario:
    def __init__(self, correo, nombre, contraseña, rol):
        self.correo = correo
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol  # 'admin' o 'estandar'

# Conexión a SQL Server
def conectar_bd():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=localhost;'
        'DATABASE=smarthome;'
        'Trusted_Connection=yes;'
    )

# Autenticación
def autenticar_usuario(correo, contraseña):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "SELECT nombre, rol FROM usuarios WHERE correo = ? AND contraseña = ?"
    cursor.execute(query, (correo, contraseña))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        nombre, rol = resultado
        return Usuario(correo, nombre, contraseña, rol)
    else:
        return None

# Crear usuario
def crear_usuario(nombre, correo, contraseña, rol):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "INSERT INTO usuarios (nombre, correo, contraseña, rol) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (nombre, correo, contraseña, rol))
    conn.commit()
    conn.close()

# Mostrar todos los usuarios
def mostrar_usuarios():
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "SELECT correo, nombre, rol FROM usuarios"
    cursor.execute(query)
    resultados = cursor.fetchall()

    conn.close()

    usuarios = []
    for correo, nombre, rol in resultados:
        usuarios.append(Usuario(correo, nombre, None, rol))  # No mostramos contraseña
    return usuarios

# Buscar usuario por correo
def buscar_usuario_por_correo(correo):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "SELECT nombre, contraseña, rol FROM usuarios WHERE correo = ?"
    cursor.execute(query, (correo,))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        nombre, contraseña, rol = resultado
        return Usuario(correo, nombre, contraseña, rol)
    else:
        return None

# Eliminar usuario
def eliminar_usuario(correo):
    conn = conectar_bd()
    cursor = conn.cursor()

    query = "DELETE FROM usuarios WHERE correo = ?"
    cursor.execute(query, (correo,))
    conn.commit()
    conn.close()
