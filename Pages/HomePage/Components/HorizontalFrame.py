import tkinter as tk
import tkinter.font as tkfont
import pyglet


class MyButton:
    def __init__(self, frame, image, text):
        self.Button = tk.Button(frame,
                                image=image,
                                text=text,
                                height=300,
                                width=300,
                                border=0,
                                compound=tk.TOP,
                                font='play',
                                background='black',
                                activebackground='black',
                                foreground='white',
                                activeforeground='white',
                                padx=10)

    def grid(self, row=0, column=0):
        self.Button.grid(row=row, column=column)


class HorizontalFrame:
    def __init__(self, master, text, content, row):
        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=16, weight="bold")

        horizontal_frame = tk.Frame(master, background='#181818')

        frame1 = tk.Frame(horizontal_frame)
        frame2 = tk.Frame(horizontal_frame)

        frame1.grid(row=0, column=0, sticky='w')
        frame2.grid(row=1, column=0)

        label = tk.Label(frame1,
                         text=text,
                         background='black',
                         foreground='white',
                         font=play,
                         anchor=tk.W,
                         justify=tk.RIGHT,
                         pady=10,
                         padx=10
                         )
        label.grid(row=0)
        column = 0
        for i in content:
            button = MyButton(frame2,
                              image=i['image'],
                              text=i['text'])
            button.grid(row=0, column=column)
            column += 1

        horizontal_frame.grid(row=row,
                              column=0,
                              sticky='ew',
                              pady=(0, 10))
        horizontal_frame.grid_rowconfigure(0, weight=1)
        horizontal_frame.grid_rowconfigure(1, weight=1)

