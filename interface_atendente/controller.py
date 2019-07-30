#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

import model
import view

class control():
    def __init__(self):
        self.model = model.avelar_model()
        self.view  = view.avelar_view()
    def inicio(self):
    	retorno = self.view.tela_inicial()
    	self.armador(retorno[0], retorno[1])
    def armador(tipo, dados):
    	if tipo is 0:
    		self.novo_velorio(dados)
    	elif tipo is 1:
    		self.editar_nome(dados)
    	elif tipo is 2:
    		self.
    def nova_sala(self):
        pass
    def novo_velorio(self):
        pass
    def editar_sala(self):
        pass
    

"""
0 - Novo Velório
1 - Editar Nome do Falecido
2 - Editar Horário do Velório
3 - Exlcuir Velório
4 - Nova sala
5 - Renomear Sala
6 - Excluir Sala
"""