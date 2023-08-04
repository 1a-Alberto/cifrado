from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Función para generar una clave secreta aleatoria
def generar_clave():
    return get_random_bytes(16)  # Generamos una clave de 128 bits (16 bytes)

# Función para cifrar un mensaje
def cifrar(mensaje, clave):
    cipher = AES.new(clave, AES.MODE_EAX)  # Creamos una instancia de cifrado AES en modo EAX
    nonce = cipher.nonce  # Generamos un número único para cada cifrado
    ciphertext, tag = cipher.encrypt_and_digest(mensaje.encode('utf-8'))  # Ciframos el mensaje
    return nonce, ciphertext, tag  # Devolvemos el nonce, el mensaje cifrado y la etiqueta

# Función para descifrar un mensaje
def descifrar(nonce, ciphertext, tag, clave):
    cipher = AES.new(clave, AES.MODE_EAX, nonce=nonce)  # Creamos una instancia de descifrado con el nonce
    decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)  # Desciframos y verificamos la autenticidad
    return decrypted_data.decode('utf-8')  # Devolvemos el mensaje descifrado en formato legible

# Función principal del programa
def main():
    print("Bienvenido al Programa de Cifrado y Descifrado Simétrico")

    while True:
        print("\nElige una opción:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            clave_secreta = generar_clave()
            mensaje_original = input("Ingresa el mensaje que deseas cifrar: ")
            nonce, ciphertext, tag = cifrar(mensaje_original, clave_secreta)

            print("\nMensaje cifrado:", ciphertext.hex())
            print("Guarda la siguiente clave secreta de forma segura:")
            print(clave_secreta.hex())

        elif opcion == '2':
            clave_secreta = bytes.fromhex(input("Ingresa la clave secreta que guardaste: "))
            mensaje_cifrado = bytes.fromhex(input("Ingresa el mensaje cifrado: "))
            nonce = bytes.fromhex(input("Ingresa el número único (Nonce): "))
            tag = bytes.fromhex(input("Ingresa la etiqueta de autenticación: "))

            mensaje_descifrado = descifrar(nonce, mensaje_cifrado, tag, clave_secreta)
            print("\nMensaje descifrado:", mensaje_descifrado)

        elif opcion == '3':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
