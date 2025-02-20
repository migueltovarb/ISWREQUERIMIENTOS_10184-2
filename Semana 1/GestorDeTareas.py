from Tarea import*

nombre_usuario = input('Ingresa tu nombre:')
correoElectronico = input('Ingresa tu correo electronico:')
#BUCLE PRINCIPAL
while  True:  # type: ignore
    
    print('---Bienvenido al Gestor de tareas---')

    print('\n')
    print('***MENÚ***')
    print('1. Crear tarea')
    print('2. ver tareas')
    print('3. Eliminar tarea')
    print('4. Marcar tarea como completada')
    print('5. modificar tarea')
    print('6. Salir')
    print('\n')

    #ENTRADA DE OPCIONES 
    
    opcion = int(input('Por favor elija una opción: '))

    #MENU DE OPCIONES: CREAR LA FUNCIONALIDAD
    match opcion:
        case 1:
            Tarea.crear_tarea(Tarea.lista_tareas)
            
        case 2:
            Tarea.ver_tareas(Tarea.lista_tareas)
        
        case 3:
            Tarea.eliminar_tarea(Tarea.lista_tareas, Tarea.ver_tareas)
        
        case 4:
            Tarea.marcar_tarea_completada(Tarea.lista_tareas, Tarea.ver_tareas )
        
        case 5:
            Tarea.modificar_tarea(Tarea.lista_tareas, Tarea.ver_tareas)
        
        case 6:
            print('GRACIAS POR USAR EL GESTOR DE TAREAS, ADIOS...')
            break
        
        case _:
            print('Opcion invalida, por favor ingrese una opcion valida: ')
            