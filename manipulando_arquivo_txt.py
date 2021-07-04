#==============================
# Site onde usar a w r etc..
# https://docs.python.org/3/library/functions.html#open
#==============================
# Este Programa e para Estudo =
#==============================
# Criado por IHURY FERREIRA	  =
#==============================
# Manipulando arquivo txt	  =
#==============================
from time import sleep #Adicionando Biblioteca tempo para Congelar o programa
arquivo = open('arquivo.txt', 'w') #Criando Arquivo txt

arquivo.write('Meu nome é ihury\n') #Adicionando Dados no arquivo e o (barra N) e para pular O texto
arquivo.write('Faço ciências da Computação.\n')
arquivo.write('Estou no Quarto Periodo do Curso.\n')

arquivo.close() # Fechando o programa!

#==================================
# Criando Leitura do arquivo Todo =
#==================================
meu_arquivo = open('arquivo.txt', 'r') #Adicionei nome e formato do arquivo e (r) para ler o arquivo

meu_arquivo.seek(0, 0) #Adicionei seek para da a cordenadas onde ira começar a ler o arquivo

print(meu_arquivo.read(), end='') #Dentro do print adicionei read para ler todo o arquivo.
# pegando as Cordenadas do seek e end para não pular linha

print('='*10) # multiplicando o = para Separar o que fiz de Cima
#==================================
#Mostrando de outra forma
#Fazendo a Segunda Leitura
#Apenas pegando uma Linha do arquivo
#===================================
meu_arquivo.seek(0, 0)

print(meu_arquivo.readline(), end='') #Pegando apenas um linha do arquivo para ler o dados de uma linha
print(meu_arquivo.readline(), end='')
print(meu_arquivo.readline(), end='')
print('='*10)

#=============================
# Mostrando de duas formas
# de Ler arquivo usando (for)
#=============================
meu_arquivo.seek(0, 0)

for linha in meu_arquivo.readlines(): #Nesta primeira forma de ler arquivo
	print(linha)					  #usei readlines para pega tudo
print("="*10)						  #Até mesmo ira pega o pular linha

meu_arquivo.seek(0, 0)

for linhax in meu_arquivo: #Segunda Forma de ler arquivo, sem pular linha
	print(linhax, end='')

meu_arquivo.close() # Fechando o programa

print("="*15)
#==============================================
# Mostrando a outra forma de adicionar dados  =
# E ler arquivo de dados, Usando try		  =
#==============================================
try:
	meu_arquivox = open('arquivo.txt', 'w+')

	meu_arquivox.write('Finalizando O que Aprendi!!!')

	meu_arquivox.seek(0)

	print(meu_arquivox.read())
finally:
	meu_arquivox.close()

print('='*13)

#============================================
# Mostrando a outra forma de adicionar dados
# E ler arquivo de dados, usando with
#============================================
with open('arquivo.txt', 'w+') as file:
	file.write('Linha 1\n')
	file.write('Linha 2\n')
	file.write('Linha 3\n')

	file.seek(0)
	print(file.read())
	sleep(5)
