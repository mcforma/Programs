# Radio_Button_Demo.py
# radio_button.py

import tkinter
import tkinter.messagebox

class RB_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Radio Button GUI")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        # Create an IntVar object to use with Radio Button

        self.radio_var = tkinter.IntVar()

        # set the IntVar onject to 1.

        self.radio_var.set(1)

        # Create the RadioButton widgets in the top frame

        self.rb1 = tkinter.Radiobutton(self.frame1,
        text = "Live in the Dorms",
        variable = self.radio_var,
        value = 1)

        self.rb2 = tkinter.Radiobutton(self.frame1,
        text = "Live in outside apartment",
        variable = self.radio_var,
        value = 2)

        self.rb3 = tkinter.Radiobutton(self.frame1,
        text = "Living at home",
        variable = self.radio_var,
        value = 3)

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()


        self.button1 = tkinter.Button(self.frame2,
        text = "Ok",
        command = self.show_choice)

        self.quit_button = tkinter.Button(self.frame2,
        text = "Quit",
        command = self.main_window.destroy)

        self.button1.pack(side = "left")
        self.quit_button.pack(side = "left")

        self.frame1.pack()
        self.frame2.pack()

        tkinter.mainloop()


    def show_choice(self):
        choice = self.radio_var.get()

        if choice == 1:
            msg = "Student lives in the dorm."

        elif choice == 2:
            msg = "Student lives in an outside apartment."

        else:
            msg = "Student lives at home with the parents."

        tkinter.messagebox.showinfo("Option", msg)

if __name__ == "__name__":
    my_gui = RB_GUI()
    