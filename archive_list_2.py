import os

# Programa para ter um dicionário de uma lista de tuplas onde a as chaves são o nome das entidades(arquivos) e os valores os atributos(tuplas)

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
	meta = {}
	for meta_data_file in  os.listdir("data/meta-data"):
		table_name = extract_name(meta_data_file)
		meta[table_name] = read_metadata(meta_data_file)

	for key, val in meta.items():
		print("Entidade {}". format(key))
		print("Atributos: ")
		for col in val:
			print("  {}: {}".format(col[1], col[0]))

if __name__ == '__main__':
	main()