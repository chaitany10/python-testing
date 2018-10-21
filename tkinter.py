from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.CreateWidgets()
    def CreateWidgets(self):
        self.LoginButton = Button(self)
        self.LoginButton["text"] = "Login"
        self.LoginButton.grid()
        self.QUIT_Button = Button(self)
        self.QUIT_Button["text"] = "Quit"
        self.QUIT_Button["command"] = self.quit
        self.QUIT_Button["fg"] = "red"

root = Tk()
root.title("Login")
root.geometry("500x500")
app = Application(root)
root.mainloop()