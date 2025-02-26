import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox

d, c = {chr(i): i for i in range(255)}, {i: chr(i) for i in range(255)}

def encrypt_message():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path: return

    img, msg, password = cv2.imread(file_path), msg_entry.get(), pass_entry_enc.get()
    if not msg or not password:
        return messagebox.showerror("Error", "Message and Password are required!")

    for i in range(len(msg)):
        img[i, i, i % 3] = d[msg[i]]

    cv2.imwrite("EncryptedMSG.png", img)
    with open("password.txt", "w") as f: f.write(password)
    with open("message_length.txt", "w") as f: f.write(str(len(msg)))

    messagebox.showinfo("Success", "Message Encrypted Successfully!")
    os.system("start EncryptedMSG.png")

root = tk.Tk()
root.title("Image Steganography - Encryption")

tk.Label(root, text="🔹 Encryption").grid(row=0, column=1, pady=5)
tk.Label(root, text="Secret Message:").grid(row=1, column=0, padx=10, pady=5)
msg_entry = tk.Entry(root, width=40); msg_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Password:").grid(row=2, column=0, padx=10, pady=5)
pass_entry_enc = tk.Entry(root, width=40, show="*"); pass_entry_enc.grid(row=2, column=1, padx=10, pady=5)
tk.Button(root, text="Encrypt Message", command=encrypt_message, bg="lightblue").grid(row=3, column=1, pady=10)

root.mainloop()
