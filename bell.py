import tkinter as tk

class popup(object):
    def __init__(self, parent):
        self.root=tk.Toplevel(parent)
        self.root.title("Popup")
        self.root.bind("<FocusOut>", self.Alarm)

    def Alarm(self, event):
        self.root.focus_force()
        self.root.bell()

main = tk.Tk()
main.title("Main")
pop = popup(main)
main.mainloop()