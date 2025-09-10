import mysql.connector
from clases import Usuario

def autenticar_usuario(correo, contraseña):
    conn = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="smarthome"
    )
    cursor = conn.cursor()

    query = "SELECT nombre, rol FROM usuarios WHERE correo = %s AND contraseña = %s"
    cursor.execute(query, (correo, contraseña))
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        nombre, rol = resultado
        return {"correo": correo, "nombre": nombre, "rol": rol}
    else:
        return None
    
    #-------------------------------------------------------------------
    #CASO DE USO
    #autenticacion
if __name__ == "__main__":
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")

    usuario = autenticar_usuario(correo, contraseña)

    if usuario:
        print(f"Bienvenido, {usuario.nombre} ({usuario.rol})")
    else:
        print("Credenciales incorrectas")
