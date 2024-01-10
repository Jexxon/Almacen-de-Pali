while True:
    numero = int(input('Ingrese un número: '))
    # Convertir el número a una cadena y obtener su longitud
    numero_str = str(numero)
    longitud = len(numero_str)

    # Inicializar variables para el bucle y el nuevo número formateado
    bucle = ''
    nuevo_numero = ''

    # Iterar sobre cada dígito del número original en sentido inverso
    for i in range(longitud - 1, -1, -1):
        bucle = numero_str[i] + bucle  # Agregar el dígito al principio del bucle

        # Si el bucle alcanza tres dígitos o es el primer dígito
        if len(bucle) == 3 or (i == 0 and len(bucle) > 0):
            nuevo_numero = ',' + bucle + nuevo_numero  # Agregar comas y el bucle al principio del nuevo número
            bucle = ''  # Reiniciar el bucle

    # Eliminar la coma inicial si existe
    nuevo_numero = nuevo_numero.lstrip(',')
    nuevo_numero = '₡' + nuevo_numero
    print(nuevo_numero)
