import tkinter as tk
from tkcalendar import Calendar
import asyncio
from tkinter import messagebox
from elements.personalized_text import PersonalizedText
from elements.personalized_entry import PersonalizedEntry
from .Themes import Themes
from datetime import date

Theme = Themes("")


class ScrollableButtonFrame(tk.Frame):
    def __init__(self, parent, items, command=None, height = 5 , width = 5, func = lambda : print("Not implemented")):


        super().__init__(parent, bg="blue" )
        self.grid(row=0, column=0,sticky= "nsew", pady= 5,padx=width * 0.03)

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Criando o Canvas para a rolagem horizontal
        self.canvas = tk.Canvas(self, bg="white", highlightthickness=0 , height = int(height * 0.05) , width=int(width * 0.3))
        self.canvas.grid(row = 0 ,column= 0 ,sticky= "ew")
        # self.canvas.rowconfigure(0, weight=1)
        # self.canvas.columnconfigure(0, weight=1)


        self.scrollbar = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scrollbar.grid(row = 1, column= 0 ,sticky="ew" )

        self.button_frame = tk.Frame(self.canvas, bg="white")
        self.button_frame.grid(row = 0, column= 0 ,sticky="nsew" )


        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.button_frame, anchor="nw")


        self.buttons = []
        for item in items:
            btn = tk.Button(self.button_frame, text=item, bg=item ,  width= int(width * 0.01) ,
                            command= lambda  item = item : func(item))
            btn.pack(side="left", padx=5, pady=5)
            self.buttons.append(btn)

        self.button_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


class Post_it_Preview(tk.Frame):
    def __init__(self, parent,width , height):
        tk.Frame.__init__(self, parent, borderwidth=2, relief="solid", 
                          bg=Theme.get_color("big_background"),width=width, height=height)
        self.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)



        self.title = tk.Text(self, font=(Theme.get_font("painel"), Theme.get_font_size("median-title")),
                    bg=Theme.get_color("element_1"), wrap="word", height=int(height * 0.9), width=width)
        self.title.grid(row=0, column=0,sticky="nsew")

        self.text = tk.Text(self,wrap="word",
                                       font=(Theme.get_font("painel"), Theme.get_font_size("median-title")),
                                       bg=Theme.get_color("element_1"),height=int(height * 0.9), width=width)
        self.text.grid(row=1, column=0,sticky="nsew") 

    def set_title(self, title):
        self.title.delete("1.0", "end")  
        self.title.insert("1.0", title)

    def set_text(self, text):
        self.text.delete("1.0", "end")  
        self.text.insert("1.0", text)
    def clear_all(self):
        self.title.delete("1.0", "end")  
        self.text.delete("1.0", "end")  
    
    def set_color(self, color):
        self.title.config(bg=color)
        self.text.config(bg=color)




class Creator(tk.Frame):
    def __init__(self, parent, controler):
        tk.Frame.__init__(self, parent, borderwidth=2, relief="solid", bg=Theme.get_color("big_background"))


        self.task_color = "white"
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_rowconfigure(2, weight=4)
        self.grid_columnconfigure(0, weight=1)
        
        self.controler = controler
        self.grid_remove()
        
        ## Layout Frames
        self.frameTopBar = tk.Frame(self, borderwidth=2, relief="solid", bg=Theme.get_color("big_background"))
        self.frameTopBar.grid(row=0, column=0, sticky="ew", pady=5, padx=5)
        self.frameTopBar.grid_columnconfigure(0, weight=1)
        self.frameTopBar.grid_columnconfigure(1, weight=8)
        self.frameTopBar.grid_columnconfigure(2, weight=1)

        ## Top Bar Elements
        self.closeIcon = tk.PhotoImage(file=Theme.get_icon("back_arrow"))
        self.closeBtn = tk.Button(self.frameTopBar, image=self.closeIcon, command=self.controler.unstack,
                                  bg=Theme.get_color("element_1"), borderwidth=0)
        self.closeBtn.grid(row=0, column=0, padx=10)

        self.titleIn = PersonalizedEntry(self.frameTopBar, bg="gray",
                                         placeholder="Insert a title for the task",
                                         font=(Theme.get_font("painel"), Theme.get_font_size("big-title")))
        self.titleIn.grid(row=0, column=1, sticky="we")

        ## Main Content Area
        self.main_frame = tk.Frame(self, bg=Theme.get_color("big_background"))
        self.main_frame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)
        self.main_frame.grid_columnconfigure(0, weight=3)  
        self.main_frame.grid_columnconfigure(1, weight=7)  
        self.main_frame.grid_rowconfigure(0, weight=1)

        ## Sidebar
        self.sidebar = tk.Frame(self.main_frame, bg=Theme.get_color("big_background"))
        self.sidebar.grid(row=0, column=0, sticky="nsew", pady=10)

        self.sidebar.grid_rowconfigure(0, weight=1)
        self.sidebar.grid_rowconfigure(1, weight=4)
        self.sidebar.grid_rowconfigure(2, weight=1)
        self.sidebar.grid_rowconfigure(3, weight=4)


        post_it_colors = [
            "#FFD966",  # Amarelo pastel
            "#FFEB99",  # Amarelo claro
            "#F4A261",  # Laranja suave
            "#FDCBBA",  # Pêssego claro
            "#AECBFA",  # Azul pastel
            "#B5EAD7",  # Azul turquesa claro
            "#D5A6BD",  # Rosa claro
            "#E6C9A8"   # Bege suave
        ]


        self.colors = ScrollableButtonFrame( self.sidebar,post_it_colors,
                                            height= controler.height, width = controler.width, func= self.change_color)

        font_s_content = Theme.get_font_size("small-title")
        self.contentIn = PersonalizedText(self.sidebar, placeholder="Insert the task content...",
                                          font=(Theme.get_font("painel"), font_s_content),
                                          height=13, width=32, bg="gray")  
        self.contentIn.grid(row=1, column=0, pady=0)


        self.calendar_label = tk.Label(self.sidebar, text="Expire Date:",
                                       font=(Theme.get_font("painel"), Theme.get_font_size("median-title")),
                                       bg=Theme.get_color("element_1"))
        self.calendar_label.grid(row=2, column=0, pady=(1, 8))

        self.calendarIn = Calendar(self.sidebar, font="Arial 12", date_pattern='mm-dd-yyyy',
                                   mindate=date.today(), showothermonthdays=False,
                                   background=Theme.get_color("big_background_lighter"))
        self.calendarIn.grid(row=3, column=0, padx=1, pady=1)

        self.main_frame.update_idletasks()
        preview_w = int(self.main_frame.winfo_width() * 0.9) 
        preview_h = int(self.main_frame.winfo_height() * 0.9) 


        ## Preview
        self.preview = Post_it_Preview(self.main_frame, preview_w, preview_h)
        self.preview.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        ## Bind para atualizar o preview dinamicamente
        self.titleIn.bind("<KeyRelease>", self.update_preview)
        self.contentIn.bind("<KeyRelease>", self.update_preview)

        ## Bottom Bar
        self.bottom_frame = tk.Frame(self, bg=Theme.get_color("big_background"))
        self.bottom_frame.grid(row=2, column=0, pady=10)

        self.createTakBtn = tk.Button(self.bottom_frame, text="Create Task",
                                      command=lambda: asyncio.create_task(self.create_task()),
                                      font=(Theme.get_font("painel"), Theme.get_font_size("small-title")),
                                      height=3, bg=Theme.get_color("element_1"), width=20)
        self.createTakBtn.grid(row=0, column=0, pady=10)

    def update_preview(self, event=None):
        title = self.titleIn.get()
        content = self.contentIn.get("1.0", "end-1c")
        self.preview.set_title(title)
        self.preview.set_text(content)

    def change_color(self,color):
        self.task_color = color
        self.preview.set_color(color)

    async def create_task(self):
        title = self.titleIn.get()
        expireD = self.calendarIn.get_date()
        content = self.contentIn.get("1.0", "end-1c")
        
        await self.controler.createTask(self.controler.unstack, title, content, expireD , self.task_color)
        self.titleIn.delete(0 , tk.END)
        self.contentIn.delete(1.0, tk.END)
        self.preview.clear_all()

