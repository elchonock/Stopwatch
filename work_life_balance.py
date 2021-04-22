# import datetime
# from tkinter import colorchooser


import time
from datetime import timedelta
# import datetime
from tkinter import *
import Stopwatch as st

stopwatch = st.Stopwatch()

tk = Tk()
tk.title("Stopwatch")
label = Label(tk, text="00:00:00", font="Arial 28 bold")
label.pack(pady=(35, 0))


def setup():

    frame = Frame(tk)
    button_1 = Button(frame, text="START", width=6, command=start, background="#AF2A7A", font="Arial 18 bold")
    button_1.pack(side="left")
    button_2 = Button(frame, text="STOP", width=6, command=stop, background="#AF2A7A", font="Arial 18 bold")
    button_2.pack(side="left")
    reset_button = Button(frame, text="RESET", width=6, command=reset, background="#AF2A7A", font="Arial 18 bold")
    reset_button.pack(side="left")
    save_button = Button(frame, text="SAVED", width=6, command=saved, background="#AF2A7A", font="Arial 18 bold")
    save_button.pack(side="left")
    frame.pack(anchor="center", pady=5)


def create_label(text):
    label["text"] = text


# def create_label(text):
#     label = Label(tk, text=text, font="Arial 28 bold")
#     label.pack(pady=(35, 0))

def start():
    stopwatch.start()
    create_label(timedelta(seconds=(stopwatch.display_time())))

def stop():
    stopwatch.stop()
    create_label(timedelta(seconds=(stopwatch.display_time())))

def reset():
    stopwatch.reset()
    create_label("00:00:00")

def saved():
    create_label(stopwatch.saved)


canvas = Canvas(tk, height=50, width=300)
canvas.pack()
# frame = Frame(tk)
# button_1 = Button(frame, text="START", width=6, command=start, background="#AF2A7A", font="Arial 18 bold")
# button_1.pack(side="left")
# button_2 = Button(frame, text="STOP", width=6, command=stop, background="#AF2A7A", font="Arial 18 bold")
# button_2.pack(side="left")
# reset_button = Button(frame, text="RESET", width=6, command=reset, background="#AF2A7A", font="Arial 18 bold" )
# reset_button.pack(side="left")
# frame.pack(anchor="center", pady=5)




if __name__ == '__main__':
    setup()
    tk.mainloop()






# c = colorchooser.askcolor()
# print(c)
# canvas.create_rectangle(50, 50, 250, 250, fill=c[1])



# current_time = time.time()
# # print(current_time)
# time.sleep(7)
# stop_time = time.time()
# # print(stop_time)
# amount_of_time = stop_time - current_time
# # print(round(amount_of_time, 2))
