import tkinter as tk
from tkinter import scrolledtext


class TaskWindow(tk.Frame):

    def __init__(self,*args,**kwargs):
        super().__init__(*args , **kwargs)



    def setup(self, task,theme , row_counter, columnN , paddX,
              parent,complete_task ,remove_task):
        
        self.task = task
        self.theme = theme
        expireDate = task.expire_date
        expireDateText = ("EXPIRED" if task.expired else "EXPIRE") + f" IN: {expireDate}"
        expireDateColor = "#FF2B52" if task.expired else "#00D9C0"
        completeIconName = "check" if task.completed else "cross"

        self.completeIcon = tk.PhotoImage(file=self.theme.get_icon(completeIconName))
        completeColor = self.theme.get_color("correct") if task.completed else self.theme.get_color("error")

        self.config(bg =task.color ) 

        self.frame_top = tk.Frame(self, bg="black",highlightbackground= "black", 
                   highlightthickness=4,pady=2)

        self.date_label = tk.Label(self.frame_top, text=expireDateText, bg=expireDateColor)

        self.complete_btn = tk.Button(self.frame_top, image=self.completeIcon, border=2, bg=completeColor, height=25,
                                      command=complete_task(task))
        self.complete_btn.completeIcon = self.completeIcon

        self.title_label = tk.Label(self, text=task.title, wraplength=170, height=3, bg=task.color,highlightthickness = 0,
                                    font=(self.theme.get_font("content"), self.theme.get_font_size("presentation")))

        self.removeImg = tk.PhotoImage(file=self.theme.get_icon("delete")).subsample(1, 1)
        self.remove_btn = tk.Button(self.frame_top, height=25, bg=self.theme.get_color("element_1"),
                                    command= remove_task(task),
                                    image=self.removeImg)
        # self.remove_btn.removeImg = self.removeImg

        canvas_size = parent.winfo_width()
        font_size = self.theme.get_font_size("small-title")
        wid = int(canvas_size / (font_size * 2.1))

        self.content_task = scrolledtext.ScrolledText(self,
                                                      width=wid, height=12, wrap=tk.WORD,bd = 0,
                                                      bg=self.task.color,highlightthickness = 0,
                                                      fg="black",padx = 10)
        # self.content_task.tag_configure("indent", lmargin1=10, lmargin2=10)
        self.content_task.configure(font=(self.theme.get_font("content"), font_size))
        self.content_task.insert(tk.INSERT, task.content)
        self.content_task.configure(state="disabled")

        # Defining elements in the grid

        self.grid(row=row_counter, column=columnN, padx=paddX, pady=5)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=10)

        self.frame_top.grid(stick="ew")
        self.frame_top.grid_columnconfigure(0, weight=1)
        self.frame_top.grid_columnconfigure(1, weight=3)
        self.frame_top.grid_columnconfigure(2, weight=1)
        self.frame_top.grid_rowconfigure(0, weight=1)


        self.date_label.grid(row=0, column=1, padx=(1, 4))
        self.complete_btn.grid(row=0, column=0)
        self.title_label.grid(row=1, column=0, padx=(1, 10), pady=2)
        self.remove_btn.grid(row=0, column=2)
        self.content_task.grid(row=2, column=0)

    def change_complete_state(self):
        
        print("to mudando o estado!")
        self.task.completed = not self.task.completed
        completeColor = self.theme.get_color("correct") if self.task.completed else self.theme.get_color("error")
        completeIconName = "check" if self.task.completed else "cross"

        self.frame_top.config(bg=completeColor)
        self.complete_btn.config(bg=completeColor)
        # self.title_label.config(bg=completeColor)
        # self.config(bg =completeColor )
        self.completeIcon.config(file=self.theme.get_icon(completeIconName))

    def set_grid(self, row, colum):
        self.grid(row=row, column=colum,padx=self.grid_info()["padx"][::-1] ,pady=5)
        self.update_idletasks()

