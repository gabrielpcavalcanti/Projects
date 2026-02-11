import ttkbootstrap as tb
from random import randint

root = tb.Window(themename="cyborg")

lista_num = []

class funcs:

    def lista_aleatoria(self):

        self.lista_num = []

        for self.n in range(10):

            self.lista_num.append(randint(1,100))

        self.label.config(text=f"Random list: {self.lista_num}")


    def BubbleSort(self):

        self.n = len(self.lista_num)

        for i in range(self.n):

            for j in range(0, self.n-i-1):

                if self.lista_num[j] > self.lista_num[j+1]:

                    self.lista_num[j], self.lista_num[j+1] = self.lista_num[j+1], self.lista_num[j]

        self.label1.config(text=f"Random list organized: {self.lista_num}")


class Aplication(funcs):

    def __init__(self):
        self.root = root
        self.lista_num = lista_num
        self.tela()
        self.widget()
        root.mainloop()
    

    def tela(self):
        self.root.title("Bubble Sort App")
        self.root.geometry("800x350")
        self.root.resizable(False, False)
               
        
    def widget(self):
       
        self.bt_adcionar_aleatorio = tb.Button(text="Random list",bootstyle="success", command=self.lista_aleatoria)
        self.bt_adcionar_aleatorio.pack(pady=20)

        self.label = tb.Label(text='', font=('Helvetica', 12), bootstyle='Light')
        self.label.pack(pady=20)

        self.bt_bubble = tb.Button(text="Bubble sort",bootstyle="success", command=self.BubbleSort)
        self.bt_bubble.pack(pady=20)

        self.label1 = tb.Label(text=f'', font=('Helvetica', 12), bootstyle='Light')
        self.label1.pack(pady=20)


Aplication()
