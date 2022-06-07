from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Affable Digital Services')

my_img1 = ImageTk.PhotoImage(Image.open('images/img_1.jpg').resize((350, 350), Image.ANTIALIAS))
my_img2 = ImageTk.PhotoImage(Image.open('images/img_2.jpg').resize((350, 350), Image.ANTIALIAS))
my_img3 = ImageTk.PhotoImage(Image.open('images/img_3.jpg').resize((350, 350), Image.ANTIALIAS))
my_img4 = ImageTk.PhotoImage(Image.open('images/img_4.jpg').resize((350, 350), Image.ANTIALIAS))
my_img5 = ImageTk.PhotoImage(Image.open('images/img_5.jpg').resize((350, 350), Image.ANTIALIAS))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
status = Label(root, text=f'Image 1 of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
my_label = Label(root, image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()  # get rid of something
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    if image_number == len(image_list):
        button_forward = Button(root, text='<<', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()  # get rid of something
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    status = Label(root, text=f'Image {image_number} of {len(image_list)}', bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='EXIT', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()