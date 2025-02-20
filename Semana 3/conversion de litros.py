def galon(litros_leche, precio_galon):
        
        if litros_leche <= 0 or precio_galon <= 0 :
            return 'ERROR: los valores ingresados deben ser positivos mayores que cero.'
        
        else:
            conversion = litros_leche / 3.785
            
            precio_del_galon = conversion * precio_galon
            
            return f'usted tiene {conversion} galones y su valor es {precio_del_galon}'

print('---BIENVENIDO---')   

while True:
    print ('---BIENVENIDO---')
    print ('\n')
    print('MENÚ')
    print('1. Calcular la cantidad de galones y su precio.')
    print('2. Salir.')
    
    opcion = int(input('Ingrese una opcion'))
    
    if opcion == 1:

        litros_leche = int(input('Ingrese la cantidad de leche en litros:  '))
        precio_galon = int(input('Ingrese el precio por galon: '))

        resultado = galon(litros_leche, precio_galon)
        print (resultado)
        
    elif opcion == 2:
        print('GRACIAS POR USAR EL CONSERSOR DE LITROS A GALONES')
        print('ADIOS...')
        break
    else:
        print('Opcion invalida, tententelo nuevamente.')