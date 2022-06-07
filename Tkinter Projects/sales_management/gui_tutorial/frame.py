import tkinter

window = tkinter.Tk()
window.title("GUI")

# creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window, bg = "green").pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# now, create some widgets in the top_frame and bottom_frame
btn1 = tkinter.Button(top_frame, text = "Button1", bg = "blue", fg = "red").pack()# 'fg - foreground' is used to color the contents
btn2 = tkinter.Button(top_frame, text = "Button2", bg = "yellow", fg = "green").pack()# 'text' is used to write the text on the Button
btn3 = tkinter.Button(bottom_frame, text = "Button3", bg = "indigo", fg = "purple").pack(side = "left")# 'side' is used to align the widgets
btn4 = tkinter.Button(bottom_frame, text = "Button4", fg = "orange").pack(side = "right")

window.mainloop()