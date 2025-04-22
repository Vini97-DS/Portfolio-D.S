

totalGasto = 0

compra = []

while True: 
    produto = input('Adicione o nome do produto: ')
    preco = float(input('Adicione o preco do produto: '))
    categoria = input('Categoria do produto: ')

    venda = {'nome': produto, 'Valor': preco, 'Categoria': categoria}
    compra.append(venda)

    totalGasto +=preco

    continuar = input('Deseja adicionais mais produtos? (sim/nao): ').lower()
    if continuar == 'nao':
        break


valores = [v['Valor'] for v in compra]

barato = compra[0]
caro = compra[0]

for item in compra:
    if item['Valor'] > caro['Valor']:
        caro = item
    if item['Valor'] < barato['Valor']:
        barato = item

#Categorias
alimento = 0
vestuario = 0
eletronico = 0
outras = 0

for item in compra:
    if item['Categoria'].lower() == 'alimento':
        alimento += 1
    elif item['Categoria'].lower() == 'vestuario':
        vestuario += 1
    elif item['Categoria'].lower() == 'eletronico':
        eletronico += 1
    else:
        outras += 1


print('\n--- Sua Compra ---')

print(f'Total de produtos cadastrados: {len(compra)}')
print(f'Total gasto: R$ {totalGasto:.2f}')
print(f'Produto mais barato: {barato["nome"]} (R$ {barato["Valor"]:.2f})')
print(f'Produto mais caro: {caro["nome"]} (R$ {caro["Valor"]:.2f})')

print('\nQuantidade por categoria:')
print(f'Alimento: {alimento}')
print(f'Vestuário: {vestuario}')
print(f'Eletrônico: {eletronico}')
print(f'Outras: {outras}')

