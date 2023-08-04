# Tabla de sustitución
codigo = ['m', 'u', 'r', 'c', 'i', 'e', 'l', 'a', 'g', 'o']
numeros = '0123456789'

# Solicitar al usuario si desea encriptar o desencriptar
x = int(input('1 para encriptar\n2 para desencriptar\n'))

# Solicitar la entrada del usuario en minúsculas
texto = input('Escriba su palabra o frase: ').lower()

# Variable para almacenar el resultado
salida = ''

# Función para encriptar
def encriptar(caracter):
    if caracter in codigo:
        return str(codigo.index(caracter))
    else:
        return caracter

# Función para desencriptar
def desencriptar(caracter):
    if caracter.isdigit():
        return codigo[int(caracter)]
    else:
        return caracter

# Procesar el texto según la elección del usuario
if x == 1:
    salida = ''.join([encriptar(caracter) for caracter in texto])
elif x == 2:
    salida = ''.join([desencriptar(caracter) for caracter in texto])

# Imprimir el resultado
print(salida)
