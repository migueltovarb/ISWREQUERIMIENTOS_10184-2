def calcular_area_terreno(base_mayor, base_menor, altura):
     if base_mayor <=0 or base_menor <= 0 or altura <= 0:
          return 'ERROR:Los valores ingresados deben ser positivos mayores que cero.'
                                        
     else:
          base_triangulo = base_mayor-base_menor
          area_triangulo = (base_triangulo * altura) /2
                                   
          area_reactangulo = base_menor * altura
                                        
          area_total = area_triangulo + area_reactangulo
          return f'el area total del terreno es: {area_total} cm2'


while True:
     
     print('---BIENVENIDO A LA CALCULADORA ---')
     print ('\n')
     print('MENÚ')
     print('1. Calcular el area.')
     print('2. Salir.')
     
     opcion = int(input('Ingrese una opcion: '))
     
     if opcion == 1:
          base_mayor= float(input('Ingrese la medida de la base mayor (B): '))
          base_menor = float(input('Ingrese la medida de la base menor (A):'))
          altura = float(input('Ingrese el valor de la altura (C): ')) 
          
          resutltado = calcular_area_terreno(base_mayor, base_menor, altura)    
          print (resutltado) 
     elif opcion == 2:
          print('ADIOS...')
          break
     
     else: 
          print('Opcion invalida, intentelo nuevamente.')
     
     
     
          

         

    
    
    