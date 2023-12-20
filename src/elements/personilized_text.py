import tkinter as tk


class personilized_text(tk.Text):
    
    def __init__(self, master=None, placeholder="", color='grey', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.insert('1.0', self.placeholder)
        self.on_focus_out(None)
        self.empty = True

    def on_focus_in(self, event):
        # print("----")
        # print(self.get("1.0" , "end").replace("\n" , ""))
        # print("-------")
        print(self.placeholder)
        if self.get("1.0" , "end").replace("\n" , "") == self.placeholder:
            print("self in")
            self.delete(1.0, tk.END)
            self.config(fg=self.default_fg_color)
            self.empty = False

    def on_focus_out(self, event):
        # print(self.get("1.0" , "end"))
        # print("-------")
        if self.get("1.0" , "end").replace("\n" , "") == "":
            self.insert("1.0", self.placeholder)
            self.config(fg=self.placeholder_color)
            self.empty = True
            
    def get(self ,  *args, **kwargs):
        if(self.empty):
            return ""
        else:
            return super().get( *args, **kwargs)