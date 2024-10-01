import random

# *********************
# ENUNCIADO
# *********************
'''
Una moneda (cargada) cae de cara con una probabilidad de 0’7. Diseña una función aleatoria que lance dicha moneda, 
y responda “cara” o “cruz” con arreglo a las probabilidades dadas. Es decir, investiga el uso de “random”.
'''

def lanzar_moneda(probabilidad_cara=0.5):
    '''
    Función aleatoria que simula el lanzamiento de una moneda (cara y cruz).

    Parameters
    ----------
    probabilidad_cara: float    
        Probabilidad del lanzamiento de la moneda.
        
    Precondition
    ------------
    probabilidad_cara > 0

    Returns
    -------
    float
        Resultado del lanzamiento aleatorio.
    '''
    resultados = ["cara", "cruz"]
    pesos = [probabilidad_cara, 1 - probabilidad_cara]  # Probabilidades de "cara" y "cruz"
    
    resultado = random.choices(resultados, weights=pesos)[0]  # Selección aleatoria
    return resultado


# *********************
# INPUT
# *********************
probabilidad_cara = float(input("Ingresa la probabilidad de obtener cara (0 a 1): "))


# *********************
# MOSTRAR RESULTADO
# *********************
if 0 <= probabilidad_cara <= 1:
    resultado = lanzar_moneda(probabilidad_cara)
    print(f"Resultado del lanzamiento: {resultado}")
else:
    print("La probabilidad debe estar entre 0 y 1.")


