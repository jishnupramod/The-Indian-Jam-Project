import os
import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk
import datetime
import time
import timeit
from opencv import percent_list

WIDTH = 1440
HEIGHT = 1200

images = ['path_ref.jpg', 'image_1.jpg',
          'image_2.jpg', 'image_3.jpg', 'image_4.jpg']

resized = []

for image in images:
    out_img = os.path.splitext(image)[0] + "_edit.jpg"
    im = Image.open(image)
    im = im.resize((400, 600))
    im.save(out_img, "JPEG")
    resized.append(out_img)


root = tk.Tk()
root.title('Signal Activation')

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# background_image = tk.PhotoImage(file='landscape.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root)
frame1.place(relx=0, y=0, relwidth=0.25, relheight=0.6)

image1 = ImageTk.PhotoImage(file=resized[1])
image1_label = tk.Label(frame1, image=image1)
image1_label.place(relwidth=0.98, relheight=1)


frame2 = tk.Frame(root)
frame2.place(relx=0.25, y=0, relwidth=0.25, relheight=0.6)

image2 = ImageTk.PhotoImage(file=resized[2])
image2_label = tk.Label(frame2, image=image2)
image2_label.place(relwidth=0.98, relheight=1)


frame3 = tk.Frame(root)
frame3.place(relx=0.5, y=0, relwidth=0.25, relheight=0.6)

image3 = ImageTk.PhotoImage(file=resized[3])
image3_label = tk.Label(frame3, image=image3)
image3_label.place(relwidth=0.98, relheight=1)


frame4 = tk.Frame(root)
frame4.place(relx=0.75, y=0, relwidth=0.25, relheight=0.6)

image4 = ImageTk.PhotoImage(file=resized[4])
image4_label = tk.Label(frame4, image=image4)
image4_label.place(relwidth=0.98, relheight=1)

oval1 = canvas.create_oval(90, 500, 210, 620, fill="red")
oval2 = canvas.create_oval(470, 500, 590, 620, fill="red")
oval3 = canvas.create_oval(850, 500, 970, 620, fill="red")
oval4 = canvas.create_oval(1230, 500, 1350, 620, fill="green")

ovals = [oval1, oval2, oval3, oval4]

timer = tk.Text(root, font=("Helvetica", 50))
x = 20
timer.insert(tk.INSERT, "{} ".format(str(datetime.timedelta(seconds=x))))
timer.place(x=590, y=650, width=260, height=120)

while(True):
    percent_match = percent_list[1:]
    x = 20
    for i in range(4):
        min_percent = min(percent_match)
        if i != 0:
            prev_index = index
        else:
            prev_index = percent_match.index(max(percent_match))
        index = percent_match.index(min_percent)
        temp = x
        while(temp >= 0):
            canvas.itemconfig(ovals[index], fill="green")
            canvas.itemconfig(ovals[prev_index], fill="red")

            root.update()
            timer.insert(tk.INSERT, "{} ".format(
                str(datetime.timedelta(seconds=temp))))
            root.update()
            temp -= 1
            time.sleep(1)
            timer.delete(1.0, tk.END)
            root.update()
        x -= 5
        percent_match.remove(min_percent)


# frame = tk.Frame(root, bg='#035afc', bd=5)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry = tk.Entry(frame, font=('Courier', 30))
# entry.place(relwidth=0.65, relheight=1)

# button = tk.Button(frame, text="Get Weather", font=(
#     'Courier', 18), command=lambda: get_weather(entry.get()))
# button.place(relx=0.7, relwidth=0.3, relheight=1)

# lower_frame = tk.Frame(root, bg='#035afc', bd=10)
# lower_frame.place(relx=0.5, rely=0.25, relheight=0.6,
#                   relwidth=0.75, anchor='n')

# label = tk.Label(lower_frame, font=('Courier', 30),
#                  anchor='nw', justify='left', bd=5)
# label.place(relwidth=1, relheight=1)

# weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
# weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
