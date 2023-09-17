import tkinter as tk
import random
import string

class PassWord_Generator:
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
#create Gui for code 
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("PASSWORD GENERATOR APP")
        self.Gui_Window()
        self.Generator = PassWord_Generator()

    def Gui_Window(self):
        self.Widgets()
        self.Layout()
    
    def Widgets(self):
        self.Length_Entry()
        self.Complexity_Entry()
        self.Generate_Button()
        self.Pass_Box()

#layout for GUI
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
        self.Len_Label = tk.Label(self.root, text="PASSWORD LENGTH:", font=("Times New Roman", 14, "bold underline"), fg="green")
        self.Len_Entry = tk.Entry(self.root, font=("Times New Roman", 12))

    def Complexity_Entry(self):
        self.Comp_Label = tk.Label(self.root, text="COMPLEXITY:", font=("Times New Roman", 14, "bold underline"), fg="red")
        self.Comp_Var = tk.StringVar()
        self.Comp_Var.set("Medium")
        self.Low_Comp = tk.Radiobutton(self.root, text="LOW", variable=self.Comp_Var, value="Low", font=("Times New Roman", 12), fg="green")
        self.Med_Comp = tk.Radiobutton(self.root, text="MEDIUM", variable=self.Comp_Var, value="Medium", font=("Times New Roman", 12), fg="blue")
        self.High_Comp = tk.Radiobutton(self.root, text="HIGH", variable=self.Comp_Var, value="High", font=("Times New Roman", 12), fg="red")

    def Generate_Button(self):
        self.Button = tk.Button(self.root, text="GENERATE PASSWORD", command=self.Pass_Generate, font=("Times New Roman", 14, "bold"), bg="lightblue2", fg="blue")
        
    def Pass_Box(self):
        self.Box = tk.Text(self.root, height=1, wrap=tk.WORD, font=("Times New Roman", 14), fg="brown")
        self.Box.config(state="normal")

#Generate password
    def Pass_Generate(self):
        try:
            L = int(self.Len_Entry.get())
            Comp = self.Comp_Var.get()
            Pass = self.Generator.Generate_Pass(L, Comp)

            self.Box.config(state="normal")
            self.Box.delete("1.0", "end")
            self.Box.insert("1.0", "GENERATED PASSWORD IS: "+ Pass)
            self.Box.config(state="normal")

        except ValueError as e:
            self.Box.config(state="normal")
            self.Box.delete("1.0", "end")
            self.Box.insert("1.0", str(e))
            self.Box.config(state="normal")

root = tk.Tk()
APP = App(root)
root.mainloop()