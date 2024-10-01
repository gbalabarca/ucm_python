# *********************
# ENUNCIADO
# *********************
'''
Completa un programa que pida una cierta cantidad de dinero y dé una salida adecuada:   

Dame la cantidad de dinero que deseas cambiar: 459
Desglose de 459 U:
18 monedas de 25 U
1 monedas de 5 U
4 monedas de 1 U
'''

def dar_cambio(monto_dinero):
    '''
    Función que permite cambiar un monto de dinero desglosando por las siguientes monedas: 25 U - 5 U - 1 U

    Parameters
    ----------
    monto_dinero : int
        Cantidad de dinero que se desea cambiar.
        
    Precondition
    ------------
    monto_dinero > 0

    Returns
    -------
    str
        desglose del monto_dinero en monedas.

    '''
    if monto_dinero.isdigit() or (monto_dinero.startswith('-') and monto_dinero[1:].isdigit()):
        dinero = int(monto_dinero)

        lista_monedas = [25, 5, 1]
        cambio = {}
        
        if dinero > 0:
            for i in lista_monedas:
                if dinero >= i:
                    queda = dinero // i
                    cambio[i] = queda
                    #print(str(queda) + (' monedas' if queda > 1 else ' moneda') + ' de ' + str(i) + ' U')
                    dinero = dinero % i                
        else:
            print('Entrada no válida. Debe ser un número entero mayor a cero.')
            
        return cambio
    else:
        print('Entrada no válida. Debe ser un número entero positivo.')  


# *********************
# INPUT
# *********************
dinero_entrada = input("Dame la cantidad de dinero que deseas cambiar: ")   


# *********************
# MOSTRAR RESULTADO
# *********************
if dar_cambio(dinero_entrada):
    for moneda, cantidad in dar_cambio(dinero_entrada).items():
        print(str(cantidad) + (' monedas' if cantidad > 1 else ' moneda') + ' de ' + str(moneda) + ' U')
