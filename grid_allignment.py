import tkinter as tk
from tkinter import ttk, messagebox

class CCTV(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (LoginPage, ChangePasswordPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(column=0, row=0, sticky="nsew")

        self.creatingAccount()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def creatingAccount(self):
        self.show_frame(LoginPage)



class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.createView()

    # def createView(self):
        # self.labelPassword = ttk.Label(self, text="Password")
        # self.entryPassword = ttk.Entry(self, show = "*")
        # self.buttonLogin = ttk.Button(self, text="Login", command=lambda: self.controller.show_frame(ChangePasswordPage))

    #     self.labelPassword.grid(row=2, column=3, sticky="w")
    #     self.entryPassword.grid(row=2, column=4, sticky="e")
    #     self.buttonLogin.grid(row=3, columnspan=6, pady=10)
    # def createView(self):
    # 	inner_frame = tk.Frame(self)
    # 	inner_frame.pack(side="top", fill="none")

    	# self.labelPassword = ttk.Label(inner_frame, text="Password")
    	# self.entryPassword = ttk.Entry(inner_frame, show = "*")
    	# self.buttonLogin = ttk.Button(inner_frame, text="Login", command=lambda: self.controller.show_frame(ChangePasswordPage))

    # 	self.labelPassword.grid(row=1, column=1, sticky="e")
    # 	self.entryPassword.grid(row=1, column=2, sticky="ew")
    # 	self.buttonLogin.grid(row=2, column=1, columnspan=2)

    def createView(self):
        self.labelPassword = ttk.Label(self, text="Password")
        self.entryPassword = ttk.Entry(self, show = "*")
        self.buttonLogin = ttk.Button(self, text="Login", command=lambda: self.controller.show_frame(ChangePasswordPage))

        self.labelPassword.grid(row=1, column=1, sticky="e")
        self.entryPassword.grid(row=1, column=2, sticky="ew")
        self.buttonLogin.grid(row=2, column=1, columnspan=2)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)

class ChangePasswordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.createView()

    def createView(self):
        self.labelSecurityQuestion = ttk.Label(self, text="A very very very very very very very very very very long string")
        self.entrySecurityQuestion = ttk.Entry(self)
        self.buttonCreateAccount = ttk.Button(self, text="Change Password", command=lambda: self.controller.show_frame(LoginPage))

        self.labelSecurityQuestion.grid(row=3, column=0, sticky="w")
        self.entrySecurityQuestion.grid(row=3, column=1, sticky="e")
        self.buttonCreateAccount.grid(row=5, columnspan=2, pady=10)


app = CCTV()
app.geometry("800x600")
app.mainloop()