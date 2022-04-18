# File:    speedLimitGUI_matt.py 
# Project: CSIS2101 Assignment 12
# Author:  Matthew Forbes 
# History: Version 1.1 April 11, 2022

"""
This is a GUI program desisgned to calculate the amount a driver should be fined for speeding,
depending upon how many miles per hour over the speed limit they are going. The calculated
fine is displayed as a label using a string variable object associated with a tkinter label.
The fine is calculated using the if, elif, else decision structure, in addition
to receiving the speed limit and speed of the driver as input from the user. 
"""

import tkinter

class Frame_GUI:
    def __init__(self): # instantiate main window object

        self.main_window = tkinter.Tk() # Window GUI

        self.main_window.title("speedlimitGUI_matt.py") # Window title

        # Create three frame widgets (containers), top, middle and bottom, to provide separate areas to pack labels and entries 
        self.top_frame = tkinter.Frame(self.main_window) # prompt labels and associated input text boxes will be associated with top frame
        self.middle_frame = tkinter.Frame(self.main_window) # fine label with StringVar variabletext and description
        self.bottom_frame = tkinter.Frame(self.main_window) # Button to calculate and button to quit

        self.prompt_speedlimit_label = tkinter.Label(self.top_frame, # Label to prompt user for speed limit of the zone
        text = "Please input the speed limit of the zone:")

        self.speedlimit_entry = tkinter.Entry(self.top_frame, # input text box for speed limit
        width = 10)

        self.prompt_speed_label = tkinter.Label(self.top_frame,  # label to prompt user for speed of vehicle
        text = "Please input the speed of the vehicle:")

        self.speed_entry = tkinter.Entry(self.top_frame, # input text box for speed of vehicle
        width = 10)

        self.prompt_szone = tkinter.Label(self.top_frame, # prompt user to enter if school zone
        text = "Did the speeding occur in a school zone? Please only enter \"yes\" or \"y\"\n" +
            "for yes, or \"no\" or \"n\" for no. Any other input will be considered \"yes\":")

        self.szone_entry = tkinter.Entry(self.top_frame, # input text box for school zone
        width = 10)

        self.desc = tkinter.Label(self.middle_frame, # description for StringVar (provides context for fine amount)
        text = "Speeding Fine: ")

        self.value = tkinter.StringVar() # String variable (StringVar) object to associate with output. Use object's set method to store the value
        self.fine_label = tkinter.Label(self.middle_frame, textvariable = self.value) # Associate with output label

        # Pack labels

        self.prompt_speedlimit_label.pack(side = "top") # pack speedlimit prompt and entry/ graphic input textbox 
        self.speedlimit_entry.pack(side = "top")

        self.prompt_speed_label.pack(side = "top") # pack speed prompt and entry/ graphic input textbox 
        self.speed_entry.pack(side = "top")

        self.prompt_szone.pack(side = "top") # pack school zone (szone) prompt and entry/ graphic input textbox
        self.szone_entry.pack(side = "top")

        self.calc_fine_button = tkinter.Button(self.bottom_frame, # calc fine button will call Forbes_SpeedLimit when click
        text = "Calculate Fine",
        command = self.Forbes_SpeedLimit)

        self.quit_button = tkinter.Button(self.bottom_frame, # quit_button will close/destroy GUI window
        text = "Quit",
        command = self.main_window.destroy)

        self.desc.pack(side = "left")
        self.fine_label.pack(side = "left") # pack fine label to display
        self.calc_fine_button.pack(side = "left") # Pack calc fine and quit buttons
        self.quit_button.pack(side = "left")

        self.top_frame.pack() # pack frames
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def Forbes_SpeedLimit(self):

        # get zone's speed limit from input text box
        matt_speedLimit = float(self.speedlimit_entry.get())

        # get speed of driver's vehicle from user
        matt_speed = float(self.speed_entry.get())

        # get if speeding occurred in school zone from user
        if matt_speed - matt_speedLimit > 0: # added this in order to prevent it from outputting if driver
            # was not speeding
            matt_s_zone = self.szone_entry.get() # get if school zone from input text box

            matt_s_zone = matt_s_zone.lower() # change case to lowercase to account for upper case characters

            # if input is not "yes", "y", "no", or "n", user is informed input is invalid
            # and school zone variable is assigned string literal "yes"
            # Accordingly nested this if statement inside the above in the even that the driver is not speeding
            # to prevent error
            if matt_s_zone != "yes" and matt_s_zone != "y" and matt_s_zone != "no" and matt_s_zone != "n":
                print("That input is invalid and will be considered as \"yes\" or \"y\".")
                matt_s_zone = "yes"

        speeding_amount = matt_speed - matt_speedLimit
        if speeding_amount <= 0:
            fine_amount = 0.0

        elif speeding_amount < 10 and speeding_amount > 0:
            fine_amount = 69.50

        elif speeding_amount < 20:
            fine_amount = 99.50

        elif speeding_amount < 30:
            fine_amount = 129.50

        elif speeding_amount < 35:
            fine_amount = 149.50

        elif speeding_amount >= 35:
            fine_amount = "Court Mandatory - Fine decided in Court"

        if speeding_amount < 35 and speeding_amount > 0:
            if matt_s_zone == "yes" or matt_s_zone == "y":
                fine_amount *= 2


        self.value.set(fine_amount)
 


if __name__ == "__main__":
    my_gui = Frame_GUI()