import tkinter as tk


class PersonalizedEntry(tk.Entry):
    
    def __init__(self, master=None, placeholder="", color='black', *args, **kwargs):
        self.empty = True
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.insert(0, self.placeholder)
        # self.on_focus_out(None)

    def on_focus_in(self, event):
        self.empty = False

        if self.get() == self.placeholder:
            print("self in")
            self.delete(0 , tk.END)
            self.config(fg=self.default_fg_color)

    def on_focus_out(self, event):
        
        if self.get() == "":
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)
            self.empty = False


    
    def get(self, *args, **kwargs):
        if self.empty:
            print("get do filho")
            return ""
        else:
            print("get do pai")

            return super().get(*args, **kwargs)