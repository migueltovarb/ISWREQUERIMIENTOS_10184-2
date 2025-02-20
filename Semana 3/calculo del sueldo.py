def calcular_pago(horas_trabajadas, costo_hora):
    if horas_trabajadas <= 0 or costo_hora<= 0:
        return 'Error: los valores ingresados deben ser positivos mayores que cero'
    
    else:
        pago_final = horas_trabajadas * costo_hora
        return f'su pago es: {pago_final: ,}'

print('---BIENVENIDO---')

while True:
    print ('---BIENVENIDO---')
    print ('\n')
    print('MENÚ')
    print('1. Calcular pago de horas trabajadas.')
    print('2. Salir.')
    
    opcion =int(input('Ingrese una opcion: '))
    
    if opcion == 1:
        
        horas_trabajadas = int(input('Ingrese el número de horas: '))
        costo_hora = int(input('Ingre el pago por hora: '))
        
        resultado = calcular_pago(horas_trabajadas, costo_hora)
        print(resultado)
    
    elif opcion == 2:
        print('GRACIAS POR USAR LA CALCULADORA DE PAGOS, ADIOS...')
        break
        
    else:
        print('Opcion invalida, intentelo nuevamente.')
        
