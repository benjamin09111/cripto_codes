# DECIFRADO CESAR

# se realiza el corrimiento del caracter
def transform(character, movement):
    if 'a' <= character <= 'z':
        ascii_code = ord(character)
        new_character = chr((ascii_code - ord('a') + movement) % 26 + ord('a'))
        return new_character
    else:
        return character

# se realiza cada desplazamiento utilizando la funcion anterior
def decifrate_all(word):
    for movement in range(26):
        result = ""
        for letter in word:
            result += transform(letter, -movement)
        print(f"Desplazamiento de {movement}: {result}")

# Se pasa el texto cifrado y se obtienen todas las combinaciones de desplazamientos.
# cifrado = "larycxpajorj h bnpdarmjm nw anmnb"
# decifrate_all(cifrado)
