from tkinter import *

def botao_div():
    global num1
    global divisao
    divisao = True
    num1 = e.get()
    e.delete(0, END)

def botao_multi():
    global num1
    global multi
    multi = True
    num1 = e.get()
    e.delete(0, END)

def botao_sub():
    global num1
    global sub
    sub = True
    num1 = e.get()
    e.delete(0, END)

def botao_soma():
    global num1
    global soma
    soma = True
    num1 = e.get()
    e.delete(0, END)

def botao_click(num):
    e.insert(END, num)

def botao_limpa():
    e.delete(0, END)

def botao_igual():
    global sub
    global soma
    global multi
    global divisao
    num2 = e.get()
    e.delete(0, END)

    if soma == True:
        e.insert(0, int(num1) + int(num2))
        soma = False
    if sub == True:
        e.insert(0, int(num1) - int(num2))
        sub = False
    if multi == True:
        e.insert(0, int(num1) * int(num2))
        multi = False
    if divisao == True:
        e.insert(0, int(num1) / int(num2))
        divisao = False

def botao_numero(num, padx=40):
    botao_num = Button(root, text=str(num),
                 fg='#FFFFFF', 
                 activeforeground='#FFFFFF',
                 bg='#320064',
                 font=('futura', 12, 'bold'),
                 padx=padx, pady=20,
                 command=lambda: botao_click(num))
    return botao_num

def botao_operacao(text, func, padx=40):
    botao_op = Button(root, text=text,
                 fg='#FFFFFF', 
                 activeforeground='#FFFFFF',
                 bg='#320064',
                 font=('futura', 12, 'bold'),
                 padx=padx, pady=20,
                 command=func)
    return botao_op

num1 = ''
num2 = ''

divisao = False
multi = False
sub = False
soma = False

root = Tk()

root.title("Sua calculadora")
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, 
          fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), 
          justify=CENTER)

e.grid(row=0, column=0, columnspan=4, pady=2)

operacao_divide = botao_operacao('÷', func=botao_div)
operacao_multiplica = botao_operacao('x', func=botao_multi)
operacao_subtrai = botao_operacao('-', func=botao_sub, padx=41.5)
operacao_soma = botao_operacao('+', func=botao_soma)


operacao_divide.grid(row=0, column=4)
operacao_multiplica.grid(row=1, column=4)
operacao_subtrai.grid(row=2, column=4)
operacao_soma.grid(row=3, column=4)


num_um = botao_numero(1)
num_dois = botao_numero(2)
num_tres = botao_numero(3)
num_quatro = botao_numero(4)
num_cinco = botao_numero(5)
num_seis = botao_numero(6)
num_sete = botao_numero(7)
num_oito = botao_numero(8)
num_nove = botao_numero(9)
num_zero = botao_numero(0, padx=91)

num_um.grid(row=3, column=1)
num_dois.grid(row=3, column=2)
num_tres.grid(row=3, column=3)
num_quatro.grid(row=2, column=1)
num_cinco.grid(row=2, column=2)
num_seis.grid(row=2, column=3)
num_sete.grid(row=1, column=1)
num_oito.grid(row=1, column=2)
num_nove.grid(row=1, column=3)
num_zero.grid(row=4, column=1, columnspan=2)

limpa = Button(root, text='C',
                 fg='#FFFFFF', 
                 activeforeground='#FFFFFF',
                 bg='#320064',
                 font=('futura', 12, 'bold'),
                 padx=38, pady=20,
                 command=botao_limpa)

limpa.grid(row=4, column=4)

igual = Button(root, text='=',
                 fg='#FFFFFF', 
                 activeforeground='#FFFFFF',
                 bg='#320064',
                 font=('futura', 12, 'bold'),
                 padx=40, pady=20,
                 command=botao_igual)

igual.grid(row=4, column=3)

root.mainloop()
