import tkinter as tk

def on_configure(event):
    # Atualiza a configuração do scrollregion quando o tamanho do Canvas muda
    canvas.configure(scrollregion=canvas.bbox("all"))

root = tk.Tk()

canvas = tk.Frame(root, bg = "red")
canvas.pack(side = "top", fill = "both" , expand= True)
canvas.grid_columnconfigure(0,weight=1)
canvas.grid_rowconfigure(0,weight=1)
# Adiciona uma barra de rolagem
# scrollbar = tk.Scrollbar(root, command=canvas.yview)
# scrollbar.pack(side="right", fill="y")
# canvas.configure(yscrollcommand=scrollbar.set)

# Cria um Frame com tamanho específico e adiciona a grade para ocupar todo o espaço
frame = tk.Frame(canvas, bg="black")
frame.grid(row = 0, column = 0, sticky ="nsew")

# Configuração da grade dentro do Frame para ocupar todo o espaço
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
# frame.propagate(False)

# Adiciona o Frame ao Canvas
# canvas.create_window((0, 0), window=frame, anchor="nw")

# # Adiciona widgets (ou outros Frames) dentro do Frame
label = tk.Label(frame, text="Conteúdo do Frame", font=("Arial", 14), bg="lightblue")
label.grid(row = 0, column = 0)
# label.pack(padx=20, pady=20)

# Atualiza a configuração do scrollregion quando o tamanho do Canvas muda
# canvas.bind("<Configure>", on_configure)
root.geometry('500x500')
root.mainloop()
