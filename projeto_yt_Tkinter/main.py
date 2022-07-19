from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class funcs:

    def variaveis(self):

        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()


    def limpar_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    
    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
        print("Conectando ao banco de dados")
    
    def desconecta_bd(self):
        self.conn.close()
        print("desconectando ao banco de dados")

    def monta_tabela(self):
        self.conecta_bd()
        # Criando a tabela

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTERGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40) 
            );
        """)
        self.conn.commit()
        print("Banco de dados criado")
        self.desconecta_bd()

    def add_cliente(self):
        
        self.variaveis()

        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (cod, nome_cliente, telefone, cidade)
                    VALUES (?, ?, ?, ? ) """, (self.codigo, self.nome, self.telefone, self.cidade)) 
        
        self.conn.commit()
        self.desconecta_bd()
        self.select_list()
        self.limpar_tela()

    def select_list(self):

        self.listaCLI.delete(*self.listaCLI.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC; """)

        for i in lista:
            self.listaCLI.insert("", END, values=i)
        
        self.desconecta_bd()
    
    def on_double_click(self, event):

        self.limpar_tela()
        self.listaCLI.selection()

        for n in self.listaCLI.selection():

            col1, col2, col3, col4 = self.listaCLI.item(n, 'values')

            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    
    def deleta_cliente(self):

        self.variaveis()

        self.conecta_bd()

        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()

        self.desconecta_bd()

        self.limpar_tela()
        self.select_list()


class Application(funcs):

    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.widget_frame_01()
        self.lista_frame_02()
        self.monta_tabela()
        self.select_list()
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

        self.bt_limpar = Button(self.frame_01, text="Limpar", bd=2, bg="#107db2", fg="white", font=("verdana", 8, "bold"), command=self.limpar_tela)
        self.bt_buscar = Button(self.frame_01, text="buscar", bd=2, bg="#107db2", fg="white", font=("verdana", 8, "bold"))
        self.bt_novo = Button(self.frame_01, text="Novo", bd=2, bg="#107db2", fg="white", font=("verdana", 8, "bold"), command=self.add_cliente)
        self.bt_alterar = Button(self.frame_01, text="Alterar", bd=2, bg="#107db2", fg="white", font=("verdana", 8, "bold"))
        self.bt_apagar = Button(self.frame_01, text="Apagar", bd=2, bg="#107db2", fg="white", font=("verdana", 8, "bold"), command=self.deleta_cliente)

        self.bt_limpar.place(relx=0.2 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_buscar.place(relx=0.3 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_novo.place(relx=0.6 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar.place(relx=0.7 , rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar.place(relx=0.8 , rely=0.1, relwidth=0.1, relheight=0.15)

        #Labels

        self.lb_codigo = Label(self.frame_01, text="Código", bg="#dfe3ee", fg="#107db2")
        self.lb_nome = Label(self.frame_01, text="Nome", bg="#dfe3ee", fg="#107db2")
        self.lb_telefone = Label(self.frame_01, text="telefone", bg="#dfe3ee", fg="#107db2")
        self.lb_cidade= Label(self.frame_01, text="cidade", bg="#dfe3ee", fg="#107db2")

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

    def lista_frame_02(self):
        self.listaCLI = ttk.Treeview(self.frame_02, height=3, columns=("col1", "col2", "col3", "col4"))

        self.listaCLI.heading("#0", text=" ")
        self.listaCLI.heading("#1", text="Código")
        self.listaCLI.heading("#2", text="Nome")
        self.listaCLI.heading("#3", text="Telefone")
        self.listaCLI.heading("#4", text="Cidade")

        self.listaCLI.column("#0", width=1)
        self.listaCLI.column("#1", width=50)
        self.listaCLI.column("#2", width=200)
        self.listaCLI.column("#3", width=125)
        self.listaCLI.column("#4", width=125)

        self.scroolista = Scrollbar(self.frame_02, orient="vertical")
        self.listaCLI.configure(yscroll=self.scroolista.set)

        self.listaCLI.place(relx=0.01 , rely=0.1, relwidth=0.95, relheight=0.85)
        self.scroolista.place(relx=0.96 , rely=0.1, relwidth=0.04, relheight=0.85)

        self.listaCLI.bind("<Double-1>", self.on_double_click)


    

Application()
