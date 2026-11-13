lista_de_alunos = []


def menu_inicial():
    print('''
1. Adicionar aluno
2. Listar todos os alunos
3. Buscar aluno pelo nome
4. Remover aluno
5. Mostrar média geral das notas
6. Editar aluno
7. Sair''')


def validacao_idade(idade):
    if idade >= 10 and idade <= 100:
        return True
    else:
        return False


def validacao_nota(nota):
    if nota >= 0 and nota <= 10:
        return True
    else:
        return False


def validacao_dados(idade, nota):
    if nota >= 0 and nota <= 10 and idade >= 10 and idade <= 100:
        return True
    else:
        return False


def printar_aluno(aluno):
    print('-' * 50)
    print(f'Aluno: {aluno['nome_do_aluno']}')
    print(f'Idade: {aluno['idade_do_aluno']}')
    print(f'Nota: {aluno['nota_do_aluno']}')
    print(f'Status: {aluno['status_do_aluno']}')
    print('-' * 50)


def adicionar_aluno(nome, idade, nota):
    if nota >= 7:
        status = 'Aprovado'
    else:
        status = 'Reprovado'
    cadastro_de_alunos = {
        'nome_do_aluno': nome,
        'idade_do_aluno': idade,
        'nota_do_aluno': nota,
        'status_do_aluno': status
    }
    lista_de_alunos.append(cadastro_de_alunos)


def listar_alunos():
    for aluno in lista_de_alunos:
        printar_aluno(aluno)


def buscar_aluno(nome):

    for aluno in lista_de_alunos:
        if aluno['nome_do_aluno'] == nome:
            printar_aluno(aluno)
            return

    print(f'Aluno ainda não cadastrado!!')


def remover_aluno(nome):
    for aluno in lista_de_alunos:
        if aluno['nome_do_aluno'] == nome:
            lista_de_alunos.remove(aluno)
            print('Aluno retirado do sistema!!')
            return
    print(f'Não existe esse aluno cadastrado!!')


def media_geral():
    total_notas = 0
    for nota in lista_de_alunos:
        total_notas += nota['nota_do_aluno']

    media = total_notas / len(lista_de_alunos)
    print(f'\nA média geral das notas é: {media:.2f} ')


def editar_aluno(nome):
    for aluno in lista_de_alunos:
        if aluno['nome_do_aluno'] == nome:
            oque_deseja_alterar = input('''
1 - Nome
2 - Idade
3 - Nota
0 - Voltar ao menu inicial

Oque deseja alterar do aluno: ''')

            match oque_deseja_alterar:
                case '1':
                    nome_novo = input('Informe o novo nome: ')
                    aluno['nome_do_aluno'] = nome_novo
                case '2':
                    idade_nova = int(input('Informe a idade nova: '))
                    if validacao_idade(idade_nova):
                        aluno['idade_do_aluno'] = idade_nova
                        print('Alteração feita com sucesso!!')
                        return

                    print('Idade incorreta!!')
                case '3':
                    nota_nova = float(input('Informe a nota nova: '))
                    if validacao_nota(nota_nova):
                        aluno['nota_do_aluno'] = nota_nova
                        print('Alteração feita com sucesso!!')

                        if aluno['nota_do_aluno'] >= 7:
                            aluno['status_do_aluno'] = 'Aprovado'
                        else:
                            aluno['status_do_aluno'] = 'Reprovado'

                        return

                    print('Nota incorreta!!')
                case '0':
                    continue
                case _:
                    print('Opção invalida!!')
            continue
        else:
            print('Nome inválido!! Tente novamente!')
