

from tkinter import *

def finaliza():
    final['text'] = 'Cadastro efetuado !'

i = Tk()
i.geometry('600x500')
i.title('Sistema de Cadastro')

cabecalho = Label(i,text='INFORME SEU DADOS PESSOAIS',fg='blue',font="-weight bold -size 12")
cabecalho.grid(row=0,column=1, padx= 0, pady=10)

nome_sup = Label(i, text='Digite seu Nome',fg='black',font="-weight bold -size 10")
nome_sup.grid(row=1,column=0, padx= 5, pady=5)

nome = Entry(i)
nome.grid(row=2,column=0, padx= 10, pady=5)

idade_titulo = Label(i,text='Informe Idade',fg='black',font="-weight bold -size 10")
idade_titulo.grid(row=1,column=1, padx= 0, pady=5)

idade = Entry(i)
idade.grid(row=2,column=1, padx= 5, pady=5)

cpf_titulo = Label(i,text='Digite CPF',fg='black',font="-weight bold -size 10")
cpf_titulo.grid(row=5,column=0, padx= 5, pady=5)
cpf = Entry(i)
cpf.grid(row=6,column=0, padx= 10, pady=5)

prob = Label(i,text='RG',fg='black',font="-weight bold -size 10")
prob.grid(row=5,column=1, padx= 5, pady=5)
prob = Entry(i)
prob.grid(row=6,column=1, padx= 5, pady=5)

bt1 = Button(i,text='Finalizar',fg='blue',font="-weight bold -size 11", command=finaliza)
bt1.grid(row=7,column=0, padx= 10, pady=10)


final = Label(i,text='',fg='blue',font="-weight bold -size 10")
final.grid(row=8,column=0, padx= 10, pady=5)

i.mainloop()







