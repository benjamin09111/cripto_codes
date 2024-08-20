def transform(character, movement):
    ascii_code = ord(character) #pasar a ascii
    new_character = chr(ascii_code+movement) #pasar de ascii a normal
    return new_character

def cifrate(word, movement):
    result = ""
    for letter in word:
        result = result + transform(letter, movement)
    return result

def decifrate(word, movement):
    result = ""
    for letter in word:
        result += transform(letter, -movement)  # restar el movimiento para descifrar
    return result

print(cifrate("C", 2))