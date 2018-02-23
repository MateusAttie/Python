# Packing
def new_user(active=False, admin=True):
	print(active)
	print(admin)

config = {"active": False,   # Dicionario
		  "admin": True}

new_user(config.get('active'), config.get('admin')) # get() funcao do dicionario para captura de valores
new_user(**config) # interpretador casa automaticamente os itens do dicionario com os parametros nomeados na funcao new_user() 


# Unpacking
def unpacking_experiment(*args): # recebimento de parametros multiplos como uma tupla ou lista
	args1 = args[0]
	args2 = args[1]
	others = args[2:]
	print(args1)
	print(args2)
	print(others)

unpacking_experiment(1, 2, 3, 4, 5, 6)

def unpacking_experiment2(**dictionary):
	print(dictionary)

unpacking_experiment2(named='Teste', other='Other')
