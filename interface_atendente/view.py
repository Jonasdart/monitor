#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

from tkinter import *
from time import sleep
import model
from trata import trata

class avelar_view():
    def __init__(self):
        self.tipo = '0'
        self.x = ["204", "438", "676"]
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
            self.cred.write("avelar\n")
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
        self.botao_excluir_velorio["command"] = self.comando_para_excluir_velorio

    def pega_dados_do_velorio(self, dados, tipo, pop_up):
        if len(dados[2]) is 5 and ":" in dados[2]:
            tmp_horario = dados[2].split(":")
            try:
                int(tmp_horario[0])
                int(tmp_horario[1])
            except:
                self.popup_info()
            else:
                if int(tmp_horario[0]) < 23 and int(tmp_horario[1]) < 59:
                    pop_up.destroy()
                    self.lancador_de_dados(tipo, dados)
                else:
                    self.popup_info()
        else:
            self.popup_info()

    def pega_dados_para_exclusao(self, tipo, dados, pop_up):
        try:
            self.pop_up.destroy()
            pop_up.destroy()
        except:
            raise
        else:
            self.lancador_de_dados(tipo, dados)


    def lancador_de_dados(self, tipo, itens):
        dados = open("dados.txt", 'w')
        dados.write(f"{tipo}\n")
        for item in itens:
            dados.write(f"{item}-")
        dados.close()
        try:
            self.tela.destroy()
        except:
            raise


    def comando_para_novo_velorio(self):
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]

        salas_livres = self.model.listar_salas_livres(id_salas)
        nome_salas_livres = self.model.listar_nome_das_salas(salas_livres)
        self.tela_novo_velorio(nome_salas_livres)


    def comando_para_editar_velorio(self):
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]

        salas_em_uso = self.model.listar_salas_em_uso(id_salas)
        nome_salas_em_uso = self.model.listar_nome_das_salas(salas_em_uso)
        self.tela_editar_velorio(nome_salas_em_uso)

    def comando_para_excluir_velorio(self):
        salas = self.model.listar_salas()
        id_salas = salas[0]
        nome_salas = salas[1]

        salas_em_uso = self.model.listar_salas_em_uso(id_salas)
        nome_salas_em_uso = self.model.listar_nome_das_salas(salas_em_uso)
        self.tela_excluir_velorio(nome_salas_em_uso)


    def tela_novo_velorio(self, salas_disponiveis):
        self.tipo = '0'
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
            nome_sala = f"{sala[0]} - {sala[1]}"
            self.lista_de_selecao.insert(END, nome_sala)
            #Criação dos Botões
        self.botao_voltar = Button(self.tela, text = "Retornar à Página Anterior", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_disponiveis) is not 0:
            self.lista_de_selecao.pack(expand = True)
            #Posição dos Botões
        self.botao_voltar.pack(expand = True)
            #Funções dos Botões
        self.botao_voltar["command"] = lambda: self.atualizar_salas()

        self.tela.mainloop()

    def tela_editar_velorio(self, salas_em_uso):
        self.tipo = '1'
        #Criação da Tela
        self.tela.destroy()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Editar Velório")
        self.tela["bg"] = "#040c31"
        self.tela.geometry("1060x580+0+0")
            #Criação os Labels
        if len(salas_em_uso) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Disponíveis", font=('Verdana','32','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhuma Sala Disponível", font=('Verdana','32','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        for sala in salas_em_uso:
            nome_sala = f"{sala[0]} - {sala[1]}"
            self.lista_de_selecao.insert(END, nome_sala)
            
            #Criação dos Botões
        self.botao_voltar = Button(self.tela, text = "Retornar à Página Anterior", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_em_uso) is not 0:
            self.lista_de_selecao.pack(expand = True)
            #Posição dos Botões
        self.botao_voltar.pack(expand = True)
            #Funções dos Botões
        self.botao_voltar["command"] = lambda: self.atualizar_salas()

        self.tela.mainloop()

    def tela_excluir_velorio(self, salas_em_uso):
        self.tipo = '2'
        #Criação da Tela
        self.tela.destroy()
        self.tela = Tk()
        self.tela.title("Funerária Avelar - Excluir Velório")
        self.tela["bg"] = "#040c31"
        self.tela.geometry("1060x580+0+0")
            #Criação os Labels
        if len(salas_em_uso) is not 0:
            self.texto_salas_disponiveis = Label(self.tela, text = "Salas Com Velórios", font=('Verdana','32','italic','bold'),  bd = "2", relief = "flat")
        else:
            self.texto_salas_disponiveis = Label(self.tela, text = "Nenhum Velório Agendado", font=('Verdana','32','italic','bold'), bd = "2", relief = "flat")
            #Criação da Lista de Seleção
        self.lista_de_selecao = Listbox(self.tela, height = "10", width = "50", bd = "10", relief = "flat")
        self.lista_de_selecao.bind('<<ListboxSelect>>', self.item_selecionado)
            #Alimentando Lista de Seleção
        for sala in salas_em_uso:
            nome_sala = f"{sala[0]} - {sala[1]}"
            self.lista_de_selecao.insert(END, nome_sala)
            
            #Criação dos Botões
        self.botao_voltar = Button(self.tela, text = "Retornar à Página Anterior", bg = "yellow", fg = "black", height = "10", width = "20", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
            #Posição da Lista de Seleção
        if len(salas_em_uso) is not 0:
            self.lista_de_selecao.pack(expand = True)
            #Posição dos Botões
        self.botao_voltar.pack(expand = True)
            #Funções dos Botões
        self.botao_voltar["command"] = lambda: self.atualizar_salas()

        self.tela.mainloop()

    def popup_novo_velorio(self, sala):
        #Criação da Tela pop_up
        pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        pop_up.title(f"Funerária Avelar - Velório na {sala}")
        pop_up["bg"] = "#040c31"
        pop_up.geometry("560x500+0+0")
            #Criação dos Labels
        self.texto_solicita_nome = Label(pop_up, text = "Informe o nome da pessoa falecida:", foreground = "white", bg = "#040c31")
        self.texto_solicita_hora_saida = Label(pop_up, text = "Informe o horário do velório:", foreground = "white", bg = "#040c31")
        self.texto_solicita_data_sepultamento = Label(pop_up, text = f"Informe a data do sepultamento", foreground = "white", bg = "#040c31")
        self.texto_solicita_cemiterio = Label(pop_up, text = f"Informe o cemitério de sepultamento", foreground = "white", bg = "#040c31")
        self.caixa_pega_nome = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_hora_saida = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_data_sepultamento = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_cemiterio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
        self.texto_solicita_hora_saida.pack(padx = "10", pady = "10")       
        self.caixa_pega_hora_saida.pack(padx = "10", pady = "10")
        self.texto_solicita_data_sepultamento.pack(padx = "10", pady = "10")
        self.caixa_pega_data_sepultamento.pack(padx = "10", pady = "10")
        self.texto_solicita_cemiterio.pack(padx = "10", pady = "10")
        self.caixa_pega_cemiterio.pack(padx = "10", pady = "10")
            #Criação dos Botões
        self.botao_enviar = Button(pop_up, text = "SALVAR", width = "35", bd = "10", relief = "flat")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.pega_dados_do_velorio([int(sala[0]), 
            self.caixa_pega_nome.get(), self.caixa_pega_hora_saida.get(), self.caixa_pega_data_sepultamento.get(), self.caixa_pega_cemiterio.get()], 
            '0', pop_up)
        
        pop_up.mainloop()

    def popup_editar_velorio(self, sala):
        velorio = self.model.listar_velorios(int(sala[0]))
        nome = str(velorio[2])
        hora_saida = str(velorio[3])
        data_sepultamento = str(velorio[4])
        cemiterio_sepultamento = str(velorio[5])
        status = bool(velorio[6])
        #Criação da Tela pop_up
        pop_up = Tk()
        #elf.pop_up.overrideredirect(True)
        pop_up.title(f"Funerária Avelar - Editar Velório na {sala}")
        pop_up["bg"] = "#040c31"
        pop_up.geometry("560x500+0+0")
            #Criação dos Labels
        self.texto_solicita_nome = Label(pop_up, text = f"Nome: {nome} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_horario = Label(pop_up, text = f"Horário de Saída: {hora_saida} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_data_sepultamento = Label(pop_up, text = f"Data Sepultamento: {data_sepultamento} - Alterar para:", foreground = "white", bg = "#040c31")
        self.texto_solicita_cemiterio = Label(pop_up, text = f"Cemitério Sepultamento: {cemiterio_sepultamento} - Alterar para:", foreground = "white", bg = "#040c31")
        self.caixa_pega_nome = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_horario = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_data_sepultamento = Entry(pop_up, width = "30", bd = "10", relief = "flat")
        self.caixa_pega_cemiterio = Entry(pop_up, width = "30", bd = "10", relief = "flat")
            #Criação dos Botões
        self.botao_enviar = Button(pop_up, text = "SALVAR", width = "35", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_solicita_nome.pack(padx = "10", pady = "10")
        self.caixa_pega_nome.pack(padx = "10", pady = "10")
        self.texto_solicita_horario.pack(padx = "10", pady = "10")       
        self.caixa_pega_horario.pack(padx = "10", pady = "10")
        self.texto_solicita_data_sepultamento.pack(padx = "10", pady = "10")
        self.caixa_pega_data_sepultamento.pack(padx = "10", pady = "10")
        self.texto_solicita_cemiterio.pack(padx = "10", pady = "10")
        self.caixa_pega_cemiterio.pack(padx = "10", pady = "10")
            #Posição dos Botões
        self.botao_enviar.pack(padx = "10", pady = "10")
            #Funções dos Botões
        self.botao_enviar["command"] = lambda: self.pega_dados_do_velorio([int(sala[0]), self.caixa_pega_nome.get(), self.caixa_pega_horario.get(), 
            self.caixa_pega_data_sepultamento.get(), self.caixa_pega_cemiterio.get()], '1', pop_up)
        
        pop_up.mainloop()

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
        self.botao_voltar = Button(self.pop_up, text = "Voltar à Página Anterior", width = "35", bd = "10", relief = "flat")
            #Posição dos Labels
        self.texto_salas_disponiveis.pack()
        if len(velorios) is not 0:
            mostra_velorios.pack()
            #Posição dos Botões
        self.botao_voltar.pack(expand = True)
            #Funções dos Botões
        self.botao_voltar["command"] = lambda: self.pop_up.destroy()

        pop_up.mainloop()
        
    def popup_excluir_velorio(self, velorio):
        pop_up = Tk()
        pop_up.title(f"Excluir {velorio}")
        texto_confirmacao = Label(pop_up,text= f"Deseja Excluir o Velório {velorio}", bd = "10", relief = "flat", foreground = "black", bg = "red")
        botao_ok = Button(pop_up, text = "OK", command = lambda: self.pega_dados_para_exclusao('2', velorio, pop_up))
        texto_confirmacao.pack()
        botao_ok.pack()
            
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
        if self.tipo is '0':
            return self.popup_novo_velorio(item)
        if self.tipo is '1':
            return self.popup_editar_velorio(item)
        if self.tipo is '2':
            return self.popup_selecionar_e_excluir_velorio(item)

    def velorio_selecionado(self, event):
        widget = event.widget
        selecionado = widget.curselection()
        velorio = widget.get(selecionado[0])

        return self.popup_excluir_velorio(velorio)

"""teste = avelar_view()
teste.credencia()"""