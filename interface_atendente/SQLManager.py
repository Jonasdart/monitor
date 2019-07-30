#!/usr/bin/env python
# -*- coding: utf-8 -*-

#dev by Jonas Duarte - Duzz System

class gera_query(object):
	def __init__(self):
		self.query = ""

	def nova_tabela(self, banco_de_dados, nova_tabela):
		self.query =  f"CREATE TABLE `{banco_de_dados}`"
		self.query += f".`{nova_tabela}`"
		self.query += "( `Pessoa` TEXT NOT NULL , "
		self.query += "`Horario` DATE NOT NULL ) ENGINE = InnoDB;"

		return self.query

	def renomear_tabela(self, banco_de_dados, nome_atual, novo_nome):
		self.query =  f"RENAME TABLE `{banco_de_dados}`"
		self.query += f".`{nome_atual}` TO"
		self.query += f"`{banco_de_dados}`.`{novo_nome}`;"

		return self.query

	def excluir_tabela(self, tabela):
		self.query = f"DROP TABLE `{tabela}`"

		return self.query

	def listar_tabelas(self):
		self.query = "SHOW TABLES"

		return self.query

	def verifica_se_tabela_esta_vazia(self, tabela, coluna_verificacao = "Pessoa")
		self.query =  "SELECT * FROM"
		self.query += f"`{tabela}` WHERE `{coluna_verificacao}`"
		self.query += "!= ''"

		return self.query

	def inserir_na_tabela(self, tabela, coluna, dados, string = True):
		"""
		string é um booleano, que
		sendo verdadeiro indica que
		o dado necessita estar entre aspas simples
		caso contrario o dado pode ser inserido 
		sem estar entre aspas
		"""
		self.query =  f"INSERT INTO `{tabela}`"
		self.query += f"`coluna` VALUES"
		if string:
			self.query += f"'{dados}';"
		else:
			self.query += f"{dados};"

		return self.query

	def alterar_dados_da_tabela(self, tabela, coluna, dados, string = True):
		"""
		string é um booleano, que
		sendo verdadeiro indica que
		o dado necessita estar entre aspas simples
		caso contrario o dado pode ser inserido 
		sem estar entre aspas
		"""
		self.query =  f"UPDATE `{tabela}` SET"
		if string:
			self.query += f"`{coluna}`= '{dados}';"
		else:
			self.query += f"`{coluna}`= {dados};"

		return self.query
