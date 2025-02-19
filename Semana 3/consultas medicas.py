print ('---BIENVENIDO---')

while True: 
    num_cita = int(input('Ingrese su número de cita: '))

    def costo_cita(mun_cita):
    
        costo_cita1 = 200000
        costo_cita2 = 150000
        costo_cita3 = 100000
        costo_cita4 = 50000
    
        saldo_total = 0
    
        for cita in range(1, num_cita +1):
    
            if mun_cita < 1:
                return 'ERROR: el número de cita debe ser positivo y mayor que cero'
        
            elif 1< num_cita <= 3:
                costo_de_cita = costo_cita1
                saldo_total += 200000
                return f'el costo de su cita es: {costo_de_cita} y su saldo atual de la cuenta es: {saldo_total}'
        
            elif 3 < num_cita <= 5:
                costo_de_cita = costo_cita2
                saldo_total += 150000
                return f'el costo de su cita es: {costo_de_cita} y su saldo atual de la cuenta es: {saldo_total}'

            elif 5 < num_cita <=8:
                costo_de_cita =  costo_cita3
                saldo_total += 100000
                return f'el costo de su cita es: {costo_de_cita} y su saldo atual de la cuenta es: {saldo_total}'
        
            else:
                num_cita > 8
                costo_de_cita = costo_cita4
                saldo_total += 50000
                return f'el costo de su cita es: {costo_de_cita} y su saldo atual de la cuenta es: {saldo_total}'
    
    resultado = costo_cita(num_cita)
    print(resultado)
        
    