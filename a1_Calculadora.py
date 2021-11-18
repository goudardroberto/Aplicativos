from tkinter import *

"""
- Com o Frame podemos definir dois pedaços independentes na tela
- bg para cor do background; 
- fg para cor da letra; 
- relief para o estilo;
- overrelief para ter efeito no botão ao passar o mouse
"""

# Cores:
cor1 = '#0a0a0a'  # Preta
cor2 = '#ffffff'  # Branca
cor4 = '#333231'  # Cinza escuro
cor5 = '#c9c8c3'  # Cinza claro
cor6 = '#f5ad42'  # Laranja

# Janela:
janela = Tk()
janela.title('Calculadora')
janela.geometry('240x310')
janela.resizable(False, False)
janela.config(bg=cor1)

# Display:
frame_tela = Frame(janela, width=240, height=50, bg=cor4)
frame_tela.grid(row=0, column=0)

# Corpo:
frame_corpo = Frame(janela, width=240, height=268)
frame_corpo.grid(row=1, column=0)

# Criando variável global para manter o histórico antes do cálculo
todos_valores = ''

valor_texto = StringVar()


# Criando funções
# Função para entrada de valores na tela
def entrar_valores(event):
    global todos_valores

    todos_valores += str(event)

    # Passando valor para tela
    valor_texto.set(todos_valores)


# Função para cálculo dos valores
def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


# Função para limpar a tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


# Criando label
app_label = Label(frame_tela, textvariable=valor_texto, width=17, height=2, padx=8, relief=FLAT, anchor='e',
                  justify=RIGHT, font='Ivy 16 bold', bg=cor4, fg=cor2)
app_label.place(x=0, y=0)

# Criando botões
b_1 = Button(frame_corpo, text='c', width=11, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=limpar_tela)
b_1.place(x=0, y=0)
b_3 = Button(frame_corpo, text='%', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: entrar_valores('%'))
b_3.place(x=120, y=0)
b_4 = Button(frame_corpo, text='/', width=5, height=2, bg=cor6, fg=cor2, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: entrar_valores('/'))
b_4.place(x=180, y=0)

b_5 = Button(frame_corpo, text='7', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: entrar_valores('7'))
b_5.place(x=0, y=52)
b_6 = Button(frame_corpo, text='8', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: entrar_valores('8'))
b_6.place(x=60, y=52)
b_7 = Button(frame_corpo, text='9', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: entrar_valores('9'))
b_7.place(x=120, y=52)
b_8 = Button(frame_corpo, text='*', width=5, height=2, bg=cor6, fg=cor2, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: entrar_valores('*'))
b_8.place(x=180, y=52)

b_9 = Button(frame_corpo, text='4', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
             overrelief=RIDGE, command=lambda: entrar_valores('4'))
b_9.place(x=0, y=104)
b_10 = Button(frame_corpo, text='5', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('5'))
b_10.place(x=60, y=104)
b_11 = Button(frame_corpo, text='6', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('6'))
b_11.place(x=120, y=104)
b_12 = Button(frame_corpo, text='-', width=5, height=2, bg=cor6, fg=cor2, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('-'))
b_12.place(x=180, y=104)

b_13 = Button(frame_corpo, text='1', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('1'))
b_13.place(x=0, y=156)
b_14 = Button(frame_corpo, text='2', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('2'))
b_14.place(x=60, y=156)
b_15 = Button(frame_corpo, text='3', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('3'))
b_15.place(x=120, y=156)
b_16 = Button(frame_corpo, text='+', width=5, height=2, bg=cor6, fg=cor2, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('+'))
b_16.place(x=180, y=156)

b_17 = Button(frame_corpo, text='0', width=11, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('0'))
b_17.place(x=0, y=208)
b_18 = Button(frame_corpo, text='.', width=5, height=2, bg=cor5, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=lambda: entrar_valores('.'))
b_18.place(x=120, y=208)
b_19 = Button(frame_corpo, text='=', width=5, height=2, bg=cor6, fg=cor2, font='Ivy 13 bold', relief=RAISED,
              overrelief=RIDGE, command=calcular)
b_19.place(x=180, y=208)

# O mainloop segura a janela aberta para ela não fechar
janela.mainloop()
