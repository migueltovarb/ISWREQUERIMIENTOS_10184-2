
print('---BIENVENIDO---')   

while True:
    

    litros_leche = int(input('Ingrese la cantidad de leche en litros:  '))
    precio_galon = int(input('Ingrese el precio por galon: '))
    
    
    def galon(litros_leche, precio_galon):
        if litros_leche <= 0 or precio_galon <= 0 :
            return 'ERROR: los valores ingresados deben ser positivos mayores que cero.'
        else:
            conversion = litros_leche / 3.785
            precio_del_galon = conversion * precio_galon
            return f'usted tiene {conversion} galones y su valor es {precio_del_galon}'

    resultado = galon(litros_leche, precio_galon)
    print (resultado)
        