import math

# *********************
# ENUNCIADO
# *********************
'''
Si tenemos los coeficientes (𝑎, 𝑏, 𝑐) de una ecuación de segundo grado de la forma 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0 
y suponiendo que tiene dos raíces reales, expresa instrucciones para calcular dichas fórmulas.
'''

def calcular_ecuacion_segundo_grado(coeficiente_a:str, coeficiente_b:str, coeficiente_c:str) -> str:
    '''
    Función que devuelve el resultado del cálculo de la ecuación de segundo grado el nombre de la persona con letra capital (primera letra en mayúscula y lo demás en minúscula.

    Parameters
    ----------
    a, b, c : str
        Coeficientes de la ecuacion
        
    Precondition
    ------------
    in_nombre != '' 

    Returns
    -------
    float
        Retorna el cálculo de la ecuación de segundo grado.
    '''
    a = int(coeficiente_a)
    b = int(coeficiente_b)
    c = int(coeficiente_c)
    
    # Calcula el discriminante
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        return "La ecuación no tiene raíces reales."
    
    # Calcula las dos raíces
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    
    return raiz1, raiz2


# *********************
# INPUT
# *********************
coeficiente_a = input('Ingresa valor para el coeficiete \"a\": ')  # 1
coeficiente_b = input('Ingresa valor para el coeficiete \"b\": ')  # -3
coeficiente_c = input('Ingresa valor para el coeficiete \"c\": ')  # 2


# *********************
# MOSTRAR RESULTADO
# *********************
raices = calcular_ecuacion_segundo_grado(coeficiente_a, coeficiente_b, coeficiente_c)

if isinstance(raices, tuple): # (x, y)
    print(f"Las raíces de la ecuación son: {raices[0]} y {raices[1]}")
else:
    print(raices)
