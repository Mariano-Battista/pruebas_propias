class Usuario:
    def __init__(self, correo, nombre, contraseña, rol):
        self.correo = correo
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol  # 'admin' o 'estandar'
    
    #def iniciar_sesion(correo, contraseña):
        #verificar en base de datos y si coinciden dar acceso