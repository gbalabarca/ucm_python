# *********************
# ENUNCIADO
# *********************
'''
Rotación del alfabeto:
Definimos una rotación de longitud "n" como aquella que lleva a una determinada letra "n"
posiciones hacia su derecha.
Ejemplo: La rotación de longitud 1 lleva la "A" a la "B", la "V" a la "W" y la "Z" a la "A"
'''

def rotacion_por_longitud(texto, longitud):
    '''
    Función para realizar la rotación de una letra del alfabeto por una longitud.

    Parameters
    ----------
    alfabeto: str
    longitud: int
        Rotación del alfabeto.
        
    Precondition
    ------------
    alfabeto != ''
    longitud > 0

    Returns
    -------
    str
        Devuelve el nuevo alfabeto con rotación según longitud.
    '''
    alfabeto_original = {}
    alfabeto_rotacion = {}
    
    print('Alfabeto original: ' + texto)    
    
    for i in range(0, 27):
        alfabeto_original[i] = texto[i]            
    
    #print(len(alfabeto_original))  
    
    for i in range(0, 27):   
        if(i < (len(alfabeto_original) - longitud)) :
            alfabeto_rotacion[i+longitud] = texto[i]
        else:
            index_new = (len(alfabeto_original) - longitud) - i        
            alfabeto_rotacion[index_new if index_new > 0 else index_new * (-1)] = texto[i]
        
    #print(sorted(alfabeto_rotacion.items()))
    
    rotacion = ''
    for i in sorted(alfabeto_rotacion.items()):        
        #print(i[1], end="") 
        rotacion += i[1]

    
    print('Alfabeto rotación: ' + rotacion)

# *********************
# INPUT
# *********************
alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
longitud = int(input("Ingrese longitud para la rotación: "))


# *********************
# MOSTRAR RESULTADO
# *********************
rotacion_por_longitud(alfabeto, longitud)


