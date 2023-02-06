import customtkinter


class MenuFrame(customtkinter.CTkFrame):

    # CONSTRUCTOR FOR THE CLASS
    def __init__(self, master):
        super(MenuFrame, self).__init__(master)
        self.master = master
        self.configure(width=650, height=350)
        self.createWidgets()


    def createWidgets(self):
        def go_back():
            self.destroy()
            btn_back.destroy()
            from main import SerialFrame
            SerialFrame(self.master).place(x=25, y=50)

        btn_back = customtkinter.CTkButton(self.master, text="Go Back",
                                           command=go_back, cursor="hand2")
        btn_back.place(x=50, y=100)