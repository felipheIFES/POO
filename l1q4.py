print('\n\n*****  EXIBIÇÃO DO RESTO DE UMA DIVISÃO  *****')
x=int(input('\n       Digite o dividendo: '))
y=int(input('       Digite o divisor: '))

while x >= y:
    x -= y

resto = x    
    
print('\n       O resto da divisão é', resto)