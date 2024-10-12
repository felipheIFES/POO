print('\n\n*****  QUANTIDADE MÍNIMA DE NOTAS  *****')

n = int(input('Digite o valor para o cálculo da quantidade mínima de notas:\n'))

qtd = 0
qt100 = 0
qt50 = 0
qt10 = 0
qt05 = 0
qt01 = 0

while n >= 100:
    qt100 += 1
    qtd += 1
    n -= 100


while n >= 50:
    qt50 += 1
    qtd += 1
    n -= 50

while n >= 10:
    qt10 += 1
    qtd += 1
    n -= 10

while n >= 5:
    qt05 += 1
    qtd += 1
    n -= 5

while n >= 1:
    qt01 += 1
    qtd += 1
    n -= 1

print(f'\nQuantidade mínima de notas: {qtd}')
print(f'\n{qt100} de 100, \n{qt50} de 50, \n{qt10} de 10, \n{qt05} de 5, \n{qt01} de 1 ')
print('\n')