# import all the modules for the gui
from tkinter import ttk
from tkinter import messagebox
import random
import string
import tkinter as tk

class Password:
    # constructor that takes the length of the password
    def __init__(self, length):
        self.length = length
        self.password = ""

    def __init__(self):
        self.length = random.randint(8, 16)
        self.password = ""

    # method to generate the password
    def generate(self):
        # get all the characters
        chars = string.ascii_letters + string.digits + string.punctuation

        # generate the password
        for _ in range(self.length):
            self.password += random.choice(chars)

        return self.password
    
    # method to get the password
    def get_password(self):
        return self.password
    
    # method to get the length of the password
    def get_length(self):
        return self.length
    
    # method to set the length of the password
    def set_length(self, length):
        self.length = length

    # method for checking the strength of the password
    def check_strength(self):

        # enum for the strength of the password
        class Strength:
            WEAK = 1
            MEDIUM = 2
            STRONG = 3

        # set the strength to weak of the enum
        strength = Strength.WEAK

        # check for the length of the password
        if self.length >= 8 and self.length <= 16:
            strength = Strength.MEDIUM
        elif self.length > 16:
            strength = Strength.STRONG

        # check for the digits in the password
        if any(char.isdigit() for char in self.password):
            strength = Strength.MEDIUM
        if any(char.isdigit() for char in self.password) and self.length > 16:
            strength = Strength.STRONG

        # check for the uppercase characters in the password
        if any(char.isupper() for char in self.password):
            strength = Strength.MEDIUM
        if any(char.isupper() for char in self.password) and self.length > 16:
            strength = Strength.STRONG

        # check for the lowercase characters in the password
        if any(char.islower() for char in self.password):
            strength = Strength.MEDIUM
        if any(char.islower() for char in self.password) and self.length > 16:
            strength = Strength.STRONG

        # check for the special characters in the password
        if any(char in string.punctuation for char in self.password):
            strength = Strength.MEDIUM
        if any(char in string.punctuation for char in self.password) and self.length > 16:
            strength = Strength.STRONG

        # return the strength of the password as a string
        if strength == Strength.WEAK:
            return "Weak"
        elif strength == Strength.MEDIUM:
            return "Medium"
        elif strength == Strength.STRONG:
            return "Strong"
    
    # method to clear the password
    def clear(self):
        self.password = ""
        self.length = 0

# class for the gui
class GUI:
    # constructor
    def __init__(self):
        # create the window
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("400x300")
        self.window.resizable(False, False)

        # create the frame
        self.frame = ttk.Frame(self.window)
        self.frame.pack()

        # create the label
        self.label = ttk.Label(self.frame, text="Password Generator")
        self.label.pack()

        # create the entry
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack()

        # create the button
        self.button = ttk.Button(self.frame, text="Generate", command=self.generate)
        self.button.pack()

        # create the strength label
        self.strength_label = ttk.Label(self.frame, text="Strength: ")
        self.strength_label.pack()

        # create the strength entry
        self.strength_entry = ttk.Entry(self.frame, width=30)
        self.strength_entry.pack()

        # create the copy button
        self.copy_button = ttk.Button(self.frame, text="Copy", command=self.copy)
        self.copy_button.pack()

        # create the clear button
        self.clear_button = ttk.Button(self.frame, text="Clear", command=self.clear)
        self.clear_button.pack()

        # create the exit button
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.exit)
        self.exit_button.pack()

        # create a length label with a menu
        self.length_label = ttk.Label(self.frame, text="Length: ")
        self.length_label.pack()

        # create a length dropdown menu
        self.length_spinbox = tk.Spinbox(self.frame, from_=8, to=32, width=5)
        self.length_spinbox.pack()

        # create the password object
        self.password = Password()

        # start the main loop
        self.window.mainloop()
        
    # method to generate the password
    def generate(self):
        # clear the password
        self.password.clear()

        # get the length from the spinbox
        length = int(self.length_spinbox.get())

        # set the length of the password
        self.password.set_length(length)

        # generate the password
        self.password.generate()

        # set the password in the entry
        self.entry.delete(0, "end")
        self.entry.insert(0, self.password.get_password())

        # set the strength of the password
        self.strength_entry.delete(0, "end")
        self.strength_entry.insert(0, self.password.check_strength())
        

    # method to copy the password
    def copy(self):
        # copy the password to the clipboard
        self.window.clipboard_clear()
        self.window.clipboard_append(self.password.get_password())

        # show a message box
        messagebox.showinfo("Password Generator", "Password copied to clipboard")

    # method to clear the password
    def clear(self):
        # clear the password
        self.password.clear()

        # clear the entry
        self.entry.delete(0, "end")
        self.strength_entry.delete(0, "end")

    # method to exit the program
    def exit(self):
        # exit the program
        self.window.destroy()

# call the main function
def main():
    gui = GUI()

if __name__ == "__main__":
    main()