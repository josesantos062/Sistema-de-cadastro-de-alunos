from funcoes import *


while True:
    menu_inicial()
    opcoes = input('\nQual das opções deseja seguir a frente: ')

    match opcoes:
        case '1':
            nome = input('Informe o nome do aluno: ').strip
            idade = int(input('Informe a idade do aluno: '))
            nota = float(input('Informe a nota do aluno: '))
            if validacao_dados(idade, nota) == True:
                adicionar_aluno(nome, idade, nota)
            else:
                print('Dados incoformes de acordo com a sociedade!!!')

        case '2':
            if len(lista_de_alunos) < 1:
                print('\nAinda não existe alunos cadastrados!!')
                continue

            listar_alunos()

        case '3':
            buscando_aluno = input(
                'Informe o nome do aluno que deseja buscar: ')
            buscar_aluno(buscando_aluno)

        case '4':
            removendo_aluno = input('Informe o aluno que deseja remover: ')
            remover_aluno(removendo_aluno)

        case '5':
            if len(lista_de_alunos) < 1:
                print('Não existe alunos cadastrados!!')
                continue

            media_geral()

        case '6':
            print('Volte sempre!')
            break

        case _:
            print('Opção invalida!!')
