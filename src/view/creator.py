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
    def __init__(self,parent, controler):
        
        tk.Frame.__init__(self , parent,borderwidth=2, relief="solid", bg=Theme.get_color("big_background"))
        # self.pack(side = "top", fill = "both" , expand= True)
        self.grid(row=0,column=0, sticky ="nsew")
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=8)
        self.grid_rowconfigure(2,weight=8)
        self.grid_rowconfigure(3,weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.controler = controler
        # self.contentIn = PersonilizedEntry(self,placeholder = "Insert the task content...", height=8,width=35)
        # self.grid_columnconfigure(1,weight=1)
        ##top bar
        self.frameTopBar = tk.Frame(self,borderwidth=2, relief="solid", bg = Theme.get_color("big_background"))
        self.frameTopBar.grid(row= 0,column=0,sticky ="nsew")
        self.frameTopBar.grid_columnconfigure(0,weight=1)
        self.frameTopBar.grid_columnconfigure(1,weight=8)
        self.frameTopBar.grid_columnconfigure(3,weight=1)
        # self.frameTopBar.grid_columnconfigure(2,weight=5) 
        ##Title creation
        self.closeIcon= tk.PhotoImage(file=Theme.get_icon("back_arrow"))
        self.closeBtn = tk.Button( self.frameTopBar,image = self.closeIcon,command= self.controler.unstack ,
                                  bg=Theme.get_color("element_1"),
                                  borderwidth=0)
        print("----")
        self.controler.update()
        self.update()
        self.frameTopBar.update()
        self.closeBtn.update()

        self.closeBtn.grid(row=0,column=0,pady=(self.frameTopBar.winfo_height() - self.closeBtn.winfo_height()) // 2)
        self.titleIn = PersonalizedEntry( self.frameTopBar,bg="gray",
                                         placeholder = "Insert a title for the task",
                                         font=('Arial 16'))
        # self.titleIn.update()
        self.titleIn.grid(row = 0, column=1,sticky="we")
        ##Calendar
        
        self.calendar_area = tk.Frame(self,bg = Theme.get_color("big_background"))
        self.calendar_area.grid(row=1,column=0)
        
        self.calendar_label = tk.Label(self.calendar_area, text= "Expire Date:" , 
                                        font=('GOOD TIMES', 14),
                                        bg = Theme.get_color("element_1"))
        self.calendar_label.grid(row=0 , column=0,pady=(1,8))
        self.calendarIn= Calendar(self.calendar_area,date_pattern = 'mm-dd-yyyy',
                                  mindate = date.today(),showothermonthdays = False,
                                  background = Theme.get_color("big_background_lighter"))
        self.calendarIn.grid(row = 1)
         ##Content area
         
        self.contentIn = PersonalizedText(self,placeholder = "Insert the task content...",  font=('COPPERPLATE GOTHIC BOLD', 10) ,
                                          height=8,width=45,bg = "gray")
        self.contentIn.grid(row=2,column=0)
        
        ##Button to create
        self.createTakBtn = tk.Button( self,text="Create Task", command= lambda : asyncio.create_task(self.create_task()),
                                        font=('COPPERPLATE GOTHIC BOLD', 9),
                                      height = 3 , bg = Theme.get_color("element_1"))
        self.createTakBtn.grid(row=3,column=0)
        
    async def create_task(self):
        title = self.titleIn.get()
        expireD = self.calendarIn.get_date()
        content = self.contentIn.get("1.0", "end-1c")
        print(title,expireD,content)
        try:
            await self.controler.createTask(title,content,expireD)
            self.controler.unstack()
        except ValueError as err:
            print(err)
            messagebox.showerror("Erro", str(err))
