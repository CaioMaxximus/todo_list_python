import tkinter as tk
from tkcalendar import Calendar
import asyncio
from tkinter import messagebox
from elements.personalized_text import PersonalizedText
from elements.personalized_entry import PersonalizedEntry
from .Themes import Themes
from datetime import date

# from icons import arrow-turn-down-left.svg
Theme = Themes("")


class Creator(tk.Frame):
    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent, borderwidth=2, relief="solid", bg=Theme.get_color("big_background"))
        # self.pack(side = "top", fill = "both" , expand= True)
        canvas_size = parent.winfo_width()

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=8)
        self.grid_rowconfigure(3, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.controler = controler
        # self.contentIn = PersonilizedEntry(self,placeholder = "Insert the task content...", height=8,width=35)
        # self.grid_columnconfigure(1,weight=1)
        ##top bar
        self.frameTopBar = tk.Frame(self, borderwidth=2, relief="solid", bg=Theme.get_color("big_background"))
        self.frameTopBar.grid(row=0, column=0, sticky="nsew")
        self.frameTopBar.grid_columnconfigure(0, weight=1)
        self.frameTopBar.grid_columnconfigure(1, weight=8)
        self.frameTopBar.grid_columnconfigure(3, weight=1)
        # self.frameTopBar.grid_columnconfigure(2,weight=5) 
        ##Title creation
        self.closeIcon = tk.PhotoImage(file=Theme.get_icon("back_arrow"))
        self.closeBtn = tk.Button(self.frameTopBar, image=self.closeIcon, command=self.controler.unstack,
                                  bg=Theme.get_color("element_1"),
                                  borderwidth=0)
        print("----")
        self.controler.update()
        self.update()
        self.frameTopBar.update()
        self.closeBtn.update()

        self.closeBtn.grid(row=0, column=0, pady=(self.frameTopBar.winfo_height() - self.closeBtn.winfo_height()) // 2)
        self.titleIn = PersonalizedEntry(self.frameTopBar, bg="gray",
                                         placeholder="Insert a title for the task",
                                         font=(Theme.get_font("painel"), Theme.get_font_size("big-title")))
        # self.titleIn.update()
        self.titleIn.grid(row=0, column=1, sticky="we")
        ##Calendar

        self.calendar_area = tk.Frame(self, bg=Theme.get_color("big_background"))
        self.calendar_area.grid(row=1, column=0)

        self.calendar_label = tk.Label(self.calendar_area, text="Expire Date:",
                                       font=(Theme.get_font("painel"),
                                             Theme.get_font_size("median-title")),
                                       bg=Theme.get_color("element_1"))
        self.calendar_label.grid(row=0, column=0, pady=(1, 8))

        print("&&&&&&&&&&")
        font_size = int(canvas_size * 0.3 / 14)
        print(font_size)
        self.calendarIn = Calendar(self.calendar_area, font=f"Arial {font_size}" , date_pattern='mm-dd-yyyy',
                                   mindate=date.today(), showothermonthdays=False,
                                   background=Theme.get_color("big_background_lighter"))
        self.calendarIn.grid(row=1)
        # Content area

        font_s_content = Theme.get_font_size("small-title")
        width_content_size = int(canvas_size * 0.8 / font_s_content)
        self.contentIn = PersonalizedText(self, placeholder="Insert the task content...",
                                          font=(Theme.get_font("painel"), font_s_content),
                                          height=8, width=width_content_size, bg="gray")
        self.contentIn.grid(row=2, column=0)

        # Button to create
        font_s_btn = Theme.get_font_size("small-title")
        width_btn_size = int(canvas_size * 0.4 / font_s_btn)
        self.createTakBtn = tk.Button(self, text="Create Task", command=lambda: asyncio.create_task(self.create_task()),
                                      font=(Theme.get_font("painel"), font_s_btn),
                                      height=3, bg=Theme.get_color("element_1"),width= width_btn_size)
        self.createTakBtn.grid(row=3, column=0)

    async def create_task(self):
        title = self.titleIn.get()
        expireD = self.calendarIn.get_date()
        content = self.contentIn.get("1.0", "end-1c")
        # print(title,expireD,content)
        await self.controler.createTask(self.controler.unstack, title, content, expireD, )
        # self.controler.unstack()
        # try:
        #     await self.controler.createTask(title,content,expireD)
        #     self.controler.unstack()
        # except ValueError as err:
        #     print(err)
        #     messagebox.showerror("Erro", str(err))
