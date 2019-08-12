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

	def nova_sala(self, nome_sala):
		colunas = self.listar_nome_dos_dados("salas")
		query = self.manager.buscar_dados_da_tabela("salas")
		salas = self.final_com_retorno(query)
		self.num = len(salas)
		for x in range(len(salas)):
			if x is not salas[x][0]:
				self.num = x
				break
		nova_sala = [self.num, nome_sala[0]]
		query = self.manager.inserir_na_tabela("salas", colunas, nova_sala)

		try:
			self.final_sem_retorno(query)
		except:
			raise

	def editar_sala(self, id_sala, novo_nome):
		query = self.manager.alterar_dados_da_tabela("salas", ["Sala"], [novo_nome], where = True, coluna_verificacao = "num_sala", valor_where = id_sala)

		try:
			self.final_sem_retorno(query)
		except:
			raise

	def excluir_sala(self, id_sala):
		query = self.manager.excluir_dados_da_tabela("salas", where = True, coluna_verificacao = "num_sala", valor_where = id_sala)

		try:
			self.final_sem_retorno(query)
		except:
			raise


	def listar_salas(self):
		query = self.manager.verifica_se_tabela_esta_vazia("salas")
		salas = self.final_com_retorno(query)
		id_sala = list()
		nome_sala = list()
		for x in range(len(salas)):
			id_sala.append(salas[x][0])
			nome_sala.append(salas[x][1])
		#salas = trata.trata_retorno_de_todas_tabelas(salas)
		return [id_sala, nome_sala]

	def listar_salas_livres(self, salas):
		salas_livres = list()
		for sala in salas:
			query = self.manager.verifica_se_tabela_esta_vazia("velorios", where = True, coluna_verificacao = "num_sala", valor_where = sala)
			resposta = self.final_com_retorno(query)
			if len(resposta) is 0:
				salas_livres.append(sala)
		return salas_livres

	def listar_salas_em_uso(self, salas):
		salas_em_uso = list()
		for sala in salas:
			query = self.manager.verifica_se_tabela_esta_vazia("velorios", where = True, coluna_verificacao = "num_sala", valor_where = sala)
			resposta = self.final_com_retorno(query)
			if len(resposta) is not 0:
				salas_em_uso.append(sala)
		return salas_em_uso

	def listar_nome_das_salas(self, salas):
		nome = list()
		for sala in salas:
			query = self.manager.buscar_dados_da_tabela(tabela = "salas", where = True, coluna_verificacao = "num_sala", valor_where = sala)
			nome.append(self.final_com_retorno(query)[0])
		return nome

	def novo_velorio(self, velorio):
		colunas = self.listar_nome_dos_dados("velorios")
		del(colunas[0])
		del(colunas[5])
		try:
			query = self.manager.inserir_na_tabela("velorios", colunas, velorio)
		except:
			raise
		else:
			try:
				self.final_sem_retorno(query)
			except:
				raise

	def editar_velorio(self, velorio):
		id_velorio = velorio[0]
		del(velorio[0])
		colunas = self.listar_nome_dos_dados("velorios")
		del(colunas[0])
		del(colunas[2])
		del(colunas[6])
		try:
			query = self.manager.alterar_dados_da_tabela("velorios", colunas, velorio, where = True, coluna_verificacao = "id", valor_where = id_velorio)
		except:
			raise
		else:
			try:
				self.final_sem_retorno(query)
			except:
				raise

	def concluir_velorio(self, velorio):
		try:
			query = self.manager.alterar_dados_da_tabela("velorios", ["Status"], ["1"], where = True, coluna_verificacao = "id", valor_where = velorio[0])
		except:
			raise
		else:
			try:
				self.final_sem_retorno(query)
			except:
				raise

	def excluir_velorio(self, velorio):
		query = self.manager.excluir_dados_da_tabela("velorios", where = True, coluna_verificacao = "id", valor_where = velorio[0])

		try:
			self.final_sem_retorno(query)
		except:
			raise

	def listar_velorios(self, sala):
		query = self.manager.buscar_dados_da_tabela("velorios", where = True, coluna_verificacao = "num_sala", valor_where = sala)

		velorio = self.final_com_retorno(query)

		return velorio

	def listar_velorios_nao_concluidos(self, sala):
		query = self.manager.buscar_dados_da_tabela("velorios", where = True, coluna_verificacao = ["num_sala", "Status"], valor_where = [sala, "0"])

		velorio = self.final_com_retorno(query)

		return velorio

	def buscar_informacoes_velorio(self, velorio):
		query = self.manager.buscar_dados_da_tabela("velorios", where = True, coluna_verificacao = "id", valor_where = velorio)
		velorio = self.final_com_retorno(query)

		return velorio

	def conta_velorio_por_sala(self, salas):
		retorno = list()
		for sala in salas:
			cont = 0
			query = self.manager.buscar_dados_da_tabela("velorios", where = True, coluna_verificacao = "num_sala", valor_where = sala)
			resposta = self.final_com_retorno(query)
			cont += len(resposta)
			retorno.append(f"{cont} velorios")
		return retorno

	def listar_nome_dos_dados(self, sala):
		retorno = list()
		query = self.manager.listar_colunas(sala)
		dados = self.final_com_retorno(query)
		for x in range(len(dados)):
			retorno.append(dados[x][0])

		return retorno

	def trata_para_subir_ao_banco(self, string):
		"""As informações do Falecido
		E do Horário do Velório
		Chegam no formato = 'sala-nome-hora_saida-data_sepultamento-cemiterio'
		e deve ser retornado ['velorio', 'sala', nome', 'hora_saida', 'data_sepultamento', 'cemiterio']
		"""
		retorno = string.split("-")
		cont = 0
		for item in retorno:
			cont += 1
		cont -= 1
		del(retorno[cont])
		return retorno

	def final_sem_retorno(self, query):
		try:
			self.cursor.execute(query)
		except:
			raise
		else:
			self.banco.commit()

	def final_com_retorno(self, query):
		try:
			self.cursor.execute(query)
		except:
			raise 
		else:
			return self.cursor.fetchall()
