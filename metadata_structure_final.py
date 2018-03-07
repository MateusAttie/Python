'''
/*----------------------------------------------------------------------------*/
/*--Autor: Mateus Ingegneri Attie---------------------------------------------*/
/*--Data: 21/03/2016--------------------------------------------------------- */
/*----------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------*/
/*-Programa para: Achar o relacionamento das entidades dos metadados----------*/
/*----------------Listar as Foreign keys das entidades informadas ou geral----*/
/*----------------Listar as entidades em questão------------------------------*/
/*----------------Listar os atributos das entidade informada------------------*/
/*----------------------------------------------------------------------------*/
/*----------------------------------------------------------------------------*/
'''

import os

# Extrai o nome da entidade
def extract_name(name):
	return name.split('.')[0]

# Le o arquivo através do nome do arquivo passado como parâmetro unificado com o caminho padrão
def read_lines(filename):
	_file = open(os.path.join("data/meta-data", filename), 'rt')
	data = _file.read().split('\n')
	_file.close()
	return data

# Function para ler os metadados e adicionar uma tupla na lista metadata através do método append()
def read_metadata(filename):
	metadata = []
	for column in read_lines(filename):
		if column:
			metadata.append(tuple(column.split('\t')[:3]))
	return metadata

# Lista as chaves estrangeiras e primárias de todas as entidades
def list_fk_pk(meta,keys):
	for key, val in meta.items():
		for col in val:
			if col[0] in keys:
				print("Entidade {} -> {}". format(key, col[0]))

# Lista as foreign keys de uma entidade escolhida
def list_fk_entity(meta,keys,entity):
	for key, val in meta.items():
		for col in val:
			if col[0] in keys and key == entity:
				# Não exibe a primary key
				if not col[0] == 'Id'+ entity:
					print("Entidade {} -> {}".format(key, col[0]))

def prompt():
	print("\nO que deseja ver?")
	print("(1) Lista de entidades")
	print("(d) Atributos de uma entidade")
	print("(r) Relacionamentos de uma entidade")
	print("(l) Lista de FK's e PK's Geral")
	print("(f) Lista de Foreign Keys por entidade")
	print("(s) Sair do programa")
	return input('')


def main():
	# dicionario entidade -> atributos
	meta = {}

	# dicionario de chaves estrangeiras
	keys = {}

	# dicionarios de relacionamentos
	relationships = {}

	for meta_data_file in os.listdir("data/meta-data"):
		table_name = extract_name(meta_data_file)
		attributes = read_metadata(meta_data_file)
		identifier = attributes[0][0]

		meta[table_name] = attributes
		keys[identifier] = table_name

	for key, val in  meta.items():
		for col in val:
			if col[0] in keys:
				if not col[0] == meta[key][0][0]:
					relationships[key] = keys[col[0]]
					print("Entidade {} -> {}". format(key, col[0]))

	opcao = prompt()
	while opcao != 's':
		if opcao == '1':
			for entity_name in meta.keys():
				print(entity_name)
		elif opcao == 'd':
			entity_name = input("Nome da entidade: ")
			for col in meta[entity_name]:
				print(col)
		elif opcao == 'r':
			entity_name = input("Nome da entidade: ")
			other_entity = relationships[entity_name]
			print(other_entity)
		elif opcao =='l':
			list_fk_pk(meta,keys)
		elif opcao =='f':
			entity_name = input("Nome da entidade: ")
			list_fk_entity(meta,keys,entity_name)
		else:
			print('Comando Inexistente\n')
		opcao = prompt()

if __name__ == '__main__':
	main()
