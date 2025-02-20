def valor_cita (numero_cita):
    
    if   1 <= numero_cita <= 3: 
        costo1 = 200000
        return f' el valor de su cita es: {costo1: ,}'
    elif 3 < numero_cita <=5 :
        costo2 = 150000
        return f' Eñ valor de su cita es: {costo2: ,}' 
    elif 5 < numero_cita <= 8:
        costo3 = 100000
        return f' El valor de su cita es: {costo3: ,}'
    else:
        costo4 = 50000
    
def valor_total(numero_cita):
    saldo_total = (min(numero_cita, 3) * 200000 +
                    max(0, min(numero_cita - 3, 2)) * 150000 +
                    max(0, min(numero_cita - 5, 3)) * 100000 +
                    max(0, numero_cita - 8) * 50000)
    
    return f'El monto total de su cuenta actual es: {saldo_total: ,}'     

while True: 
    print ('---BIENVENIDO---')
    print ('\n')
    print('MENÚ')
    print('1. consultar el valor de su cita.')
    print('2. Consultar el valor actual de su cuenta.')
    print('3. salir.')
    
    try:
        opcion = int(input('Ingrese una opcion: '))
        
    except ValueError: 
        print('ERROR: el numero de opcion debe ser positivo y mayor que cero.') 
        continue
    
    if opcion == 1:
        
        numero_cita = int(input('ingrese el numero de su cita: '))
        
        resultado = valor_cita(numero_cita)
        print (resultado)
    
    elif opcion ==2:
        numero_cita = int(input('Ingrese el numero de su ultima cita: '))
        
        resultado = valor_total(numero_cita)
        print(resultado)
    
    elif opcion == 3:
        print ('ADIOS...')
        break
    
    else:
        print('Opcion invalida.') 
        
        
    
    
    
             

    