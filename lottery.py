"""
Program: lottery.py
Anthor: Li Chan
Project: Lottery Quick Pick

This program generates 5 random numbers between 1 and 50. By clicking the Quick Pick button,the computer randomly selects the numbers for you.

"""
from tkinter import *
import random

# This function generates 5 random numbers between 1 and 50.
def pickNum():
   lottoNum = []
   for i in range(5):
     number = random.randint(1, 50)
     lottoNum.append(number)
   return lottoNum

class Lottery(Frame):
   """This class represents GUI-based Lottery numbers generator."""
   def __init__(self):
        """Set up the window and the widgets."""
        Frame.__init__(self)
        self.master.title("Lottery Game")

        # Set up the heading
        self.grid()
        self._label = Label(self, text = "Welcome to New York Lottery", fg = "red",
        font = ("Arial", 25), justify = "center")
        self._label.grid(row = 0, column = 0, columnspan = 6)

        # Set up the entry fields for selected numbers
        self.grid_rowconfigure(2, minsize=20)
        self._Num1Var = IntVar()
        self._Num1Entry = Entry(self, textvariable = self._Num1Var, bd=10, insertwidth=0.2,
        width = 10, font = ("Arial", 15))
        self._Num1Entry.grid(row = 3, column = 1)
         
        self._Num2Var = IntVar()
        self._Num2Entry = Entry(self, textvariable = self._Num2Var, bd=10, insertwidth=0.2,
        width = 10, font = ("Arial", 15))
        self._Num2Entry.grid(row = 3, column = 2)

        self._Num3Var = IntVar()
        self._Num3Entry = Entry(self, textvariable = self._Num3Var, bd=10, insertwidth=0.2,
        width = 10, font = ("Arial", 15))
        self._Num3Entry.grid(row = 3, column = 3)

        self._Num4Var = IntVar()
        self._Num4Entry = Entry(self, textvariable = self._Num4Var, bd=10, insertwidth=0.2,
        width = 10, font = ("Arial", 15))
        self._Num4Entry.grid(row = 3, column = 4)

        self._Num5Var = IntVar()
        self._Num5Entry = Entry(self, textvariable = self._Num5Var, bd=10, insertwidth=0.2,
        width = 10, font = ("Arial", 15))
        self._Num5Entry.grid(row = 3, column = 5)

        # Set up button to quick pick 5 ramdom numbers
        self.grid_rowconfigure(15, minsize=50)
        self._button1 = Button(self, text = "Quick Pick", fg = "green", 
        font = ("Arial", 15), command = self._quickPick)
        self._button1.config(height = 1, width = 15)
        self._button1.grid(row = 5, column = 1, columnspan = 2)

        # Set up button to clear the selected numbers
        self.grid_rowconfigure(15, minsize=50)
        self._button2 = Button(self, text = "Reset", fg = "blue",
        font = ("Arial", 15), command = self._reset)
        self._button2.config(height = 1, width = 15)
        self._button2.grid(row = 5, column = 3, columnspan = 2)

   def _quickPick(self):
      """Event handler for the Quick Pick button"""
      numbers = pickNum()
      self._Num1Var.set(numbers[0])
      self._Num2Var.set(numbers[1])
      self._Num3Var.set(numbers[2])
      self._Num4Var.set(numbers[3])
      self._Num5Var.set(numbers[4])

   def _reset(self):
      """Reset all the selected numbers when clicking the Reset button"""
      self._Num1Var.set(0)
      self._Num2Var.set(0)
      self._Num3Var.set(0)
      self._Num4Var.set(0)
      self._Num5Var.set(0)

def main():
    """Initialize and pop up the window."""
    Lottery().mainloop()
	
main()
