from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar
from services import task_services
from tkinter import messagebox
from .Themes import Themes
from screeninfo import get_monitors

import asyncio
from .home import Home
Theme = Themes("")

class to_do_app(tk.Tk):
    def __init__(self, tasks, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        screen_siz_w = 0
        screen_siz_h = 0
        for e in get_monitors():
            if e.is_primary:
                screen_siz_w = e.width
                screen_siz_h = e.height
        width = int(screen_siz_w / 3)
        height = int(screen_siz_h * 0.7)
        width = 1000
        height = 1000
        print("root criado")
        self.geometry(f'{width}x{height}')
        #self.minsize(width - 10, height - 10)
        #self.maxsize(width + 10, height + 10)
        self.resizable(False,False)
        # self.loop = asyncio.get_event_loop()
        self.destroyed = False
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.container = tk.Canvas(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.stack = []
        # self.pages = []
        self.tasks = tasks

        frame = Home(self.container, self, tasks)
        frame.grid(row=0, column=0, sticky="nsew")
        self.stack.append(frame)
        print(self.stack[-1])
        frame.tkraise()
        self.observers = []
        self.observers.append(frame)
        # asyncio.create_task(self.updater(1/120))

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.setDestroyed()

    def setDestroyed(self):
        print("chamou o destroy!!")
        self.destroyed = True

    def unstack(self):
        if (len(self.stack) > 1):
            self.stack.pop()
        self.stack[-1].tkraise()

    def stack_page(self, page):
        self.stack.append(page(self.container, self))
        print(self.stack[-1])
        self.stack[-1].tkraise()

    async def createTask(self, callback, title, content, expireD):
        print(self.tasks)
        # self.tasks = await task_services.add_new_task(title,content,expireD)
        self.tasks = await self.requests_pool(self.tasks, task_services.add_new_task, callback, title, content, expireD)
        self.notify()

    def notify(self):
        for e in self.observers:
            e.notify()

    def get_tasks(self):
        return self.tasks

    async def updater(self, interval):
        while not self.destroyed:
            self.update()
            await asyncio.sleep(interval)
            # print("updater chamou")
        print("updater shutdown")

    async def remove_task_confirmed(self, new_window, callback, task_id):
        # print(task_id)
        # print(self.tasks[task_id])
        print("removi tudo!")
        # self.tasks = await task_services.remove_task_by_id(task_id)
        self.tasks = await self.requests_pool(self.tasks, task_services.remove_task_by_id, None, task_id)
        # self.deiconify()
        callback()
        new_window.destroy()

    def remove_task(self, task, callback):

        new_window = tk.Toplevel(self)
        new_window.title("REMOVE TASK")

        def close_window(event):
            self.deiconify()

        frame = tk.Frame(new_window, bg=Theme.get_color("big_background_lighter"))
        frame.pack(side="top", fill="both", expand=True)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=3)
        frame.columnconfigure(0, weight=1)

        top_frame = tk.Frame(frame)
        top_frame.grid(row=0, column=0, padx=5, pady=10)
        message = tk.Label(top_frame, text=f"remove '{task}' permanently?")
        message.grid(row=0, column=0, padx=10, pady=5)

        bottow_frame = tk.Frame(frame, bg=Theme.get_color("big_background_lighter"))
        bottow_frame.grid(row=1, column=0)
        bottow_frame.grid_columnconfigure(0, weight=1)
        bottow_frame.grid_columnconfigure(1, weight=1)

        cancel_btn = tk.Button(bottow_frame, bg=Theme.get_color("correct"), text="CANCEL", command=new_window.destroy)
        cancel_btn.grid(row=0, column=0, padx=(1, 10))
        remove_btn = tk.Button(bottow_frame, text="REMOVE", bg=Theme.get_color("error"),
                               command=lambda: asyncio.create_task(
                                   self.remove_task_confirmed(new_window, callback, task)))
        remove_btn.grid(row=0, column=1, padx=(10, 1))
        new_window.bind("<Destroy>", lambda event: close_window(event))
        new_window.geometry('250x150')
        new_window.minsize(245, 140)
        new_window.maxsize(265, 160)
        self.withdraw()
        # self.wait_window(new_window)

    async def set_task_complete(self, id):
        print("id ->" + id)
        await self.requests_pool(None, task_services.set_task_complete, None, id)
        await self.get_all_tasks()

    async def get_all_tasks(self):
        self.tasks = await self.requests_pool(self.tasks, task_services.get_all_tasks, None)
        self.notify()

    async def requests_pool(self, default_output, func, callback, *args):
        print(func)
        print(args)
        try:

            res = await func(*args)
            if callback:
                callback()
            return res
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            return default_output


async def init(tasks, args):
    root = to_do_app(tasks)
    if len(args) > 1 and args[1] == "minimize":
        root.state(newstate='iconic')

    await root.updater(1 / 120)
