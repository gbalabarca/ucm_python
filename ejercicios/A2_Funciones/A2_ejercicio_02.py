# *********************
# ENUNCIADO
# *********************
'''
La vida está cada vez más cara. (a) Diseña una función que, sabiendo el precio de un artículo y 
el porcentaje de aumento, calcule el precio nuevo de dicho artículo. 
Como el porcentaje puede ser negativo, la misma función puede servir para las rebajas.
(b) Diseña unos pocos ejemplares de test y pon a prueba tu función.
(c) Documenta adecuadamente la función. Examina esta documentación desde el inspector de objetos de Spyder.
(d) Desearíamos que el resultado apareciera redondeado con dos cifras decimales.
'''

def obtener_porcentaje(in_precio:float, in_porcentaje:float) -> float:
    return in_precio * (in_porcentaje / 100)


def calcular_nuevo_precio_articulo(in_precio:str, in_porcentaje:str):
    '''
    Función que devuelve el nuevo precio de un artículo con el % de aumento o disminución.

    Parameters
    ----------
    in_precio, in_porcentaje: str
        Precio y porcentaje del artículo
        
    Precondition
    ------------
    in_precio > 0 and in_porcentaje > 0

    Returns
    -------
    float
        Retorna el nuevo precio de un artículo.
    '''    
    if in_precio.isdigit() or (in_precio.startswith('-') and in_precio[1:].isdigit()):
        precio_articulo = int(in_precio)  # 200
        
        if in_porcentaje.isdigit() or (in_porcentaje.startswith('-') and in_porcentaje[1:].isdigit()):
            cantidad_porcentaje = int(in_porcentaje)  # 15
        else:
            print('Entrada no válida. El porcentaje debe ser un número entero positivo.')        
    else:
        print('Entrada no válida. El precio debe ser un número entero positivo.')    
    
    return round(precio_articulo + obtener_porcentaje(precio_articulo, cantidad_porcentaje), 2)
    

# *********************
# INPUT
# *********************
precio_articulo = input('Ingrese precio del artículo: ')
cantidad_porcentaje = input('Ingrese cantidad de %: ')


# *********************
# MOSTRAR RESULTADO
# *********************
print(f'Precio inicial: {precio_articulo}')
print(f'Porcentaje: {cantidad_porcentaje}%')
print(f"El {cantidad_porcentaje}% de {precio_articulo} es: {obtener_porcentaje(int(precio_articulo), int(cantidad_porcentaje))}")
print(f'Nuevo precio del artículo: {calcular_nuevo_precio_articulo(precio_articulo, cantidad_porcentaje)}')



