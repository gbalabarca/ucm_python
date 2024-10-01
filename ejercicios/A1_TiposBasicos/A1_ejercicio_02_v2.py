# *********************
# ENUNCIADO
# *********************
'''
Otra, que pregunta también la edad y le contesta con su nombre, la edad y los años que cumplirá la próxima vez. 
(Esto es simplemente para que convierta la edad en un número…)
'''

def saludo_nombre_edad(in_nombre:str, in_edad:str):
    '''
    Función que devuelve un saludo a una persona por su nombre y edad.

    Parameters
    ----------
    nombre, edad : str
        Nombre y edad de la persona.
        
    Precondition
    ------------
    nombre != ''
    edad != '' and edad > 0 

    Returns
    -------
    str
        Saludo por nombre y edad de la persona.

    '''
    if len(in_nombre.strip()) > 0 and in_nombre.isalpha(): 
        if in_edad.isdigit() or (in_edad.startswith('-') and in_edad[1:].isdigit()):
            edad = int(in_edad) 
            #print('Hola ' + nombre + ', tienes ' + str(edad) + ' años y pronto cumplirás ' + str(int(edad) + 1) + ' años.')
            print(f'Hola {nombre}, tienes {edad} años y pronto cumplirás {int(edad)+1} años.')
        else:
            print('Entrada no válida en la Edad. Debe ingresar número entero positivo.')
        
    else:
        print('Entrada inválida. No debe estar vacío el campo nombre y no debe ser numérico.')


# *********************
# INPUT
# *********************
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuál es tu edad? ')


# *********************
# MOSTRAR RESULTADO
# *********************
saludo_nombre_edad(nombre, edad)


