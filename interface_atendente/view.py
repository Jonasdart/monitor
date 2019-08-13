#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

from tkinter import *
from time import sleep
import model
from trata import trata

class avelar_view():
    def __init__(self):
        self.x = list()
        self.y = list()
        self.tipo = '0'

    def posiciona_janela(self, x = 3, y = 2):
        try:
            self.x.clear()
            self.y.clear()
        except:
            pass

        #self.tela.attributes("-fullscreen", False)
        self.altura = self.tela.winfo_screenheight()
        self.largura = self.tela.winfo_screenwidth()
        altura = (self.altura/2) + 50
        largura = (self.largura/2) - 80
        valor = -234
        if x is 4:
            valor = valor*1.5
        for x in range(x):
            self.x.append(str(int(largura+valor)))
            valor += 234
        valor = -200
        for x in range(y):
            self.y.append(str(int(altura+valor)))
            valor += 200

    def credencia(self, verifica = False):
        local_bd = open("bd.txt", "r")
        local_bd = local_bd.readline()
        if not verifica:
            self.menu_login()
        else:
            self.cred = open(".crd.txt", 'w')
            usuario = self.caixa_pega_usuario.get()
            senha = self.caixa_pega_senha.get()
            self.cred.write(f"{local_bd}\n")
            self.cred.write(f"{usuario}\n")
            self.cred.write(f"{senha}\n")
            self.cred.write("avelar\n")
            self.cred.close()

            self.limpa_view()

            return

    def menu_login(self):
        #Criação da Tela
        self.tela_login = Tk()
        self.tela_login.title(f"DuzzSystem - Login")
        self.tela_login["bg"] = "#040c31"
        self.tela_login.geometry("360x300+0+0")
            #Criação dos Labels
        self.texto_solicita_usuario = Label(self.tela_login, text = "Informe o Login:", width = "30", foreground = "white", bg = "#040c31")
        self.texto_solicita_senha = Label(self.tela_login, text = "Informe a Senha:", width = "30", foreground = "white", bg = "#040c31")
        self.caixa_pega_usuario = Entry(self.tela_login, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_senha = Entry(self.tela_login, width = "30", bd = "10", relief = "flat", show = "*")
            #Posição dos Labels
        self.texto_solicita_usuario.pack(padx = "10", pady = "10")
        self.caixa_pega_usuario.pack(padx = "10", pady = "10")
        self.texto_solicita_senha.pack(padx = "10", pady = "10")       
        self.caixa_pega_senha.pack(padx = "10", pady = "10")
            #Criação dos Botões
        self.botao_entrar = Button(self.tela_login, text = "ENTRAR", width = "35", bd = "10", relief = "flat")
            #Posição dos Botões
        self.botao_entrar.pack(padx = "10", pady = "10")
            #Funções dos Botões
        self.botao_entrar["command"] = lambda: self.credencia(True)

        self.tela_login.mainloop()

    def tela_inicial(self, banco = "", cursor = ""):
        if banco is not "":
            self.model = model.avelar_model(banco, cursor)
        #Verifica se tem janela de login aberta
        self.limpa_view()
        #Criação da Tela
        self.tela = Tk()
        self.tela.title("Funerária Avelar - DuzzSystem")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")
        #self.tela.geometry("1060x580+0+0")
            #Criação dos Botões
        self.botao_atualizar_salas = Button(self.tela, text = "Atualizar Velórios", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_gerenciamento = Button(self.tela, text = "Gerenciamento", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_suporte = Button(self.tela, text = "Suporte",height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Botões
        self.botao_atualizar_salas.place(x = self.x[0], y = self.y[0])
        self.botao_gerenciamento.place(x = self.x[1], y = self.y[0])
        self.botao_suporte.place(x = self.x[2], y = self.y[0])
            #Funções dos Botões
        self.botao_atualizar_salas["command"] = self.atualizar_velorios
        self.botao_gerenciamento["command"] = self.gerenciamento
        self.botao_suporte["command"] = self.suporte

        self.tela.mainloop()

    def suporte(self):
        #Criação da Tela pop_up
        self.pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        self.pop_up.title(f"Duzz System - SUPORTE")
        self.pop_up["bg"] = "#040c31"
        self.posiciona_janela(x = 2, y = 2)
        self.pop_up.state("zoomed")
        self.pop_up.geometry(f"{self.largura}x{self.altura}+0+0")

        numero = Label(self.pop_up, text = "(11) 9 6861 - 3644", font=('Verdana','32','italic','bold'))
        numero.place(x = str(int(self.x[1]) - 165), y = self.y[0])
        email = Label(self.pop_up, text = "duzzsystem@gmail.com", font=('Verdana','32','italic','bold'))
        email.pack(side = "bottom", expand = True)

        botao_menu = Button(self.pop_up, text = "Retornar à Página Anterior", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
        botao_menu.place(x = str(int(self.x[1]) - 240), y = self.y[1])
        botao_menu["command"] = lambda: self.pop_up.destroy()

    def gerenciamento(self):
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Gerenciamento")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")
            #Criação dos Botões
        self.botao_nova_sala = Button(self.tela, text = "Nova Sala", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_editar_sala = Button(self.tela, text = "Editar Sala", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_excluir_sala = Button(self.tela, text = "Excluir Sala",height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Botões
        self.botao_nova_sala.place(x = self.x[0], y = self.y[0])
        self.botao_editar_sala.place(x = self.x[1], y = self.y[0])
        self.botao_excluir_sala.place(x = self.x[2], y = self.y[0])
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_nova_sala["command"] = self.tela_nova_sala
        self.botao_editar_sala["command"] = self.comando_para_editar_sala
        self.botao_excluir_sala["command"] = self.comando_para_excluir_sala
        self.botao_menu["command"] = self.tela_inicial

        self.tela.mainloop()

    def tela_nova_sala(self):
        self.tipo = '3'
        self.limpa_view()
        #Criação da Tela pop_up
        self.tela = Tk()
        #elf.pop_up.overrideredirect(True)
        self.tela.title(f"Funerária Avelar - Nova Sala")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")
            #Criação dos Labels
        self.texto_solicita_nome = Label(self.tela, text = "Informe o nome da sala que deseja adicionar:", foreground = "white", bg = "#040c31")
        self.caixa_pega_nome = Entry(self.tela, width = "30", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
            #Criação dos Botões
        self.botao_enviar = Button(self.tela, text = "SALVAR", width = "35", bd = "10", relief = "flat")
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.lancador_de_dados('3', [self.caixa_pega_nome.get()])
        self.botao_menu["command"] = self.gerenciamento
        
        self.tela.mainloop()

    def tela_editar_sala(self, salas_existentes):
        self.tipo = '4'
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Editar Sala")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")

            #Criação os Labels
        if len(salas_existentes) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Disponíveis", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhuma Sala Existente", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        for sala in salas_existentes:
            self.lista_de_selecao.insert(END, sala)
            
            #Criação dos Botões
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_existentes) is not 0:
            self.lista_de_selecao.place(x = str(int(self.x[0]) + 160), y = self.y[0])
            #Posição dos Botões
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_menu["command"] = self.gerenciamento

        self.tela.mainloop()

    def popup_editar_sala(self, sala):
        #Criação da Tela pop_up
        pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        pop_up.title(f"Funerária Avelar - Editar a sala número {sala[0]}")
        pop_up["bg"] = "#040c31"
        pop_up.geometry("560x500+0+0")

        nome_sala = sala.split("-")

            #Criação dos Labels
        self.texto_solicita_nome = Label(pop_up, text = f"Nome: {nome_sala[1]} - Alterar para:", foreground = "white", bg = "#040c31")
        self.caixa_pega_nome = Entry(pop_up, width = "30", bd = "10", relief = "flat")
            #Criação dos Botões
        self.botao_enviar = Button(pop_up, text = "SALVAR", width = "35", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.lancador_de_dados('4', [nome_sala[0], self.caixa_pega_nome.get()], pop_up = pop_up)
        
        pop_up.mainloop()

    def tela_excluir_sala(self, salas_para_exluir):
        self.tipo = '5'
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Excluir Sala")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")

            #Criação os Labels
        if len(salas_para_exluir) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Disponíveis", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhuma Sala Existente", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        for sala in salas_para_exluir:
            self.lista_de_selecao.insert(END, sala)
            
            #Criação dos Botões
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")            
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_para_exluir) is not 0:
            self.lista_de_selecao.place(x = str(int(self.x[0]) + 160), y = self.y[0])
            #Posição dos Botões
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_menu["command"] = self.gerenciamento

        self.tela.mainloop()

    def popup_excluir_sala(self, sala):
        pop_up = Tk()
        pop_up.title(f"Excluir {sala}")
        texto_confirmacao = Label(pop_up,text= f"Deseja Excluir a {sala}", bd = "10", relief = "flat", foreground = "black", bg = "red")
        sala = sala.split("-")
        botao_ok = Button(pop_up, text = "OK", command = lambda: self.lancador_de_dados('5', [sala[0], sala[1]], pop_up = pop_up))
        texto_confirmacao.pack()
        botao_ok.pack()
            
        pop_up.mainloop()

    def atualizar_velorios(self):
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Atualizar Velórios")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela(x = 4, y = 2)
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")
            #Criação dos Botões
        self.botao_novo_velorio = Button(self.tela, text = "Novo Velório", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_editar_velorio = Button(self.tela, text = "Editar Velório", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_concluir_velorio = Button(self.tela, text = "Concluir Velório", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_excluir_velorio = Button(self.tela, text = "Excluir Velório",height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Botões
        self.botao_novo_velorio.place(x = self.x[0], y = self.y[0])
        self.botao_editar_velorio.place(x = self.x[1], y = self.y[0])
        self.botao_concluir_velorio.place(x = self.x[2], y = self.y[0])
        self.botao_excluir_velorio.place(x = self.x[3], y = self.y[0])
        self.botao_menu.place(x = str(int(self.x[1]) - 120), y = self.y[1])
            #Funções dos Botões
        self.botao_novo_velorio["command"] = self.comando_para_novo_velorio
        self.botao_editar_velorio["command"] = self.comando_para_editar_velorio
        self.botao_concluir_velorio["command"] = self.comando_para_concluir_velorio
        self.botao_excluir_velorio["command"] = self.comando_para_excluir_velorio
        self.botao_menu["command"] = self.tela_inicial

        self.tela.mainloop()

    def tela_novo_velorio(self, salas_disponiveis, quantidade_velorio):
        self.tipo = '0'
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Novo Velório")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")
            #Criação os Labels
        if len(salas_disponiveis) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Disponíveis", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhuma Sala Disponível", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        x = 0
        for sala in salas_disponiveis:
            texto_sala = f"{sala} - {quantidade_velorio[x]}"
            x += 1
            self.lista_de_selecao.insert(END, texto_sala)
            #Criação dos Botões
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_disponiveis) is not 0:
            self.lista_de_selecao.place(x = str(int(self.x[0]) + 160), y = self.y[0])
            #Posição dos Botões
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_menu["command"] = self.atualizar_velorios

        self.tela.mainloop()

    def popup_novo_velorio(self, sala):
        #Criação da Tela pop_up
        pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        pop_up.title(f"Funerária Avelar - Velório na {sala}")
        pop_up["bg"] = "#040c31"
            #Criação dos Labels
        self.texto_solicita_nome = Label(pop_up, text = "Informe o nome da pessoa falecida:", foreground = "white", bg = "#040c31")
        self.texto_solicita_data_velorio = Label(pop_up, text = "Informe a Data do Velório", foreground = "white", bg = "#040c31")
        self.texto_solicita_hora_inicio = Label(pop_up, text = "Informe o horário do velório:", foreground = "white", bg = "#040c31")
        self.texto_solicita_data_sepultamento = Label(pop_up, text = f"Informe a data do sepultamento", foreground = "white", bg = "#040c31")
        self.texto_solicita_hora_saida = Label(pop_up, text = "Informe a hora de saída da funerária", foreground = "white", bg = "#040c31")
        self.texto_solicita_cemiterio = Label(pop_up, text = f"Informe o cemitério de sepultamento", foreground = "white", bg = "#040c31")
        self.caixa_pega_nome = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_data_velorio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_hora_inicio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_data_sepultamento = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_hora_saida = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_cemiterio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
        self.texto_solicita_data_velorio.pack(padx = "10", pady = "10")
        self.caixa_pega_data_velorio.pack(padx = "10", pady = "10")
        self.texto_solicita_hora_inicio.pack(padx = "10", pady = "10")
        self.caixa_pega_hora_inicio.pack(padx = "10", pady = "10")
        self.texto_solicita_data_sepultamento.pack(padx = "10", pady = "10")
        self.caixa_pega_data_sepultamento.pack(padx = "10", pady = "10")
        self.texto_solicita_hora_saida.pack(padx = "10", pady = "10")       
        self.caixa_pega_hora_saida.pack(padx = "10", pady = "10")
        self.texto_solicita_cemiterio.pack(padx = "10", pady = "10")
        self.caixa_pega_cemiterio.pack(padx = "10", pady = "10")
            #Criação dos Botões
        self.botao_enviar = Button(pop_up, text = "SALVAR", width = "35", bd = "10", relief = "flat")
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.pega_dados_do_velorio([self.caixa_pega_data_velorio.get(), self.caixa_pega_hora_inicio.get(), int(sala[0]), self.caixa_pega_nome.get(), self.caixa_pega_hora_saida.get(), 
            self.caixa_pega_data_sepultamento.get(), self.caixa_pega_cemiterio.get()], '0', pop_up = pop_up)
        self.botao_menu["command"] = self.atualizar_velorios
        
        pop_up.mainloop()

    def tela_editar_velorio(self, salas_em_uso):
        self.tipo = '1'
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Editar Velório")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")
            #Criação os Labels
        if len(salas_em_uso) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Com Velórios", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhum Velório Agendado", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        for sala in salas_em_uso:
            nome_sala = f"{sala[0]} - {sala[1]}"
            self.lista_de_selecao.insert(END, nome_sala)
            
            #Criação dos Botões
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_em_uso) is not 0:
            self.lista_de_selecao.place(x = str(int(self.x[0]) + 160), y = self.y[0])
            #Posição dos Botões
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_menu["command"] = self.atualizar_velorios

        self.tela.mainloop()

    def popup_selecionar_e_editar_velorio(self, sala):
        velorios = self.model.listar_velorios(int(sala[0]))
        #Criação da Tela pop_up
        self.pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        self.pop_up.title(f"Funerária Avelar - Editar Velório na {sala}")
        self.pop_up["bg"] = "#040c31"
        self.posiciona_janela()
        self.pop_up.state("zoomed")
        self.pop_up.geometry(f"{self.largura}x{self.altura}+0+0")
        #Criação da Lista de Seleção
        mostra_velorios = Listbox(self.pop_up, height = "10", width = "50", bd = "10", relief = "flat")
        mostra_velorios.bind('<<ListboxSelect>>', self.velorio_selecionado)
            #Alimentando Lista de Seleção
        for velorio in velorios:
            texto_velorio = f"{velorio[0]} - {velorio[4]} - {velorio[2]} - Cemitério {velorio[7]}"
            mostra_velorios.insert(END, texto_velorio)
            #Criação os Labels
        if len(velorios) is not 0:
            self.texto_salas_disponiveis = Label(self.pop_up, text = f"Velórios na {sala}", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.pop_up, text = f"Nenhum Velório Agendado na {sala}", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação dos Botões
        botao_menu = Button(self.pop_up, text = "Retornar à Página Anterior", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
        if len(velorios) is not 0:
            mostra_velorios.place(x = str(int(self.x[0]) + 160), y = self.y[0])
            #Posição dos Botões
        botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        botao_menu["command"] = lambda: self.pop_up.destroy()

        self.pop_up.mainloop()

    def popup_editar_velorio(self, velorio):
        velorio = self.model.buscar_informacoes_velorio(str(velorio).split("-")[0])
        data_velorio = str(velorio[0][1])
        hora_inicio = str(velorio[0][2])
        nome = str(velorio[0][4])
        hora_saida = str(velorio[0][5])
        data_sepultamento = str(velorio[0][6])
        cemiterio_sepultamento = str(velorio[0][7])
        status = bool(velorio[0][8])
        #Criação da Tela pop_up
        pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        pop_up.title(f"Funerária Avelar - Editar Velório num {velorio[0][0]}")
        pop_up["bg"] = "#040c31"
            #Criação dos Labels
        self.texto_solicita_nome = Label(pop_up, text = f"Nome: {nome} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_data_velorio = Label(pop_up, text = f"Data do Velório: {data_velorio} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_hora_inicio = Label(pop_up, text = f"Hora do Inicio do Velório: {hora_inicio} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_data_sepultamento = Label(pop_up, text = f"Data Sepultamento: {data_sepultamento} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_hora_saida = Label(pop_up, text = f"Horário de Saída: {hora_saida} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_cemiterio = Label(pop_up, text = f"Cemitério Sepultamento: {cemiterio_sepultamento} - Alterar para:", foreground = "white", bg = "#040c31")
        self.caixa_pega_data_velorio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_hora_inicio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_nome = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_hora_saida = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_data_sepultamento = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_cemiterio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
            #Criação dos Botões
        self.botao_enviar = Button(pop_up, text = "SALVAR", width = "35", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
        self.texto_solicita_data_velorio.pack(padx = "10", pady = "10")
        self.caixa_pega_data_velorio.pack(padx = "10", pady = "10")
        self.texto_solicita_hora_inicio.pack(padx = "10", pady = "10")       
        self.caixa_pega_hora_inicio.pack(padx = "10", pady = "10")
        self.texto_solicita_data_sepultamento.pack(padx = "10", pady = "10")       
        self.caixa_pega_data_sepultamento.pack(padx = "10", pady = "10")
        self.texto_solicita_hora_saida.pack(padx = "10", pady = "10")       
        self.caixa_pega_hora_saida.pack(padx = "10", pady = "10")
        self.texto_solicita_cemiterio.pack(padx = "10", pady = "10")
        self.caixa_pega_cemiterio.pack(padx = "10", pady = "10")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.pega_dados_do_velorio([int(velorio[0][0]), self.caixa_pega_data_velorio.get(), self.caixa_pega_hora_inicio.get(), self.caixa_pega_nome.get(), self.caixa_pega_hora_saida.get(), 
            self.caixa_pega_data_sepultamento.get(), self.caixa_pega_cemiterio.get()], '1', pop_up)
        
        pop_up.mainloop()

    def tela_concluir_velorio(self, salas_em_uso):
        velorios = list()
        self.tipo = '6'
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Concluir Velório")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")

        for sala in salas_em_uso:
            velorios.append(self.model.listar_velorios_nao_concluidos(int(sala[0])))
        #Criação da Lista de Seleção
        mostra_velorios = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        mostra_velorios.bind('<<ListboxSelect>>', self.velorio_selecionado)
            #Alimentando Lista de Seleção
        for velorio in velorios:
            for item in velorio:
                texto_velorio = f"{item[0]} - {item[4]} - {item[2]} - Cemitério {item[7]}"
                mostra_velorios.insert(END, texto_velorio)
            #Criação os Labels
        if len(velorios) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = f"Velórios Não Finalizados", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = f"Nenhum Velório Em Andamento", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação dos Botões
        botao_menu = Button(self.tela, text = "Retornar à Página Anterior", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
        if len(velorios) is not 0:
            mostra_velorios.place(x = str(int(self.x[0]) + 160), y = self.y[0])
            #Posição dos Botões
        botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        botao_menu["command"] = self.atualizar_velorios

        self.tela.mainloop()

    def popup_concluir_velorio(self, velorio):
        pop_up = Tk()
        pop_up.title(f"Excluir Velório {velorio}")
        texto_confirmacao = Label(pop_up,text= f"Deseja Concluir o Velório {velorio}", bd = "10", relief = "flat", foreground = "black", bg = "yellow")
        botao_ok = Button(pop_up, text = "OK", command = lambda: self.lancador_de_dados('6', [velorio], pop_up = pop_up))
        texto_confirmacao.pack()
        botao_ok.pack()
            
        pop_up.mainloop()

    def tela_excluir_velorio(self, salas_em_uso):
        self.tipo = '2'
        #Criação da Tela
        self.limpa_view()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Excluir Velório")
        self.tela["bg"] = "#040c31"
        self.posiciona_janela()
        self.tela.state("zoomed")
        self.tela.geometry(f"{self.largura}x{self.altura}+0+0")
            #Criação os Labels
        if len(salas_em_uso) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Com Velórios", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhum Velório Agendado", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        for sala in salas_em_uso:
            nome_sala = f"{sala[0]} - {sala[1]}"
            self.lista_de_selecao.insert(END, nome_sala)
            
            #Criação dos Botões
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_em_uso) is not 0:
            self.lista_de_selecao.place(x = str(int(self.x[0]) + 160), y = self.y[0])
            #Posição dos Botões
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_menu["command"] = self.atualizar_velorios

        self.tela.mainloop()

    def popup_selecionar_e_excluir_velorio(self, sala):
        velorios = self.model.listar_velorios(int(sala[0]))
        #Criação da Tela pop_up
        self.pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        self.pop_up.title(f"Funerária Avelar - Excluir Velório na {sala}")
        self.pop_up["bg"] = "#040c31"
        self.pop_up.geometry("560x500+0+0")
        #Criação da Lista de Seleção
        mostra_velorios = Listbox(self.pop_up, height = "10", width = "50", bd = "10", relief = "flat")
        mostra_velorios.bind('<<ListboxSelect>>', self.velorio_selecionado)
            #Alimentando Lista de Seleção
        for velorio in velorios:
            texto_velorio = f"{velorio[0]} - {velorio[2]} - Finalizado = {bool(velorio[6])}"
            mostra_velorios.insert(END, texto_velorio)
            #Criação os Labels
        if len(velorios) is not 0:
            self.texto_salas_disponiveis = Label(self.pop_up, text = f"Velórios na {sala}", font=('Verdana','22','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.pop_up, text = f"Nenhum Velório Agendado na {sala}", font=('Verdana','22','italic','bold'), bd = "2", relief = "flat")
            #Criação dos Botões
        self.botao_menu = Button(self.tela, text = "Retornar ao menu", fg = "black", height = "2", width = "90", bd = "2", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
        if len(velorios) is not 0:
            mostra_velorios.pack()
            #Posição dos Botões
        self.botao_menu.place(x = self.x[0], y = self.y[1])
            #Funções dos Botões
        self.botao_menu["command"] = self.atualizar_velorios

        self.pop_up.mainloop()

    def popup_excluir_velorio(self, velorio):
        pop_up = Tk()
        pop_up.title(f"Excluir Velório {velorio}")
        texto_confirmacao = Label(pop_up,text= f"Deseja Excluir o Velório {velorio}", bd = "10", relief = "flat", foreground = "black", bg = "red")
        botao_ok = Button(pop_up, text = "OK", command = lambda: self.lancador_de_dados('2', [velorio], pop_up = pop_up))
        texto_confirmacao.pack()
        botao_ok.pack()
            
        pop_up.mainloop()
        

    def popup_info(self, texto = "Horário Inválido", cor = "red", cor_letra = "white", limpa = True):
        if limpa:
            self.limpa_view()

        pop_up = Tk()
        pop_up.title(f"{texto}")
        texto_msg_erro = Label(pop_up,text= texto, bd = "10", relief = "flat", foreground = cor_letra, bg = cor)
        botao_ok = Button(pop_up, text = "OK")
        if limpa:
            botao_ok["command"] = lambda: self.limpa_view(popup = pop_up)
        else:
            botao_ok["command"] = lambda: pop_up.destroy()
        texto_msg_erro.pack()
        botao_ok.pack()
            
        pop_up.mainloop()

    def comando_para_editar_sala(self):
        salas_existentes = list()
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]
        for x in range(len(id_salas)):
            salas_existentes.append(f"{id_salas[x]} - {nome_salas[x]}") 

        self.tela_editar_sala(salas_existentes)

    def comando_para_excluir_sala(self):
        salas_existentes = list()
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]
        salas_para_exluir = list()
        salas_livres = self.model.listar_salas_livres(id_salas)

        for x in range(len(salas_livres)):
            for y in range(len(id_salas)):
                if id_salas[y] is salas_livres[x]:
                    salas_para_exluir.append(f"{id_salas[y]} - {nome_salas[y]}")

        self.tela_excluir_sala(salas_para_exluir)

    def comando_para_novo_velorio(self):
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = list()
        for x in range(len(id_salas)):
            nome_salas.append(f"{id_salas[x]} - {salas[1][x]}")
        quantidade_velorio = self.model.conta_velorio_por_sala(id_salas)
        self.tela_novo_velorio(nome_salas, quantidade_velorio)


    def comando_para_editar_velorio(self):
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]

        salas_em_uso = self.model.listar_salas_em_uso(id_salas)
        nome_salas_em_uso = self.model.listar_nome_das_salas(salas_em_uso)
        self.tela_editar_velorio(nome_salas_em_uso)

    def comando_para_concluir_velorio(self):
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]

        salas_em_uso = self.model.listar_salas_em_uso(id_salas)
        nome_salas_em_uso = self.model.listar_nome_das_salas(salas_em_uso)
        self.tela_concluir_velorio(nome_salas_em_uso)

    def comando_para_excluir_velorio(self):
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]

        salas_em_uso = self.model.listar_salas_em_uso(id_salas)
        nome_salas_em_uso = self.model.listar_nome_das_salas(salas_em_uso)
        self.tela_excluir_velorio(nome_salas_em_uso)

    def pega_dados_do_velorio(self, dados, tipo, pop_up):
        if tipo is '0':
            indice = [1, 4]
        else:
            indice = [2, 4]
        if len(dados[indice[0]]) is 5 and ":" in dados[indice[0]]:
            tmp_horario = dados[indice[0]].split(":")
            try:
                int(tmp_horario[0])
                int(tmp_horario[1])
            except:
                self.popup_info(limpa = False)
            else:
                if int(tmp_horario[0]) <= 23 and int(tmp_horario[1]) <= 59:
                    if len(dados[indice[1]]) is 5 and ":" in dados[indice[1]]:
                        tmp_horario = dados[indice[1]].split(":")
                        try:
                            int(tmp_horario[0])
                            int(tmp_horario[1])
                        except:
                            self.popup_info(limpa = False)
                        else:
                            if int(tmp_horario[0]) <= 23 and int(tmp_horario[1]) <= 59:
                                self.limpa_view(popup = pop_up)
                                self.lancador_de_dados(tipo, dados, pop_up = pop_up)
                            else:
                                self.popup_info(limpa = False)
                    else:
                        self.popup_info(limpa = False)
                else:
                    self.popup_info(limpa = False)
        else:
            self.popup_info(limpa = False)


    def lancador_de_dados(self, tipo, itens, pop_up = None):
        dados = open("dados.txt", 'w')
        dados.write(f"{tipo}\n")
        for item in itens:
            dados.write(f"{item}-")
        dados.close()

        self.limpa_view(popup = pop_up)
        
    def item_selecionado(self, event):
        widget = event.widget
        selecionado = widget.curselection()
        item = widget.get(selecionado[0])
        if self.tipo is '0':
            return self.popup_novo_velorio(item)
        if self.tipo is '1':
            return self.popup_selecionar_e_editar_velorio(item)
        if self.tipo is '2':
            return self.popup_selecionar_e_excluir_velorio(item)
        if self.tipo is '4':
            return self.popup_editar_sala(item)
        if self.tipo is '5':
            return self.popup_excluir_sala(item)

    def velorio_selecionado(self, event):
        widget = event.widget
        selecionado = widget.curselection()
        velorio = widget.get(selecionado[0])
        if self.tipo is '1':
            return self.popup_editar_velorio(velorio)
        if self.tipo is '2':
            return self.popup_excluir_velorio(str(velorio).split("-")[0])
        if self.tipo is '6':
            return self.popup_concluir_velorio(str(velorio).split("-")[0])

    def limpa_view(self, popup = ""):
        try:
            self.tela.destroy()
        except:
            pass
        try:
            self.tela_login.destroy()
        except:
            pass
        try:
            self.pop_up.destroy()
        except:
            pass
        try:
            popup.destroy()
        except:
            pass
