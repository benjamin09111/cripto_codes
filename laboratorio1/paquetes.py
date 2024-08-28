from scapy.all import IP, ICMP, Raw, send
import time

def create_icmp_packet(data, packet_id, sequence_number):
    # Timestamp fijo de 5 bytes (valor 12345 en bytes)
    fixed_timestamp = (12345).to_bytes(5, byteorder='big')

    # Crea un paquete ICMP Echo Request con datos personalizados
    packet = IP(dst="8.8.8.8") / ICMP(id=packet_id, seq=sequence_number) / Raw(load=fixed_timestamp + data)
    
    return packet

def send_packets(input_string):
    # Se inicia el ID del paquete en 1
    packet_id = 1

    for i, char in enumerate(input_string):
        # Crea el paquete con el carácter actual, donde el timestamp se incluye en el payload
        packet = create_icmp_packet(char.encode(), packet_id, i+1)
        print(f"Enviando paquete con carácter: {char}, ID: {packet_id}")
        send(packet)
        time.sleep(1)  # Retraso para no enviar paquetes demasiado rápido
        
        # Incrementa el ID para el siguiente paquete
        packet_id += 1

# Texto a enviar
input_string = "larycxpajorj h bnpdarmjm nw anmnb"
send_packets(input_string)
