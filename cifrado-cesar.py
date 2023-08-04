import tkinter as tk

def encrypt_cesar(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_cesar(ciphertext, shift):
    return encrypt_cesar(ciphertext, -shift)

def encrypt_button_click():
    shift = int(shift_entry.get())
    plaintext = input_text.get("1.0", "end-1c")
    encrypted_text = encrypt_cesar(plaintext, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_text)

def decrypt_button_click():
    shift = int(shift_entry.get())
    ciphertext = input_text.get("1.0", "end-1c")
    decrypted_text = decrypt_cesar(ciphertext, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_text)

# Crear la ventana principal
root = tk.Tk()
root.title("Cifrado César")

# Etiqueta y entrada para la clave de cifrado
shift_label = tk.Label(root, text="Desplazamiento:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

# Área de entrada de texto
input_text = tk.Text(root, height=5, width=40)
input_text.pack()

# Botón para cifrar
encrypt_button = tk.Button(root, text="Cifrar", command=encrypt_button_click)
encrypt_button.pack()

# Botón para descifrar
decrypt_button = tk.Button(root, text="Descifrar", command=decrypt_button_click)
decrypt_button.pack()

# Área de salida de texto
output_text = tk.Text(root, height=5, width=40)
output_text.pack()

# Iniciar el bucle de la interfaz gráfica
root.mainloop()
