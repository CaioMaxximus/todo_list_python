import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()

# Configurando o widget ScrolledText
content_label = scrolledtext.ScrolledText(root, state="disabled", width=22, height=20, wrap="word")
content_label.grid(row=0, column=0)

# Configurando a espessura da barra de rolagem
frame_scrollbar = tk.Frame(root)
frame_scrollbar.grid(row=0, column=1, sticky='ns')
scrollbar = tk.Scrollbar(frame_scrollbar, orient='vertical', command=content_label.yview)
scrollbar.pack(side='right', fill='y')

# Configurando a espessura da borda da Frame
frame_scrollbar['highlightthickness'] = 2  # Ajuste o valor conforme necessário

# Conectar a barra de rolagem ao widget ScrolledText
content_label['yscrollcommand'] = scrollbar.set

# Exemplo de inserção de texto
content_label.config(state="normal")
content_label.insert('1.0', "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 10)
content_label.config(state="disabled")

root.mainloop()
