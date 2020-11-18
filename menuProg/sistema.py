from menuProg.lib.interface import *
from menuProg.lib.arquivo import *
from time import sleep

arq = 'Curso em video.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        #Listar o conteudo do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #Opção cadastrar nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('Erro. Digite uma opção valida!')
    sleep(2)

