# *********************
# ENUNCIADO
# *********************
'''
Un nombre propio ha de escribirse con la primera letra mayúscula. Diseña instrucciones para que, 
en el caso de que se dé con minúscula, lo arregle:
    
>>> nombre_propio = “blacky”
...
>>> print(nombre_propio)
Blacky
'''

def obtener_nombre_capitalize_funcion(in_nombre:str) -> str:
    '''
    Función que devuelve el nombre de la persona con letra capital (primera letra en mayúscula y lo demás en minúscula.

    Parameters
    ----------
    in_nombre : str
        Nombre de la persona.
        
    Precondition
    ------------
    in_nombre != '' 

    Returns
    -------
    str
        Retorna el nombre de la persona con la primera letra mayúscula.

    '''
    if len(in_nombre.strip()) > 0 and in_nombre.isalpha():
        return nombre.capitalize()
    else:
       return 'Entrada inválida. No debe estar vacío el campo nombre y no debe ser numérico.'
    
   
    
def obtener_nombre_capitalize_logica(in_nombre:str()) -> str:
    '''
    Función que devuelve el nombre de la persona con letra capital (primera letra en mayúscula y lo demás en minúscula.

    Parameters
    ----------
    in_nombre : str
        Nombre de la persona.
        
    Precondition
    ------------
    in_nombre != '' 

    Returns
    -------
    str
        Retorna el nombre de la persona con la primera letra mayúscula.

    '''
    if len(in_nombre.strip()) > 0 and in_nombre.isalpha():
        return nombre[0].upper() + nombre[1:].lower()
    else:
        return 'Entrada inválida. No debe estar vacío el campo nombre y no debe ser numérico.'
    


# *********************
# INPUT
# *********************
nombre = input('Dime tu nombre: ')


# *********************
# MOSTRAR RESULTADO
# *********************
print('Nombre con función Capitalize: ' + obtener_nombre_capitalize_funcion(nombre))
print('Nombre con lógica programación: ' + obtener_nombre_capitalize_logica(nombre))

