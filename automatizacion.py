class Automatizacion:
    def __init__(self, nombre, hora_inicio, hora_fin, estado):
        self.nombre = nombre
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.dispositivos = []

    def ejecutar_automatizaciones(vivienda, hora_actual):
        for auto in vivienda.automatizaciones:
            if auto.estado == "activa":
                if auto.hora_inicio <= auto.hora_fin: # Rango normal (ej. 11:00 a 18:00)
                    if auto.hora_inicio <= hora_actual <= auto.hora_fin:
                        for dispositivo in auto.dispositivos:
                            dispositivo.encender()
                else:                                 # Rango que cruza la medianoche (ej. 19:00 a 06:00)
                    if hora_actual >= auto.hora_inicio or hora_actual <= auto.hora_fin:
                        for dispositivo in auto.dispositivos:
                            dispositivo.encender()

    def cargar_automatizaciones(vivienda): # mas adelante para agregar a la base de datos
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tu_contraseña",
            database="smarthome"
        )
        cursor = conn.cursor()

        query = """
            SELECT nombre, hora_inicio, hora_fin, estado
            FROM automatizaciones
            WHERE id_vivienda = %s
        """
        cursor.execute(query, (vivienda.id,))
        resultados = cursor.fetchall()
        conn.close()

        for nombre, hora_inicio, hora_fin, estado in resultados:
            auto = Automatizacion(nombre, hora_inicio, hora_fin, estado)
            vivienda.automatizaciones.append(auto)

    
    