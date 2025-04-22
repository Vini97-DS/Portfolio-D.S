alunos = []

while True:
    nome = input('Adicione o nome do aluno: ')
    notas = []

    for i in range(3):
        nota = float(input(f'Digite a nota {i+1}: '))
        notas.append(nota)

    media = sum(notas) / len(notas)

    aluno = {'Nome': nome, 'Notas': notas, 'Média': media}
    alunos.append(aluno)

    continuar = input('Deseja adicionar mais alunos? (s/n): ').lower()
    if continuar != 's':
        break


maiorMedia = alunos[0]
menorMedia = alunos[0]
somaMedias = 0
aprovados = 0

for n in alunos:
    somaMedias += n['Média']

    if n['Média'] > maiorMedia['Média']:
        maiorMedia = n
    if n['Média'] < menorMedia['Média']:
        menorMedia = n

    if n['Média'] >= 7:
        aprovados += 1

mediaGeral = somaMedias / len(alunos)

print('\n--- Resumo Final ---')
print(f'Alunos cadastrados: {len(alunos)}')
print(f'Média geral da turma: {mediaGeral:.2f}')
print(f'Maior média: {maiorMedia["Nome"]} ({maiorMedia["Média"]:.2f})')
print(f'Menor média: {menorMedia["Nome"]} ({menorMedia["Média"]:.2f})')
print(f'Alunos aprovados: {aprovados}')



