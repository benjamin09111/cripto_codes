def generar_clave(mensaje, clave):
    clave = list(clave)
    if len(mensaje) == len(clave):
        return clave
    else:
        for i in range(len(mensaje) - len(clave)):
            clave.append(clave[i % len(clave)])
    return "".join(clave)

def cifrar_vigenere(mensaje, clave):
    mensaje_cifrado = []
    for i in range(len(mensaje)):
        if mensaje[i].isalpha():  # Cifrar solo letras
            # Convertir las letras a números (A=0, B=1, ..., Z=25)
            # Este es el algoritmo, se suman en ASCII y saca el modulo de 26, que son las letras totales, asegurando que esté en el rango. Esto pasa porque al final se desplaza cierta posición del abecedario.
            x = (ord(mensaje[i].upper()) + ord(clave[i].upper())) % 26
            # Convertir de nuevo a una letra y agregar al resultado
            mensaje_cifrado.append(chr(x + ord('A')))
        else:
            mensaje_cifrado.append(mensaje[i])  # No cifrar caracteres no alfabéticos
    return "".join(mensaje_cifrado)

def main():
    mensaje = "CRIPTOGRAMASRESUELTOS"
    clave = "MECA"
    clave = generar_clave(mensaje, clave)
    mensaje_cifrado = cifrar_vigenere(mensaje, clave)
    print("Mensaje original:", mensaje)
    print("Clave:", clave)
    print("Mensaje cifrado:", mensaje_cifrado)

if __name__ == "__main__":
    main()
