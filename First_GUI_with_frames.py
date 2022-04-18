#First_GUI_WITH_FRAMES.py

#A tkinter GUI using frames

import tkinter


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


        self.label4 = tkinter.Label(self.top_frame,
        text = "SuperMan")

        self.label5 = tkinter.Label(self.top_frame,
        text = "SpiderMan")

        self.label6 = tkinter.Label(self.top_frame,
        text = "WonderWoman")

        self.label4.pack(side = "right")
        self.label5.pack(side = "right")
        self.label6.pack(side = "right")

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

if __name__ == "__main__":
    my_gui = Frame_GUI()