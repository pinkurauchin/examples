import customtkinter as customtkinter

import input_frame
import menu_frame


class SerialFrame(customtkinter.CTkFrame):

    # CONSTRUCTOR FOR THE FRAME
    def __init__(self, master, *args, **kwargs):
        super(SerialFrame, self).__init__(master)
        self.master = master
        self.configure(width=400, height=400)
        self.createWidgetsMain()

    def createWidgetsMain(self):
        # BUTTON AND COMMAND FOR THE NEXT FRAMES
        def segmented_button_callback(value):

            if value == "Inputs":
                self.destroy()
                input_frame.InputFrame(self.master).place(x=75, y=75)

            if value == "Menu":
                try:
                    self.destroy()
                    menu_frame.MenuFrame(self.master).place(x=25, y=75)
                except:
                    self.destroy()
                    SerialFrame(self.master).place(x=25, y=50)

        segemented_button = customtkinter.CTkSegmentedButton(master=self,
                                                             values=["Menu", "Inputs"],
                                                             command = segmented_button_callback)

        segemented_button.place(x=50, y=100)


# CREATING THE APP
root = customtkinter.CTk()
root.geometry("700x500")
root.title("Lumalcol Conf")
# CREATING THE FIRST FRAME CALLING THE CLASS MY APP
SerialFrame(root).place(x=25, y=50)
root.mainloop()