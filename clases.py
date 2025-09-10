import mysql.connector
from datetime import datetime

class Usuario:
    def __init__(self, correo, nombre, contraseña, rol):
        self.correo = correo
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol  # 'admin' o 'estandar'

#-----------------------------------------------------------  
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

#-----------------------------------------------------------
class Ubicacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

#-----------------------------------------------------------
class Dispositivo:
    def __init__(self, nombre, estado, ubicacion):
        self.nombre = nombre
        self.estado = estado
        self.ubicacion = ubicacion

    def encender(self):
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

#-----------------------------------------------------------
class Automatizacion:
    def __init__(self, nombre, hora_inicio, hora_fin, estado):
        self.nombre = nombre
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.dispositivos = []

    def cargar_automatizaciones(vivienda):
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

#-----------------------------------------------------------
#Ejemplo de uso

# Crear dispositivo
luz_patio = Dispositivo("Luz del patio", "luz")

# Crear ubicación y agregar dispositivo
patio = Ubicacion("Patio")
patio.agregar_dispositivo(luz_patio)

# Crear vivienda y agregar ubicación
mi_casa = Vivienda("Monte Cristo 123")
mi_casa.agregar_ubicacion(patio)

# Crear automatización
auto_luz_noche = Automatizacion("Encender luz por la noche", "19:00", "06:00", [luz_patio])
mi_casa.automatizaciones.append(auto_luz_noche)

# Obtener hora actual
hora_actual = datetime.now().strftime("%H:%M")

# Ejecutar automatización
auto_luz_noche.ejecutar(hora_actual)  # Enciende la luz del patio


# Mostrar estado
print(f"Hora actual: {hora_actual}")
print(f"Estado de la luz del patio: {luz_patio.estado}")


