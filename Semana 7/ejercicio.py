
catalogo = ['camiseta', 'pantalon', 'sombrero']

def realizar_pedido():

    print('---BIENVENIDO---')
    while True:
        try: 
        
            nombre = input('Ingrese su nombre completo: ')
            direccion = input('Ingrese la direccion de entrega: ')
            contacto = int(input('Ingrese el numero de contacto: '))
            correo = input('Ingrese su correo electronico: ')
            producto = input('Ingrese el producto: ')

            if producto in catalogo:
                total = 100
                metodo_pago = input('Elija el metodo de pago: ')

                print('pedido realizado. ')
                break 

            else: 
                print('EL PRODUCTO INGRESADO NO SE ENCUENTRA DISPONIBLE EN EL CATALOGO.')
        except ValueError: 
            print('dato incorrecto, digite nuevamente la infomarcion')

realizar_pedido()

