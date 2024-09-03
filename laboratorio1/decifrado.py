def transform(character, movement, alphabet='abcdefghijklmnopqrstuvwxyz'):
    if character in alphabet:
        ascii_code = alphabet.index(character)
        new_character = alphabet[(ascii_code + movement) % len(alphabet)]
        return new_character
    else:
        return character

def cifrate(text, movement):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for letter in text:
        result += transform(letter.lower(), movement, alphabet)
    return result

def decifrate(text, movement):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""
    for letter in text:
        result += transform(letter.lower(), -movement, alphabet)
    return result

def decifrate_with_probability(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyzñ'
    
    # Frecuencias de letras en español
    frecuencia_esp = {
        'a': 11.72, 'b': 2.22, 'c': 4.02, 'd': 5.87, 'e': 13.68,
        'f': 0.69, 'g': 1.01, 'h': 0.70, 'i': 6.25, 'j': 0.44,
        'k': 0.01, 'l': 4.67, 'm': 3.15, 'n': 6.71, 'ñ': 0.31,
        'o': 8.68, 'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98,
        't': 4.63, 'u': 2.83, 'v': 1.09, 'w': 0.01, 'x': 0.22,
        'y': 1.00, 'z': 0.52
    }

    def frecuencia_texto(text, frecuencia_esp):
        total_letras = sum(text.count(letra) for letra in frecuencia_esp)
        puntuacion = 0.0
        for letra, freq in frecuencia_esp.items():
            frecuencia_texto = text.count(letra) / total_letras * 100 if total_letras > 0 else 0
            puntuacion += abs(frecuencia_texto - freq)
        return 100 - puntuacion

    best_match = None
    best_score = 0
    best_movement = 0
    
    results = []
    
    for movement in range(len(alphabet)):
        result = decifrate(word, movement)
        
        # Calcular la puntuación basada en la frecuencia de letras
        score = frecuencia_texto(result, frecuencia_esp)

        results.append((movement, result, score))
        
        if score > best_score:
            best_score = score
            best_match = result
            best_movement = movement

    # Imprimir todos los resultados y resaltar el mejor
    for movement, result, score in results:
        if movement == best_movement:
            print(f"\033[32mDesplazamiento de {movement}: {result} (Puntuación: {score})\033[0m")  # Verde
        else:
            print(f"Desplazamiento de {movement}: {result} (Puntuación: {score})")

# Texto cifrado de prueba
cifrado = "larycxpajorj h bnpdarmjm nw anmnb"
decifrate_with_probability(cifrado)
