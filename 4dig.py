import tkinter as tk
import random

root=tk.Tk()
root.geometry("300x100")
root.title("Emplyee Code Generator v1.0.0")

def employeecodeprint():
	code=random.choice(range(1001,10000))
	result.config(text=code)

result=tk.Label(root, text="", font=('Arial', 20))
butt=tk.Button(root, text="Generate", font=('Arial', 20), command=lambda:employeecodeprint())

result.pack()
butt.pack()

root.mainloop()