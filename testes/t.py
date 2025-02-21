import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tkkbs

# Função para exibir uma mensagem quando o botão for clicado
def on_button_click():
    label.config(text="Olá, mundo!")

# Configuração da janela principal
root = tk.Tk()
root.title("Exemplo com Tkinter e TTKBootstrap")
root.geometry("300x200")

# Configuração do estilo TTKBootstrap
style = tkkbs.Style(theme="flatly")

# Aplicação do estilo ao tema
style.theme_use()

# Criação de um frame
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Criação de um botão
button = tk.Button(frame, text="Clique em mim!", command=on_button_click)
button.pack(pady=20)

# Criação de um label
label = ttk.Label(frame, text="")
label.pack()

# Iniciar o loop principal da aplicação
root.mainloop()