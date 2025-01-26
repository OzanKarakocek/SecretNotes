import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
cipher = Fernet(key)

NOTES_DIR = "notes"
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

master_keys = {}

def kaydet_ve_sifrele():
    title = title_entry.get()
    secret = secret_entry.get()
    master_key = master_key_entry.get()

    if not title or not secret or not master_key:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    encrypted_secret = cipher.encrypt(secret.encode()).decode()

    master_keys[title] = master_key

    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    with open(file_path, "w") as f:
        f.write(f"Encrypted Note: {encrypted_secret}\n")

    messagebox.showinfo("Success", f"Note '{title}' has been saved in '{file_path}'!")
    title_entry.delete(0, tkinter.END)
    secret_entry.delete(0, tkinter.END)
    master_key_entry.delete(0, tkinter.END)

def decrypt_note():
    title = title_entry.get()
    master_key = master_key_entry.get()

    if not title or not master_key:
        messagebox.showerror("Error", "Please enter both Title and Master Key!")
        return

    file_path = os.path.join(NOTES_DIR, f"{title}.txt")
    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"No note found with title '{title}'!")
        return

    if title not in master_keys or master_keys[title] != master_key:
        messagebox.showerror("Error", "Incorrect Master Key!")
        return

    with open(file_path, "r") as f:
        encrypted_secret = f.readline().strip().split(": ")[1]

    decrypted_secret = cipher.decrypt(encrypted_secret.encode()).decode()
    secret_entry.delete(0, tkinter.END)
    secret_entry.insert(0, decrypted_secret)
    messagebox.showinfo("Success", f"Note '{title}' has been decrypted!")

window = tkinter.Tk()
window.title("Secret Notes")
window.minsize(500, 800)
window.resizable(width=False, height=False)

logo = Image.open("logo.png")
resized_logo = logo.resize((100, 100))
logo = ImageTk.PhotoImage(resized_logo)

logo_label = tkinter.Label(window, image=logo)
logo_label.pack(pady=20)

title_label = tkinter.Label(window, text="Enter Your Title", font=("Arial", 14, "bold"))
title_label.pack(pady=5)

title_entry = tkinter.Entry(window, width=30, font=("Arial", 14), fg="blue")
title_entry.pack(pady=10)

secret_label = tkinter.Label(window, text="Enter Your Secret", font=("Arial", 14, "bold"))
secret_label.pack(pady=5)

secret_entry = tkinter.Entry(window, width=40, font=("Arial", 14), fg="blue")
secret_entry.pack(pady=10, ipady=20)

master_key_label = tkinter.Label(window, text="Enter Master Key", font=("Arial", 14, "bold"))
master_key_label.pack(pady=5)

master_key_entry = tkinter.Entry(window, width=30, font=("Arial", 14), fg="blue", show="*")
master_key_entry.pack(pady=10)

save_button = tkinter.Button(window, text="Save & Encrypt", command=kaydet_ve_sifrele, bg="green", fg="white")
save_button.pack(pady=20)

decrypt_button = tkinter.Button(window, text="Decrypt", command=decrypt_note, bg="blue", fg="white")
decrypt_button.pack(pady=20)

window.mainloop()
