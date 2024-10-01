# *********************
# ENUNCIADO
# *********************
'''
Una, que pregunta el nombre del usuario y lo saluda con dicho nombre:    

¿Cómo te llamas? Edmundo
Hola, Edmundo
'''

def saludo(nombre:str) -> str:
    '''
    Función que devuelve un saludo a una persona por su nombre.

    Parameters
    ----------
    nombre : str
        Nombre de la persona.
        
    Precondition
    ------------
    nombre != ''

    Returns
    -------
    str
        Saludo por nombre de la persona.

    '''
    if len(nombre.strip()) > 0:        
        if nombre.isalpha():
            print('Hola, ' + nombre)            
        else:
            print('Entrada no válida. Debe ingresar nombre')            
    else:
        print('Entrada inválida. No debe estar vacío el campo nombre.')
        
        
        
# *********************
# INPUT
# *********************
nombre = input('¿Cómo te llamas? ')


# *********************
# MOSTRAR RESULTADO
# *********************
saludo(nombre)

