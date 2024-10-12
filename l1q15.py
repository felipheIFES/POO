print('\n***** Método de Newton *****')

opcao = ' '

while opcao != 'x' and opcao != 'X':

    print('\nPara fechar o programa digite X ...')
    opcao = input('\nDigite um número para calculo da raiz quadrada: ')

    if opcao == 'x' or opcao == 'X':
        print('\n Fim do Programa !!!')
        print('')

    else:
        m = float(opcao)
        x = 0.0001
        b = 2.0000

        while x >= 0.0001:

            p = (b + m/b) / 2

            qp = p**2

            b = p

            x = m - qp
            if x < 0:
                x = x * (-1)

        print('\nA raiz quadrada de', m, 'é',f'{b:.4f}')
        print('')