"""
Gerador de Senhas
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import random

# Cores:
cor1 = "#020203"  # Preta
cor2 = "#fafcff"  # Branca
cor3 = "#626366"  # Cinza escuro
cor4 = "#f7bc19"  # Amarelo
cor5 = "#f79719"  # Laranja

# Janela
janela = Tk()
janela.title("***")
janela.geometry("400x400")
janela.configure(bg=cor3)
janela.resizable(False, False)

# Estilo
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Dividindo a tela em dois frames
frame_cima = Frame(janela, width=400, height=50, bg=cor3, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)
frame_baixo = Frame(janela, width=400, height=300, bg=cor3, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Frame de cima
app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0,
                 relief='flat', anchor='nw', font='Ivy 16 bold', bg=cor3, fg=cor2)
app_nome.place(x=80, y=8)
app_linha = Label(frame_cima, text='', width=400, height=1, padx=0,
                  relief='flat', anchor='nw', font='Ivy 1', bg=cor5, fg=cor1)
app_linha.place(x=0, y=45)

# Caixa para apresetar a senha aleatória
app_senha = Label(frame_baixo, text='- - -', width=15, height=2, padx=0,
                  relief='solid', anchor='center', font='Ivy 12 bold', bg=cor2, fg=cor1)
app_senha.grid(row=0, column=0, sticky=NSEW, padx=5, pady=10)

# Subtítulo informativo 1
app_info = Label(frame_baixo, text='- Selecione o limite de caracteres por senha:', height=1, padx=0,
                 relief='flat', anchor='nw', font='Ivy 10 bold', bg=cor3, fg=cor1)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx=10, pady=6)

# Caixa para manipular a quantidade de caracteres
var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=1, column=1, columnspan=1, sticky=NW, padx=17, pady=8)

# Campos para seleção das opções
frame_caracteres = Frame(frame_baixo, width=400, height=210, bg=cor3, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW)

# Especificações das opções
alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'
simbolos = '[]{}()*;/,_-'


# Função para gerar senha
def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'
    simbolos = '[]{}()*;/,_-'

    global combinar
    combinar = ''

    # Condição para maiúscula
    if estado_1.get() == alfabeto_maior:
        combinar = combinar + alfabeto_maior
    else:
        pass

    # Condição para minúscula
    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass

        # Condição para números
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    # Condição para símbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Sistema", "A senha foi copiada com sucesso!")
    botao_copiar_senha = Button(frame_baixo, command=copiar_senha, text='Copiar',
                                width=5, height=2, relief='raised', overrelief='solid',
                                anchor='center', font='Ivy 12 bold', bg=cor2, fg=cor1)
    botao_copiar_senha.grid(row=0, column=1, sticky=W, padx=10, pady=10, columnspan=1)


# Subtítulo informativo 2
app_info = Label(frame_baixo, text='- Selecione abaixo as especificidades:', height=1, padx=0,
                 relief='flat', anchor='nw', font='Ivy 10 bold', bg=cor3, fg=cor1)
app_info.grid(row=2, column=0, columnspan=2, sticky=NSEW, padx=10, pady=6)

# Check Letras Maiúsculas
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior,
                      offvalue='off', relief='flat', bg=cor3)
check_1.grid(row=0, column=0, sticky=E, padx=10, pady=5)

app_info_1 = Label(frame_caracteres, text='Letras maiúsculas: ABC', height=1, padx=0,
                   relief='flat', anchor='nw', font='Ivy 10 bold', bg=cor3, fg=cor4)
app_info_1.grid(row=0, column=1, sticky=W, padx=0, pady=5)

# Check Letras Minúsculas
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_menor,
                      offvalue='off', relief='flat', bg=cor3)
check_2.grid(row=1, column=0, sticky=E, padx=10, pady=5)

app_info_2 = Label(frame_caracteres, text='Letras minúsculas: abc', height=1, padx=0,
                   relief='flat', anchor='nw', font='Ivy 10 bold', bg=cor3, fg=cor4)
app_info_2.grid(row=1, column=1, sticky=W, padx=2, pady=5)

# Check Números
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros,
                      offvalue='off', relief='flat', bg=cor3)
check_3.grid(row=2, column=0, sticky=E, padx=10, pady=5)

app_info_3 = Label(frame_caracteres, text='Números: 123', height=1, padx=0,
                   relief='flat', anchor='nw', font='Ivy 10 bold', bg=cor3, fg=cor4)
app_info_3.grid(row=2, column=1, sticky=W, padx=2, pady=5)

# Check Símbolos
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos,
                      offvalue='off', relief='flat', bg=cor3)
check_4.grid(row=3, column=0, sticky=E, padx=10, pady=5)

app_info_4 = Label(frame_caracteres, text='Símbolos: []{}()*;/,_-', height=1, padx=0,
                   relief='flat', anchor='nw', font='Ivy 10 bold', bg=cor3, fg=cor4)
app_info_4.grid(row=3, column=1, sticky=W, padx=2, pady=5)

# Botão GERADOR e COPIAR
botao_gerar_senha = Button(frame_caracteres, command=criar_senha, text='Randomizar Senha',
                           width=30, height=1, relief='flat', overrelief='solid',
                           anchor='center', font='Ivy 10', bg=cor5, fg=cor2)
botao_gerar_senha.grid(row=5, column=1, sticky=NSEW, padx=11, pady=25)
botao_copiar_senha = Button(frame_baixo, text='Copiar',
                            width=5, height=2, relief='raised', overrelief='solid',
                            anchor='center', font='Ivy 12 bold', bg=cor2, fg=cor1)
botao_copiar_senha.grid(row=0, column=1, sticky=W, padx=10, pady=10, columnspan=1)

# Segurar a janela em looping para não fechar
janela.mainloop()
