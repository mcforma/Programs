#First_GUI_WITH_FRAMES.py

#A tkinter GUI using frames

import tkinter
import tkinter.messagebox


class Frame_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("MYFRAME GUI")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame,
        text = "SuperMan")

        self.label2 = tkinter.Label(self.top_frame,
        text = "SpiderMan")

        self.label3 = tkinter.Label(self.top_frame,
        text = "WonderWoman")

        # Pack labels

        self.label1.pack(side = "top")
        self.label2.pack(side = "top")
        self.label3.pack(side = "top")

        self.button1 = tkinter.Button(self.bottom_frame,
        text = "Click Me",
        command = self.click_me)

        self.quit_button = tkinter.Button(self.bottom_frame,
        text = "Quit",
        command = self.main_window.destroy)

        self.button1.pack(side = "left")
        self.quit_button.pack(side = "left")


        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def click_me(self):
        tkinter.messagebox.showinfo("Response", "Thanks for clicking me.")

if __name__ == "__main__":
    my_gui = Frame_GUI()