import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

d, c = {chr(i): i for i in range(255)}, {i: chr(i) for i in range(255)}

def decrypt_message():
    file_path = filedialog.askopenfilename(title="Select an Encrypted Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path: return

    img, input_password = cv2.imread(file_path), pass_entry_dec.get()
    
    try:
        with open("password.txt", "r") as f: stored_password = f.read().strip()
        with open("message_length.txt", "r") as f: msg_length = int(f.read().strip())
    except FileNotFoundError:
        return messagebox.showerror("Error", "Missing password or message length file!")

    if stored_password != input_password:
        return messagebox.showerror("Error", "Incorrect Password!")

    message = "".join(c[img[i, i, i % 3]] for i in range(msg_length))
    messagebox.showinfo("Decryption Result", f"Decrypted Message: {message}")

root = tk.Tk()
root.title("Image Steganography - Decryption")

tk.Label(root, text="🔹 Decryption").grid(row=0, column=1, pady=5)
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
pass_entry_dec = tk.Entry(root, width=40, show="*"); pass_entry_dec.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Decrypt Message", command=decrypt_message, bg="lightgreen").grid(row=2, column=1, pady=10)

root.mainloop()
