import tkinter as tk
from tkinter import ttk


class ScrollableFrame(tk.Frame):
    name = 1

    def __init__(self, container, *args, **kwargs):
        tk.Frame.__init__(self, container, *args, **kwargs)

        self.canvas = tk.Canvas(self,
                                borderwidth=0,
                                highlightthickness=0,
                                bg='#181818')
        # -----------------------------------------------------------------------------
        name_of_style = 'My'+str(ScrollableFrame.name)+'.Vertical.Scrollbar'
        self.style = ttk.Style()

        self.style.element_create(name_of_style+".trough", "from", "default")
        self.style.element_create(name_of_style+".uparrow", "from", "default")
        self.style.element_create(name_of_style+".downarrow", "from", "default")
        self.style.element_create(name_of_style+".thumb", "from", "default")
        self.style.element_create(name_of_style+".grip", "from", "default")

        self.style.layout("My.Vertical.TScrollbar",
                          [(name_of_style+'.trough', {'children': [
                              (name_of_style+'.uparrow',
                               {'side': 'top', 'sticky': ''}),
                              (name_of_style+'.downarrow',
                               {'side': 'bottom', 'sticky': ''}),
                              (name_of_style+'.thumb',
                               {
                                   'unit': '1',
                                   'children': [(name_of_style+'.grip',
                                                 {'sticky': ''})],
                                   'sticky': 'nswe'
                               })], 'sticky': 'ns', })])

        self.style.configure("My.Vertical.TScrollbar", self.style.configure("Vertical.TScrollbar"))
        self.style.configure("My.Vertical.TScrollbar",
                             troughcolor="#181818",
                             arrowcolor='#181818',
                             background='#535353',
                             borderwidth=0,
                             relief=tk.FLAT)

        self.style.theme_settings("vista", {
            "My.Vertical.TScrollbar": {
                'map': {
                    'background': [('active', '#818181')]
                }
            }
        })

        self.scrollbar = ttk.Scrollbar(self,
                                       orient="vertical",
                                       command=self.canvas.yview,
                                       style='My.Vertical.TScrollbar'
                                       )
        ScrollableFrame.name += 1
        # ---------------------------------------------------------------------------
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox('all'),
            )
        )

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.size)

        self.canvas.grid(row=0, column=0, sticky=tk.N+tk.S+tk.W+tk.E)
        self.scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.canvas.bind("<Enter>", self._bind_mouse)
        self.canvas.bind("<Leave>", self._unbind_mouse)

        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

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
        width = event.width
        height = event.height
        self.canvas.create_window((0, 0),
                                  window=self.scrollable_frame,
                                  anchor="nw",
                                  width=width,
                                  )
