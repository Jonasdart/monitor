#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

from tkinter import *
from time import sleep

class avelar_view():
    def __init__(self):
        self.x = ["188", "422", "660"]
        self.y = "150"
    def tela_inicial(self):
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
        self.botao_novo_velorio["command"] = lambda: self.tela_novo_velorio(["sala1", "sala2", "sala3"])
    def tela_novo_velorio(self, salas_disponiveis):
        #Criação da Tela
        self.tela.destroy()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Novo Velório")
        self.tela["bg"] = "#040c31"
        self.tela.geometry("1060x580+0+0")
            #Criação os Labels
        if len(salas_disponiveis) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Disponíveis")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhuma Sala Disponível")
            #Posição dos Labels
        self.texto_salas_disponiveis.place(x = self.x[0], y = str(int(self.y)-50))
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "20", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
        self.lista_de_selecao.place(x = self.x[0], y = self.y)
            #Alimentando Lista de Seleção
        for sala in salas_disponiveis:
            self.lista_de_selecao.insert(END, sala)
            #Criação dos Botões
        self.botao_novo_velorio = Button(self.tela, text = "Novo Velório", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_editar_velorio = Button(self.tela, text = "Editar Velório", height = "10", width = "20", bd = "10", relief = "flat")
        self.botao_excluir_velorio = Button(self.tela, text = "Excluir Velório",height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Botões
            #Funções dos Botões
    def popup_novo_velorio(self, sala):
        #Criação da Tela pop_up
        self.pop_up = Tk()
        self.pop_up.title(f"Funerária Avelar - Velório na {sala}")
        self.pop_up["bg"] = "#040c31"
        self.pop_up.geometry("360x300+0+0")
            #Criação dos Labels
        self.texto_solicita_nome = Label(self.pop_up, text = "Informe o nome da pessoa falecida:", width = "30", foreground = "white", bg = "#040c31")
        self.texto_solicita_horario = Label(self.pop_up, text = "Informe o horário do velório:", width = "30", foreground = "white", bg = "#040c31")
        self.caixa_pega_nome = Entry(self.pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_horario = Entry(self.pop_up, width = "30", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
        self.texto_solicita_horario.pack(padx = "10", pady = "10")       
        self.caixa_pega_horario.pack(padx = "10", pady = "10")
            #Criação dos Botões
        self.botao_enviar = Button(self.pop_up, text = "SALVAR", width = "35", bd = "10", relief = "flat")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.pega_dados_do_velorio(self.caixa_pega_nome.get(), self.caixa_pega_horario.get())

    def pega_dados_do_velorio(self, pessoa, horario):
        if len(horario) is 5 and ":" in horario:
            tmp_horario = horario.split(":")
            try:
                int(tmp_horario[0])
                int(tmp_horario[1])
            except:
                self.popup_erro()
            else:
                return [0, [pessoa, horario]]
        else:
            self.popup_erro()

    def popup_erro(self, texto = "Horário Inválido"):
        popup_temporario = Tk()
        popup_temporario.title(f"{texto}")
        texto_msg_erro = Label(popup_temporario,text= texto, width = "35", bd = "10", relief = "flat", foreground = "white", bg = "red")
        texto_msg_erro.pack()
        popup_temporario.mainloop()
        
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


if __name__ == "__main__":
    teste = avelar_view()
    teste.tela_inicial()
