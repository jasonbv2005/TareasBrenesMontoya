# Elborado por: Jason Brenes Vásquez y Andrés Montoya Viales.

def count_char(cadena, caracter):
    """
    Funcionamiento: Cuenta cuántas veces aparece un carácter en una cadena.
    Entradas:
    - cadena: str, la cadena en la que se cuenta el carácter.
    - caracter: str, el carácter a contar en la cadena.
    Salidas:
    Devuelve una tupla según los siguientes casos:
    - código de error (-100, None) si la cadena no es un str.
    - código de error (-200, None) si cadena no es alfanumérica
      (solo letras y números del 0 al 9).
    - código de error (-300, None) si caracter no es un único carácter
      alfanumérico (letras o números del 0 al 9).
    - código de éxito y cantidad (0, cantidad) si se logró el conteo.
      cantidad es el número de veces que caracter aparece en cadena.
    """

    # Verificar que 'cadena' sea un string.
    if not isinstance(cadena, str):
        return -100, None

    # Verificar que 'cadena' sea alfanumérica.
    if not cadena.isalnum():
        return -200, None

    # Verificar que 'caracter' sea string de un solo carácter alfanumérico.
    if not (isinstance(caracter, str) and len(caracter) == 1
            and caracter.isalnum()):
        return -300, None

    # Contar ocurrencias de 'caracter' en 'cadena'.
    cantidad = cadena.count(caracter)
    return 0, cantidad


def multiplo_2(base, multiplo):
    """
    Funcionamiento: Calcula multiplo * base, con multiplo en (1, 2, 4, 8, 16).
    Entradas:
    - base: int, el número base.
    - multiplo: int, el múltiplo de 2 a aplicar.
    Salidas:
    Devuelve una tupla con resultados según sea el caso:
    - código de error (-400, None) si multiplo o base no son enteros positivos.
    - código de error (-500, None) si el multiplo no está en {1, 2, 4, 8, 16}.
    - código de éxito y resultado (0, resultado) si se logró la operación.
    resultado es el valor de multiplo * base.
    """

    # Verificar que multiplo y base sean enteros.
    if not (isinstance(base, int) and isinstance(multiplo, int)):
        return (-400, None)

    # Verificar que multiplo y base sean positivos.
    if not (base > 0 and multiplo > 0):
        return (-400, None)

    # Verificar que multiplo esté en la lista {1, 2, 4, 8, 16}.
    if multiplo not in (1, 2, 4, 8, 16):
        return (-500, None)

    # Cálculo de multiple * base empleando desplazamiento de bits.
    shift_amount = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4}[multiplo]
    resultado = base << shift_amount  # Multiplicación por potencia de 2.

    # Retornar código de éxito y el resultado de la operación.
    return (0, resultado)
