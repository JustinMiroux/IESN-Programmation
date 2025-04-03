"""
This program is a counter with a gui.
It uses : 
    -Tkinter
    -ttk & messagebox from Tkinter

And finally uses classes for clean code.
"""

# pylint: disable=W0401, W0614, R0903
# WildImport Error Ignored due to me being lazy and not wanting to import every tkinter module
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main_window = Tk()

frame = ttk.Frame(main_window, height=500, width=700)
frame.pack()

class CounterLabel:
    """
    This class is the class that saves the counter number.
    It also contains :
        -addx
        -reset
    """
    def __init__(self, parent):
        self.counter = 0
        self.label = ttk.Label(parent, text=self.counter)
        self.label.pack()

    def addx(self, x):
        """ This function is used to add x to counter """
        self.counter += x
        self.label.config(text=self.counter)

    def reset(self):
        """ This function reset x to 0 """
        self.counter = 0
        self.label.config(text=self.counter)

class ButtonPlusOne:
    """
    This class contains a button and a function that add 1 to counter from CounterLabel
    contains :
        -add_one
    """
    def __init__(self, parent, label):
        self.label = label
        self.button = ttk.Button(parent, text="Add 1", command=self.add_one)
        self.button.pack()

    def add_one(self):
        """ This function calls CounterLabel.addx and adds 1 """
        self.label.addx(1)

class EnterXFrame:
    """
    This class contains it's own frame only the text entry and button of this class are in it.
    it's purpose is to add any number to counter from CounterLabel
    Contains :
        -add_x
    """
    def __init__(self, parent, label):
        self.label = label
        self.frame = ttk.Frame(parent)
        self.value = StringVar()
        self.entry = ttk.Entry(self.frame, textvariable=self.value)
        self.validate_button = ttk.Button(self.frame, text="Add X", command=self.add_x)
        self.frame.pack()
        self.entry.pack()
        self.validate_button.pack()

    def add_x(self):
        """ add_x try to add the user input as an int fails if string is inputed """
        try:
            self.label.addx(int(self.value.get()))
        except ValueError as e:
            messagebox.showerror(title="Input Error",
            message=f"Le nombre X que vous avez rentré n'a pas pu être transformé en entié ( {e} )")

class ResetButton:
    """
    This class contains a button to reset the counter
    Contains :
        -reset
    """
    def __init__(self, parent, label):
        self.label = label
        self.button = ttk.Button(parent, text="RESET", command=self.reset)
        self.button.pack()

    def reset(self):
        """ This function calls CounterLabel.reset """
        self.label.reset()


counter_label = CounterLabel(frame)
button_add_one = ButtonPlusOne(frame, counter_label)
entry_add_X = EnterXFrame(frame, counter_label)
reset_button = ResetButton(frame, counter_label)


main_window.mainloop()
