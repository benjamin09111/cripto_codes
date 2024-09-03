# CIFRADO CESAR

def transform(character, movement):
    if 'a' <= character <= 'z':
        # se calcula el nuevo carácter desplazado dentro del rango 'a'-'z'
        ascii_code = ord(character)
        new_character = chr((ascii_code - ord('a') + movement) % 26 + ord('a'))
        return new_character
    else:
        # si el carácter no está en el rango 'a'-'z', se deja sin cambios
        return character

# se cifra el texto letra por letra segun movimiento
def cifrate(text, movement):
    result = ""
    for letter in text:
        result = result + transform(letter, movement)
    return result

# input del laboratorio
print(cifrate("criptografia y seguridad en redes", 9))
