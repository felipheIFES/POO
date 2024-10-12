print('\n\n*****  CÁLCULO DA MÉDIA  *****')
print('*****   RESULTADO FINAL  *****')

x=float(input('\n       Digite a primeira nota: '))
y=float(input('       Digite a segunda nota: '))

media = (x + y) / 2

if media >= 9.5:
    print(f'\n       Sua média final foi: {media:.3}') 
    print('       "Aprovado com Distinção"')
    print('\n')
else:
    if media >= 7.0:
        print(f'\n       Sua média final foi: {media:.3}')
        print('       "Aprovado"')
        print('\n')
    else:
        print(f'\n       Sua média final foi: {media:.3}')
        print('       "Reprovado"')
        print('\n')