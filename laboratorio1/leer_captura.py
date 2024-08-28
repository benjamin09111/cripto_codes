from scapy.all import rdpcap, ICMP, Raw

def read_pcap(file_path):
    # Cargar el archivo pcapng
    packets = rdpcap(file_path)
    
    seen_ids = set()  # Conjunto para rastrear IDs ya vistos
    
    for packet in packets:
        if packet.haslayer(ICMP):
            icmp_layer = packet[ICMP]
            
            # Filtrar solo paquetes ICMP Echo Request (tipo 8)
            if icmp_layer.type == 8:  # 8 es el tipo para Echo Request
                payload = packet[Raw].load if packet.haslayer(Raw) else b''
                
                # Extraer el timestamp fijo de 5 bytes del payload
                if len(payload) > 5:
                    timestamp = int.from_bytes(payload[:5], byteorder='big')
                    payload = payload[5:]  # Obtener el payload restante después del timestamp
                
                else:
                    timestamp = None
                    payload = payload
                
                packet_id = icmp_layer.id
                sequence_number = icmp_layer.seq

                if (packet_id, sequence_number) not in seen_ids:
                    # Mostrar datos del paquete
                    print(f"ID: {packet_id}")
                    print(f"Sequence Number: {sequence_number}")
                    print(f"Timestamp: {timestamp}")  # Mostrar el timestamp
                    print(f"Payload: {payload.decode(errors='ignore')}")  # Decodifica el payload a texto, ignorando errores
                    
                    # Añadir ID y número de secuencia al conjunto de vistos
                    seen_ids.add((packet_id, sequence_number))

# Ruta al archivo pcapng
file_path = 'envio_paquetes_timestamp.pcapng'
read_pcap(file_path)
