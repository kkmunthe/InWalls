#  FUNDING SITE - fodboldtur gui
#  21HTXCP PROGRAMMERING B - Kristine June Munthe

#  IMPORTS .
import tkinter
import pickle

import customtkinter
from customtkinter import *
from tkinter.ttk import *

filename = 'betalinger.pk'
logInOptions = [
    'Ole Olsen',
    'Jeppe Jeppesen',
    'Anders Andersen',
    'Henrik Henriksen',
    'Klaus Klausen',
    'Bent Bentsen',
    'Jens Jensen',
    'Ib Ibsen'
]


#  HOME CLASS .
class LogInWindow(CTk):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.target = 4500
        self.configure(background="black", padx=10, pady=5)
        self.geometry("854x480")
        self.title("FUNDING")

        title = CTkLabel(self, text="FODBOLDTUREN", font=('Times New Roman', 65, 'bold'), anchor='center', justify='center')
        title.grid(row=0, columnspan=60, sticky='n')

        # USERNAME & PASSWORD ENTRY
        name = CTkLabel(self, text="Name")
        password = CTkLabel(self, text="Password")
        self.usernameentry = CTkEntry(self)
        self.passwordentry = CTkEntry(self)
        # USERNAME & PASSWORD GRID
        name.grid(row=2, sticky="e")
        password.grid(row=3, sticky="e")
        self.usernameentry.grid(row=2, column=3)
        self.passwordentry.grid(row=3, column=3)

        # LOG IN BUTTON
        logInbutton = CTkButton(self, text="Log In", command=self.Submit)
        logInbutton.grid(row=4, column=3)

        self.mainloop()

    def Submit(self):
        print("Name:" + self.usernameentry.get())
        print("Password:" + self.passwordentry.get())

        if self.usernameentry.get() in fodboldtur.keys():
            accessAccepted = CTkLabel(self, text="Log in valid.")
            accessAccepted.grid(row=5, column=3)
            print("Name is valid.")
            HomeWindow()
        else:
            # ACCESSDENIED
            accessDenied = CTkLabel(self, text="Entry denied. Try again.")
            accessDenied.grid(row=5, column=3)
            print("Log in invalid.")

class HomeWindow(CTk):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.target = 4500
        self.configure(background="black", padx=10, pady=5)
        self.geometry("854x480")
        self.title("FUNDING")
        title = CTkLabel(self, text="FODBOLDTUREN", font=('Times New Roman', 65, 'bold'), anchor='center', justify='center')
        title.grid(row=0, columnspan=60, sticky='n')
#        homePhoto = CTkImage(self, )




if __name__ == "__main__":
        infile = open(filename, 'rb')
        fodboldtur = pickle.load(infile)
        infile.close()

        Webapp = LogInWindow()


