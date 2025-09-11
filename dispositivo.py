class Dispositivo:
    def __init__(self, nombre, estado, ubicacion):
        self.nombre = nombre
        self.estado = estado
        self.ubicacion = ubicacion

    def encender_apagar(self):
        self.estado = "encendido"

    def cargar_dispositivos(vivienda):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tu_contraseña",
            database="smarthome"
        )
        cursor = conn.cursor()

        query = """
            SELECT d.nombre, d.estado, u.nombre
            FROM dispositivos d
            JOIN ubicacion u ON d.ubicacion_id = u.id_ubicacion
            WHERE u.vivienda_id = %s
        """
        cursor.execute(query, (vivienda.id,))
        resultados = cursor.fetchall()
        conn.close()

        for nombre, estado, ubicacion_nombre in resultados:
            dispositivo = Dispositivo(nombre, estado, ubicacion_nombre)
            vivienda.ubicaciones.append(dispositivo)