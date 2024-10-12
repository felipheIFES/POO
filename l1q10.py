print('\n\n*****  PREÇO DA ENERGIA ELÉTRICA]  *****')

tipo = input('\nInforme o tipo de consumidor: R (residência) ou I (indústria) ou C (comércio)\n')

if tipo == 'R' or tipo == 'r' :
    consumo = float(input('Informe a quantidade de kWh consumida: \n'))
    if consumo <= 500:
        total = consumo * 0.4
    else:
        total = consumo * 0.65

    print(f'\nO valor a ser pago será de R${total:0.2f}')

elif tipo == 'I' or tipo == 'i' :
    consumo = float(input('Informe a quantidade de kWh consumida: \n'))
    if consumo <= 5000:
        total = consumo * 0.55
    else:
        total = consumo * 0.60
    
    print(f'\nO valor a ser pago será de R${total:0.2f}')

elif tipo == 'C' or tipo == 'c' :
    consumo = float(input('Informe a quantidade de kWh consumida: \n'))
    if consumo <= 1000:
        total = consumo * 0.55
    else:
        total = consumo * 0.60

    print(f'\nO valor a ser pago será de R${total:0.2f}')
        
else:
    print('\nErro ao digitar o tipo de consumidor')


print('\n')