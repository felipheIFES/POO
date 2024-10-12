print('\n\n*****  CÁLCULO DO PREÇO DA PASSAGEM  *****')

distancia = float(input('Insira a distância a ser percorrida (em Km): '))

if distancia <= 200:
    valor = distancia*0.8
else:
    valor = distancia*0.5

print(f'\nO preço da passagem ficou em R$ {valor:0.2f}.')
print('\n')