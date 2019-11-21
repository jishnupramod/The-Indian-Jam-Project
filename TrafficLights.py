from tkinter import *

import time
import datetime
import timeit


# if __name__ == '__main__':
#     print(timeit.timeit(lambda: countdown_timer(20), number=1))


class TrafficLights:

    def countdown_timer(self, x):
        while x > 0:
            x -= 1
            print("{} ".format(str(datetime.timedelta(seconds=x))))
            print("\n")
            time.sleep(1)
        return 0

    def __init__(self):

        window = Tk()
        window.title("Traffic Light")

        frame = Frame(window)
        frame.pack()

     

        self.color = StringVar()

        start = Radiobutton(frame, text="START", bg="green", 
                                    variable=self.color, value="R", command=self.on_RadioChange)
        start.grid(row=10, column=2)

        # radio_red = Radiobutton(frame, text="STOP", bg="red",
        #                         variable=self.color, value="R", command=self.on_RadioChange)
        # radio_red.grid(row=10, column=1)

        # radio_yellow = Radiobutton(frame, text="CAUTION", bg="yellow",
        #                            variable=self.color, value="Y", command=self.on_RadioChange)
        # radio_yellow.grid(row=10, column=2)

        # radio_green = Radiobutton(frame, text="GO", bg="green",
        #                           variable=self.color, value="G", command=self.on_RadioChange)
        # radio_green.grid(row=10, column=3)

        self.canvas = Canvas(window, width=450, height=500, bg="white")
        self.canvas.pack()

        self.rectangle_bg = self.canvas.create_rectangle(10, 20, 380, 180, fill="black")
        self.pole = self.canvas.create_rectangle(140, 180, 240, 400, fill="brown")

        self.oval_red = self.canvas.create_oval(30, 40, 130, 140, fill="white")
        self.oval_yellow = self.canvas.create_oval(
            140, 40, 240, 140, fill="white")
        self.oval_green = self.canvas.create_oval(
            250, 40, 350, 140, fill="white")

        self.color.set('R')
        self.canvas.itemconfig(self.oval_green, fill="green")



        # self.x = int(input("Time: "))
        # window.after(1000, self.on_RadioChange(10))
        
        
        window.mainloop()

    def on_RadioChange(self):
        # color = self.color.get()

        import opencv1
        percent = opencv1.match_percent

        if percent > 90:
            x = 5
        elif percent > 50:
            x = 10
        elif percent > 21:
            x = 15
        elif percent > 20:
            x = 20
        else:
            x = 25

        # self.canvas.create_text(200, 100, text="{} ".format(
        #     str(datetime.timedelta(seconds=x))))


        if self.countdown_timer(x) != 0:
            self.canvas.itemconfig(self.oval_red, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_green, fill="green")
            
            self.canvas.create_text(400, 400, text="{} ".format(
                str(datetime.timedelta(seconds=x))))


        # elif color == 'Y':
        #     self.canvas.itemconfig(self.oval_red, fill="white")
        #     self.canvas.itemconfig(self.oval_yellow, fill="yellow")
        #     self.canvas.itemconfig(self.oval_green, fill="white")
        # elif color == 'G':
        #     self.canvas.itemconfig(self.oval_red, fill="white")
        #     self.canvas.itemconfig(self.oval_yellow, fill="white")
        #     self.canvas.itemconfig(self.oval_green, fill="green")

        else:
            # time.sleep(1)

            self.canvas.itemconfig(self.oval_green, fill="white")
            self.canvas.itemconfig(self.oval_yellow, fill="yellow")
            # self.canvas.itemconfig(self.oval_green, fill="white")

            # self.countdown_timer(2)

            # time.sleep(4)
            
            self.canvas.itemconfig(self.oval_yellow, fill="white")
            self.canvas.itemconfig(self.oval_red, fill="red")
            # self.canvas.itemconfig(self.oval_red, fill="white")
            # self.canvas.itemconfig(self.oval_yellow, fill="white")
            # self.canvas.itemconfig(self.oval_green, fill="green")

        


TrafficLights()
