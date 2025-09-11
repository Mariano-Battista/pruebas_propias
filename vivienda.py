class Vivienda:

    def __init__(self, direccion):
        self.direccion = direccion
        self.ubicaciones = []
        self.automatizaciones = []

    def agregar_ubicacion(self, ubicacion):
        self.ubicaciones.append(ubicacion)
    
    def obtener_vivienda_del_usuario(correo): #CONSULTA SQL QUE VIVIENDA CORRESPONDE A QUE USUARIO
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tu_contraseña",
            database="smarthome"
        )
        cursor = conn.cursor()

        query = """
            SELECT v.id_vivienda, v.direccion
            FROM viviendas v
            JOIN usuario_vivienda uv ON v.id_vivienda = uv.vivienda_id
            WHERE uv.correo = %s
        """
        cursor.execute(query, (correo,))
        resultado = cursor.fetchone()
        conn.close()

        if resultado:
            id_vivienda, direccion = resultado
            return Vivienda(id_vivienda, direccion)
        else:
            return None