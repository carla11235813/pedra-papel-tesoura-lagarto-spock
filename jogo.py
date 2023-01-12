import tkinter
from tkinter import *
from random import choice
from tkinter import ttk

#CORES
fundo = '#7CFFC4'
cor1 = '#001524'
cor2 = '#58A4B0'
cor3 = '#F7B801'
cor4 = '#BF211E'
cor5 = '#04F06A'


#CONFIGURAÇÕES DA JANELA
janela = Tk() #Criando a jenela
janela.title('PEDRA-PAPEL-TESOURA-LAGARTO-SPOCK')
janela.geometry('500x600+400+50') #largura, altura, posiçãoX, posiçãoY
janela.resizable(False, False) #ñ pode mudar o tamanho da janela, (False e True; 0 e 1)
janela.configure(bg=fundo)

#DIVIDINDO ENTRE DOIS FRAMES
#FRAME DE CIMA
frame_cima = Frame(janela, width=500, height=200, bg=cor1, relief=RAISED)
frame_cima.grid(row=0, column=0)

#FRAME DE BAIXO
frame_baixo = Frame(janela, width=500, height=400, bg=cor2, relief=FLAT)
frame_baixo.grid(row=1, column=0)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#CONFIGURANDO O FRAME DE CIMA
#JOGADOR---------------------------------
#nome
voce_nome = Label(frame_cima, text='VOCÊ', height=3, font=('Ivy 15 bold'), bg=cor1, fg=cor2)
voce_nome.place(x=40, y=130)
#linha indicativa do jogador
voce_linha = Label(frame_cima, height=13, width=2, bg='white', fg=cor2)
voce_linha.place(x=0, y=0)
#pontuação do jogador
voce_pontos = Label(frame_cima, height=1, text='0',font="Ivy 70 bold", bg=cor1, fg=cor2)
voce_pontos.place(x=110, y=30)
#----------------------------------------

#DOIS PONTOS
dois_pontos = Label(frame_cima, height=1, text=':', font='Ivy 70 bold', bg=cor1, fg=cor2)
dois_pontos.place(x=230, y=25)

#COMPUTADOR---------------------------------
#nome
computador_nome = Label(frame_cima, text='COMPUTADOR', height=3, font=('Ivy 15 bold'), bg=cor1, fg=cor2)
computador_nome.place(x=310, y=130)
#linha indicativa do computador
computador_linha = Label(frame_cima, height=13, width=2, bg='white', fg=cor2)
computador_linha.place(x=480, y=0)
#pontuação do computador
computador_pontos = Label(frame_cima, height=1, text='0',font="Ivy 70 bold", bg=cor1, fg=cor2)
computador_pontos.place(x=330, y=30)
#----------------------------------------


#LINHA EMPATE
empate_linha = Label(frame_baixo, height=1, width=500, bg='white', fg=cor2)
empate_linha.place(x=0, y=0)



#FUNÇÃO LÓGICA DO JOGO
pc_label = Label(frame_baixo, text='',font='Ivy 15 bold',bg=cor2, fg=cor1)
pc_label.place(x=400, y=30)

vc_label = Label(frame_baixo, text='',font='Ivy 15 bold',bg=cor2, fg=cor1)
vc_label.place(x=40, y=30)

pontos_vc = 0
pontos_pc = 0

def jogar(jogada):
    global pontos_vc, pontos_pc

    opcoes = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    pc = choice(opcoes)

    vc = jogada

    print(vc, pc)


    #LÓGICA PEDRA -----------------------------------
    if vc == 'pedra' and pc == 'pedra':
        print('EMPATE')
        voce_linha['bg'] = 'white'
        computador_linha['bg'] = 'white'
        empate_linha['bg'] = cor3
        vc_label['text'] = vc
        pc_label['text'] = pc

    elif vc == 'pedra' and pc == 'papel':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'pedra' and pc == 'tesoura':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'pedra' and pc == 'lagarto':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'pedra' and pc == 'spock':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    #LÓGICA PAPEL -----------------------------------
    if vc == 'papel' and pc == 'pedra':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'papel' and pc == 'papel':
        print('EMPATE')
        voce_linha['bg'] = 'white'
        computador_linha['bg'] = 'white'
        empate_linha['bg'] = cor3
        vc_label['text'] = vc
        pc_label['text'] = pc

    elif vc == 'papel' and pc == 'tesoura':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'papel' and pc == 'lagarto':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'papel' and pc == 'spock':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 


    #LÓGICA TESOURA --------------------------------
    if vc == 'tesoura' and pc == 'pedra':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'tesoura' and pc == 'papel':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'tesoura' and pc == 'tesoura':
        print('EMPATE')
        voce_linha['bg'] = 'white'
        computador_linha['bg'] = 'white'
        empate_linha['bg'] = cor3
        vc_label['text'] = vc
        pc_label['text'] = pc

    elif vc == 'tesoura' and pc == 'lagarto':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'tesoura' and pc == 'spock':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1


    # LÓGICA DO LAGARTO -----------------------
    if vc == 'lagarto' and pc == 'pedra':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'lagarto' and pc == 'papel':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'lagarto' and pc == 'tesoura':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'lagarto' and pc == 'lagarto':
        print('EMPATE')
        voce_linha['bg'] = 'white'
        computador_linha['bg'] = 'white'
        empate_linha['bg'] = cor3
        vc_label['text'] = vc
        pc_label['text'] = pc

    elif vc == 'lagarto' and pc == 'spock':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 
        

    #LÓGICA SPOCK -------------------------------------
    if vc == 'spock' and pc == 'pedra':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'spock' and pc == 'papel':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'spock' and pc == 'tesoura':
        print('VOCÊ GANHOU')
        voce_linha['bg'] = cor5
        computador_linha['bg'] = cor4
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_vc += 1 

    elif vc == 'spock' and pc == 'lagarto':
        print('COMPUTADOR GANHOU')
        voce_linha['bg'] = cor4
        computador_linha['bg'] = cor5 
        empate_linha['bg'] = 'white'
        vc_label['text'] = vc
        pc_label['text'] = pc
        pontos_pc += 1

    elif vc == 'spock' and pc == 'spock':
        print('EMPATE')
        voce_linha['bg'] = 'white'
        computador_linha['bg'] = 'white'
        empate_linha['bg'] = cor3
        vc_label['text'] = vc
        pc_label['text'] = pc
    



    #ATUALIZANDO PONTUAÇÃO 
    voce_pontos['text'] = pontos_vc
    computador_pontos['text'] = pontos_pc




#CONFIGURANDO O FRAME DE BAIXO-------------------------------------------------------
#BOTÕES----------------------------------
pedra = PhotoImage(file='imagens/pedra.png')
#o lambda permite enviar dados
b_pedra = Button(frame_baixo, command=lambda: jogar('pedra'), bd=0, image=pedra, width=150, height=150, bg=cor2, fg=cor2)
b_pedra.place(x=10, y=80)

papel = PhotoImage(file='imagens/papel.png')
b_papel = Button(frame_baixo, command=lambda: jogar('papel'), bd=0, image=papel, width=150, height=150, bg=cor2, fg=cor2)
b_papel.place(x=175, y=80)

tesoura = PhotoImage(file='imagens/tesoura.png')
b_tesoura = Button(frame_baixo, command=lambda: jogar('tesoura'), bd=0, image=tesoura, width=150, height=150, bg=cor2, fg=cor2)
b_tesoura.place(x=335, y=80)

lagarto = PhotoImage(file='imagens/lagarto.png')
b_lagarto = Button(frame_baixo, command=lambda: jogar('lagarto'), bd=0, image=lagarto, width=150, height=150, bg=cor2, fg=cor2)
b_lagarto.place(x=80, y=235)

spock = PhotoImage(file='imagens/spock.png')
b_spock = Button(frame_baixo, command=lambda: jogar('spock'), bd=0, image=spock, width=150, height=150, bg=cor2, fg=cor2)
b_spock.place(x=270, y=235)

#BOTÃO DE ATUALIZAR-----------------------------------------------------------------------
def atualizar_jogo():
    global voce_pontos, computador_pontos, pontos_pc, pontos_vc, vc_label, pc_label, voce_linha, computador_linha, empate_linha
    voce_pontos['text'] = 0
    computador_pontos['text'] = 0
    pontos_vc = 0
    pontos_pc = 0
    pc_label['text'] = ''
    vc_label['text'] = ''
    voce_linha['bg'] = 'white'
    computador_linha['bg'] = 'white'
    empate_linha['bg'] = 'white'

atualizar = PhotoImage(file='imagens/atualizar.png')
b_atualizar = Button(frame_baixo, command=atualizar_jogo, image=atualizar, width=30, height=30)
b_atualizar.place(x=230, y=30)


janela.mainloop() #Mantendo a janela aberta