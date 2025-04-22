empresa = []

while True:
    nome = str(input('Digite o nome do funcionario: '))
    idade = int(input('Digite a idade do funcionario: '))
    cargo = str(input('Digite o cargo do funcionario: '))


    funcionarios = {'nome': nome, 'idade': idade, 'cargo': cargo}

    empresa.append(funcionarios)

    continuar = input('Deseja adicionais mais funcionarios? (sim/nao): ').lower()
    if continuar == 'nao':
        break

years = [y['idade'] for y in empresa]

maisVelho = empresa[0]
maisNovo = empresa[0]

for cat in empresa:
    if cat['idade'] > maisVelho['idade']:
        maisVelho = cat
    if cat['idade'] < maisNovo['idade']:
        maisNovo = cat


analista = 0
gerente = 0
engenheiro = 0 
outros = 0

for cat in empresa: 
    if cat['cargo'].lower() == 'analista':
        analista += 1
    elif cat['cargo'].lower() == 'gerente':
        gerente += 1
    elif cat['cargo'].lower() == 'engenheiro':
        engenheiro += 1
    else:
        outros += 1


print('--- Relatorio final ---')

print(f'Total de funcionarios cadastrados: {len(empresa)}')
print(f"funcionario mais velho: {maisVelho['idade']}")
print(f"funcionario mais velho: {maisNovo['idade']}")
print(f"analistas: {analista}")
print(f"analistas: {gerente}")
print(f"analistas: {engenheiro}")