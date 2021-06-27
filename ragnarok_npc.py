import os
from time import sleep

print('=-='*17)
print('Desenvolvedor\n')
print('IHURY FERREIRA DE FRANÇA\n')
print('=-='*17)
print('Sistema de criação de npc para Ragnarok\n')
print('=-='*17)
opcao = 0
while opcao != 5:
	print('''Menu opção:\n
- [1] Criar arquivo texto
- [2] Criar Npc dentro do arquivo texto criado
- [3] Deletar arquivo Existente
- [4] Editar algum arquivo pronto
- [5] Sair do programa''')
	print('=-='*17)
	opcao = int(input('Escolha uma das opções a Cima digitando o número: '))
	#arquivo = open('arquivo.txt', 'w')
	if opcao == 1:
		print('=-='*17)
		opcao2 = int(input('Quantos arquivo de texto você queira criar? '))
		for n in range(1, opcao2 + 1):
			print('=-='*17)
			print('Quantos arquivo de texto queira criar? #', n)
			print('=-='*17)
			print('Dica:')
			print('Não precisa colocar txt, apenas digite o nome do arquivo.\n')
			print('=-='*17)
			nome = input('Digite o nome do arquivo: ')
			arquivo = open(nome + '.txt', 'w')

			print()

		arquivo.close()
		print("Criação do arquivo com sucesso!!!")
		sleep(3)
	
	elif opcao == 2:
		nomeArquivo = input('Digite o nome do Arquivo que você criou, sem .txt: ')
		arquivox = open(nomeArquivo + '.txt', 'w')
		
		escrita = input('Escreva o nome da cidade ou nome do mapa onde npc vai ficar: ')
		cordenadaX = input('Escreva a cordenada x do mapa: ')
		cordenadaY = input('Escreva a cordenada y do mapa: ')
		direcaoDoNpc = input('Digite a direção do Npc Ex: 1,2,3,4 e 5: ')
		nomeDoNPC = input('Digite O nome do Npc que ira aparecer: ')
		print('Para você Saber onde ver o nome acessa site: http://nn.ai4rei.net/dev/npclist/?qq=8: ')
		imagemDONpc = input('Digite o comando do Npc que ira aparecer Ex: 1_F_MARIA : ')
		ms = input('Digite a Mensagem que ira usar no arquivo: ')
		#ms2 = input('Aqui você ira criar comandos exemplo if else etc..: ')

		arquivox.write(escrita +','+cordenadaX+','+cordenadaY+','+direcaoDoNpc+'\tscript\t'+nomeDoNPC+'\t'+imagemDONpc+','+'{'+'\n')
		arquivox.write('\t'+'mes '+'"'+'['+nomeDoNPC+']'+'"'+';'+'\n')
		arquivox.write('\t'+'mes '+'"'+ms+'"'+';'+'\n')
		#arquivox.write('\t'+ ms2 +'\n')
		arquivox.write('}')
		print()
		
		arquivox.close()
		print('Cadastro de dados com sucesso!!!')
		sleep(3)

	elif opcao == 3:
		nomeArq = input('Digite o nome do arquivo que queira deletar: ')

		arquivo2 = (nomeArq+'.txt')
		if arquivo2 == nomeArq+'.txt':
			os.remove(arquivo2)
			print('Arquivo deletado com sucesso!!')
			sleep(5)
		else:
			print('Digite apenas o nome do arquivo. Ex: nome_do_arquivo\n')
			print('Não precisa colocar .txt.')
		
	elif opcao == 4:
		nome = input('Digite o nome do arquivo: ')
		arquivo = open(nome +'.txt', 'r') # Abra o arquivo (leitura)
		conteudo = arquivo.readlines()
		escrita = input('Escreva o que queira usar')
		conteudo.append(escrita +'\n')  # insira seu conteúdo

		arquivo2 = open(nome +'.txt', 'w') # Abre novamente o arquivo (escrita)
		arquivo2.writelines(conteudo)    # escreva o conteúdo criado anteriormente nele.

		arquivo.close()
	elif opcao == 5:
		print('=-='*9)
		print(' Fechando o programa!')
		print('=-='*9)
	else:
		print('Opção Invalida, Tente Novamente!!!')
	print('Fim do Programa...')
	sleep(5)





