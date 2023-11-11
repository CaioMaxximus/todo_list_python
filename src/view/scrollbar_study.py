import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")

        self.frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        width = event.width
        self.canvas.itemconfig("self.frame", width=width)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Exemplo com Coleção de Frames e Barra de Rolagem")

    scrollable_frame = ScrollableFrame(root)
    scrollable_frame.pack(fill="both", expand=True)

    for i in range(20):
        frame = tk.Frame(scrollable_frame.frame, width=200, height=50, bd=1, relief="solid")
        frame.pack(side="top", fill="both", expand=True)

    root.mainloop()
