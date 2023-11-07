import tkinter as tk
from tkinter import ttk


tasks = [
    {"title": "Tarefa 1", "content": "Conteúdo da Tarefa 1", "class_": "Classe A"},
    {"title": "Tarefa 2", "content": "Conteúdo da Tarefa 2", "class_": "Classe B"},
    # Adicione mais tasks conforme necessário
]

def getAllTask():
    return tasks

def list_filtered_tasks(canvas , task_class = "Class A"):
    
    
    for widget in canvas.winfo_children():
        widget.destroy()
    filtered = tasks
    if(task_class != "Todas Classes"):
        filtered = [task for task in tasks if task["class_"] == task_class]
    row_counter = 0
    print("list_filtered")
    for i , task in enumerate(filtered):
        frame = ttk.Frame(canvas)
        frame.grid(row = (row_counter // 2) , column = (i % 2))
        title_label = ttk.Label(frame, text=task["title"])
        title_label.grid(row=0, column=0, padx=5, pady=2)
        content_label = ttk.Label(frame, text=task["content"])
        content_label.grid(row=1, column=0, padx=5, pady=2)
    
    print(filtered)
    canvas.update_idletasks()
    # canvas.config(scrollregion=canvas.bbox("all"))
            


def create_home_view(root ):
    classe_var = tk.StringVar()
    classe_var.set("Todas as Classes")
    classes = ["Todas Classes" ,"Classe A", "Classe B", "Classe C"]
    canvas = tk.Canvas(root)
    canvas.grid(row=3)
    selector  = ttk.Combobox(root, textvariable=classe_var, values=classes)
    selector.grid(row= 0 , column= 0 )
    selector.bind("<<ComboboxSelected>>", lambda event: list_filtered_tasks(canvas , classe_var.get()))
    list_filtered_tasks(canvas, task_class= "Todas Classes")



root = tk.Tk()
root.title(" ToDo Manager")
root.geometry("500x500")
create_home_view(root)
root.mainloop()

