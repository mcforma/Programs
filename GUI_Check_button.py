# GUI with check buttons
# A tkinter using a check button

import tkinter
import tkinter.messagebox

class CB_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Check Button GUI")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)

        # Create the three IntVar objects to use with
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(self.frame1,
        text = "Option1",
        variable = self.cb_var1)

        self.cb2 = tkinter.Checkbutton(self.frame1,
        text = "Option2",
        variable = self.cb_var2)

        self.cb3 = tkinter.Checkbutton(self.frame1,
        text = "Option3",
        variable = self.cb_var3)


        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

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
        self.message = "You selected:\n"

        if self.cb_var1.get() == 1:
            self.message += "Option 1.\n"
        if self.cb_var2.get() == 1:
            self.message += "Option 2.\n"
        if self.cb_var3.get() == 1:
            self.message += "Option 3.\n"

        tkinter.messagebox.showinfo("Choice", self.message)


if __name__ == "__main__":
    my_gui = CB_GUI()
        
        