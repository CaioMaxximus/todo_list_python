import tkinter as tk
from tkinter import ttk

# Lista de tasks
tasks = [
    {"title": "Tarefa 1", "content": "Conteúdo da Tarefa 1", "classe": "Classe A"},
    {"title": "Tarefa 2", "content": "Conteúdo da Tarefa 2", "classe": "Classe B"},
    # Adicione mais tasks conforme necessário
]

def exibir_tasks(classe_selecionada=None):
    # Limpa o Canvas antes de exibir as tasks
    for widget in tasks_canvas.winfo_children():
        widget.destroy()

    # Filtra as tasks com base na classe selecionada
    if classe_selecionada:
        tasks_filtradas = [task for task in tasks if task["classe"] == classe_selecionada]
    else:
        tasks_filtradas = tasks

    for i, task in enumerate(tasks_filtradas):
        frame = ttk.Frame(tasks_canvas)
        frame.grid(row=i, column=i, padx=5, pady=5, sticky="w")

        title_label = ttk.Label(frame, text=task["title"])
        title_label.grid(row=0, column=0, padx=5, pady=2)

        content_label = ttk.Label(frame, text=task["content"])
        content_label.grid(row=1, column=0, padx=5, pady=2)

    # Atualiza o Canvas após adicionar as tasks
    tasks_canvas.update_idletasks()
    tasks_canvas.config(scrollregion=tasks_canvas.bbox("all"))

def criar_task():
    title = title_entry.get()
    content = content_entry.get()
    classe = classe_var.get()

    tasks.append({"title": title, "content": content, "classe": classe})
    exibir_tasks()

root = tk.Tk()
root.title("Tasks App")
root.geometry("800x400")

# Canvas para rolagem
tasks_canvas = tk.Canvas(root)
tasks_canvas.grid(row=2, column=0, sticky="nsew")

# Barra de rolagem vertical
# scrollbar = ttk.Scrollbar(root, orient="vertical", command=tasks_canvas.yview)
# scrollbar.grid(row=0, column=1, sticky="ns")
# tasks_canvas.configure(yscrollcommand=scrollbar.set)

# Frame para conter as tasks
tasks_frame = ttk.Frame(tasks_canvas)
tasks_canvas.create_window((0, 0), window=tasks_frame, anchor="nw")

# Menu suspenso para escolher classes de tasks
classes = ["Todas as Classes", "Classe A", "Classe B", "Classe C"]
classe_var = tk.StringVar()
classe_var.set("Todas as Classes")
classes_dropdown = ttk.Combobox(root, textvariable=classe_var, values=classes)
classes_dropdown.grid(row=0, column=0, padx=10, pady=10)
classes_dropdown.bind("<<ComboboxSelected>>", lambda event: exibir_tasks(classe_var.get()))

# # Entradas para criar uma nova task
# title_label = ttk.Label(root, text="Título:")
# title_label.grid(row=1, column=0, padx=10, pady=5)
# title_entry = ttk.Entry(root)
# title_entry.grid(row=1, column=1, padx=10, pady=5)

# content_label = ttk.Label(root, text="Conteúdo:")
# content_label.grid(row=2, column=0, padx=10, pady=5)
# content_entry = ttk.Entry(root)
# content_entry.grid(row=2, column=1, padx=10, pady=5)

# create_button = ttk.Button(root, text="Criar Task", command=criar_task)
# create_button.grid(row=3, column=0, columnspan=2, pady=10)

# Chame a função para exibir as tasks
exibir_tasks()

root.mainloop()
