from cryptography.fernet import Fernet
from generar_clave import*

vehiculos = []

#Requerimiento funcional: Registrar y gestionar los datos del vehiculo.


def registrar_vehiculo(modelo, matricula, año_de_fabricacion, capacidad_carga, estado_mantenimiento, estado_entregas):

    vehiculo = {
        'modelo': str(encriptar_dato(modelo)), 
        'matricula':  str(encriptar_dato(matricula)), 
        'año de fabricacion':  str(encriptar_dato(año_de_fabricacion)),
         'capacidad de carga':  str(encriptar_dato(capacidad_carga)),
        'estado de mantenimiento':  str(encriptar_dato(estado_mantenimiento)),
        'estado de entregas':  str(encriptar_dato(estado_entregas))
        }
    vehiculos.append(vehiculo)

    return f'Vehiculo agregado con exito. {vehiculo} '

#Requerimiento no funcional: encriptacion de los datos del vehiculo


def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as key_file:
        key_file.write(clave)

def cargar_clave():
    with open("clave.key", "rb") as key_file:
        return key_file.read()

def encriptar_dato(dato):
    return fernet.encrypt(str(dato).encode()).decode()


clave = cargar_clave()
fernet = Fernet(clave)
generar_clave()


print('---BIENVENIDO AL ADMINISTRADOR DE FLOTA DE VEHICULOS---')

while True: 


    print('\n')
    print('---MENÚ---')

    print('1. Registrar Vehiculo.')
    print('3. Salir')

    opcion = int(input('INGRESE UNA OPCION: '))


    if opcion == 1:

        modelo = input('Ingrese el modelo de su vehiculo: ')
        matricula = input('Ingrese la matricula del vehiculo: ')
        año_de_fabricacion = int(input('Ingrese el año de fabricacion de su vehiculo: '))
        capacidad_carga = input(('Ingrese la capacidad de carga (kg): '))
        estado_mantenimiento = input('Ingrese el estado de mantenimiento del vehiculo ( mantimiento al dia o  fecha de mantenimiento proxima a vencer.  ): ')
        estado_entregas = input('Ingrese el estado de entregas ( ccompletadas = completado, sin completar = no completadas.)')

        print('\n')

        print(registrar_vehiculo(modelo, matricula, año_de_fabricacion, capacidad_carga, estado_mantenimiento, estado_entregas))
        print('\n')
        print(vehiculos)

    elif opcion == 3:
        break 

    else:
        print('OPCION INVALIDA, POR FAVOR ELIGA NUEVAMENTE')

            

