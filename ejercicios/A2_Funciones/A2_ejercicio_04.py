# *********************
# ENUNCIADO
# *********************
'''
Diseña una función que calcule la raíz de un número, así: cuando no decimos el índice, se sobre entiende que es dos;
esto es, la raíz cuadrada:
raiz(5) → 2.23606797749979
raiz(5, índice=2) → 2.23606797749979
raiz(5, índice=3) → 1.7099759466766968
Esta posibilidad recibe el nombre de “parámetros por defecto”.
'''

def calcular_raiz(in_numero:float, in_indice:int=2) -> float:
    '''
    Función que devuelve la raíz de un número, cuando no se indica índice, calcula por defecto la raíz cuadrada del número.

    Parameters
    ----------
    in_numero: float
    in_indice: int
        Para el cálculo de la raíz del número.
        
    Precondition
    ------------
    in_numero > 0 and in_indice >= 0

    Returns
    -------
    float
        Retorna la raíz de un número.
    '''    
    if in_indice <= 0:
        return 'El valor del índice debe ser un número positivo.'       
    return in_numero ** (1/in_indice)
    
    
# *********************
# INPUT
# *********************
numero = float(input('Ingrese número: '))
indice = input('Ingrese el índice de la raíz que desea calcular: ')

if len(str(indice).strip()) > 0:
    indice = int(indice)
else:
    indice = 0

# *********************
# MOSTRAR RESULTADO
# *********************
print(f'La raíz {indice} de {numero} es: {calcular_raiz(numero, indice)}') 
print(f'La raíz 2 de {numero} es: {calcular_raiz(numero)}')
    
    
    