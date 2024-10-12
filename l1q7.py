print('\n\n*****  CÁLCULO PARA APROVAÇÃO DE EMPRÉSTIMO  *****')
Valor_imovel=float(input('\n       Valor do imóvel: '))
valor_salario=float(input('\n       Valor do salário: '))
qtd_parcelas=int(input('\n       Quantidade de parcelas: '))

max_prestacao = 0.4 * valor_salario

valor_prestacao = Valor_imovel / qtd_parcelas

if valor_prestacao > max_prestacao:
    print('\nEmpréstimo *NEGADO*')
    print(f'O valor das parcelas excedem 40% do salário: R${valor_prestacao}')
else:
    print('\n    !!! Empréstimo APROVADO !!!')
    print(f'    O valor das {qtd_parcelas} parcelas será de R${valor_prestacao}')
    print('\n')