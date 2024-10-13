from tkinter import *

valor = 0

def imprimir():   #função
    x = valor**2
    frase = f'''
    Olá Mundo!
    {x}'''
                    # " ''' ": imprime o que está dentro dos '''
    texto_teste["text"] = frase

def obter():
    global valor
    try:
        valor = int(input.get())   
    except ValueError:
        valor = 9
    texto_teste["text"]=valor

janela = Tk()
janela.title("Título da Janela")
janela.geometry("400x400")

texto_orientacao = Label(janela, text="Label 1", bg='green')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

texto_orientacao2 = Label(janela, text="Label 2", bg='yellow')
texto_orientacao2.grid(column=0, row=1)

texto_orientacao3 = Label(janela, text="Label 3", bg='red')
texto_orientacao3.grid(column=1, row=0)

botao = Button(janela, text="Imprimir", command=imprimir) #command chama sempre uma função #se eu colocasse imprimir() com parenteses, ele executaria instantaneamente a função
botao.grid(column=2, row=2)

botao1 = Button(janela, text="Obter", command=obter)
botao1.grid(column=1, row=2)

texto_teste=Label(janela, text="")
texto_teste.grid(column=2, row=3)

input = Entry(janela, width=10, font=('Arial 10'))
input.grid(row=3, column=1, padx=10, pady=5)

janela.mainloop()