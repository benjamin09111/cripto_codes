from Crypto.Cipher import DES, DES3, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def adjust_key_length(input_key, required_length, algorithm_name):
    if len(input_key) < required_length:
        input_key += get_random_bytes(required_length - len(input_key))
    elif len(input_key) > required_length:
        input_key = input_key[:required_length]
    print(f"Adjusted key for {algorithm_name} (hex format): {input_key.hex()}")
    return input_key

def encrypt_decrypt_DES(message, encryption_key, init_vector):
    des_cipher = DES.new(encryption_key, DES.MODE_CBC, init_vector)
    encrypted_message = des_cipher.encrypt(pad(message.encode(), DES.block_size))
    print(f"Encrypted message with DES (hex): {encrypted_message.hex()}")

    des_cipher = DES.new(encryption_key, DES.MODE_CBC, init_vector)
    decrypted_message = unpad(des_cipher.decrypt(encrypted_message), DES.block_size).decode()
    print(f"Decrypted message with DES: {decrypted_message}")

def encrypt_decrypt_3DES(message, encryption_key, init_vector):
    triple_des_cipher = DES3.new(encryption_key, DES3.MODE_CBC, init_vector)
    encrypted_message = triple_des_cipher.encrypt(pad(message.encode(), DES3.block_size))
    print(f"Encrypted message with 3DES (hex): {encrypted_message.hex()}")

    triple_des_cipher = DES3.new(encryption_key, DES3.MODE_CBC, init_vector)
    decrypted_message = unpad(triple_des_cipher.decrypt(encrypted_message), DES3.block_size).decode()
    print(f"Decrypted message with 3DES: {decrypted_message}")

def encrypt_decrypt_AES(message, encryption_key, init_vector):
    aes_cipher = AES.new(encryption_key, AES.MODE_CBC, init_vector)
    encrypted_message = aes_cipher.encrypt(pad(message.encode(), AES.block_size))
    print(f"Encrypted message with AES-256 (hex): {encrypted_message.hex()}")

    aes_cipher = AES.new(encryption_key, AES.MODE_CBC, init_vector)
    decrypted_message = unpad(aes_cipher.decrypt(encrypted_message), AES.block_size).decode()
    print(f"Decrypted message with AES-256: {decrypted_message}")

def main():
    # Input gathering for encryption parameters
    message_to_encrypt = input("Enter the message you wish to encrypt: ")
    user_key = input("Enter your encryption key: ").encode()
    user_iv = input("Enter your initialization vector (IV): ").encode()

    # Adjust keys to required sizes for each encryption algorithm
    des_key = adjust_key_length(user_key, 8, "DES")  # DES requires 8 bytes
    triple_des_key = adjust_key_length(user_key, 24, "3DES")  # 3DES requires 24 bytes
    aes_key = adjust_key_length(user_key, 32, "AES-256")  # AES-256 requires 32 bytes

    # Adjust IVs to required sizes for each algorithm
    des_triple_des_iv = adjust_key_length(user_iv, 8, "DES and 3DES IV")  # IV of 8 bytes for DES/3DES
    aes_iv = adjust_key_length(user_iv, 16, "AES-256 IV")  # IV of 16 bytes for AES-256

    # Encryption and decryption processes for each algorithm
    print("\n--- DES Encryption and Decryption ---")
    encrypt_decrypt_DES(message_to_encrypt, des_key, des_triple_des_iv)

    print("\n--- 3DES Encryption and Decryption ---")
    encrypt_decrypt_3DES(message_to_encrypt, triple_des_key, des_triple_des_iv)

    print("\n--- AES-256 Encryption and Decryption ---")
    encrypt_decrypt_AES(message_to_encrypt, aes_key, aes_iv)

if __name__ == "__main__":
    main()
