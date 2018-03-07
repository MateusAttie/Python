import os

# Programa para achar o relacionamento das entidades dos metadados(foreign keys)

# Extrai o nome da entidade
def extract_name(name):
	return name.split('.')[0]

# Le o arquivo
def read_lines(filename):
	_file = open(os.path.join("data/meta-data", filename), 'rt')
	data = _file.read().split("\n")
	_file.close()
	return data

# Function para ler os meta dados e adicionar uma tupla na lista metadata através do método append()
def read_metadata(filename):
	metadata = []
	for column in read_lines(filename):
		if column:
			values = column.split('\t')
			nome = values[0]
			tipo = values[1]
			desc = values[2]
			metadata.append((nome, tipo, desc))
	return metadata

def main():
	# dicionario entidade -> atributos
	meta = {}

	# dicionario identificador(id) -> nome entidade
	keys = {}

	for meta_data_file in  os.listdir("data/meta-data"):
		table_name = extract_name(meta_data_file)
		attributes = read_metadata(meta_data_file)

		identifier = attributes[0][0]

		meta[table_name] = attributes
		keys[identifier] = table_name
	print(keys)


	for key, val in meta.items():
		for col in val:
			if col[0] in keys:
				if not col[0] == meta[key][0][0]:
					print("Entidade {} -> {}". format(key, col[0]))


if __name__ == '__main__':
	main()