print('---BIENVENIDO---')

while True:
    try:

        horas_trabajadas = int(input('Ingrese el número de horas: '))
        costo_hora = int(input('Ingre el pago por hora: '))
    except: print('Error:Los valores no pueden ser negativos o iguales a cero.')

    def calcular_pago(horas_trabajadas, costo_hora):
        if horas_trabajadas <= 0 or costo_hora<= 0:
            return 'Error: los valores ingresados deben ser positivos mayores que cero'
    
        else:
            pago_final = horas_trabajadas * costo_hora
            return f'su pago es: {pago_final}'
    
    resultado = calcular_pago(horas_trabajadas, costo_hora)
    print(resultado)
    
