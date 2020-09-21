import tkinter as tk
from tkinter import ttk, Radiobutton


class ToggledFrame(tk.Frame):

    def __init__(self, parent, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)

        self.show = tk.StringVar()
        self.show.set("No")

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        ttk.Label(self.title_frame, text=text).grid(row = 0, column = 0)

        self.choice1 = Radiobutton(self.title_frame, width = 2, text = "Yes", value = "Yes", command = self.toggle, variable = self.show)
        self.choice2 = Radiobutton(self.title_frame, width = 2, text = "No", value = "No", command = self.toggle, variable = self.show)
        
        self.choice1.grid(row = 0, column = 1)
        self.choice2.grid(row = 0, column = 2)

        self.sub_frame = tk.Frame(self, relief="sunken", borderwidth=1)

    def toggle(self):
        if self.show.get() == "Yes":
            self.sub_frame.pack(fill="x", expand=1)
        else:
            self.sub_frame.forget()


if __name__ == "__main__":
    root = tk.Tk()

    t = ToggledFrame(root, text='Do you have assigned users?', relief="raised", borderwidth=1)
    t.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(t.sub_frame, text='Rotation [deg]:').pack(side="left", fill="x", expand=1)
    ttk.Entry(t.sub_frame).pack(side="left")

    t2 = ToggledFrame(root, text='Resize', relief="raised", borderwidth=1)
    t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    for i in range(10):
        ttk.Label(t2.sub_frame, text='Test' + str(i)).pack()

    t3 = ToggledFrame(root, text='Fooo', relief="raised", borderwidth=1)
    t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    for i in range(10):
        ttk.Label(t3.sub_frame, text='Bar' + str(i)).pack()

    root.mainloop()