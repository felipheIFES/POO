from datetime import date
ano_corrente = date.today().year

bissexto = False
dia_valido = False
mes_valido = False
ano_valido = False
max_dia = 30

print('\n\n*****  VALIDAÇÃO DE DATA DE NASCIMENTO  *****')
print('\n       Digite a data de seu nascimento (dd.mm.aaaa) :')

dia_input=int(input('       dia: '))
mes_input=int(input('       mês: '))
ano_input=int(input('       ano: '))

#VERIFICAÇÃO DE ANO BISSEXTO
resto100=ano_input%100
if resto100==0:
    resto400=ano_input%400
    if resto400==0:
        bissexto=True
else:
    resto4=ano_input%4
    if resto4==0:
        bissexto=True

#CONTROLE DE DIAS DO MêS
match mes_input:
    case 4|6|9|11:
        max_dia=31
    case 2:
        if bissexto:
            max_dia=29
        else:
            max_dia=28

#Validação da data de nascimento
if 1 <= dia_input <= max_dia:
    dia_valido=True
if 1 <= mes_input <= 12:
    mes_valido=True
if ano_input <= ano_corrente:
    ano_valido=True

if dia_valido and mes_valido and ano_valido:
    print('\nOK !!!  Data Válida\n')
else:
    print('\nData Inválida\n')