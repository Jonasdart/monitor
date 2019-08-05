#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

import model
import view
from __login__ import login
from time import sleep
import os

class control():
    def __init__(self):
        self.view  = view.avelar_view()
        self.controle = login()
        self.status = False


    def inicio(self):
        if not self.status:
            try:
                self.view.credencia()
                self.status = self.login(self.autentica())
            except:
                
                self.view.popup_info("Login Não Estabelecido!")
                self.inicio()
            else:
                self.view.popup_info("Seja Bem Vindo!", "green", "black")
                self.view.tela_inicial(self.banco, self.cursor)
                dados = self.buscador_de_dados()
                self.armador(dados)
        else:
            self.view.tela_inicial(self.banco, self.cursor)
            dados = self.buscador_de_dados()
            self.armador(dados)


    def armador(self, dados):
        tipo = dados[0]
        if tipo is '0':
            velorio = self.model.trata_para_subir_ao_banco(dados[1])
            self.novo_velorio(velorio)
        elif tipo is '1':
            velorio = self.model.trata_para_subir_ao_banco(dados[1])
            self.editar_velorio(velorio)
        elif tipo is '2':
            velorio = self.model.trata_para_subir_ao_banco(dados[1])
            self.excluir_velorio(velorio)
        elif tipo is '3':
            sala = self.model.trata_para_subir_ao_banco(dados[1])
            self.nova_sala(sala)
        elif tipo is '4':
            sala = self.model.trata_para_subir_ao_banco(dados[1])
            self.editar_sala(sala)
        elif tipo is '5':
            sala = self.model.trata_para_subir_ao_banco(dados[1])
            self.excluir_sala(sala)

    def login(self, cred):
        try:
            self.banco = self.controle.faz_login(cred)
        except:
            
            self.view.popup_info("Login Não Estabelecido!")
            self.inicio()
        else:
            self.cursor = self.banco.cursor()
            self.model = model.avelar_model(self.banco, self.cursor)
            return True

    def autentica(self):
        dados_login = list()
        try:
            self.cred = open(".crd.txt", 'r')
        except:
            raise
        else:
            for line in self.cred.readlines():
                dados_login.append(line.strip())
            self.cred.close()
            os.remove(".crd.txt")
            return dados_login

    def buscador_de_dados(self):
        dados = open("dados.txt", 'r')
        itens = list()
        for dado in dados.readlines():
            itens.append(dado.strip())
        dados.close()
        os.remove("dados.txt")
        return itens

    def novo_velorio(self, velorio):
        try:
            self.model.novo_velorio(velorio)
        except:
            self.view.popup_info("Velório Não Foi Salvo!")
            self.inicio()
        else:
            self.view.popup_info("Velório Salvo Com Sucesso!", cor = "green", cor_letra = "black")
            self.inicio()

    def editar_velorio(self, velorio):
        try:
            self.model.editar_velorio(velorio)
        except:
            self.view.popup_info("Dados Não Alterados!")
            self.inicio()
        else:
            self.view.popup_info("Velório Atualizado com Sucesso!", cor = "green", cor_letra = "black")
            self.inicio()

    def excluir_velorio(self, velorio):
        try:
            self.model.excluir_velorio(velorio)
        except:
            self.view.popup_info("Velório Não Excluído!")
            self.inicio()
        else:            
            self.view.popup_info("Velório Excluído com Sucesso!", cor = "green", cor_letra = "black")
            self.inicio()

    def nova_sala(self, sala):
        try:
            self.model.nova_sala(sala)
        except:
            self.view.popup_info("Sala Não Foi Criada!")
            self.inicio()
        else:
            self.view.popup_info(f"'{sala}' criada com Sucesso!", cor = "green", cor_letra = "black")
            self.inicio()


    def editar_sala(self, sala):
        id_sala = sala[0]
        novo_nome = sala[1]
        try:
            self.model.editar_sala(id_sala, novo_nome)
        except:
            self.view.popup_info("Sala Não Foi Editada!")
            self.inicio()
        else:
            self.view.popup_info(f"A sala '{sala[0]}' agora se chama {sala[1]}", cor = "green", cor_letra = "black")
            self.inicio()

    def excluir_sala(self, sala):
        id_sala = sala[0]
        try:
            self.model.excluir_sala(id_sala)
        except:
            self.view.popup_info("Sala Não Foi Excluída!")
            self.inicio()
        else:
            self.view.popup_info(f"A sala '{sala[0]} - {sala[1]}' \nFoi Excluída Com Sucesso!", cor = "green", cor_letra = "black")
            self.inicio()

if __name__ == "__main__":
    start = control()
    start.inicio()

"""
0 - Novo Velório
1 - Editar Velório
2 - Excluir Velório
3 - Nova sala
4 - Editar Sala
5 - Excluir Sala
"""