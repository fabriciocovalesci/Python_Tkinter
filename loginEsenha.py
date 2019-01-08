## Sistema de Login e Senha

from tkinter import *

usuario = ['fabricio','Luis'] # usuarios que tem acesso ao sistema
senha1 = ['1234','7890'] # senha dos usuarios

def verifica():
    if lg.get() == usuario[0] and sh.get() == senha1[0]: # verifica primeiro usuario
        resultado['text'] = 'Bem vindo ao sistema'
        resultado['fg'] = 'blue'
    elif lg.get() == usuario[1] and sh.get() == senha1[1]: # verifica segundo usuario
        resultado['text'] = 'Bem vindo ao sistema'
        resultado['fg'] = 'blue'
    elif lg.get() != usuario and sh.get() != senha1: # confere usuarios não cadastrados
        resultado['text'] = 'Usuario ou Senha Incorreto'
        resultado['fg'] = 'red'

def novo(): # Adiciona novos usuarios ( em desenvolvimento ainda )
    cria_finaliza.append(usuario)
    cria_finaliza.append(senha1)
    cria_finaliza['text'] = 'Usuário cadastrado'
    cria_finaliza['fg'] = 'blue'

i = Tk()
i.title('Login')
i.geometry('300x300')

# Descrição usuario
login = Label(i,text='Usuário',fg='black')

# Caixa de entrada usuario
lg = Entry(i)

# Descrição senha
senha = Label(i,text='Senha',fg='black')

# Caixa de entrada senha ocultando senha com ****
sh = Entry(i,show='*')

# Botao para entrar sistema
entra = Button(i,text='Acessar',fg='blue', command=verifica)

# Exibe se usuario tem acesso ao sistema
resultado = Label(i,text='',fg='blue')

# Botao para criar novo usuario
criar_novo = Button(i,text='Novo',fg='blue', command=novo)

# Mensagem de novo usuario criado (em desenvonvimento ainda)
cria_finaliza = Label(i,text='')

# Enpacotamento de interfaces criadas acima
login.pack()
lg.pack()
senha.pack()
sh.pack()
entra.pack(side=LEFT)

criar_novo.pack(side=RIGHT)
resultado.pack()
cria_finaliza.pack()

i.mainloop()




