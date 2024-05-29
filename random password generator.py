#RANDOM PASSWORD GENERATOR
import tkinter  as tk
from tkinter import *
from tkinter import messagebox

import string
import random
def random_password_generator():
  l=int(length.get())
  
  if l<=0:
    messagebox.showinfo("","password length must be atleast 1!")
  elif l>=1:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(l))
    
    
    messagebox.showinfo("",f"password is:{password}")
  else:
    messagebox.showinfo("","error! enter a valid length for password")


root=tk.Tk()
root.title("RANDOM PASSWORD GENERATOR")
root.geometry("300x300")
global length
label=tk.Label(root,text="Enter the length of the password")
label.grid(column=0, row=0)
length=Entry(root,width=10)
length.grid(column=1, row=0)

button=Button(root,text="Generate",bg="blue",fg="white",command=random_password_generator)
button.grid(column=2, row=0)




root.mainloop()
