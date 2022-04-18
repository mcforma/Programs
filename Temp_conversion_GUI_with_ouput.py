#First_GUI_WITH_FRAMES.py
#A tkinter GUI using frames

# Switch to convert to Fahrenheit for participation question 12

import tkinter
import tkinter.messagebox


class Temp_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Temperature GUI")

        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame,
        text = "Enter temperature in Farenheit to be converted into Celsius")

        self.fahr_entry = tkinter.Entry(self.top_frame,
        width = 10)

        # Pack labels

        self.prompt_label.pack(side = "top")
        self.fahr_entry.pack(side = "top")

        self.desc_label = tkinter.Label(self.middle_frame,
        text = "Temperature converted into Celcius")

        # We need a String variable object to associate with an output. Use the
        # object's set method to store the value
        self.value = tkinter.StringVar()

        self.celsius_label = tkinter.Label(self.middle_frame,
        textvariable = self.value)

        self.desc_label.pack( side = "left")
        self.celsius_label.pack( side = "left" )

        self.button1 = tkinter.Button(self.bottom_frame,
        text = "Convert into Celsius",
        command = self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame,
        text = "Quit",
        command = self.main_window.destroy)

        self.button1.pack(side = "left")
        self.quit_button.pack(side = "left")


        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def convert(self):
        # Get the value enter into the entry point
        fahr = float(self.fahr_entry.get())

        # convert Fahrenheit to celsius
        cel = (fahr - 32) * 5/9

        self.value.set(cel)

if __name__ == "__main__":
    my_gui = Temp_GUI()