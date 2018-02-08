# import webbrowser
# import time

# total_breaks = 3
# break_count = 0

# print("This program startes on " + time.ctime())
# while(break_count < total_breaks):
# 	time.sleep(10)
# 	webbrowser.open("http://www.youtube.com.br")
# 	break_count = break_count + 1
import os

def rename_files():
	file_list = os.listdir(r"/Users/Attie/Downloads/prank")
	print(file_list)
	#encontro o diretorio atual que estou e salvo
	saved_path = os.getcwd()
	#mudo para o diretoria que quero mudar o nome dos arquivos
	os.chdir(r"/Users/Attie/Downloads/prank")
	for file_name in file_list:
		print("Old name: "+file_name)
		print("New name: "+file_name.translate(None,"0123456789"))
		#translate(tabel,list of characters to remove)
		os.rename(file_name, file_name.translate(None,"0123456789"))
	os.chdir(saved_path)
rename_files()