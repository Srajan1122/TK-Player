import tkinter as tk
from tkinter import ttk


class HorizontalScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        tk.Frame.__init__(self, container, *args, **kwargs)

        self.canvas = tk.Canvas(self,
                                borderwidth=0,
                                highlightthickness=0,
                                bg='#181818',
                                height=300
                                )

        # self.scrollbar = ttk.Scrollbar(self,
        #                                orient="horizontal",
        #                                command=self.canvas.xview,
        #                                )

        self.scrollable_frame = tk.Frame(self.canvas, bg='#181818')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox('all'),
            )
        )

        self.canvas.bind('<Configure>', self.size)

        self.canvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)
        # self.scrollbar.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        # self.canvas.configure(xscrollcommand=self.scrollbar.set)
        # self.canvas.bind("<Enter>", self._bind_mouse)
        # self.canvas.bind("<Leave>", self._unbind_mouse)

        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _bind_mouse(self, event=None):
        self.canvas.bind_all("<4>", self._on_mousewheel)
        self.canvas.bind_all("<5>", self._on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbind_mouse(self, event=None):
        self.canvas.unbind_all("<4>")
        self.canvas.unbind_all("<5>")
        self.canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        """Linux uses event.num; Windows / Mac uses event.delta"""
        func = self.canvas.xview_scroll if event.state & 1 else self.canvas.yview_scroll
        if event.num == 4 or event.delta > 0:
            func(-1, "units")
        elif event.num == 5 or event.delta < 0:
            func(1, "units")

    def size(self, event):
        self.canvas.create_window((0, 0),
                                  window=self.scrollable_frame,
                                  anchor="nw",
                                  )

    def left(self):
        func = self.canvas.xview_scroll(-10, 'units')

    def right(self):
        func = self.canvas.xview_scroll(10, 'units')
