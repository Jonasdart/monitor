#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

from tkinter import *
from time import sleep
import model
from trata import trata

class avelar_view():
    def __init__(self):
        self.x = ["188", "422", "660"]
        self.y = "150"

    def credencia(self, verifica = False):
        if not verifica:
            self.menu_login()
        else:
            self.cred = open(".crd.txt", 'w')
            usuario = self.caixa_pega_usuario.get()
            senha = self.caixa_pega_senha.get()
            self.cred.write("localhost\n")
            self.cred.write(f"{usuario}\n")
            self.cred.write(f"{senha}\n")
            self.cred.write("Salas\n")
            self.cred.close()

            self.tela_login.destroy()

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

    def tela_inicial(self, banco, cursor):
        self.model = model.avelar_model(banco, cursor)
        #Verifica se tem janela de login aberta
        try:
            self.tela_login.destroy()
        except:
            pass
        #Criação da Tela
        self.tela = Tk()
        self.tela.title("Funerária Avelar - DuzzSystem")
        self.tela["bg"] = "#040c31"
        self.tela.geometry("1060x580+0+0")
            #Criação dos Botões
        self.botao_atualizar_salas = Button(self.tela, text = "Atualizar Salas", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_gerenciamento = Button(self.tela, text = "Gerenciamento", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_suporte = Button(self.tela, text = "Suporte",height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Botões
        self.botao_atualizar_salas.place(x = self.x[0], y = self.y)
        self.botao_gerenciamento.place(x = self.x[1], y = self.y)
        self.botao_suporte.place(x = self.x[2], y = self.y)
            #Funções dos Botões
        self.botao_atualizar_salas["command"] = self.atualizar_salas

        self.tela.mainloop()

    def atualizar_salas(self):
        #Criação da Tela
        self.tela.destroy()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Atualizar Salas")
        self.tela["bg"] = "#040c31"
        self.tela.geometry("1060x580+0+0")
            #Criação dos Botões
        self.botao_novo_velorio = Button(self.tela, text = "Novo Velório", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_editar_velorio = Button(self.tela, text = "Editar Velório", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_excluir_velorio = Button(self.tela, text = "Excluir Velório",height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Botões
        self.botao_novo_velorio.place(x = self.x[0], y = self.y)
        self.botao_editar_velorio.place(x = self.x[1], y = self.y)
        self.botao_excluir_velorio.place(x = self.x[2], y = self.y)
            #Funções dos Botões
        self.botao_novo_velorio["command"] = self.comando_para_novo_velorio
        self.botao_editar_velorio["command"] = self.comando_para_editar_velorio

    def comando_para_novo_velorio(self):
        salas = self.model.listar_salas()
        salas_livres = self.model.listar_salas_livres(salas)
        self.tela_novo_velorio(salas_livres)

    def tela_novo_velorio(self, salas_disponiveis):
        #Criação da Tela
        self.tela.destroy()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Novo Velório")
        self.tela["bg"] = "#040c31"
        self.tela.geometry("1060x580+0+0")
            #Criação os Labels
        if len(salas_disponiveis) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Disponíveis", font=('Verdana','32','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhuma Sala Disponível", font=('Verdana','32','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        for sala in salas_disponiveis:
            self.lista_de_selecao.insert(END, sala)
            
            #Criação dos Botões
        self.botao_voltar = Button(self.tela, text = "Retornar A Página Anterior", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_disponiveis) is not 0:
            self.lista_de_selecao.pack(expand = True)
            #Posição dos Botões
        else:
            self.botao_voltar.pack(expand = True)
            #Funções dos Botões
        self.botao_voltar["command"] = lambda: self.atualizar_salas()

    def pega_dados_do_velorio(self, sala, pessoa, horario, pop_up):
        if len(horario) is 5 and ":" in horario:
            tmp_horario = horario.split(":")
            try:
                int(tmp_horario[0])
                int(tmp_horario[1])
            except:
                self.popup_info()
            else:
                if int(tmp_horario[0]) < 23 and int(tmp_horario[1]) < 59:
                    pop_up.destroy()
                    self.lancador_de_dados(0, sala, [pessoa, horario])
                else:
                    self.popup_info()
        else:
            self.popup_info()

    def lancador_de_dados(self, tipo, sala, itens):
        dados = open("dados.txt", 'w')
        dados.write(f"{tipo}\n")
        dados.write(f"{sala}-")
        for item in itens:
            dados.write(f"{item}-")
        try:
            self.tela.destroy()
        except:
            pass

    def popup_novo_velorio(self, sala):
        #Criação da Tela pop_up
        pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        pop_up.title(f"Funerária Avelar - Velório na {sala}")
        pop_up["bg"] = "#040c31"
        pop_up.geometry("360x300+0+0")
            #Criação dos Labels
        self.texto_solicita_nome = Label(pop_up, text = "Informe o nome da pessoa falecida:", width = "30", foreground = "white", bg = "#040c31")
        self.texto_solicita_horario = Label(pop_up, text = "Informe o horário do velório:", width = "30", foreground = "white", bg = "#040c31")
        self.caixa_pega_nome = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_horario = Entry(pop_up, width = "30", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
        self.texto_solicita_horario.pack(padx = "10", pady = "10")       
        self.caixa_pega_horario.pack(padx = "10", pady = "10")
            #Criação dos Botões
        self.botao_enviar = Button(pop_up, text = "SALVAR", width = "35", bd = "10", relief = "flat")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.pega_dados_do_velorio(sala, self.caixa_pega_nome.get(), self.caixa_pega_horario.get(), pop_up)
        
        pop_up.mainloop()


    def popup_info(self, texto = "Horário Inválido", cor = "red", cor_letra = "white"):
        try:
            self.tela_login.destroy()
        except:
            pass

        pop_up = Tk()
        pop_up.title(f"{texto}")
        texto_msg_erro = Label(pop_up,text= texto, width = "35", bd = "10", relief = "flat", foreground = cor_letra, bg = cor)
        botao_ok = Button(pop_up, text = "OK", command = lambda: pop_up.destroy())
        texto_msg_erro.pack()
        botao_ok.pack()
            
        pop_up.mainloop()
        
    def editar_velorio(self):
        pass
    def excluir_velorio(self):
        pass
    def nova_sala(self):
        pass
    def editar_sala(self):
        pass

    def item_selecionado(self, event):
        widget = event.widget
        selecionado = widget.curselection()
        item = widget.get(selecionado[0])

        return self.popup_novo_velorio(item)

"""teste = avelar_view()
teste.credencia()"""