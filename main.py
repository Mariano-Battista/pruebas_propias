#Caso de usos Usuarios
from usuario import autenticar_usuario, crear_usuario, mostrar_usuarios

if __name__ == "__main__":
    print("1. Crear usuario")
    print("2. Autenticar usuario")
    print("3. Mostrar todos los usuarios")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        rol = input("Rol (admin/estandar): ")
        crear_usuario(nombre, correo, contraseña, rol)
        print("Usuario creado correctamente.")

    elif opcion == "2":
        correo = input("Correo: ")
        contraseña = input("Contraseña: ")
        usuario = autenticar_usuario(correo, contraseña)
        if usuario:
            print(f"Bienvenido, {usuario.nombre} ({usuario.rol})")
        else:
            print("Credenciales incorrectas.")

    elif opcion == "3":
        usuarios = mostrar_usuarios()
        for u in usuarios:
            print(f"{u.nombre} - {u.correo} - {u.rol}")

#Caso de usos Viviendas
from vivienda import crear_vivienda, obtener_viviendas_del_usuario

if __name__ == "__main__":
    print("1. Crear vivienda")
    print("2. Ver viviendas de un usuario")
    opcion = input("Opción: ")

    if opcion == "1":
        direccion = input("Dirección de la vivienda: ")
        correo = input("Correo del usuario: ")
        rol = input("Rol en la vivienda (admin/estandar): ")
        vivienda = crear_vivienda(direccion, correo, rol)
        print(f"Vivienda creada: {vivienda.direccion} (ID: {vivienda.id})")

    elif opcion == "2":
        correo = input("Correo del usuario: ")
        viviendas = obtener_viviendas_del_usuario(correo)
        if viviendas:
            print("Viviendas asociadas:")
            for v in viviendas:
                print(f"- {v.direccion} (ID: {v.id})")
        else:
            print("No se encontraron viviendas.")

#Caso de usos Dispositivos
from dispositivo import cargar_dispositivos, mostrar_dispositivos

if __name__ == "__main__":
    print("1. Ver dispositivos de una vivienda")
    print("2. Mostrar todos los dispositivos")
    opcion = input("Opción: ")

    if opcion == "1":
        correo = input("Correo del usuario: ")
        viviendas = obtener_viviendas_del_usuario(correo)
        if viviendas:
            vivienda = viviendas[0]  # ejemplo: tomar la primera
            cargar_dispositivos(vivienda)
            print(f"Dispositivos en la vivienda: {vivienda.direccion}")
            for ubicacion in vivienda.ubicaciones:
                print(f"Ubicación: {ubicacion.nombre}")
                for dispositivo in ubicacion.dispositivos:
                    print(f"  - {dispositivo.nombre} ({dispositivo.estado})")
        else:
            print("No se encontraron viviendas.")

    elif opcion == "2":
        dispositivos = mostrar_dispositivos()
        for d in dispositivos:
            print(f"{d.nombre} - {d.estado} - Ubicación: {d.ubicacion.nombre}")

#Caso de usos Ubicacion
from ubicacion import crear_ubicacion, buscar_ubicaciones_por_vivienda

if __name__ == "__main__":
    print("1. Crear ubicación")
    print("2. Ver ubicaciones de una vivienda")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre de la ubicación: ")
        id_vivienda = int(input("ID de la vivienda: "))
        crear_ubicacion(nombre, id_vivienda)
        print("Ubicación creada correctamente.")

    elif opcion == "2":
        id_vivienda = int(input("ID de la vivienda: "))
        ubicaciones = buscar_ubicaciones_por_vivienda(id_vivienda)
        if ubicaciones:
            print("Ubicaciones encontradas:")
            for u in ubicaciones:
                print(f"- {u.nombre} (ID: {u.id})")
        else:
            print("No se encontraron ubicaciones.")

#Caso de usos Automatizacion
from automatizacion import crear_automatizacion, buscar_automatizaciones_por_vivienda

if __name__ == "__main__":
    print("1. Crear automatización")
    print("2. Ver automatizaciones de una vivienda")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre de la automatización: ")
        hora_inicio = input("Hora inicio (HH:MM): ")
        hora_fin = input("Hora fin (HH:MM): ")
        estado = input("Estado (activa/inactiva): ")
        id_vivienda = int(input("ID de la vivienda: "))
        crear_automatizacion(nombre, hora_inicio, hora_fin, estado, id_vivienda)
        print("Automatización creada correctamente.")

    elif opcion == "2":
        id_vivienda = int(input("ID de la vivienda: "))
        automatizaciones = buscar_automatizaciones_por_vivienda(id_vivienda)
        if automatizaciones:
            print("Automatizaciones encontradas:")
            for a in automatizaciones:
                print(f"- {a.nombre} ({a.estado}) de {a.hora_inicio} a {a.hora_fin}")
        else:
            print("No se encontraron automatizaciones.")
