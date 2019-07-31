#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

class trata():
	def __init__(self):
		pass

	def trata_retorno_de_todas_tabelas(tabelas):
		salas = list()
		salas_tratadas = list()
		tratando = tabelas
		for tratado in tratando:
			salas.append(str(tratado))
		for string in salas:
			t_string = string.split("'")
			salas_tratadas.append(t_string[1])

		return salas_tratadas