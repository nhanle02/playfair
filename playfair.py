import tkinter as tk
from tkinter import messagebox

# Lê Đình Nhân - lớp 20CCNTD - nhom 9
def generate_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I")
    key_set = set(key)
    english_alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key_set:
        english_alphabet = english_alphabet.replace(char, "")
    key += english_alphabet
    playfair_matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return playfair_matrix

def encrypt(plaintext, key):
    playfair_matrix = generate_playfair_matrix(key)
    ciphertext = ""
    plaintext = plaintext.replace(" ", "").upper()
    plaintext = plaintext.replace("J", "I")
    for i in range(0, len(plaintext), 2):
        a = plaintext[i]
        b = plaintext[i+1] if i+1 < len(plaintext) else 'X'
        if a not in ''.join(playfair_matrix) or b not in ''.join(playfair_matrix):
            continue
        row1, col1 = divmod(''.join(playfair_matrix).index(a), 5)
        row2, col2 = divmod(''.join(playfair_matrix).index(b), 5)
        if row1 == row2:
            ciphertext += playfair_matrix[row1][(col1+1) % 5] + playfair_matrix[row2][(col2+1) % 5]
        elif col1 == col2:
            ciphertext += playfair_matrix[(row1+1) % 5][col1] + playfair_matrix[(row2+1) % 5][col2]
        else:
            ciphertext += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]
    return ciphertext

def encrypt_button_click():
    plaintext = plaintext_entry.get()
    key = key_entry.get()
    if len(plaintext) < 2:
        messagebox.showerror("Error", "Plaintext should be at least 2 characters long.")
        return
    if len(key) == 0:
        messagebox.showerror("Error", "Please enter a key.")
        return
    ciphertext = encrypt(plaintext, key)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(tk.END, ciphertext)

window = tk.Tk()
window.title("Playfair Cipher")
window.geometry("500x400")

plaintext_label = tk.Label(window, text="Plaintext:")
plaintext_label.grid(row=0, column=0, padx=10, pady=10)
key_label = tk.Label(window, text="Key:")
key_label.grid(row=1, column=0, padx=10, pady=10)
ciphertext_label = tk.Label(window, text="Ciphertext:")
ciphertext_label.grid(row=2, column=0, padx=10, pady=10)

plaintext_entry = tk.Entry(window, width=30)
plaintext_entry.grid(row=0, column=1, padx=10, pady=10)
key_entry = tk.Entry(window, width=30)
key_entry.grid(row=1, column=1, padx=10, pady=10)
ciphertext_entry = tk.Entry(window, width=30)
ciphertext_entry.grid(row=2, column=1, padx=10, pady=10)

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_button_click)
encrypt_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()