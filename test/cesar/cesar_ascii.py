caracter = 'A'
codigo_ascii = ord(caracter)

desplazamiento = 5

codigo_ascii_desplazado = codigo_ascii + desplazamiento

letra_desplazada = chr(codigo_ascii_desplazado)

print(f"El código ASCII de '{caracter}' de código {codigo_ascii} desplazado en {desplazamiento} es {codigo_ascii_desplazado} y representa la {letra_desplazada}")