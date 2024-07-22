import random
import tkinter as tk
from tkinter import messagebox

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "1234567890"
symbols = ".,;:()[]{}/\\'?"

upper, lower, nums, syms = True, True, True, True

all = ''

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols 


def show_password():
    length = int(text.get(1.0, 'end'))
    password = ''.join(random.sample(all, length))
    messagebox.showinfo(title ="Password", message = password)


root = tk.Tk()
root.geometry("290x120")
root.title("Password Generator")

Password_length = tk.Label(root, text = "Password length", font=('Arial', 16))
Password_length.grid(row=1, column = 1, padx=40, pady=10)

text = tk.Text(root, height=1, width = 2, font = ('Arial', 12))
text.grid(row=1, column=2)
btn_1 = tk.Button(root, text = "Generate", font = ('Arial', 16), command= show_password)
btn_1.grid(row= 2, column = 1, columnspan=2, padx=50, pady = 10)

root.mainloop()