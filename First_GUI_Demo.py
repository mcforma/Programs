# First_GUI_Demo.py
# You are creating a GUI using tkinter


import tkinter

class FirstGUI:
    def __init__(self):
        # create the main window
        self.main_window = tkinter.Tk()

        self.main_window.title("MY FIRST GUI")

        # create a label on the window
        self.label = tkinter.Label(self.main_window,
        text = "CSIS2101",
        borderwidth = 4,
        relief = "solid")

        self.label2 = tkinter.Label(self.main_window,
        text = "This is my fourth programming class",
        borderwidth = 10,
        relief = "sunken")

        # Call the pack method to pack label
        self.label.pack(ipadx = 20, ipady = 50, padx = 20, pady = 50)
        self.label2.pack(ipadx = 50, ipady = 20, padx = 50, pady = 20)

        tkinter.mainloop()

if __name__ == "__main__":
    my_gui = FirstGUI()