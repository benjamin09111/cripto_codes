def transform(character, movement):
    if 'a' <= character <= 'z':
        ascii_code = ord(character)
        new_character = chr((ascii_code - ord('a') + movement) % 26 + ord('a'))
        return new_character
    else:
        return character

def print_colored(text, color_code):
    # Código de escape ANSI para el color
    print(f"\033[{color_code}m{text}\033[0m")

def decifrate_all(word):
    target_message = "criptografia y seguridad en redes"
    for movement in range(26):
        result = ""
        for letter in word:
            result += transform(letter, -movement)
        
        # Verifica si el resultado es el mensaje objetivo
        if result == target_message:
            print_colored(f"Desplazamiento de {movement}: {result}", '32')  # Verde
        else:
            print(f"Desplazamiento de {movement}: {result}")

# Se pasa el texto cifrado y se obtienen todas las combinaciones de desplazamientos.
# cifrado = "larycxpajorj h bnpdarmjm nw anmnb"
# decifrate_all(cifrado)
