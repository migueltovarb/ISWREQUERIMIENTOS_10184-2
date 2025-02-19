from datetime import datetime
class Tarea:
    
    lista_tareas = []
    indice = []
    
    for tarea in enumerate(lista_tareas):
        print(lista_tareas)
        
    def crear_tarea(lista_tareas):
        nombre_tarea = input('ingresa el nombre de tu tarea: ')
        descripcion_tarea = input('Ingrese la descripcion de su tarea: ')
        fecha_de_vencimiento = input('Ingrese la fecha de vencimiento (DD-MM-AAAA): ')
       
        
        tarea = {'nombre': nombre_tarea, 'descripcion': descripcion_tarea, 'fecha de vencimiento': fecha_de_vencimiento, 'completada': False}
        lista_tareas.append(tarea)
        
        print(f' se agrego la tarea: {tarea["nombre"]}. Su tarea es la numero: {len(lista_tareas)}')
        
    
    def ver_tareas(lista_tareas):
        if lista_tareas:
                print(lista_tareas)
           
        else:
            print('no hay tareas para mostrar.')
            
        print('---FIN DEL LISTADO DE TAREAS---')
        
        
    def marcar_tarea_completada(lista_tareas, ver_tareas):
        ver_tareas(lista_tareas)      
        completada = int(input('Introduzca el número de la tarea a completar: '))

        if 1 <= completada <= len(lista_tareas):  
            tarea = lista_tareas[completada - 1] 

            if tarea["completada"]: 
                print('La tarea ya estaba marcada como completada.')  
            else:
                tarea["completada"] =True 
            print(f' La tarea "{tarea["nombre"]}" ha sido marcada como completada.')
        else: 
            print(' Opción inválida, su tarea no existe.')
        

            
    def eliminar_tarea(lista_tareas,ver_tareas):
        ver_tareas(lista_tareas)
        if lista_tareas: 
            tarea = int(input('introduzca el nuemero de la tarea a eliminar: '))
            
            if 0 <= tarea <= len(lista_tareas):
                eliminada = lista_tareas.pop(tarea - 1)
                print(f'Tarea eliminada {eliminada}')
            else: 
                print('numero invalido.')
        else: 
            print('no hay tareas para eliminar.')
            
    def modificar_tarea(lista_tareas, ver_tareas):
        ver_tareas(lista_tareas)
        modificar = int(input('ingrse el numero de tarea a modificar: '))
        if 0<= modificar <= len(lista_tareas):
            
            nuevo_nombre = input('ingrese el nuevo nombre: ')
            nueva_descripcion = input('ingrese una nueva descripcion: ')
            lista_tareas[modificar-1] = f'{nuevo_nombre}:{nueva_descripcion}'
            print('tarea modificada.')

        else: 
            print('número de tarea invalido.')
        
            
    
            
    
    
        
        
        