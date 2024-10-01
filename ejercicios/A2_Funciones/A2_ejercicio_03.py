# *********************
# ENUNCIADO
# *********************
'''
Diseña una función que calcule el mínimo y el máximo de dos reales dados.
Observa que, para este ejercicio, a lo mejor necesitas usar una expresión condicional, o una instrucción condicional.
'''

def calcular_min_max(in_numero1:float, in_numero2:float):
    '''
    Función que devuelve el mínimo y el máximo de 2 números reales.

    Parameters
    ----------
    in_numero1, in_numero2: float
        Número1 y número2 para la comparación de números.
        
    Precondition
    ------------
    in_numero1 > 0 and in_numero2 > 0

    Returns
    -------
    float
        Retorna el mínimo y máximo de ambos números.
    ''' 
    minimo = min(numero1, numero2)
    maximo = max(numero1, numero2)
    return minimo, maximo


def calcular_min_max_logica(numero1, numero2):
    '''
    Función que devuelve el mínimo y el máximo de 2 números reales.

    Parameters
    ----------
    in_numero1, in_numero2: float
        Número1 y número2 para la comparación de números.
        
    Precondition
    ------------
    in_numero1 > 0 and in_numero2 > 0

    Returns
    -------
    float
        Retorna el mínimo y máximo de ambos números.
    ''' 
    minimo = numero1 if numero1 < numero2 else numero2
    maximo = numero1 if numero1 > numero2 else numero2    
    return minimo, maximo


# *********************
# INPUT
# *********************
numero1 = float(input('Ingresa el primer número: '))
numero2 = float(input('Ingresa el segundo número: '))


# *********************
# MOSTRAR RESULTADO
# *********************
minimo_funcion, maximo_funcion = calcular_min_max(numero1, numero2)
print(f'El mínimo de {numero1} y {numero2} es: {minimo_funcion}')
print(f'El máximo de {numero1} y {numero2} es: {maximo_funcion}')
print('---------------------')
minimo_logica, maximo_logica = calcular_min_max_logica(numero1, numero2)
print(f'El mínimo de {numero1} y {numero2} es: {minimo_logica}')
print(f'El máximo de {numero1} y {numero2} es: {maximo_logica}')

