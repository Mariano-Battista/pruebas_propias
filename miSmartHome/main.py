from auth import *
from states import states
from automatizaciones import  *
from menu import *  

def main():
    print(f"----BIENVENIDO A SMART HOME SOLUTIONS----{datetime.datetime.now().strftime("%H:%M")}")
    #iniciar_automatizacion_aspiradora()
    #iniciar_automatizacion_luces_del_patio()
    while True:
        mostrar_opciones_principal_de_app()
        opcion=input('Ingrese una opcion: ')
    
        match opcion:
            case '1':
               register()
            case '2':
                login()
                while (states['is_auth']):
                    role=verificar_rol()
                    match role:
                        case "admin":
                            menu_admin()
                            
                        case "estandar":
                            menu_estandar()
            case '3':
                print("Hasta la proxima.")
                break
            case _:
                print("la opcion ingresada no es correcta")

if __name__ == "__main__":
    main()
