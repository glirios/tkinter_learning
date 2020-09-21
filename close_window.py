import sys
from tkinter import *

class App(Frame):
    def __init__(self, parent = None):
        Frame.__init__(self, parent)
        self.grid()

        self.button = Button(self, text = "Create Dialog", command=self.CreateDialog)
        self.button.grid()

    def CreateDialog(self):
        dialog = Toplevel(self)
        dialog.wm_title("Dialog window")
        dialog.wm_transient(self)
        dialog.wm_protocol("WM_DELETE_WINDOW", lambda: self.onDeleteChild(dialog))
        button = Button(dialog, text="Close", command=lambda: self.onDeleteChild(dialog))
        button.grid()

    def onDeleteChild(self, w):
        w.destroy()


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    sys.exit(main())