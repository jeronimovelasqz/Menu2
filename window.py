from tkinter import *



class Menu2:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("677x746")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 746,
            width = 677,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"backgroundMenu2.png")
        self.background = self.canvas.create_image(
            590.5, 440.5,
            image=self.background_img)

        self.img0 = PhotoImage(file = f"img0Menu2.png")
        self.b0 = Button(
            image = self.img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b0.place(
            x = 11, y = 610,
            width = 181,
            height = 44)

        self.img1 = PhotoImage(file = f"img1Menu2.png")
        self.b1 = Button(
            image = self.img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b1.place(
            x = 467, y = 663,
            width = 213,
            height = 52)

        self.img2 = PhotoImage(file = f"img2Menu2.png")
        self.b2 = Button(
            image = self.img2,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")

        self.b2.place(
            x = 473, y = 599,
            width = 207,
            height = 53)

        self.window.resizable(False, False)
        self.window.mainloop()


    def btn_clicked(self):
        print("Button Clicked")

eso = Menu2()