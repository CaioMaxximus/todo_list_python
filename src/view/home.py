from tkinter import ttk
import tkinter as tk
import asyncio
from .creator import Creator
from tkinter import scrolledtext
from .Themes import Themes

# from icons import arrow-turn-down-left.svg
Theme = Themes("")


class Home(tk.Frame):
    def __init__(self, parent, controler, tasks):
        tk.Frame.__init__(self, parent, borderwidth=2, relief="solid", bg=Theme.get_color("big_background_darker"))
        # self.pack(side = "top", fill = "both" , expand= True)

        self.tasks = tasks
        self.parent = parent
        self.controler = controler

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

        # Top  bar
        self.frameTopBar = tk.Frame(self, borderwidth=0, relief="solid",
                                    background=Theme.get_color("big_background_darker"))
        self.frameTopBar.grid(row=0, column=0, sticky="ew")

        self.frameTopBar.grid_columnconfigure(0, weight=1)
        self.frameTopBar.grid_columnconfigure(1, weight=2)
        self.frameTopBar.grid_columnconfigure(2, weight=2)

        self.variable = tk.StringVar(self.frameTopBar)
        self.variable.set("NOT COMPLETED")
        opM = tk.OptionMenu(self.frameTopBar,
                            self.variable, "ALL", "COMPLETED", "NOT COMPLETED",
                            )
        opM.config(width=20)
        # opM.pack()
        opM.grid(row=0, column=0)
        ##delayin button creation on the top bar
        ##Creation Button

        filterImg = tk.PhotoImage(file=Theme.get_icon("filter"))

        buttonFilter = tk.Button(self.frameTopBar, text="Filter", bg=Theme.get_color("element_1"),
                                 command=lambda: asyncio.create_task(self.controler.get_all_tasks()), image=filterImg)
        buttonFilter.filterImg = filterImg
        buttonFilter.grid(row=0, column=1)
        # button.pack()

        ##create new task
        addImg = tk.PhotoImage(file=Theme.get_icon("add-circle"))
        buttonCreateT = tk.Button(self.frameTopBar, text="+",
                                  command=lambda: controler.stack_page(Creator)
                                  , width=35, height=35, bg=Theme.get_color("element_1"), image=addImg)
        buttonCreateT.image = addImg
        buttonCreateT.grid(row=0, column=2)

        self.downFrame = tk.Frame(self, bg=Theme.get_color("big_background_darker"),
                                  borderwidth=0)
        self.downFrame.grid(row=1, column=0, sticky="nsew")
        self.downFrame.grid_rowconfigure(0, weight=1)
        self.downFrame.grid_columnconfigure(0, weight=14)
        self.downFrame.grid_columnconfigure(1, weight=2)

        self.canvas = tk.Canvas(self.downFrame, bg=Theme.get_color("big_background_darker"))
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.rowconfigure(0, weight=1)
        self.canvas.columnconfigure(0, weight=1)

        self.scroll_bar = tk.Scrollbar(self.downFrame,
                                       orient="vertical",
                                       command=self.canvas.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=self.scroll_bar.set)

        # Frames list
        self.frameTasks = tk.Frame(self.canvas, borderwidth=2,
                                    bg=Theme.get_color("big_background_darker"))
        # self.frameTasks.grid(row = 0 ,column=0,sticky= 'ew')
        self.frameTasks.grid_columnconfigure(0, weight=10)
        self.frameTasks.grid_columnconfigure(1, weight=10)
        #self.frameTasks.propagate(False)
        #self.frameTasks.bind("<B1-Motion>", lambda event, frame=self.frameTasks: self.resize_frame(event, frame))
        self.canvas.create_window((0, 0), window=self.frameTasks, anchor='n')

        self.filter_tasks_by_complete()

    def resize_frame(self, event, frame):
        width = event.x
        height = event.y
        frame.config(width=width, height=height)
        print(width, height)
        self.filter_tasks_by_complete()
        print("Resize canvas")
        self.on_canvas_resize(None)  # Atualiza o tamanho do Canvas

    def list_tasks(self, tasks):

        ## GET TASKS AS LISTS , ALWAYS

        for widget in self.frameTasks.winfo_children():
            # print(type(widget))
            widget.destroy()
        row_counter = 0
        # print("_________")
        # print(tasks)
        for i, task in enumerate(tasks):
            #print(task)
            # print(task)
            columnN = (i % 2)
            paddX = (1, 8) if columnN == 0 else (8, 1)
            expireDate = task.get_expire_date()
            expireDateText = ("EXPIRED" if task.expired else "EXPIRE") + f" IN: {expireDate}"
            expireDateColor = "#FF2B52" if task.expired else "#00D9C0"

            completeIconName = "check" if task.get_completed() else "cross"
            completeIcon = tk.PhotoImage(file=Theme.get_icon(completeIconName))

            completeColor = Theme.get_color("correct") if task.get_completed() else Theme.get_color("error")
            frame_task = tk.Frame(self.frameTasks, borderwidth=2, relief="solid"
                                  , bg=completeColor)
            frame_task.grid(row=(row_counter // 2), column=columnN, padx=paddX, pady=5)
            frame_task.rowconfigure(0, weight=1)
            frame_task.rowconfigure(1, weight=1)
            frame_task.rowconfigure(2, weight=10)

            frame_top = tk.Frame(frame_task, bg=completeColor)
            frame_top.grid(stick="ew")
            frame_top.grid_columnconfigure(0, weight=1)
            frame_top.grid_columnconfigure(1, weight=3)
            frame_top.grid_columnconfigure(2, weight=1)
            frame_top.grid_rowconfigure(0, weight=1)

            date_label = tk.Label(frame_top, text=expireDateText, bg=expireDateColor)
            date_label.grid(row=0, column=1, padx=(1, 4))

            complete_btn = tk.Button(frame_top, image=completeIcon, border=2
                                     , bg=completeColor, height=25, command=lambda t=task: asyncio.create_task(
                    self.controler.set_task_complete(t.get_id())))
            complete_btn.grid(row=0, column=0)
            complete_btn.completeIcon = completeIcon

            title_label = tk.Label(frame_task, text=task.title, wraplength=170,
                                   height=3, bg=completeColor,
                                   font=(Theme.get_font("content"), Theme.get_font_size("presentation")))
            title_label.grid(row=1, column=0, padx=(1, 10), pady=2)

            removeImg = tk.PhotoImage(file=Theme.get_icon("delete")).subsample(1, 1)

            remove_btn = tk.Button(frame_top, height=25, bg=Theme.get_color("element_1"),
                                   command=lambda t=task: (self.controler.remove_task(t.id, self.notify)),
                                   image=removeImg)
            remove_btn.removeImg = removeImg
            remove_btn.grid(row=0, column=2)

            self.frameTasks.update()
            canvas_size = self.parent.winfo_width()
            font_size = (Theme.get_font_size("small-title"))
            wid = int(canvas_size / (font_size * 2))
            print(f"canvas_size {canvas_size}")
            print(font_size)
            print(wid)

            content_task = scrolledtext.ScrolledText(frame_task, state="normal",
                                                     width=wid, height=22, wrap=tk.WORD,
                                                     bg=Theme.get_color("big_background_lighter"),
                                                     fg=(Theme.get_color("font_1")),
                                                     )
            content_task.configure(font=(Theme.get_font("content"), font_size))

            content_task.grid(row=2, column=0)
            content_task.insert(tk.INSERT, task.content)
            content_task.configure(state="disabled")

            row_counter += 1

        self.frameTasks.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def filter_tasks_by_complete(self):

        method = self.variable.get()
        # print("filter_tasks")
        # print(self.tasks)
        if (method == "ALL"):
            print("ALL")
            print(self.tasks.values())
            self.list_tasks(self.tasks.values())

        else:
            exit = []
            # print(method)
            completed = int(method == "COMPLETED")
            print(completed)
            for task in (self.tasks.values()):
                if task.completed == completed:
                    # print(task.completed)
                    exit.append(task)
            # print(exit)        
            self.list_tasks(exit)

    def notify(self):
        self.tasks = self.controler.get_tasks()
        print("######")
        print("chamou o notify")
        print(self.tasks)
        # self.list_tasks(self.tasks.values())
        self.filter_tasks_by_complete()
