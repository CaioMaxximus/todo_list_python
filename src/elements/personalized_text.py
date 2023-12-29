import tkinter as tk


class PersonalizedText(tk.Text):

    # empty = True
    
    def __init__(self, master=None, placeholder="", color='grey', *args, **kwargs):
        self.empty = True
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.insert('1.0', self.placeholder)
        # self.on_focus_out(None)
        print("chamou init")
        


    def on_focus_in(self, event):
        self.empty = False
        print("focus in get -> " + self.get("1.0" , "end"))
        if self.get("1.0" , "end").replace("\n" , "") == self.placeholder:
            print("entrou no focus in")
            self.delete(1.0, tk.END)
            self.config(fg=self.default_fg_color)

    def on_focus_out(self, event):
        if self.get("1.0" , "end").replace("\n" , "") == "":
            self.insert("1.0", self.placeholder)
            self.config(bg = self.bg)
            self.config(fg=self.placeholder_color)
            self.empty = True


    def get(self, *args, **kwargs):
        if self.empty:
            print("get do filho")
            return ""
        else:
            print("get do pai")

            return super().get(*args, **kwargs)
