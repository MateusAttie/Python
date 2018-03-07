import os

# Lista os arquivos de uma pasta
for meta_file in os.listdir('data/meta-data'):
	print(meta_file)

# Function que retira a extensão .txt do nome do arquivo
def extract_entity_name(filename):
	return filename.split('.')[0]

extraido = extract_entity_name('Licitacao.txt')
print(extraido)

# Function para ler os meta dados e adicionar uma tupla na lista através do método append()
def read_meta_data(path):
	data = open(path, 'rt')
	meta_data = []
	for line in data:
		line_data = line.split('\t')
		meta_data.append((line_data[0],line_data[1],line_data[2]))

	data.close()
	return meta_data

meta_data_appended = read_meta_data('data/meta-data/Instituicao.txt')
print(meta_data_appended)


