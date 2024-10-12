print('\n***** AUTOMAÇÃO DA LOJA *****')

valor = 0
forma = 'x'
qtd = 1

# Coloquei uma opção para inserir a quantidade de itens
# Para habilitar essa opção, basta retirar o "#" das linhas 12 e 19

preco = float(input('Informe o preço: '))
if preco != 0:
    #qtd = int(input('Quantidade: '))
    valor += preco*qtd
    print(f'R${valor:.2f}\n')

while preco != 0:
    preco = float(input('Informe o preço : '))
    if preco != 0:
        #qtd = int(input('Quantidade: '))
        valor += preco*qtd
        print(f'R${valor:.2f}\n')

while forma != '1' and forma != '2' and valor != 0:

    forma = input('Escolha a foma de pagamento: 1 (à vista) ou 2 (cartão de crédito)\n')

    if forma == '1':
        print(f'\nValor total: R${valor:.2f}')
        total = 0.85 * valor
        print (f'Valor final com desconto de 15%: R${total:.2f}')
        print('')
    elif forma == '2':
        total = valor
        vezes = valor / 4
        print (f'\nTotal: R${total:.2f} em 4 parcelas de R${vezes:.2f}')
        print('')
    else:
        print ('Erro na opção de pagamento\n')