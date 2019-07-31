#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

import MySQLdb as mdb
from SQLManager import gera_query 
from trata import trata

class avelar_model():
	def __init__(self, banco, cursor):
		self.manager = gera_query()
		self.cursor = cursor
		self.banco = banco

	def nova_sala(self, nome_nova_sala):
		query = self.manager.novo_velorio(banco_de_dados = "salas", nova_tabela = nome_nova_sala)
		self.final_sem_retorno(query)

	def listar_salas(self):
		query = self.manager.listar_tabelas()
		salas = self.final_com_retorno(query)
		salas = trata.trata_retorno_de_todas_tabelas(salas)
		return salas

	def listar_salas_livres(self, salas):
		salas_livres = list()
		for sala in salas:
			try:
				sala = str(sala)
			except:
				raise
			query = self.manager.verifica_se_tabela_esta_vazia(sala)
			resposta = self.final_com_retorno(query)
			if len(resposta) is 0:
				salas_livres.append(sala)

		return salas_livres

	def renomear_sala(self, sala, novo_nome):
		query = self.manager.renomear_tabela("salas", sala, novo_nome)
		self.final_sem_retorno(query)

	def excluir_sala(self, sala):
		query = self.manager.excluir_tabela(sala)
		self.final_sem_retorno(query)

	def novo_velorio(self, sala, pessoa, horario):
		query = self.manager.inserir_na_tabela(tabela = str(sala), dados = [str(pessoa), str(horario)])
		try:
			self.final_sem_retorno(query)
		except:
			raise

	def editar_nome(self, sala, novo_nome):
		query = self.manager.alterar_dados_da_tabela(tabela = sala, coluna = "Pessoa", dados = novo_nome)
		self.final_sem_retorno(query)

	def editar_horario(self, sala, novo_horario):
		query = self.manager.alterar_dados_da_tabela(tabela = sala, coluna = "Horario", dados = novo_horario)
		self.final_sem_retorno(query)

	def final_sem_retorno(self, query):
		try:
			self.cursor.execute(query)
		except:
			raise #Exception("Não Foi Possível Salvar Dados no Banco de Dados!")
		else:
			self.banco.commit()

	def final_com_retorno(self, query):
		try:
			self.cursor.execute(query)
		except:
			raise #Exception("Não Foi Possível Usar Dados do Banco de Dados!")
		else:
			return self.cursor.fetchall()

	def trata_novo_velorio(self, string):
		"""As informações do Falecido
		E do Horário do Velório
		Chegam no formato = 'sala-nome-hora-'
		e deve ser retornado ['sala', nome', 'hora']
		"""
		retorno = string.split("-")
		del(retorno[3])
		return retorno

"""teste = avelar_model()
teste.trata_novo_velorio("adfasfasfas-13:50-")"""