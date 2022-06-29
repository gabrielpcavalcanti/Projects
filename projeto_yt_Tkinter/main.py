from tkinter import *

root = Tk()

class Application:

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.widget_frame_01()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de clientes")
        self.root.configure(background="#1e3743")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=600)
    
    def frame_da_tela(self):
        self.frame_01 = Frame(self.root, bd=4, bg="#dfe3ee",
        highlightbackground="#759fe6", highlightthickness=3)
        self.frame_02 = Frame(self.root, bd=4, bg="#dfe3ee",
        highlightbackground="#759fe6", highlightthickness=3)

        self.frame_01.place(relx=0.02 , rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_02.place(relx=0.02 , rely=0.5, relwidth=0.96, relheight=0.46)

    def widget_frame_01(self):
        #Botões

        self.bt_limpar = Button(self.frame_01, text="Limpar")
        self.bt_buscar = Button(self.frame_01, text="buscar")
        self.bt_novo = Button(self.frame_01, text="Novo")
        self.bt_alterar = Button(self.frame_01, text="Alterar")
        self.bt_apagar = Button(self.frame_01, text="Apagar")

        self.bt_limpar.place(relx=0.2 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_buscar.place(relx=0.3 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_novo.place(relx=0.6 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar.place(relx=0.7 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar.place(relx=0.8 , rely=0.1, relwidth=0.1, relheight=0.15)

        #Labels

        self.lb_codigo = Label(self.frame_01, text="Código")
        self.lb_nome = Label(self.frame_01, text="Nome")
        self.lb_telefone = Label(self.frame_01, text="telefone")
        self.lb_cidade= Label(self.frame_01, text="cidade")

        self.lb_codigo.place(relx=0.05 , rely=0.05)
        self.lb_nome.place(relx=0.05 , rely=0.35)
        self.lb_telefone.place(relx=0.05 , rely=0.6)
        self.lb_cidade.place(relx=0.5 , rely=0.6)

        #Entrys

        self.codigo_entry = Entry(self.frame_01)
        self.nome_entry = Entry(self.frame_01)
        self.telefone_entry = Entry(self.frame_01)
        self.cidade_entry = Entry(self.frame_01)

        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)


    

Application()
