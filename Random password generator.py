import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    """Generates a secure random password with uppercase, lowercase, digits, and symbols."""
    if length < 4:
        messagebox.showerror("Error", "Password length should be at least 4 characters.")
        return ""
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(string.ascii_uppercase, 1) + \
               random.sample(string.ascii_lowercase, 1) + \
               random.sample(string.digits, 1) + \
               random.sample(string.punctuation, 1) + \
               random.choices(all_characters, k=length - 4)
    
    random.shuffle(password)
    return ''.join(password)

def generate_passphrase(word_count=4):
    """Generates a random passphrase using common words."""
    words = ["apple", "banana", "cherry", "delta", "elephant", "falcon", "giraffe", "horizon", "island", "jungle"]
    if word_count < 2:
        messagebox.showerror("Error", "Passphrase should have at least 2 words.")
        return ""
    passphrase = '-'.join(random.sample(words, min(word_count, len(words))))
    return passphrase

def generate_and_display():
    try:
        if var.get() == 1:
            length = int(entry.get())
            password = generate_password(length)
            result_var.set(password)
        else:
            word_count = int(entry.get())
            result_var.set(generate_passphrase(word_count))
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.configure(bg="#800080")  # Purplish pink background

tk.Label(root, text="Enter length (password) or word count (passphrase):", bg="#800080", fg="white").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

var = tk.IntVar(value=1)
tk.Radiobutton(root, text="Password", variable=var, value=1, bg="#800080", fg="white").pack()
tk.Radiobutton(root, text="Passphrase", variable=var, value=2, bg="#800080", fg="white").pack()

tk.Button(root, text="Generate", command=generate_and_display, bg="#FF69B4", fg="white").pack(pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12, "bold"), bg="#800080", fg="white")
result_label.pack(pady=5)

root.mainloop()