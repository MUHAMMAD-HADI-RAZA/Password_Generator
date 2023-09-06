import tkinter as tk
import random
import string

class PassWord_Genertaor:
    def __init__(self):
        self.lower = string.ascii_lowercase
        self.upper = string.ascii_uppercase
        self.digit = string.digits
        self.Special_Char = "<>?/{}[]|\!@#$%^&*()_+-="

    def Generate_Pass(self, l, comp="Medium"):  #comp = complexity
        if l <= 0:
            raise ValueError("Password should contain length greater than Zero")
        char = self.lower + self.digit

        if comp == "Medium":
            char += self.upper
        elif comp == "High":
            char += self.upper + self.Special_Char
        Pass = "".join(random.choice(char) for j in range(l))
        return Pass
    
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PASSWORD GENERATOR APP")
        self.Gui_Window()
        self.Generator = PassWord_Genertaor()

    def Gui_Window(self):
        self.Widgets()
        self.Layout()
    
    def Widgets(self):
        self.Length_Entry()
        self.Complexity_Entry()
        self.Generate_Button()
        self.Pass_Box()

    def Layout(self):
        self.root.geometry("400x360")
        self.Len_Label.pack(pady=10)
        self.Len_Entry.pack(pady=5)
        self.Comp_Label.pack(pady=10)
        self.Low_Comp.pack()
        self.Med_Comp.pack()
        self.High_Comp.pack()
        self.Button.pack(pady=20)
        self.Box.pack(pady=10, padx=10, fill="both", expand=True)

    def Length_Entry(self):
        self.Len_Label = tk.Label(self.root, text="PASSWORD LENGTH:", font=("Times New Roman", 14, "bold underline"))
        self.Len_Entry = tk.Entry(self.root, font=("Times New Roman", 12))

    def Complexity_Entry(self):
        self.Comp_Label = tk.Label(self.root, text="COMPLEXITY:", font=("Times New Roman", 14))
        self.Comp_Var = tk.StringVar()
        self.Comp_Var.set("Medium")
        self.Low_Comp = tk.Radiobutton(self.root, text="LOW", variable=self.Comp_Var, value="Low", font=("Times New Roman", 12))
        self.Low_Comp = tk.Radiobutton(self.root, text="MEDIUM", variable=self.Comp_Var, value="Medium", font=("Times New Roman", 12))
        self.Low_Comp = tk.Radiobutton(self.root, text="HIGH", variable=self.Comp_Var, value="High", font=("Times New Roman", 12))