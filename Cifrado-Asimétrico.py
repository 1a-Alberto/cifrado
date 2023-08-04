from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generar par de claves (pública y privada)
def generar_par_claves():
    clave_privada = RSA.generate(2048)
    clave_publica = clave_privada.publickey()
    return clave_privada, clave_publica

# Cifrar un mensaje
def cifrar_mensaje(mensaje, clave_publica):
    cifrador = PKCS1_OAEP.new(clave_publica)
    mensaje_cifrado = cifrador.encrypt(mensaje.encode())
    return mensaje_cifrado

# Descifrar un mensaje cifrado
def descifrar_mensaje(mensaje_cifrado, clave_privada):
    descifrador = PKCS1_OAEP.new(clave_privada)
    mensaje_descifrado = descifrador.decrypt(mensaje_cifrado)
    return mensaje_descifrado.decode()

# Función principal
def main():
    print("Bienvenido al Programa de Cifrado Asimétrico")

    while True:
        print("\nElige una opción:")
        print("1. Cifrar mensaje")
        print("2. Descifrar mensaje")
        print("3. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            clave_privada, clave_publica = generar_par_claves()
            mensaje_original = input("Ingresa el mensaje que deseas cifrar: ")
            mensaje_cifrado = cifrar_mensaje(mensaje_original, clave_publica)

            print("\nMensaje cifrado:")
            print(mensaje_cifrado.hex())
            print("\nGuarda la clave privada de manera segura para descifrar el mensaje posteriormente:")
            print(clave_privada.export_key().decode())

        elif opcion == '2':
            clave_privada_archivo = input("Ingresa el nombre del archivo de clave privada (en formato PEM): ")
            with open(clave_privada_archivo, 'rb') as f:
                clave_privada_pem = f.read()

            clave_privada = RSA.import_key(clave_privada_pem)

            mensaje_cifrado_hex = input("Ingresa el mensaje cifrado en formato hexadecimal: ")
            mensaje_cifrado = bytes.fromhex(mensaje_cifrado_hex)

            mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave_privada)
            print("\nMensaje descifrado:", mensaje_descifrado)

        elif opcion == '3':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()

