from datetime import datetime
from autenticacion import autenticar_usuario
from clases import (
    obtener_vivienda_del_usuario,
    cargar_automatizaciones,
    ejecutar_automatizaciones
)

# Paso 1: Autenticación
correo = input("Correo: ")
contraseña = input("Contraseña: ")

usuario = autenticar_usuario(correo, contraseña)

if usuario:
    print(f"\nBienvenido, {usuario.nombre} ({usuario.rol})")

    # Paso 2: Obtener vivienda
    vivienda = obtener_vivienda_del_usuario(usuario.correo)

    if vivienda:
        print(f"Vivienda: {vivienda.direccion}")

        # Paso 3: Cargar automatizaciones
        cargar_automatizaciones(vivienda)

        # Paso 4: Ejecutar automatizaciones
        hora_actual = datetime.now().strftime("%H:%M")
        print(f"Hora actual: {hora_actual}")
        ejecutar_automatizaciones(vivienda, hora_actual)

        # Paso 5: Mostrar estado de dispositivos
        print("\nEstado de dispositivos:")
        for auto in vivienda.automatizaciones:
            for dispositivo in auto.dispositivos:
                print(f"{dispositivo.nombre} en {dispositivo.ubicacion}: {dispositivo.estado}")
    else:
        print("No se encontró vivienda asociada.")
else:
    print("Credenciales incorrectas")
