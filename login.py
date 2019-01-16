
from tkinter import *
AZUL = '#1654ba'
usuario = 'Fabricio'
senha = '1234'

class Criar(object):
    def __init__(self, a):
        self.font = ('Arial', '15')
        self.font2 = ('Arial', '15')
        self.font3 = ('Verdana', '12', 'bold')
        self.font4 = ('Arial', '10')
           # foto inserida
        logo = PhotoImage(file='Imagens/bg_python.gif')

        # Frame dos contem os checkbotons
        self.frame10 = Frame(a)

        self.frame1 = Frame(a)

        # Frame titulo = Usuario
        self.frame2 = Frame(a)
        self.frame2['bg'] = AZUL

        # Frame Caixa de entrada usuario
        self.frame3 = Frame(a, pady= 10)

        # Frame para titulo senha
        self.frame4 = Frame(a)

        # Frame para caixa de entrada senha
        self.frame5 = Frame(a, pady= 10)

        # Frame para botao entrar
        self.frame6 = Frame(a)

        #  Frame para aprovaçao
        self.frame7 = Frame(a, pady= 20)

        self.frame8 = Frame(a)

        # Empacota todos os frames
        self.frame10.pack() # Tela principal
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame7.pack()
        self.frame8.pack()

        self.logo = Label(self.frame1)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        #  Titulo Usuario
        self.titUsuario = Label(self.frame2, text='Usuário',fg='black', font= self.font)
        self.titUsuario.pack()

        # Caixa de entrada para digitar
        self.entraUs = Entry(self.frame3, font=self.font4)
        self.entraUs.pack()

        # Titulo senha
        self.titSenha = Label(self.frame4, text='Senha', fg='black', font= self.font)
        self.titSenha.pack()

        # Caixa para senha
        self.senha = Entry(self.frame5, show='*', font= self.font4)
        self.senha.pack()

        # Botao entrar
        self.bt1 = Button(self.frame6, text='Entrar', fg='blue', font= self.font2, command=self.Valida)
        self.bt1.pack()

        self.validacao = Label(self.frame7, font= self.font3)
        self.validacao.pack()

        # Botao sair usa o quit() que destroi o mainloop() saindo so sistema
        self.bt2 = Button(self.frame8, text='Sair', fg='red', font= self.font2, command= self.frame10.quit)
        self.bt2.pack()

    def Valida(self):
        if self.entraUs.get() == usuario and self.senha.get() == senha:
           self.validacao['text'] = 'Acesso Liberado'
           self.validacao['fg'] = 'blue'

        elif self.entraUs.get() != usuario and self.senha.get() == senha:
            self.validacao['text'] = 'Usuario Incorreto'
            self.validacao['fg'] = 'red'

        elif self.entraUs.get() == usuario and self.senha.get() != senha:
            self.validacao['text'] = 'Senha Incorreta'
            self.validacao['fg'] = 'red'

        elif self.entraUs.get() != usuario and self.senha.get() != senha:
            self.validacao['text'] = 'Usuário / Senha Incorreta'
            self.validacao['fg'] = 'red'

# Cria tela
a = Tk()

# Cria instancia dos objetos
Criar(a)

# define a area da tela
a.geometry('450x500')

# Titulo da tela
a.title('Login')

# inicia o programa
a.mainloop()
