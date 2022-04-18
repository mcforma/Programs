# Participation_week13.py
# A tkinter GUI using button

# Switch to convert to Fahrenheit for participation question 12

import tkinter # allows creation of simple GUI programs
import tkinter.messagebox


class Temp_GUI:
    def __init__(self): # instantiate main window object
        self.main_window = tkinter.Tk()

        self.main_window.title("Temperature GUI") # Window title

        self.top_frame = tkinter.Frame(self.main_window) # Create two frame widgets (containers), top and bottom, to 
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,
        text = "Enter temperature in Celsius to be converted into Fahrenheit")

        self.celsius_entry = tkinter.Entry(self.top_frame,
        width = 10) # set width to 10 (though width is automatically adjusted to minimum width to fit label)

        # Pack labels

        self.prompt_label.pack(side = "top") # label object must be packed to determine where to place and to to display
        self.celsius_entry.pack(side = "top") # Entry widget object must be packed to determine where to place and to to display

        self.button1 = tkinter.Button(self.bottom_frame, # Button widget that user can click to cause action to occur
        text = "Convert into Fahrenheit",
        command = self.convert) # callback function / event handler

        self.quit_button = tkinter.Button(self.bottom_frame,
        text = "Quit",
        command = self.main_window.destroy) # "Quit" (close window)

        self.button1.pack(side = "left") 
        self.quit_button.pack(side = "left")


        self.top_frame.pack() # pack frames
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        # Get the value enter into the entry point
        cels = float(self.celsius_entry.get()) # get user input and cast to float

        # convert Fahrenheit to celsius
        fahr = cels * 9/5 + 32 # convert to fahrenheit

        tkinter.messagebox.showinfo("Results", # Output in message box as string, so cast cels and fahr to string
        str(cels) + " in celsius is equal to " 
        + str(fahr) + " in fahrenheit.")

if __name__ == "__main__": 
    my_gui = Temp_GUI()